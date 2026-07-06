# Import BaseModel from Pydantic
from pydantic import BaseModel

# Import required typing hints
from typing import List, Dict, Optional


# Player model
class Players(BaseModel):

    # Player's name
    name: str

    # Player's age
    age: int

    # Player's Body Mass Index
    bmi: float

    # Optional field (defaults to None if not provided)
    married: Optional[bool] = None

    # Total international centuries
    centuries: int

    # List of dictionaries containing player statistics
    stats: List[Dict[str, str]]

    # Dictionary containing contact information
    contact: Dict[str, str]


# Function to display player information
def insertPlayerInfo(player: Players):

    print('\nName: ', player.name)
    print('Age: ', player.age)
    print('BMI: ', player.bmi)
    print('Married: ', player.married)
    print('Centuries: ', player.centuries)
    print('Stats: ', player.stats)
    print('Contact: ', player.contact)

    print("\nSuccessfully inserted to Database\n")


# Player 1 data
player_info1 = {
    'name': 'Virat Kohli',
    'age': 37,
    'bmi': 24.4,

    # Pydantic converts 1 to True automatically
    'married': 1,

    'centuries': 85,

    # List of dictionaries storing batting statistics
    'stats': [
        {"odi_runs": '14797', "test_runs": '9230'},
        {"odi_average": '58.72', "test_average": '46.85'}
    ],

    # Dictionary storing contact details
    'contact': {
        "email": "vk18@gmail.com",
        'phone': "xxxxxx7944"
    }
}


# Player 2 data
player_info2 = {
    'name': 'Hardik Pandya',
    'age': 32,
    'bmi': 22.4,

    # married is omitted, so it defaults to None
    'centuries': 1,

    'stats': [
        {"odi_runs": '1904', "test_runs": '532'},
        {"odi_average": '32.83', "test_average": '31.29'}
    ],

    'contact': {
        "email": "hp33@gmail.com",
        'phone': "xxxxxx4585"
    }
}


# Convert dictionaries into validated Pydantic objects
player1 = Players(**player_info1)
player2 = Players(**player_info2)

# Display player information
insertPlayerInfo(player1)
insertPlayerInfo(player2)