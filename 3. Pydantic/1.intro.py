from pydantic import BaseModel, StrictInt

class Patient(BaseModel):

    name: str
    age: int

class Patient2(BaseModel):
    name: str
    age: StrictInt

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age, type(patient.age))
    print("Successfully inserted to Database\n")

patient_info1 = {'name': 'John Doe', 'age': 37}
patient_info2 = {'name': 'Johnny Depp', 'age': '38'}

patient1 = Patient(**patient_info1)
patient2 = Patient(**patient_info2)

insert_patient_data(patient1)
insert_patient_data(patient2)

patient2 = Patient2(**patient_info2)
insert_patient_data(patient2)