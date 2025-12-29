from fastapi import APIRouter, HTTPException
from API.services.Danger_level_prediction import predict_danger_level
import pandas as pd

router = APIRouter()

@router.post("/predict_Danger_level")
async def make_prediction(lat:float, lon:float, hour:int, month:int, year:int):
    input_data = pd.DataFrame([[lat, lon, hour, month, year]], 
                              columns=['latitude', 'longitude', 'hour', 'month', 'year'])  
    try:
        prediction = predict_danger_level(input_data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))