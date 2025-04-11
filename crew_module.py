import os
import tempfile
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDtrfi5aYctFGhrp_WlB1LggX_frbVjni0"  # Replace with your actual key

# Initialize Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)

# Enhanced prompt for clean, structured expert report
prompt_template = ChatPromptTemplate.from_template("""
You are a multi-agent agricultural assistant composed of expert roles.

Context:
- Crop: {crop}
- Soil Type: {soil}
- Season: {season}
- Region: {region}

Respond in the following **structured format**:
1. Crop Expert's Analysis:
   - [Detailed bullet-point analysis]
2. Soil Advisor's Validation:
   - [Bullet-point compatibility discussion]
3. Regional Analyst's Assessment:
   - [Assessment points with regional context]
4. Equipment Recommendations:
   - Equipment 1: [Name + reasoning]
   - Equipment 2: [Name + reasoning]
   - Equipment 3 (optional): [Optional equipment + reasoning]
5. Conclusion:
   - [2–3 sentence summary and final recommendation]

Use proper paragraph formatting and bullet points. Avoid using asterisks (*). Use a formal tone suitable for a PDF report.
""")

# Chain setup
chain = prompt_template | llm | StrOutputParser()

def run_crew(crop, soil, season, region):
    """Run the multi-agent reasoning system."""
    try:
        return chain.invoke({
            "crop": crop,
            "soil": soil,
            "season": season,
            "region": region
        })
    except Exception as e:
        return f"[Error] Failed to generate report: {e}"

def generate_pdf(content, output_path=None):
    """Generate a clean PDF report from structured text."""
    try:
        # Temporary file if no custom output path
        if not output_path:
            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            output_path = temp.name

        doc = SimpleDocTemplate(output_path, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=72)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='ReportBody', fontSize=11, leading=16))
        styles.add(ParagraphStyle(name='SectionHeading', fontSize=14, spaceAfter=12, spaceBefore=12, leading=18, underlineWidth=1))

        flow = []

        # Split the content into sections by headers like "1. Crop Expert's Analysis:"
        lines = content.strip().split("\n")
        current_paragraph = ""

        for line in lines:
            if line.strip().startswith(("1.", "2.", "3.", "4.", "5.")):
                # Add previous paragraph first
                if current_paragraph:
                    flow.append(Paragraph(current_paragraph.strip(), styles['ReportBody']))
                    flow.append(Spacer(1, 12))
                    current_paragraph = ""

                flow.append(Paragraph(f"<b>{line.strip()}</b>", styles['SectionHeading']))
            else:
                current_paragraph += line + "<br/>"

        # Add remaining paragraph
        if current_paragraph:
            flow.append(Paragraph(current_paragraph.strip(), styles['ReportBody']))

        doc.build(flow)
        return output_path
    except Exception as e:
        print(f"[PDF Generation Error]: {e}")
        return None
