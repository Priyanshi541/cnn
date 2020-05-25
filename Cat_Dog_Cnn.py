from keras.layers import Convolution2D

from keras.layers import MaxPooling2D

from keras.layers import Flatten

from keras.layers import Dense

from keras.models import Sequential

model = Sequential()

neurons1 = 512

epochs1 = 5

model.add(Convolution2D (filters = 32, kernel_size=(3,3), activation='relu',input_shape=(64, 64, 3)) )

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(filters = 32, kernel_size=(3,3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Flatten())

model.add(Dense(units= neurons1 , activation='relu'))

model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

from keras_preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        '/root/workspace/cnn_dataset/training_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/root/workspace/cnn_dataset/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
mode = model.fit(
        training_set,
        steps_per_epoch=100,
        epochs = epochs1,
        validation_data=test_set,
        validation_steps=75)

model.save('Cnn_Model.h5')

print(mode.history['accuracy'][epochs1-1] * 100)
file = open('/root/workspace/cur_accuracy.txt' , 'w')
file.write('%d' %int(mode.history['accuracy'][epochs1-1] * 100))
file.close()
