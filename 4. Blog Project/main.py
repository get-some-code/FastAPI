from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
import json
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).parent
with open(BASE_DIR / "blogs.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False)
@app.get("/home", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/post/{post_id}")
def get_post(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return templates.TemplateResponse(request, "blog.html", {"post": post, "title": post['title'][:50]})
    return templates.TemplateResponse(request, "404.html", status_code=404)
