from fastapi import FastAPI, Path, Query, HTTPException
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

@app.get("/patients/{patient_id}")
def viewPatient(patient_id: str = Path(..., description='ID of the patient in the database', example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Oops! Patient Not Found!')

@app.get("/sort")
def sortPatients(sort_by: str = Query(..., description='Sort on the basis of height, weight and bmi'), order: str = Query('asc', description='sort in ascending or descending order. Ascending is set by default.')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field. Select from {valid_fields}')
    if order not in ['asc', 'des']:
        raise HTTPException(status_code=400, detail='Invalid order. Select from ["asc", "des"].')
    
    data = load_data()

    sort_order = True if order == 'des' else False
    sorted_data = sorted(data.values(), key=lambda x : x.get(sort_by, 0), reverse=sort_order)

    return sorted_data