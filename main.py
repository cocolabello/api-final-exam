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

# get /cars: recup la liste d'objet sauuvegardée en memoire precedemment
@app.get("/cars", response_model=List[Car])
def get_cars():
    return cars

# get /cars/{id} : permet d'obtenir un phone particulier u {id} est l'identifiant de la voiture
# dans le cas ou l'identifiant fourni n'est pas trouvé dans la liste sauvegardée en memoire vive, alors il faut retourner une reponse avec un code status 404 ainisi qu'un message d''erreur indiquant que le phone comportant l'id fourni n'existe pas ou pas trouvée
@app.get("/cars/{id}", response_model=Car)
def get_car(id: str):
    car = next((car for car in cars if car.id == id), None)
    if car is not None:
        return car
    return {"error": "Car not found"}, 404

# uvicorn main:app --reload

