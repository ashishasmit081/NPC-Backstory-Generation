
# 🎮 NPC Backstory & Dialogue Generator

This project is an **AI-powered web app** that generates **RPG-style backstories** and **mission dialogues** for fantasy NPCs. It's built with **FastAPI**, styled with medieval fantasy flair, and powered by a fine-tuned **DistilGPT-2** model.

---

## 🔧 Features

- Generate rich, fantasy-inspired character backstories
- Automatically create matching RPG-style NPC missions
- Lightweight model suitable for CPU usage (DistilGPT-2)
- Stylized HTML interface with a medieval RPG look

---

## 🚀 How to Run It

💠 How to Run Locally

1. ✅ Fine-tune the Model

- Before anything, you must fine-tune the distilgpt2 model on your dataset:

- Open the notebook:red-pandas-gaming-assignment (1).ipynb

- Run all cells. This will:

- Load and format the dataset.

- Fine-tune the distilgpt2 model on character backstories.

- Save the model to a directory called finetuned-distilgpt2-backstory.

💾 After training, download the entire finetuned-distilgpt2-backstory/ folder and place it in your project root directory.

Structure your directory like this:

```
├── api.py               # FastAPI backend logic
├── frontend_html/       # HTML templates
│   └── frontend.html
├── frontend_css/        # Medieval-styled CSS
│   └── frontend.css
├── finetuned-distilgpt2-backstory/ # Trained model directory
├── red-pandas-gaming-assignment.ipynb # Notebook for fine-tuning
└── README.md            # You're here!
```

2. ✅ Install Dependencies

Make sure you have Python 3.8+ installed.

Option A: Use Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```
Option B: Use Conda
```bash
conda create -n npcgen python=3.9
conda activate npcgen
```
Install Required Packages

If you don’t already have a requirements.txt, install these manually:
```bash
pip install fastapi uvicorn transformers torch jinja2 python-multipart
```
Optional: Save dependencies to a filepip freeze > requirements.txt

3. ✅ Run the FastAPI Server

Start the API server:
```bash
uvicorn api:app --reload
```
Open your browser and go to:
```bash
http://localhost:8000
```
You’ll see the front-end interface where you can enter NPC descriptions and generate backstories & quests.

---

## 💾 Dataset

- **Source**: `/kaggle/input/synthnobilitas-ai-generated-noble/noble_data.jsonl`
- **Details**: Custom-generated noble NPC dataset including:
  - `Name`, `Age`, `Sex`, `Realm`, `Title`, `MBTI Personality`, `Hobby`, and `Backstory`
- **Processing**:
  - Converted to natural prompt format
  - Tokenized using GPT-2 tokenizer
  - Fine-tuned on `DistilGPT-2` with prompt + backstory

---

## 🧠 Models Used

- **Backstory Generator**: Fine-tuned `distilgpt2` (lightweight & CPU-friendly)
- **Mission Generator**: Pre-trained `google/flan-t5-large` (for creative text generation)

> 💡 Consider replacing `flan-t5-large` with `flan-t5-small` or `flan-t5-base` if memory is an issue.

---

## 📝 Sample Input/Output

### 🧝 Prompt:
> `Aria, a noble archer from Eldoria`

### ✨ Output:
**Backstory**:
> Aria, born into the noble house of Silvaran, trained in the moonlit forests of Eldoria. Gifted with elven precision and a burning sense of justice, she turned from palace life to protect the borders from dark spirits that plague the land...

**Dialogue / Missions**:
- Help Aria retrieve a lost heirloom bow from the cursed ruins
- Escort a merchant caravan through haunted woods
- Investigate shadowy dealings near the Elden border

*(📸 Screenshot )*
- Screenshot of UI before Backstory Generation 
<img src="screenshot-before-generation.png" alt="NPC Generator UI" width="600"/>
- Screenshot of UI after Backstory Generation 
<img src="screenshot-after-generation.png" alt="NPC Generator UI" width="600"/>


---

## 📁 Project Structure

```
├── api.py               # FastAPI backend logic
├── frontend_html/       # HTML templates
│   └── frontend.html
├── frontend_css/        # Medieval-styled CSS
│   └── frontend.css
├── finetuned-distilgpt2-backstory/ # Trained model directory
├── red-pandas-gaming-assignment.ipynb # Notebook for fine-tuning
└── README.md            # You're here!
```

---

## ✍️ Author

Built by **Ashish Asmit** for the **Red Pandas Gaming Assignment** 🐾  
> Proudly trained with 💻 CPU power and imagination.
