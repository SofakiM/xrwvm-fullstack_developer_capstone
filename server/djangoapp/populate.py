from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology",
            "website": "https://www.nissan.de",
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
            "website": "https://www.mercedes-benz.de",
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology",
            "website": "https://www.audi.de",
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology",
            "website": "https://www.kia.com",
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology",
            "website": "https://www.toyota.de",
        },
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'],
                                  description=data['description'],
                                  website=data['website'])
        )


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {
        "name": "Pathfinder",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[0],
        "fuel_consumption": "23 MPG",
      },
      {
        "name": "Qashqai",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[0],
        "fuel_consumption": "23 MPG",
      },
      {
        "name": "XTRAIL",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[0],
        "fuel_consumption": "20 MPG",
      },
      {
        "name": "A-Class",
        "type": "SUV",
        "year": 2023
        "car_make": car_make_instances[1],
        "fuel_consumption": "19 MPG",
      },
      {
        "name": "C-Class",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[1],
        "fuel_consumption": "25 MPG",
      },
      {
        "name": "E-Class",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[1],
        "fuel_consumption": "23 MPG",
      },
      {
        "name": "A4",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[2],
        "fuel_consumption": "21 MPG",
      },
      {
        "name": "A5",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[2],
        "fuel_consumption": "15 MPG",
      },
      {
        "name": "A6",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[2],
        "fuel_consumption": "17 MPG",
      },
      {
        "name": "Sorrento",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[3],
        "fuel_consumption": "25 MPG",
      },
      {
        "name": "Carnival",
        "type": "SUV", 
        "year": 2023,
        "car_make": car_make_instances[3],
        "fuel_consumption": "18 MPG",
      },
      {
        "name": "Cerato",
        "type": "Sedan",
        "year": 2023,
        "car_make": car_make_instances[3],
        "fuel_consumption": "22 MPG",
      },
      {
        "name": "Corolla",
        "type": "Sedan",
        "year": 2023,
        "car_make": car_make_instances[4],
        "fuel_consumption": "23 MPG",
      },
      {
        "name": "Camry",
        "type": "Sedan",
        "year": 2023,
        "car_make": car_make_instances[4],
        "fuel_consumption": "20 MPG",
      },
      {
        "name": "Kluger",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[4],
        "fuel_consumption": "15 MPG",
      },
    ]

    for data in car_model_data:
        CarModel.objects.create(name = data['name'],
                                car_make = data['car_make'],
                                type = data['type'],
                                year = data['year'],
                                fuel_consumption = ['fuel_consumption'],
        )
