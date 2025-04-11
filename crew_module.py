import os
import tempfile
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from googletrans import Translator, LANGUAGES
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDtrfi5aYctFGhrp_WlB1LggX_frbVjni0"  # Replace with your actual key

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)

# Prompt template for multi-agent expert discussion
prompt_template = ChatPromptTemplate.from_template("""
You are an agricultural assistant composed of the following experts:
1. Crop Expert: Analyzes best crops for soil, season, and region.
2. Soil Advisor: Validates soil compatibility with crops.
3. Regional Analyst: Assesses environmental suitability.
4. Equipment Recommender: Suggests farming equipment with reasoning.

Given the following context:
- Crop: {crop}
- Soil Type: {soil}
- Season: {season}
- Region: {region}

Provide a detailed response simulating a discussion between the experts,
and conclude with 2–3 recommended agricultural equipment and why they're suitable.
""")

# Combine prompt, LLM, and output parser
chain = prompt_template | llm | StrOutputParser()

# Translator instance
translator = Translator()

# Display name to code map
LANGUAGE_MAP = {
    "English": "en",
    "Hindi (हिंदी)": "hi",
    "Tamil (தமிழ்)": "ta",
    "Telugu (తెలుగు)": "te",
    "Marathi (मराठी)": "mr",
    "Gujarati (ગુજરાતી)": "gu",
    "Punjabi (ਪੰਜਾਬੀ)": "pa",
    "Kannada (ಕನ್ನಡ)": "kn",
    "Bengali (বাংলা)": "bn",
    "Spanish (Español)": "es",
    "French (Français)": "fr",
    "German (Deutsch)": "de",
}

def run_crew(crop, soil, season, region):
    """Run the expert chain for a given agricultural context."""
    try:
        return chain.invoke({
            "crop": crop,
            "soil": soil,
            "season": season,
            "region": region
        })
    except Exception as e:
        return f"[Error] Failed to generate response: {e}"

def translate_text(text, target_lang):
    """Translate text using googletrans with robust handling."""
    if not text:
        return "No text to translate."

    normalized_input = target_lang.strip().lower()

    # Match from custom map
    target_code = None
    for name, code in LANGUAGE_MAP.items():
        if normalized_input in name.lower() or name.lower() in normalized_input:
            target_code = code
            break

    # Fallback to direct code match
    if not target_code and normalized_input in LANGUAGES:
        target_code = normalized_input

    if not target_code:
        return f"[Translation Error] Unsupported language: {target_lang}"

    if target_code == "en":
        return text

    try:
        translation = translator.translate(text, dest=target_code)
        return translation.text if translation and translation.text else "Translation not available."
    except Exception as e:
        print(f"[Translation Error]: {e}")
        return "[Translation Error] Please try again or use English."

def generate_pdf(content, output_path="report.pdf"):
    """Generate a PDF file from the given content."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
            c = canvas.Canvas(tmpfile.name, pagesize=letter)
            width, height = letter
            text_object = c.beginText(40, height - 40)
            text_object.setFont("Helvetica", 12)

            for line in content.split('\n'):
                text_object.textLine(line)

            c.drawText(text_object)
            c.save()
            return tmpfile.name  # Correct return path
    except Exception as e:
        print(f"[PDF Generation Error]: {e}")
        return None
