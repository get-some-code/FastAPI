# Import BaseModel and StrictInt from Pydantic
from pydantic import BaseModel, StrictInt


# Patient model with normal integer validation
class Patient(BaseModel):

    # Patient's name
    name: str

    # Pydantic automatically converts compatible values to int
    age: int


# Patient model with strict integer validation
class Patient2(BaseModel):

    # Patient's name
    name: str

    # Only accepts an actual integer (no type conversion)
    age: StrictInt


# Function to display patient details
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age, type(patient.age))
    print("Successfully inserted to Database\n")


# Valid data (age is already an integer)
patient_info1 = {
    'name': 'John Doe',
    'age': 37
}

# Age is provided as a string
patient_info2 = {
    'name': 'Johnny Depp',
    'age': '38'
}


# Creates a Patient object successfully
patient1 = Patient(**patient_info1)

# Also creates successfully because Pydantic converts "38" -> 38
patient2 = Patient(**patient_info2)

insert_patient_data(patient1)
insert_patient_data(patient2)


# This line raises a ValidationError because StrictInt
# does not allow automatic conversion from string to integer
patient2 = Patient2(**patient_info2)

# This line will never execute because the previous line throws an error
insert_patient_data(patient2)