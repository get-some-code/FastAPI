import jwt

SECRET_KEY = "my-super-secret-key-for-fastapi-jwt-2026"
ALGORITHM = "HS256"


def create_access_token(email: str):

    payload = {
        "sub": email
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# token = create_access_token("moni@gmail.com")

# print("TOKEN:")
# print(token)

# decoded = jwt.decode(
#     token,
#     SECRET_KEY,
#     algorithms=[ALGORITHM]
# )

# print("DECODED:")
# print(decoded)