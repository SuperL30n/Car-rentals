### SETTING UP THE PROJECT
## IMPORT INFORMATION 
all this should be done with the command prompt and not windows powershell
## CLONE THE REPO INTO THE LOCAL MACHINE
```
    git clone https://github.com/ruggedwizard/car_rentals.git
```

## SETTING UP A VIRTUAL ENVIRONMENT FOR LOCAL DEVELOPMENT (OPTIONAL)
>[!note] This step will prevent dependencies error, it will also ensure dependencies dont conflict with the systems dependencties
``` 
    python -m venv venv
```

## TO ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS BASE COMPUTER)
```
    venv\scripts\activate
```
## INSTALLING THE PROJECT DEPENDENCIES 
```
    pip install -r requirements.txt
```
## RUNNING THE LOCAL SERVER
```
    python manage.py runserver
```

