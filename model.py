import cv2
import tensorflow as tf
import numpy as np

img_width, img_height = 150, 150 
INPUT_SHAPE = (img_width, img_height, 1)

labels_predict = {
    0: "DRUSEN",
    1: "CNV",
    2: "NORMAL",
    3: "DME",
}

def retine_model():
    model = tf.keras.models.load_model('models/retinal-oct-final.h5', compile=False)
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    return model

def predict_image(img):
    model = retine_model()

    # Load the image with OpenCV
    file_bytes = np.asarray(bytearray(img.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Prepare the image
    img_file = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (img_width, img_height))
    img_file = np.array(img_file)
    img_file = img_file.astype('float32')
    img_file /= 255
    img_file = np.reshape(img_file, (1, img_width, img_height, 1, 1))

    # Predict the result
    result = np.argmax(model.predict(img_file))
    category = labels_predict[result]
    return category