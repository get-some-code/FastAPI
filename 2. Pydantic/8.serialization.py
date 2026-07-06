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
    # Pydantic will validate this field using the Address model.
    address: Address


# ----------------------- Example Data -----------------------

# Address information
address1 = {
    "city": "Kolkata",
    "state": "West Bengal",
    "pincode": "700104"
}

# Convert the dictionary into an Address object
address = Address(**address1)

# Patient information
patient1 = {
    "name": "John Doe",
    "gender": "M",
    "age": 24,

    # Pass the Address object
    "address": address
}

# Create a validated Patient object
patient = Patient(**patient1)


# ============================================================
# model_dump()
# Converts the Pydantic model into a Python dictionary.
# ============================================================

temp1 = patient.model_dump()

print("\n================== model_dump() ==================\n")
print(temp1)
print(type(temp1))      # <class 'dict'>


# ============================================================
# model_dump_json()
# Converts the model into a JSON string.
# ============================================================

temp2 = patient.model_dump_json()

print("\n================ model_dump_json() ================\n")
print(temp2)
print(type(temp2))      # <class 'str'>


# ============================================================
# include
# Returns only the specified fields.
# ============================================================

temp3 = patient.model_dump(include={"name", "gender"})

print("\n==================== include ======================\n")
print(temp3)


# ============================================================
# exclude
# Excludes the specified fields.
# ============================================================

temp4 = patient.model_dump(exclude={"name", "gender"})

print("\n==================== exclude ======================\n")
print(temp4)


# ============================================================
# Excluding a nested field
# Removes only the 'state' field from the nested Address model.
# ============================================================

temp5 = patient.model_dump(
    exclude={
        "address": {"state"}
    }
)

print("\n============== exclude nested field ===============\n")
print(temp5)


# ============================================================
# exclude_unset=True
#
# Returns only the fields that were explicitly provided while
# creating the model.
#
# In this example, all fields were supplied by the user,
# so the output is the same as model_dump().
# ============================================================

temp6 = patient.model_dump(exclude_unset=True)

print("\n=============== exclude_unset=True ================\n")
print(temp6)


# ============================================================
# exclude_none=True
#
# Removes fields whose value is None.
# Since none of the fields are None, the output remains unchanged.
# ============================================================

temp7 = patient.model_dump(exclude_none=True)

print("\n================ exclude_none=True ================\n")
print(temp7)


# ============================================================
# exclude_defaults=True
#
# Removes fields whose values are equal to their default values.
# Since no fields have default values in this model,
# the output remains unchanged.
# ============================================================

temp8 = patient.model_dump(exclude_defaults=True)

print("\n============= exclude_defaults=True ===============\n")
print(temp8)

print("\n===================================================\n")