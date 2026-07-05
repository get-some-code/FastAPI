from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List

class Profile(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedIn: AnyUrl
    contact: str
    skills: List[str]

def insertProfile(profile: Profile):
    print("Name: ", profile.name)
    print("Age: ", profile.age)
    print("Email: ", profile.email)
    print("Linked In: ", profile.linkedIn)
    print("Skills: ", profile.skills)

    print("\nProfile Added to Database\n")

profile1 = {
    'name': 'Monideep Mistry',
    'age': 20,
    'email': 'monideepmistry365@gmail.com',
    'linkedIn': 'https://www.linkedin.com/in/monideepmistry/',
    'contact': 'xxxxxx3909',
    'skills': ["Python", "Java", "Generative AI", "Machine Learning", "Deep Learning", "SQL"]
}

profile2 = {
    'name': 'John Doe',
    'age': 24,
    'email': 'jd02gmail.com', # '@' missing -> pydantic won't validate
    'linkedIn': 'https://www.linkedin.com/in/johndoe/',
    'contact': 'xxxxxx3909',
    'skills': ["Python", "Ruby", "Generative AI", "Pytorch", "Deep Learning", "SQL"]
}


insertProfile(profile=Profile(**profile1))
insertProfile(profile=Profile(**profile2))