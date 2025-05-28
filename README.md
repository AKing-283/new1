# 🌾 FarmChain: AI-Powered Agricultural Expert Reports

**Live App**: [https://farmchain.streamlit.app](https://farmchain.streamlit.app)

FarmChain is an AI-powered agricultural decision-support system that assists farmers, agronomists, and agri-tech consultants by providing expert analysis and equipment recommendations. The system combines the capabilities of four specialized agents—**Crop Expert**, **Soil Advisor**, **Regional Analyst**, and **Equipment Recommender**—into a single, intelligent assistant powered by **Google Gemini Flash 2.0**. It generates structured, professional PDF reports tailored to user inputs such as crop type, soil, region, and season.

## 🧠 Key Features

- 🔎 **Multi-Agent Intelligence** – Combines insights from four agricultural experts
- 📝 **Structured Report Output** – Well-organized and actionable recommendations
- 📄 **PDF Export** – High-quality, professional-grade reports for offline use
- 🌍 **Context-Aware Analysis** – Considers soil type, region, crop, and seasonal factors
- ⚡ **Powered by Gemini Flash 2.0** – Fast, cost-efficient, and accurate language model reasoning

## 🛠️ Tech Stack

- **LangChain** – Framework for chaining LLM components  
- **Google Gemini Flash 2.0** – Large Language Model for expert reasoning  
- **Streamlit** – Python-based web app frontend  
- **ReportLab** – PDF generation library  
- **python-dotenv** – Environment variable management

## 🚀 Getting Started (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/Aking-283/new1.git
cd new1
pip install -r requirements.txt
```

Create a .env file which will store your gemini api key
```bash
GOOGLE_API_KEY=your_gemini_api_key
```

Alternatively, you can export it in your terminal:
```bash
export GOOGLE_API_KEY="your_gemini_api_key"
```

Run the applicaton:
```bash
streamlit run app.py
```

📄 Example Report Sections
Crop Expert Analysis – Crop suitability, care, and productivity tips

Soil Advisor Validation – Soil compatibility and treatment

Regional Assessment – Climate and geographic considerations

Equipment Recommendations – Suggested tools with usage rationale

Conclusion – Final advice summarizing the above sections

PDFs are styled for clarity and offline sharing.

📁 Project Structure
```bash
.
├── app.py           # Main Streamlit frontend
├── backend.py       # Gemini agent logic + PDF generation
├── requirements.txt # Project dependencies
├── .env             # Environment variables (excluded from version control)
└── README.md
```

📦 Dependencies
langchain

langchain_google_genai

streamlit

reportlab

python-dotenv

👨‍💻 Author
Name: Pushpak Dakkata
Email: dpreddy294@gmail.com
GitHub: @AKing-283

🧠 Credits
Built with ❤️ using LangChain, Google Gemini, and Streamlit.
