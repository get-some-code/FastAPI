# Import required modules
from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
from pathlib import Path as FilePath
import json

# ---------------------------------------------------------------------
# Path to patients.json
# Project Structure:
#
# FASTAPI/
# │── patients.json
# └── 3. HTTP Methods/
#     └── 2. POST/
#         └── main.py
# ---------------------------------------------------------------------

DATA_FILE = FilePath(__file__).resolve().parent.parent / "patients.json"

# ---------------------------------------------------------------------
# Pydantic Model
# ---------------------------------------------------------------------

class Patient(BaseModel):
    id: Annotated[
        str,
        Field(
            description="ID of the patient",
            examples=["P001"]
        )
    ]

    name: Annotated[
        str,
        Field(
            max_length=50,
            description="Name of the patient"
        )
    ]

    city: Annotated[
        str,
        Field(
            max_length=20,
            description="City where the patient lives"
        )
    ]

    age: Annotated[
        int,
        Field(
            gt=0,
            lt=120,
            description="Age of the patient"
        )
    ]

    gender: Annotated[
        Literal["male", "female", "others"],
        Field(description="Gender of the patient")
    ]

    height: Annotated[
        float,
        Field(
            gt=0,
            description="Height in meters"
        )
    ]

    weight: Annotated[
        float,
        Field(
            gt=0,
            description="Weight in kilograms"
        )
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Underweight"

        elif self.bmi < 25:
            return "Normal"

        elif self.bmi < 30:
            return "Overweight"

        return "Obese"


# ---------------------------------------------------------------------
# FastAPI App
# ---------------------------------------------------------------------

app = FastAPI()


# ---------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------

def load_data():

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# ---------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------

@app.get("/")
def homePage():
    return {
        "message": "Patient Management System API"
    }


# ---------------------------------------------------------------------
# About
# ---------------------------------------------------------------------

@app.get("/about")
def aboutPage():
    return {
        "message": "A fully functional API to manage your patient records."
    }


# ---------------------------------------------------------------------
# Get all patients
# ---------------------------------------------------------------------

@app.get("/patients")
def allPatientsPage():
    return load_data()


# ---------------------------------------------------------------------
# Get a patient by ID
# ---------------------------------------------------------------------

@app.get("/patients/{patient_id}")
def viewPatient(
    patient_id: str = Path(
        ...,
        description="ID of the patient",
        examples=["P001"]
    )
):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found."
        )

    return data[patient_id]


# ---------------------------------------------------------------------
# Sort patients
# ---------------------------------------------------------------------

@app.get("/sort")
def sortPatients(

    sort_by: str = Query(
        ...,
        description="Sort by height, weight or bmi"
    ),

    order: str = Query(
        "asc",
        description="asc or des"
    )

):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Choose one of {valid_fields}"
        )

    if order not in ["asc", "des"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be asc or des."
        )

    data = load_data()

    sorted_data = sorted(
        data.values(),
        key=lambda patient: patient.get(sort_by, 0),
        reverse=(order == "des")
    )

    return sorted_data


# ---------------------------------------------------------------------
# Create a new patient
# ---------------------------------------------------------------------

@app.post("/create", status_code=201)
def createPatient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient ID already exists."
        )

    # Store patient without the ID field
    data[patient.id] = patient.model_dump(exclude={"id"})

    save_data(data)

    return {
        "message": "Patient created successfully."
    }

@app.delete("/delete/{patient_id}")
def deletePatient(patient_id):
    
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Oops! Patient Not Found")
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content="Patient deleted!")