# Import required classes and functions from Pydantic
from pydantic import BaseModel, Field, EmailStr, field_validator

# Import Annotated to add validation metadata to fields
from typing import Annotated


# Student model with field validations
class Student(BaseModel):

    # Student name
    name: str

    # Age must be an integer (strict), between 16 and 40
    age: Annotated[int, Field(strict=True, ge=16, le=40)]

    # Section must contain exactly one character (e.g., A, B, C)
    section: Annotated[str, Field(min_length=1, max_length=1)]

    # Roll number must be between 1 and 99
    rollNo: Annotated[int, Field(ge=1, le=99)]

    # Must be a valid email address
    collegeMail: EmailStr

    # Degree name can have a maximum of 20 characters
    degree: Annotated[str, Field(max_length=20)]

    # Department name can have a maximum of 20 characters
    department: Annotated[str, Field(max_length=20)]

    # Specialization can have a maximum of 20 characters
    specialization: Annotated[str, Field(max_length=20)]

    # Duration must be an integer between 1 and 6 years
    duration: Annotated[
        int,
        Field(
            strict=True,
            ge=1,
            le=6,
            description="Enter duration of your course"
        )
    ]

    # Converts the student's name to uppercase
    @field_validator('name')
    @classmethod
    def transformName(cls, value):
        return value.upper()

    # Validates that the email belongs to IEM or UEM
    @field_validator('collegeMail')
    @classmethod
    def emailValidator(cls, value):

        # List of allowed college email domains
        valid_domain = ['uem.edu.in', 'iem.edu.in']

        # Extract domain from the email address
        domain_name = value.split('@')[-1]

        # Raise an error if the domain is not allowed
        if domain_name not in valid_domain:
            raise ValueError("Please provide your institution mail id")

        return value


# Function to display student details after successful validation
def IEM_Hackathon(student: Student):

    print("Name: ", student.name)
    print("Age: ", student.age)
    print("Section: ", student.section)
    print("Roll No: ", student.rollNo)
    print("Institute mail id: ", student.collegeMail)
    print("Degree: ", student.degree)
    print("Department: ", student.department)
    print("Specialization: ", student.specialization)
    print("Duration: ", student.duration)

    print("\nStudent eligible for hackathon\n")


# Invalid student (email domain is not allowed)
student1 = {
    'name': 'Dinesh Karthik',
    'age': 21,
    'section': 'G',
    'rollNo': 75,
    'collegeMail': 'dk19@gmail.com',
    'degree': 'B.Tech',
    'department': 'CSE',
    'specialization': 'Data Science',
    'duration': 4
}

# Valid student (college email belongs to iem.edu.in)
student2 = {
    'name': 'Gautam Gambhir',
    'age': 24,
    'section': 'D',
    'rollNo': 1,
    'collegeMail': 'gg@iem.edu.in',
    'degree': 'B.Tech',
    'department': 'CSE',
    'specialization': 'AI/ML',
    'duration': 4
}

# This will pass all validations and print the student details
IEM_Hackathon(student=Student(**student2))

# This will raise a ValidationError because the email domain is invalid
IEM_Hackathon(student=Student(**student1))