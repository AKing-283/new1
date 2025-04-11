import streamlit as st
from crew_module import run_crew, translate_text, generate_pdf

st.set_page_config(page_title="Equipment Recommender Agent 🌾", layout="centered")
st.title("🌿 Smart Equipment Recommender (Multi-Agent AI)")

with st.form("input_form"):
    crop = st.selectbox("Select Crop", ["Wheat", "Rice", "Sugarcane", "Maize", "Cotton", "Millet", "Pulses"])
    soil = st.selectbox("Select Soil Type", ["Loamy", "Clayey", "Sandy", "Alluvial", "Black"])
    season = st.selectbox("Select Season", ["Rabi", "Kharif"])
    region = st.selectbox("Select Region", ["Punjab", "Tamil Nadu", "Maharashtra", "Uttar Pradesh", "Gujarat", "Rajasthan", "Andhra Pradesh", "Madhya Pradesh", "Karnataka"])
    language = st.selectbox("Select Language for Report", {
        "English": "en",
        "Hindi (हिंदी)": "hi",
        "Tamil (தமிழ்)": "ta",
        "Telugu (తెలుగు)": "te",
        "Marathi (मराठी)": "mr",
        "Gujarati (ગુજરાતી)": "gu",
        "Punjabi (ਪੰਜਾਬੀ)": "pa",
        "Kannada (ಕನ್ನಡ)": "kn",
        "Bengali (বাংলা)": "bn"
    })

    submitted = st.form_submit_button("Recommend Equipment")

if submitted:
    with st.spinner("🤖 Agents analyzing and collaborating..."):
        result = run_crew(crop, soil, season, region)
        translated = translate_text(result, language)
        pdf_path = generate_pdf(translated)

    st.success("✅ Recommendation Ready!")
    st.markdown("### 📋 Recommended Equipment:")
    st.markdown(translated)

    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📥 Download Report (PDF)",
            data=f,
            file_name="equipment_recommendation.pdf",
            mime="application/pdf"
        )
