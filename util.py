import pickle
import numpy as np

__model = None

def get_estimated_price(age,bmi,female,male,northeast,northwest,southeast,southwest,no,yes):
    x = np.zeros(10)
    x[0] = age
    x[1] = bmi
    x[2] = female
    x[3] = male
    x[4] = northeast
    x[5] = northwest
    x[6] = southeast
    x[7] = southwest
    x[8] = no
    x[9] =yes
    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    if __model is None:
        with open('./artifacts/medical_cost_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()