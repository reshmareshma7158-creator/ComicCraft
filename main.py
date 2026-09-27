from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from routes import generate_comic

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
    request,
    "index.html",
    {}
    )


@app.post("/generate")
async def generate(request: Request):
    form = await request.form()
    prompt = form.get("prompt")

    result = generate_comic(prompt)

    return templates.TemplateResponse(
    request,
    "index.html",
    {"result": result}
    )
