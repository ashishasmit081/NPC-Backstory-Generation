import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel, AutoTokenizer, AutoModelForSeq2SeqLM
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],  # Allow both origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount frontend assets
app.mount("/frontend_css", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "frontend_css")), name="frontend_css")

# Use absolute path for templates directory
templates_dir = os.path.join(os.path.dirname(__file__), "frontend_html")
templates = Jinja2Templates(directory=templates_dir)

# Track uptime
start_time = time.time()

# Load backstory model
tokenizer = GPT2Tokenizer.from_pretrained(os.path.join(os.path.dirname(__file__), "finetuned-distilgpt2-backstory"))
model = GPT2LMHeadModel.from_pretrained(os.path.join(os.path.dirname(__file__), "finetuned-distilgpt2-backstory"))
backstory_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Load mission model
mission_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
mission_tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
mission_generator = pipeline("text2text-generation", model=mission_model, tokenizer=mission_tokenizer)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("frontend.html", {"request": request})

@app.get("/status")
def status():
    return {"status": "ok", "uptime": round(time.time() - start_time, 2)}

@app.get("/generate")
def generate(prompt: str, style: str = "medium"):
    styled_prompt = f"Tell me a {style} backstory of {prompt}"

    backstory = backstory_generator(
        styled_prompt,
        max_length=350 if style == "short" else 600 if style == "medium" else 1000,
        do_sample=True,
        temperature=0.9,
        top_k=50,
        top_p=0.95,
        truncation=True  # Explicitly enable truncation to avoid warnings
    )[0]["generated_text"]

    mission_prompt = f"""
    You are an NPC with the following backstory:
    \"\"\"{backstory}\"\"\"
    Generate 3 interesting missions they might give to a player in a fantasy RPG. Format as bullet points.
    """

    missions = mission_generator(
        mission_prompt,
        max_length=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        truncation=True
    )[0]["generated_text"]

    return {
        "backstory": backstory.strip(),
        "dialogue": missions.strip()
    }