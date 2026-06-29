# VerifyAI – Truth Lens

A Streamlit-based AI content verification dashboard built for Hackathon 2025. This project analyzes AI-generated text using Google Gemini (`gemini-2.5-flash`) and returns a reliability score, fact checking summary, bias analysis, plagiarism risk, source information, and red-flag detection.

## ✨ Project Overview

`VerifyAI – Truth Lens` is designed to help users verify AI-generated content quickly and visually. It provides:
- Reliability scoring (0-100)
- Fact accuracy classification
- Bias and tone analysis
- Source extraction hints
- Plagiarism risk assessment
- Summary and quick-read insights
- Red flag detection

## 🧩 Key Files

- `hackday.py` - Main Streamlit app containing UI, custom CSS, sidebar configuration, Gemini API integration, and result rendering.
- `requirements.txt` - Python dependencies for the app.
- `vercel.json` - Vercel deployment config for running the app as a Python serverless function.
- `.gitignore` - Excludes local secrets and environment files such as `.env` and `.venv/`.

## 📦 Dependencies

The project depends on:
- `streamlit`
- `google-generativeai`

Install with:

```bash
python -m pip install -r requirements.txt
```

## 🔧 Setup

1. Create a Python virtual environment.
2. Install dependencies.
3. Set the Gemini API key.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root or export the environment variable directly:

```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
```

If using `.env`, add:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> Note: `.env` is intentionally excluded from git via `.gitignore`.

## 🚀 Run Locally

Start the Streamlit app:

```bash
streamlit run hackday.py
```

Then open the local URL shown in the terminal.

## 🖥️ Usage

- Enter the Gemini API key in the sidebar if not already set in the environment.
- Paste AI-generated text into the main input area.
- Click `Analyze Content` to run the Gemini-powered verification workflow.
- Review the generated dashboard with score, summary, bias, plagiarism, strengths, and red flags.

## 🧠 How It Works

`hackday.py`:
- Applies premium custom CSS for a polished dark UI.
- Uses `google.generativeai` to configure the Gemini API key.
- Sends a prompt to `gemini-2.5-flash` asking for strict JSON output.
- Parses the JSON output into fields such as:
  - `summary`
  - `reliability_score`
  - `confidence_level`
  - `factual_accuracy`
  - `tone_bias`
  - `bias_direction`
  - `quick_read`
  - `plagiarism_risk`
  - `originality_note`
  - `red_flags`
  - `strengths`
  - `content_type`
  - `reading_time`
  - `complexity_level`
- Displays the results in interactive Streamlit cards.

## 📄 Deployment

The app is configured for Vercel using `vercel.json`:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "hackday.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/hackday.py"
    }
  ]
}
```

To deploy on Vercel:
1. Connect the repository.
2. Add `GEMINI_API_KEY` to Vercel environment variables.
3. Deploy using Vercel’s dashboard.

## 🧾 Notes

- `streamlit_qr.png` is present locally but not referenced by the app code.
- `.venv/` and `.env` are ignored and not committed.
- There is no `package.json` in the current project workspace.

## ✅ Recommended Improvements

- Add stronger JSON validation for Gemini responses.
- Add a dedicated `README` screenshot or demo GIF.
- Introduce automated tests for prompt output parsing.
- Add a sample input text file or example content.

## 📁 Project Structure

```
.gitignore
hackday.py
requirements.txt
vercel.json
```

---

If you want, I can also add a `README` badge section, example inputs, or a `docker-compose` setup for local deployment.