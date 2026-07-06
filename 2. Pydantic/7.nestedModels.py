# Import BaseModel from Pydantic
from pydantic import BaseModel


# Nested model to store address details
class Address(BaseModel):

    # City name
    city: str

    # State name
    state: str

    # Postal/PIN code
    pincode: str


# Patient model
class Patient(BaseModel):

    # Patient's name
    name: str

    # Patient's gender
    gender: str

    # Patient's age
    age: int

    # Nested Address model
    # Instead of storing address as a normal dictionary,
    # it is validated using the Address model.
    address: Address


# Address data
address1 = {
    'city': 'Kolkata',
    'state': 'West Bengal',
    'pincode': '700104'
}

# Convert dictionary into an Address object
address = Address(**address1)


# Patient data
patient1 = {
    'name': 'John Doe',
    'gender': 'M',
    'age': 24,

    # Pass the Address object
    'address': address
}

# Create a validated Patient object
patient = Patient(**patient1)

# Print the complete patient object
print(patient)

# Access nested model attributes
print(patient.address.city)
print(patient.address.state)
print(patient.address.pincode)