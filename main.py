from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/cars", status_code=201)
def create_car(car: Car):
    cars.append(car)
    return car

class Car(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: Characteristics

class Characteristics(BaseModel):
    max_speed: float
    max_fuel_capacity: float

@app.get("/cars", response_model=List[Car])
def get_cars():
    return cars

 
@app.get("/cars/{id}", response_model=Car)
def get_car(id: str):
    car = next((car for car in cars if car.id == id), None)
    if car is not None:
        return car
    return {"error": "Car not found"}, 404


@app.put("/cars/{id}/characteristics", response_model=Car)
def update_car_characteristics(id: str, characteristics: Characteristics):
    car = next((car for car in cars if car.id == id), None)
    if car is not None:
        car.characteristics = characteristics
        return car
    return {"error": "Car not found"}, 404


