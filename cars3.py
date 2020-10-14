def makeCar(make, model, **details):
    """
    Returns make, model, and other details for a car.
    """
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in details.items():
        car[key] = value
    return car

newCar = makeCar('tesla', 'model 3', type='P100D', color='forest green')
print(newCar)