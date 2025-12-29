from API.core.config import settings
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

model_path = settings.MODEL_PATH
model = joblib.load(model_path)

le_path = settings.MODEL_ENCODER
le = joblib.load(le_path)


def predict_danger_level(data):
    prediction = model.predict(data)
    predict_level = le.inverse_transform(prediction)[0]
    return predict_level
