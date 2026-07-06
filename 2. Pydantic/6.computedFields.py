# Import BaseModel and computed_field from Pydantic
from pydantic import BaseModel, computed_field


# Patient model
class Patient(BaseModel):

    # Patient's name
    name: str

    # Patient's age
    age: int

    # Height in meters
    height: float

    # Weight in kilograms
    weight: float

    # Computed field (not provided by the user)
    # BMI is automatically calculated from height and weight
    @computed_field
    @property
    def bmi(self) -> float:

        # BMI = Weight / (Height²)
        bmi = round(self.weight / (self.height ** 2), 2)

        return bmi


# Function to display patient details
def insertPatient(patient: Patient):

    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Height:", patient.height, "m")
    print("Weight:", patient.weight, "kg")

    # Access the computed field like a normal attribute
    print("BMI:", patient.bmi)

    print("\nSuccessfully inserted into Database\n")


# Patient data
patient_info = {
    "name": "Virat Kohli",
    "age": 37,
    "height": 1.75,
    "weight": 70
}


# Create a validated Patient object
patient = Patient(**patient_info)

# Display patient information
insertPatient(patient)

# Convert the model into a dictionary
# Notice that the computed field (bmi) is included
print(patient.model_dump())