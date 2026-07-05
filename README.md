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
- [📨 Request Body & Pydantic Models](#-request-body--pydantic-models)
- [🧬 Pydantic Deep Dive](#-pydantic-deep-dive)
- [✅ Data Validation](#-data-validation)
- [🧠 Dependency Injection](#-dependency-injection)
- [🔐 Authentication (OAuth2 + JWT)](#-authentication-oauth2--jwt)
- [🗄️ Database Integration](#️-database-integration)
- [⚙️ Middleware](#️-middleware)
- [🚨 Error Handling](#-error-handling)
- [📟 HTTP Status Codes Reference](#-http-status-codes-reference)
- [📄 Automatic Docs](#-automatic-docs)
- [🧵 Async & Concurrency](#-async--concurrency)
- [🔄 Background Tasks](#-background-tasks)
- [📡 WebSockets](#-websockets)
- [📁 File Uploads](#-file-uploads)
- [🧪 Testing](#-testing)
- [🐳 Docker & Deployment](#-docker--deployment)
- [📁 Recommended Project Structure](#-recommended-project-structure)
- [🧭 Best Practices Checklist](#-best-practices-checklist)
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
| ⚡ **Async-native** | Built on ASGI — supports `async`/`await` throughout |

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
- 🌍 **Standards-based**: Based on (and fully compatible with) OpenAPI and JSON Schema

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

This includes `uvicorn`, `pydantic-settings`, `python-multipart`, `jinja2`, `httpx`, `orjson`, `email-validator`, and more.

</details>

---

## ⚡ Quick Start

**1. Create `main.py`**

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="A sample FastAPI application",
    version="1.0.0",
)

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
| `--host 0.0.0.0` | make the server accessible from other machines |
| `--port 8080` | run on a custom port |
| `--workers 4` | run multiple worker processes (production) |

**3. Check it out**

```
🌐 http://127.0.0.1:8000            → {"message": "Hello, World!"}
📄 http://127.0.0.1:8000/docs       → Swagger UI
📘 http://127.0.0.1:8000/redoc      → ReDoc
🧬 http://127.0.0.1:8000/openapi.json → Raw OpenAPI schema
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
    vgg = "vgg"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name is ModelName.resnet:
        return {"model_name": model_name, "message": "Deep Residual Learning"}
    return {"model_name": model_name, "message": "Some other model"}
```

**Path parameters containing paths:**

```python
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}
```

**Order matters** — fixed paths must be declared before dynamic ones:

```python
@app.get("/users/me")      # ✅ must come first
def read_current_user():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")  # otherwise this would catch "/users/me" too
def read_user(user_id: str):
    return {"user_id": user_id}
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
- Booleans, ints, floats, lists, and enums are all supported and auto-converted

**Multiple values / lists:**

```python
from fastapi import Query

@app.get("/tags/")
def get_tags(tag: list[str] = Query(default=[])):
    return {"tags": tag}

# GET /tags/?tag=python&tag=fastapi&tag=ai → {"tags": ["python", "fastapi", "ai"]}
```

---

## 📨 Request Body & Pydantic Models

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

**Combining path, query, and body parameters:**

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

FastAPI figures out where each parameter comes from automatically:
- Declared in the **path** → path parameter
- A **singular type** (`int`, `str`, `bool`, etc.) → query parameter
- Declared as a **Pydantic model** → request body

---

## 🧬 Pydantic Deep Dive

Pydantic is the data-validation backbone of FastAPI. It's what turns raw JSON into validated, typed Python objects — and back again.

**Field customization with `Field()`:**

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, examples=["Laptop"])
    price: float = Field(gt=0, description="Must be greater than zero")
    tags: set[str] = Field(default_factory=set)
    is_offer: bool | None = None
```

**Nested models:**

```python
class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    price: float
    images: list[Image] | None = None
```

**Validators (custom logic):**

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v
```

**Config & aliasing:**

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    full_name: str = Field(alias="fullName")
```

**Separate schemas for input/output** (common real-world pattern):

```python
class UserIn(BaseModel):
    username: str
    password: str  # accepted on input, never returned

class UserOut(BaseModel):
    username: str  # what the client actually sees

@app.post("/users/", response_model=UserOut)
def create_user(user: UserIn):
    # save user.password securely (hashed) — never echo it back
    return user
```

**Settings management with `pydantic-settings`** (great for env-based config):

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My API"
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
```

> 🧬 Pydantic v2 is written in Rust under the hood (via `pydantic-core`), which is a big part of why FastAPI's validation is so fast compared to older Python web frameworks.

---

## ✅ Data Validation

FastAPI leans on **Pydantic** + `Field`/`Query`/`Path`/`Body` for rich, declarative validation:

```python
from fastapi import Query, Path
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0, description="Must be greater than zero")

@app.get("/search/")
def search(q: str | None = Query(default=None, max_length=50, min_length=3)):
    return {"q": q}

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="Item ID", ge=1)):
    return {"item_id": item_id}
```

Common validation constraints:

| Constraint | Applies to | Meaning |
|---|---|---|
| `gt`, `ge` | numbers | greater than / greater or equal |
| `lt`, `le` | numbers | less than / less or equal |
| `min_length`, `max_length` | strings | length bounds |
| `regex` / `pattern` | strings | must match pattern |
| `min_items`, `max_items` | lists | number of items |

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

**Class-based dependencies:**

```python
class Pagination:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit

@app.get("/items/")
def list_items(pagination: Pagination = Depends()):
    return {"skip": pagination.skip, "limit": pagination.limit}
```

**Sub-dependencies (dependencies that depend on other dependencies):**

```python
def get_token(authorization: str = Header(...)):
    return authorization.replace("Bearer ", "")

def get_current_user(token: str = Depends(get_token)):
    return decode_token(token)

@app.get("/me")
def read_me(user=Depends(get_current_user)):
    return user
```

- ♻️ Reusable across many path operations
- 🧵 Supports sync **and** async dependencies
- 🪆 Dependencies can depend on other dependencies (nested)
- 🌍 Can be applied globally via `app = FastAPI(dependencies=[Depends(verify_key)])`

---

## 🔐 Authentication (OAuth2 + JWT)

```python
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + expires_delta})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

@app.get("/users/me")
def read_current_user(current_user: str = Depends(get_current_user)):
    return {"username": current_user}
```

> 🔑 FastAPI has built-in utilities for **OAuth2**, **API keys**, **HTTP Basic**, and **JWT**-based flows via the `fastapi.security` module.

**API key auth (simple alternative):**

```python
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

@app.get("/secure-data")
def get_secure_data(api_key: str = Depends(api_key_header)):
    if api_key != "expected-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"data": "secret"}
```

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

**Async SQLAlchemy (for high-concurrency apps):**

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db")

async def get_session():
    async with AsyncSession(engine) as session:
        yield session

@app.get("/heroes/")
async def list_heroes(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Hero))
    return result.scalars().all()
```

---

## ⚙️ Middleware

```python
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myfrontend.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"])
```

**Custom middleware (e.g. request timing / logging):**

```python
import time
from fastapi import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start_time)
    return response
```

| Middleware | Purpose |
|---|---|
| `CORSMiddleware` | Cross-Origin Resource Sharing |
| `GZipMiddleware` | Compress large responses |
| `TrustedHostMiddleware` | Restrict allowed `Host` headers |
| `HTTPSRedirectMiddleware` | Force HTTPS |
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

**Overriding the default validation error handler:**

```python
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )
```

---

## 📟 HTTP Status Codes Reference

FastAPI ships with `from fastapi import status`, giving you readable constants instead of magic numbers (`status.HTTP_404_NOT_FOUND` instead of `404`).

```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item
```

### 1xx — Informational

| Code | Constant | Meaning |
|---|---|---|
| 100 | `HTTP_100_CONTINUE` | Client should continue the request |
| 101 | `HTTP_101_SWITCHING_PROTOCOLS` | Server is switching protocols (e.g. WebSocket upgrade) |

### 2xx — Success

| Code | Constant | Meaning | Typical use |
|---|---|---|---|
| 200 | `HTTP_200_OK` | Standard success | `GET`, `PUT` responses |
| 201 | `HTTP_201_CREATED` | Resource created | `POST` that creates something |
| 202 | `HTTP_202_ACCEPTED` | Request accepted, processing async | Background jobs |
| 204 | `HTTP_204_NO_CONTENT` | Success, no body returned | `DELETE` operations |
| 206 | `HTTP_206_PARTIAL_CONTENT` | Partial resource returned | Range requests (video/file streaming) |

### 3xx — Redirection

| Code | Constant | Meaning |
|---|---|---|
| 301 | `HTTP_301_MOVED_PERMANENTLY` | Resource permanently moved |
| 302 | `HTTP_302_FOUND` | Temporary redirect |
| 304 | `HTTP_304_NOT_MODIFIED` | Cached version is still valid |
| 307 | `HTTP_307_TEMPORARY_REDIRECT` | Redirect, method/body preserved |

### 4xx — Client Errors

| Code | Constant | Meaning | Typical use |
|---|---|---|---|
| 400 | `HTTP_400_BAD_REQUEST` | Malformed request | Generic client-side error |
| 401 | `HTTP_401_UNAUTHORIZED` | Missing/invalid credentials | Auth required |
| 403 | `HTTP_403_FORBIDDEN` | Authenticated but not allowed | Permission denied |
| 404 | `HTTP_404_NOT_FOUND` | Resource doesn't exist | Wrong ID/path |
| 405 | `HTTP_405_METHOD_NOT_ALLOWED` | Wrong HTTP verb used | e.g. `DELETE` on a read-only route |
| 409 | `HTTP_409_CONFLICT` | Conflicting state | Duplicate resource, race condition |
| 410 | `HTTP_410_GONE` | Resource permanently removed | Deprecated endpoints |
| 415 | `HTTP_415_UNSUPPORTED_MEDIA_TYPE` | Wrong `Content-Type` | Wrong upload format |
| 422 | `HTTP_422_UNPROCESSABLE_ENTITY` | Validation failed | **FastAPI's default for bad request bodies/params** |
| 429 | `HTTP_429_TOO_MANY_REQUESTS` | Rate limit exceeded | Throttling |

### 5xx — Server Errors

| Code | Constant | Meaning | Typical use |
|---|---|---|---|
| 500 | `HTTP_500_INTERNAL_SERVER_ERROR` | Unhandled exception | Bugs, unexpected crashes |
| 501 | `HTTP_501_NOT_IMPLEMENTED` | Feature not built yet | Stubbed endpoints |
| 502 | `HTTP_502_BAD_GATEWAY` | Upstream server error | Reverse proxy / gateway issues |
| 503 | `HTTP_503_SERVICE_UNAVAILABLE` | Server temporarily down | Maintenance, overload |
| 504 | `HTTP_504_GATEWAY_TIMEOUT` | Upstream server timed out | Slow downstream service |

**Setting status codes three ways:**

```python
# 1. Default status code for the whole route
@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item

# 2. Dynamically via Response object
from fastapi import Response

@app.post("/items/")
def create_item(item: Item, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return item

# 3. Via raising HTTPException (for error paths)
raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
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

**Enriching docs with metadata:**

```python
@app.get(
    "/items/{item_id}",
    summary="Get an item",
    description="Retrieve a single item by its unique ID.",
    response_description="The requested item",
    tags=["items"],
)
def read_item(item_id: int):
    """
    This docstring also shows up in the docs:

    - **item_id**: the ID of the item to fetch
    """
    return {"item_id": item_id}
```

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
- ⚠️ Never call blocking code (e.g. `time.sleep()`, sync DB drivers) inside an `async def` — it blocks the entire event loop

---

## 🔄 Background Tasks

Run something after returning a response, without making the client wait:

```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/send-notification/{email}")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification sent in the background"}
```

> For heavier async workloads (emails, video processing), pair with a task queue like **Celery** or **ARQ** instead.

---

## 📡 WebSockets

```python
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
```

---

## 📁 File Uploads

```python
from fastapi import File, UploadFile

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}

@app.post("/upload-multiple/")
async def upload_files(files: list[UploadFile] = File(...)):
    return {"filenames": [f.filename for f in files]}
```

> Requires `python-multipart`: `pip install python-multipart`

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

def test_create_item():
    response = client.post("/items/", json={"name": "Pen", "price": 2.5})
    assert response.status_code == 200
    assert response.json()["total_price"] == 2.5
```

```bash
pytest -v
```

**Testing async endpoints with async test client:**

```python
import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_async_endpoint():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
```

---

## 🐳 Docker & Deployment

**Dockerfile:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

**requirements.txt:**

```
fastapi==0.115.0
uvicorn[standard]==0.30.0
pydantic==2.9.0
python-multipart==0.0.9
```

**Build & run:**

```bash
docker build -t my-fastapi-app .
docker run -d -p 8000:80 --name fastapi-container my-fastapi-app
```

**docker-compose.yml** (app + Postgres example):

```yaml
version: "3.9"

services:
  api:
    build: .
    ports:
      - "8000:80"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:16
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```bash
docker compose up --build
```

**Multi-stage Dockerfile (smaller production image):**

```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

**Production server (with Gunicorn + Uvicorn workers):**

```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

**Deployment targets:**

| Platform | Notes |
|---|---|
| **Railway / Render** | Push Dockerfile, zero-config deploys |
| **AWS ECS / Fargate** | Container-native, scales well |
| **Google Cloud Run** | Pay-per-request, auto-scales to zero |
| **Fly.io** | Great for low-latency global deployment |
| **Kubernetes** | For larger, multi-service systems |

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
├── 📄 docker-compose.yml
├── 📄 .env
└── 📄 README.md
```

**Splitting routes with `APIRouter`:**

```python
# routers/items.py
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def list_items():
    return []

# main.py
from fastapi import FastAPI
from routers import items

app = FastAPI()
app.include_router(items.router)
```

---

## 🧭 Best Practices Checklist

- ✅ Use `response_model` to control exactly what's returned (never leak passwords/internal fields)
- ✅ Split routes into `APIRouter`s per resource/domain
- ✅ Keep settings in `pydantic-settings` + `.env`, never hardcode secrets
- ✅ Use dependency injection for DB sessions and auth, not globals
- ✅ Prefer `async def` only when you actually await I/O
- ✅ Return proper status codes — don't default everything to `200`
- ✅ Add `tags` and `summary` to endpoints for cleaner docs
- ✅ Write tests with `TestClient` / `httpx.AsyncClient` for every route
- ✅ Use multi-stage Docker builds for smaller production images
- ✅ Run behind Gunicorn + Uvicorn workers (or Uvicorn's own `--workers`) in production

---

## 📚 Resources

| Resource | Link |
|---|---|
| 📘 Official Docs | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| 💻 GitHub Repo | [github.com/fastapi/fastapi](https://github.com/fastapi/fastapi) |
| 🧬 Starlette (ASGI toolkit) | [starlette.io](https://www.starlette.io) |
| ✅ Pydantic (validation) | [docs.pydantic.dev](https://docs.pydantic.dev) |
| 🗄️ SQLModel | [sqlmodel.tiangolo.com](https://sqlmodel.tiangolo.com) |
| 🐳 Docker Docs | [docs.docker.com](https://docs.docker.com) |
| 📜 HTTP Status Codes (MDN) | [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) |

---

<div align="center">

### 🧡 Built with FastAPI

*"Fast to code, fast to run."*

<sub>This README is a learning/reference document formatted in the style of official framework documentation.</sub>

</div>