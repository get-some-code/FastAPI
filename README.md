<div align="center">

# ⚡ FastAPI

### The modern, fast (high-performance) web framework for building APIs with Python

<em>Based on standard Python type hints.</em>

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Uvicorn](https://img.shields.io/badge/Server-Uvicorn-2E2E2E?style=for-the-badge)](https://www.uvicorn.org)
[![Pydantic](https://img.shields.io/badge/Validation-Pydantic-E92063?style=for-the-badge)](https://docs.pydantic.dev)

<br>

**Key features:** Fast to code • Fewer bugs • Intuitive • Easy • Short • Robust • Standards-based

</div>

---

## 📖 Table of Contents

- [✨ Overview](#-overview)
- [🚀 Why FastAPI?](#-why-fastapi)
- [📦 Installation](#-installation)
- [⚡ Quick Start](#-quick-start)
- [🧩 Path Parameters](#-path-parameters)
- [🔎 Query Parameters](#-query-parameters)
- [📨 Request Body (Pydantic Models)](#-request-body-pydantic-models)
- [✅ Data Validation](#-data-validation)
- [🧠 Dependency Injection](#-dependency-injection)
- [🔐 Authentication (OAuth2 + JWT)](#-authentication-oauth2--jwt)
- [🗄️ Database Integration](#️-database-integration)
- [⚙️ Middleware](#️-middleware)
- [🚨 Error Handling](#-error-handling)
- [📄 Automatic Docs](#-automatic-docs)
- [🧵 Async & Concurrency](#-async--concurrency)
- [🧪 Testing](#-testing)
- [🐳 Deployment](#-deployment)
- [📁 Recommended Project Structure](#-recommended-project-structure)
- [📚 Resources](#-resources)

---

## ✨ Overview

> **FastAPI** is a modern, high-performance web framework for building APIs with Python, based on standard Python type hints. It combines the raw speed of **Starlette** (ASGI) with the data validation power of **Pydantic**.

| Feature | Description |
|---|---|
| 🚀 **Performance** | One of the fastest Python frameworks available, on par with **NodeJS** and **Go** |
| 🧠 **Intuitive** | Great editor support, autocompletion everywhere, less debugging |
| 📝 **Type Hints** | Uses standard Python type hints — no new syntax to learn |
| 📄 **Auto Docs** | Interactive API documentation generated automatically (Swagger UI & ReDoc) |
| ✅ **Validation** | Automatic request validation, serialization, and clear error messages |
| 🔌 **Standards-based** | Fully compatible with **OpenAPI** and **JSON Schema** |

---

## 🚀 Why FastAPI?

```
📈 Benchmarks (relative throughput)

FastAPI (Uvicorn)   ████████████████████  🟢 Very High
Flask               ███████               🟡 Moderate
Django              ██████                🟡 Moderate
```

- 🏎️ **Fast**: Very high performance, thanks to Starlette and Pydantic
- ⏱️ **Fast to code**: Increases development speed by 200%–300%
- 🐛 **Fewer bugs**: Reduces ~40% of human-induced errors
- 💡 **Intuitive**: Best-in-class editor support with completion everywhere
- 📏 **Easy**: Designed to be easy to use and learn — less time reading docs
- 🔗 **Short**: Minimizes code duplication, fewer bugs from each parameter declaration

---

## 📦 Installation

> Requires **Python 3.8+**

```bash
pip install fastapi
```

You'll also need an ASGI server for production, such as **Uvicorn** or **Hypercorn**:

```bash
pip install "uvicorn[standard]"
```

<details>
<summary>💡 <strong>Install with all optional dependencies</strong></summary>

```bash
pip install "fastapi[all]"
```

This includes `uvicorn`, `pydantic-settings`, `python-multipart`, `jinja2`, and more.

</details>

---

## ⚡ Quick Start

**1. Create `main.py`**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

**2. Run the server**

```bash
uvicorn main:app --reload
```

| Symbol | Meaning |
|---|---|
| `main` | the file `main.py` (the Python "module") |
| `app` | the object created inside `main.py` with `app = FastAPI()` |
| `--reload` | restart the server after code changes (development only) |

**3. Check it out**

```
🌐 http://127.0.0.1:8000            → {"message": "Hello, World!"}
📄 http://127.0.0.1:8000/docs       → Swagger UI
📘 http://127.0.0.1:8000/redoc      → ReDoc
```

---

## 🧩 Path Parameters

```python
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
```

> ⚠️ Because of the `int` type hint, FastAPI automatically **validates** and **converts** the value. If someone sends `/users/abc`, they get a clean HTTP 422 error — automatically.

**Predefined values with Enums:**

```python
from enum import Enum

class ModelName(str, Enum):
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    return {"model_name": model_name}
```

---

## 🔎 Query Parameters

```python
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10, q: str | None = None):
    return {"skip": skip, "limit": limit, "q": q}
```

```
GET /items/?skip=0&limit=10&q=laptop
```

- Parameters **not** in the path are automatically treated as query parameters
- Parameters with a default value are **optional**
- Parameters without a default value are **required**

---

## 📨 Request Body (Pydantic Models)

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
def create_item(item: Item):
    total = item.price + (item.tax or 0)
    return {"name": item.name, "total_price": total}
```

<div align="left">

📥 **Request**
```json
{
  "name": "Mechanical Keyboard",
  "price": 59.99,
  "tax": 4.5
}
```

📤 **Response**
```json
{
  "name": "Mechanical Keyboard",
  "total_price": 64.49
}
```

</div>

---

## ✅ Data Validation

FastAPI leans on **Pydantic** + `Field`/`Query`/`Path` for rich, declarative validation:

```python
from fastapi import Query
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0, description="Must be greater than zero")

@app.get("/search/")
def search(q: str | None = Query(default=None, max_length=50)):
    return {"q": q}
```

> 🛑 Invalid input never reaches your function body — FastAPI rejects it with a descriptive `422 Unprocessable Entity` response before your code even runs.

---

## 🧠 Dependency Injection

A first-class, elegant **Dependency Injection** system — great for shared logic (DB sessions, auth, pagination, etc.).

```python
from fastapi import Depends

def common_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/users/")
def read_users(commons: dict = Depends(common_params)):
    return commons
```

- ♻️ Reusable across many path operations
- 🧵 Supports sync **and** async dependencies
- 🪆 Dependencies can depend on other dependencies (nested)

---

## 🔐 Authentication (OAuth2 + JWT)

```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_current_user(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"token": token}
```

> 🔑 FastAPI has built-in utilities for **OAuth2**, **API keys**, **HTTP Basic**, and **JWT**-based flows via the `fastapi.security` module.

---

## 🗄️ Database Integration

Works with any ORM. Common pairing: **SQLModel** (by the same author) or **SQLAlchemy**.

```python
from sqlmodel import SQLModel, Field, Session, create_engine

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    power: str

engine = create_engine("sqlite:///database.db")

def get_session():
    with Session(engine) as session:
        yield session

@app.post("/heroes/")
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero
```

---

## ⚙️ Middleware

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

| Middleware | Purpose |
|---|---|
| `CORSMiddleware` | Cross-Origin Resource Sharing |
| `GZipMiddleware` | Compress large responses |
| `TrustedHostMiddleware` | Restrict allowed `Host` headers |
| Custom `@app.middleware("http")` | Logging, timing, auth headers, etc. |

---

## 🚨 Error Handling

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]
```

**Custom exception handlers:**

```python
from fastapi.responses import JSONResponse
from fastapi import Request

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something wrong."},
    )
```

---

## 📄 Automatic Docs

FastAPI generates interactive documentation automatically, from your code, for free:

```
┌────────────────────────────────────────────┐
│  📄  /docs    → Swagger UI (try it live)    │
│  📘  /redoc   → ReDoc (clean reference)     │
│  🧬  /openapi.json → Raw OpenAPI schema     │
└────────────────────────────────────────────┘
```

> No extra config needed — the docs update automatically as you add or change endpoints.

---

## 🧵 Async & Concurrency

```python
import httpx

@app.get("/external-data")
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
    return response.json()
```

- Use `async def` when your function performs `await`-able I/O (DB calls, HTTP requests)
- Use regular `def` for CPU-bound or blocking sync code — FastAPI runs it in a thread pool automatically
- Both can be mixed freely across different path operations

---

## 🧪 Testing

FastAPI is built for easy testing with `TestClient` (powered by `httpx`):

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
```

```bash
pytest -v
```

---

## 🐳 Deployment

**Dockerfile:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

**Production server (with Gunicorn + Uvicorn workers):**

```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

---

## 📁 Recommended Project Structure

```
📦 my-fastapi-app
├── 📂 app
│   ├── 📄 main.py            # FastAPI app instance & route includes
│   ├── 📂 routers            # Modular route definitions
│   │   ├── users.py
│   │   └── items.py
│   ├── 📂 models             # Pydantic / SQLModel schemas
│   ├── 📂 dependencies       # Shared dependencies (auth, db, etc.)
│   ├── 📂 core               # Config, security, settings
│   └── 📂 db                 # Database session & models
├── 📂 tests
├── 📄 requirements.txt
├── 📄 Dockerfile
└── 📄 README.md
```

---

## 📚 Resources

| Resource | Link |
|---|---|
| 📘 Official Docs | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| 💻 GitHub Repo | [github.com/fastapi/fastapi](https://github.com/fastapi/fastapi) |
| 🧬 Starlette (ASGI toolkit) | [starlette.io](https://www.starlette.io) |
| ✅ Pydantic (validation) | [docs.pydantic.dev](https://docs.pydantic.dev) |
| 🗄️ SQLModel | [sqlmodel.tiangolo.com](https://sqlmodel.tiangolo.com) |

---

<div align="center">

### 🧡 Built with FastAPI

*"Fast to code, fast to run."*

<sub>This README is a learning/reference document formatted in the style of official framework documentation.</sub>

</div>