import numpy as np
from keras.models import load_model

path = ''


def predict_label(params_data):
    model = load_model('apps/api_endpoints/params/ParamsCreate/service/cancer_predicter.h5')
    input_data = [
        params_data['x2'],
        params_data['x6'],
        params_data['x11'],
        params_data['x12'],
        params_data['x18'],
        params_data['x19']
    ]
    input_data = np.array(input_data).reshape(1, -1)
    predicted_class_probabilities = model.predict(input_data)[0]
    result = {
        'class1': predicted_class_probabilities[0]*100,
        'class2': predicted_class_probabilities[1]*100,
        'class3': predicted_class_probabilities[2]*100,
        'class4': predicted_class_probabilities[3]*100,
    }
    return result
