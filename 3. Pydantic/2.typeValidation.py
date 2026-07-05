from pydantic import BaseModel
from typing import List, Dict, Optional

class Players(BaseModel):
    name: str
    age: int
    bmi: float
    married: Optional[bool] = None #optional field
    centuries: int
    stats: List[Dict[str, str]]
    contact: Dict[str, str]


def insertPlayerInfo(player: Players):
    print('\nName: ', player.name)
    print('Age: ',player.age)
    print('BMI: ',player.bmi)
    print('Married: ',player.married)
    print('Centuries: ',player.centuries)
    print('Stats: ',player.stats)
    print('Contact: ',player.contact)

    print("\nSuccessfully inserted to Database\n")


player_info1 = {
    'name': 'Virat Kohli', 
    'age': 37, 
    'bmi': 24.4, 
    'married': 1, 
    'centuries': 85, 
    'stats': [{"odi_runs": '14797', "test_runs": '9230'}, {"odi_average": '58.72', "test_average": '46.85'}],
    'contact': {"email": "vk18@gmail.com", 'phone': "xxxxxx7944"}
}

player_info2 = {
    'name': 'Hardik Pandya', 
    'age': 32, 
    'bmi': 22.4,  
    'centuries': 1, 
    'stats': [{"odi_runs": '1904', "test_runs": '532'}, {"odi_average": '32.83', "test_average": '31.29'}],
    'contact': {"email": "hp33@gmail.com", 'phone': "xxxxxx4585"}
}

player1 = Players(**player_info1)
player2 = Players(**player_info2)

insertPlayerInfo(player1)
insertPlayerInfo(player2)