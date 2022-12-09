"""
    BKPI/BIOMA Challenge Code
    CRUD by Rafael Henrique Guimarães 
"""

from fastapi import FastAPI

app = FastAPI()

"""
    Using Hash Map, because it becomes more easiear to implement alterations, like put and delete.
"""
CARS = {
    'car_1': {'nome': 'gol', 'marca': 'volkswagen'},
    'car_2': {'nome': 'uno', 'marca': 'fiat'},
    'car_3': {'nome': 'palio', 'marca': 'fiat'},
    'car_4': {'nome': 'hb20', 'marca': 'hyundai'},   
}
"""
GET ---- Return all cars
"""

@app.get("/")
def all_cars():
    return CARS

"""
GET Specific cars by ID
"""
@app.get("/{car_id}")
def read_car(car_id: str):
    return CARS[car_id]
"""
POST --- Insert into Hash Map, another vehicle
"""
@app.post("/")
def create_car(car_name, car_marca):
    current_car_id = 0

    if len(CARS) > 0:
        for car in CARS:
            x = int(car.split('_')[-1])
            if x > current_car_id:
                current_car_id = x

    CARS[f'car_{current_car_id + 1}'] = {'name': car_name, 'marca': car_marca}
    return CARS[f'car_{current_car_id + 1}']

"""
PUT ---- Update a specific car by ID (car_id)
"""
@app.put("/{car_name}")
def update_car(car_id:str, car_name: str, car_marca: str):
    car_content = {'name': car_name, 'marca': car_marca}
    CARS[car_id] = car_content
    return car_content

"""
DELETE ---- Delete a specific car by ID (car_id) 

"""
@app.delete("/{car_name}")
def delete_car(car_name):
    del CARS[car_name]
    return f'Car {car_name} deleted.'
