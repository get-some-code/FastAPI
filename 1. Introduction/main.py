# Import the FastAPI class
from fastapi import FastAPI

# Create a FastAPI application instance
app = FastAPI()


# Home endpoint
# Access it at: http://127.0.0.1:8000/
@app.get("/")
def greet():
    return {
        'message': 'Hello'
    }


# About endpoint
# Access it at: http://127.0.0.1:8000/about
@app.get("/about")
def about():
    return {
        'message': 'Learning FastAPI'
    }