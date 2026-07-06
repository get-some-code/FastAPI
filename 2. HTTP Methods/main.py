# Import required modules
from fastapi import FastAPI, Path, Query, HTTPException
import json

# Create a FastAPI application instance
app = FastAPI()


# Function to read patient data from the JSON file
def load_data():
    with open('./patients.json', 'r') as f:
        data = json.load(f)
    return data


# Home endpoint
@app.get("/")
def homePage():
    return {'message': 'Patient Management System API'}


# About endpoint
@app.get("/about")
def aboutPage():
    return {'message': "A fully functional API to manage your patient records."}


# Returns all patients from the JSON file
@app.get("/patients")
def allPatientsPage():
    data = load_data()
    return data


# Returns details of a specific patient using the patient ID
@app.get("/patients/{patient_id}")
def viewPatient(
    patient_id: str = Path(
        ...,
        description="ID of the patient in the database",
        example="P001"
    )
):
    data = load_data()

    # Check if the patient exists
    if patient_id in data:
        return data[patient_id]

    # Return a 404 error if the patient is not found
    raise HTTPException(
        status_code=404,
        detail="Oops! Patient Not Found!"
    )


# Sort patients based on height, weight or BMI
@app.get("/sort")
def sortPatients(

    # Query parameter for selecting the sorting field
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight and bmi"
    ),

    # Query parameter for selecting sort order
    # Default is ascending
    order: str = Query(
        "asc",
        description="Sort in ascending or descending order. Ascending is the default."
    )
):

    # Allowed fields for sorting
    valid_fields = ["height", "weight", "bmi"]

    # Validate the sort field
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Select from {valid_fields}"
        )

    # Validate the sort order
    if order not in ["asc", "des"]:
        raise HTTPException(
            status_code=400,
            detail='Invalid order. Select from ["asc", "des"].'
        )

    # Load patient data
    data = load_data()

    # reverse=True -> Descending
    # reverse=False -> Ascending
    sort_order = True if order == "des" else False

    # Sort patients based on the selected field
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    # Return the sorted list
    return sorted_data