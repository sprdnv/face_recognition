import os
import requests
import numpy as np
from io import BytesIO
from PIL import Image
from models import detection, features

def load_pictures(directory):
    x, y = [], []
    for file_name in os.listdir(directory):
        with open(os.path.join(directory, file_name)) as f:
            content = f.readlines()
        temp = []
        indicies = np.random.randint(0, len(content), 20)
        for i in set(indicies):
            try:
                response = requests.get(content[i].split(' ')[1], timeout=1)
                temp.append(np.asarray(Image.open(BytesIO(response.content))))
            except:
                pass
        x.extend(temp)
        y.extend([file_name.split('.')[0]]*len(temp))
    print('Saving data...')
    np.savez_compressed('data.npz', np.asarray(x), np.asarray(y))
    
def get_features(images, labels, retina_model, facenet_model):
    x, y = [], []
    for img, person in zip(images, labels):
        try:
            face = features(detection(img, retina_model), facenet_model)
            x.append(face)
            y.append(person)
        except:
            pass
    print('Saving features...')
    np.savez_compressed('features.npz', np.asarray(x), np.asarray(y))