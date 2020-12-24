import joblib
import insightface
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

retina_model = insightface.model_zoo.get_model('retinaface_r50_v1')
retina_model.prepare(ctx_id = -1, nms=0.4)
facenet_model = load_model('facenet_keras.h5')
SVC_model = joblib.load('model.joblib')
in_encoder = joblib.load('in_encoder.joblib')
out_encoder = joblib.load('out_encoder.joblib')

def detection(pix_img, required_size=(160, 160)):
    pix_img = np.asarray(Image.fromarray(pix_img).convert('RGB'))
    borders, _ = retina_model.detect(pix_img, threshold=0.5, scale=1)
    borders = np.abs(borders[0].astype(int))
    face = pix_img[borders[1]:borders[3],borders[0]:borders[2]]
    img = Image.fromarray(face)
    img = img.resize(required_size)
    return np.asarray(img)

def features(pix_img):
    pix_img = pix_img.astype('float32')
    mean, std = pix_img.mean(), pix_img.std()
    pix_img = (pix_img - mean) / std
    pix_img = np.expand_dims(pix_img, axis=0)
    face_features = facenet_model.predict(pix_img)
    return face_features[0]

def make_predictions(face_features):
    face_features = in_encoder.transform(face_features.reshape(1,-1))
    predictions = SVC_model.predict_proba(face_features)[0]
    text = 'Вы похожи на...:'
    for person, prob in zip(np.argsort(predictions)[-5:][::-1], sorted(predictions)[-5:][::-1]):
        text += '\n' '{}, {:.2%}'.format(out_encoder.inverse_transform([person])[0].replace('_', ' '), prob)
    return text