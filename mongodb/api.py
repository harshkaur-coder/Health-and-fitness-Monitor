from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
app = FastAPI()
FILE_PATH = "C:/Users/harshdeep kaur/OneDrive/Desktop/mongodb/fitness_logs_50.csv"
@app.get("/")
def home():
    return {"message": "Health & Fitness API is running"}
@app.get("/fitness")
def get_fitness_data():
    df = pd.read_csv(FILE_PATH)
    return df.to_dict(orient="records")
class FitnessData(BaseModel):
    user_id: int
    date: str
    steps: int
    calories: int
    heart_rate: int
    workout_minutes: int
@app.post("/fitness")
def add_fitness_data(data: FitnessData):
    df = pd.read_csv(FILE_PATH)
    new_row = pd.DataFrame([data.dict()])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
    return {"message": "Fitness data added successfully"}
{
  "user_id": 1,
  "date": "2025-03-06",
  "steps": 9500,
  "calories": 480,
  "heart_rate": 82,
  "workout_minutes": 55
}
