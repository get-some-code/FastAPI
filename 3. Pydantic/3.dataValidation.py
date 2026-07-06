# Import required classes from Pydantic
from pydantic import BaseModel, EmailStr, AnyUrl, Field

# Import List and Annotated for type annotations and field metadata
from typing import List, Annotated


# Profile model with validation rules
class Profile(BaseModel):

    # Name should have a maximum of 50 characters
    # title, description and examples are mainly used in API documentation
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the person",
            description="Name of the person must have less than 50 characters",
            examples=["John Doe", "Johnny Depp"]
        )
    ]

    # Age must be greater than 16 and less than 45
    age: int = Field(gt=16, lt=45)

    # Must be a valid email address
    email: EmailStr

    # Experience defaults to 0 if not provided
    experience: Annotated[
        int,
        Field(
            default=0,
            description="Is the person experienced in tech?"
        )
    ]

    # Must be a valid URL
    linkedIn: AnyUrl

    # Contact number (no validation applied here)
    contact: str

    # Maximum of 8 skills can be provided
    skills: List[str] = Field(max_length=8)


# Function to display profile details
def insertProfile(profile: Profile):

    print("Name: ", profile.name)
    print("Age: ", profile.age)
    print("Email: ", profile.email)
    print("Experience: ", profile.experience)
    print("Linked In: ", profile.linkedIn)
    print("Skills: ", profile.skills)

    print("\nProfile Added to Database\n")


# Valid profile
profile1 = {
    'name': 'Monideep Mistry',
    'age': 20,
    'email': 'monideepmistry365@gmail.com',
    'experience': 1,
    'linkedIn': 'https://www.linkedin.com/in/monideepmistry/',
    'contact': 'xxxxxx3909',
    'skills': [
        "Python",
        "Java",
        "Generative AI",
        "Machine Learning",
        "Deep Learning",
        "SQL"
    ]
}


# Invalid profile (email format is incorrect)
profile2 = {
    'name': 'John Doe',
    'age': 24,
    'email': 'jd02mail.com',  # '@' is missing
    'linkedIn': 'https://www.linkedin.com/in/johndoe/',
    'contact': 'xxxxxx3909',
    'skills': [
        "Python",
        "Ruby",
        "Generative AI",
        "Pytorch",
        "Deep Learning",
        "SQL"
    ]
}


# This will pass all validations
insertProfile(profile=Profile(**profile1))

# This will raise a ValidationError because the email is invalid
insertProfile(profile=Profile(**profile2))