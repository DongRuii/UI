import pandas as pd
import numpy as np
import glob
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
import os,shutil
from keras import models,layers,optimizers
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D
from keras.applications.resnet50 import ResNet50

df= pd.read_csv("/Users/rui/desktop/train.csv")
df = df.replace(0,'buildings').replace(1,'forest').replace(2,'glacier').replace(3,'mountain').replace(4,'sea').replace(5,'street')


datagen = ImageDataGenerator(rescale=1./255,
                           shear_range = 0.2,
                           zoom_range = 0.2,
                           horizontal_flip=True,
                           preprocessing_function= preprocess_input,
                           validation_split=0.25)
train_generator = datagen.flow_from_dataframe(dataframe=df,
                        directory="/Users/rui/desktop/train",
                        x_col="image_name",
                        y_col="label",
                        subset="training",
                        batch_size=100,
                        seed=42,
                        shuffle=True,
                        class_mode="categorical",
                        target_size=(150,150))
valid_generator = datagen.flow_from_dataframe(dataframe=df,
                        directory="/Users/rui/desktop/train",
                        x_col="image_name",
                        y_col="label",
                        subset="validation", batch_size=10,
                        seed=42,
                        shuffle=True,
                        class_mode="categorical",
                        target_size=(150,150))

res_conv = ResNet50(include_top=False,
                    weights='imagenet',
                    input_tensor=None,
                    input_shape=(150, 150, 3),
                    pooling=None, classes=1000)
model = models.Sequential()
model.add(res_conv)

model.add(Conv2D(32, 3, 3, border_mode='same', input_shape=(150, 150, 3), activation='relu'))
model.add(Conv2D(32, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(128, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(1, 1)))

model.add(Conv2D(256, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(256, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(1, 1)))

model.add(layers.Flatten())
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(6, activation='softmax'))

# Show a summary of the model. Check the number of trainable parameters
model.summary()
model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=1e-4), metrics=['acc'])

STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
STEP_SIZE_VALID=valid_generator.n//valid_generator.batch_size
history =model.fit_generator(generator=train_generator,
                    steps_per_epoch=STEP_SIZE_TRAIN,
                    validation_data=valid_generator,
                    validation_steps=STEP_SIZE_VALID,
                    epochs=20,verbose=1)

model.save("inception.h5")