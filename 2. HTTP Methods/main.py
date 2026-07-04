from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('./patients.json', 'r') as f:
        data = json.load(f)      
    return data

@app.get("/")
def homePage():
    return {'message': 'Patient Management System API'}

@app.get("/about")
def aboutPage():
    return {'message': "A fully functional API to manage your patient records."}

@app.get("/patients")
def allPatientsPage():
    data = load_data()
    return data