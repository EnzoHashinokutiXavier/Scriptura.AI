# ScripturaAI

ScripturaAI is a web application that uses OpenAI's API to provide explanations for Bible excerpts. The backend is built with FastAPI, and the frontend is a simple HTML/CSS interface. Users can request different types of explanations: simple, literal, or interpretative.

---

## Features

- **Simple Explanation:** Understand Bible passages in plain language, suitable for laypeople and children.
- **Literal Explanation:** Get explanations based on original languages and literal translations.
- **Interpretation Explanation:** See how different Christian traditions interpret a passage.

---

## Recommended For

- Students and teachers of theology or religious studies
- Anyone interested in understanding the Bible more deeply
- People seeking accessible explanations of biblical texts

---

## Requirements

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/)
- The packages listed in `requirements.txt`

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/ScripturaAI.git
   cd ScripturaAI
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key as an environment variable:**

   On Windows (Command Prompt):
   ```sh
   setx OPENAI_API_KEY "your-openai-key"
   ```
   Note: After running this command, close your terminal and open a new one before starting the backend, so the environment variable is recognized.
   
   On Linux/Mac:
   ```sh
   export OPENAI_API_KEY="your-openai-key"
   ```

---

## Usage

1. **Start the backend server:**
   ```sh
   uvicorn main:app --reload
   ```

2. **Access the frontend:**  
   Open [http://localhost:8000](http://localhost:8000) in your browser.

3. **Enter a Bible excerpt and choose the type of explanation.**

---

## Project Structure

```
ScripturaAI/
│
├── main.py              # FastAPI backend
├── requirements.txt     # Python dependencies
├── static/              # Static frontend files
│   ├── index.html       # Frontend HTML
│   └── css/
│       └── index.css    # Frontend CSS
└── __pycache__/         # Python cache files
```

---

## Notes

- The application requires an internet connection to access the OpenAI API.
- Usage of the OpenAI API may incur costs depending on your plan.

---

## License

This project is for educational and personal use.
