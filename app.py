import streamlit as st
from crew_module import run_crew, generate_pdf

st.set_page_config(page_title="Equipment Recommender Agent 🌾", layout="centered")
st.title("🌿 Smart Equipment Recommender (Multi-Agent AI)")

st.markdown(
    """
Welcome to the **AI-powered agricultural equipment recommender**.  
Select your inputs below and let our expert agents analyze the best equipment for your needs.
    """
)

# Input Form
with st.form("input_form"):
    crop = st.selectbox("🌾 Select Crop", ["Wheat", "Rice", "Sugarcane", "Maize", "Cotton", "Millet", "Pulses"])
    soil = st.selectbox("🧱 Select Soil Type", ["Loamy", "Clayey", "Sandy", "Alluvial", "Black"])
    season = st.selectbox("☀️ Select Season", ["Rabi", "Kharif"])
    region = st.selectbox("🌍 Select Region", [
        "Punjab", "Tamil Nadu", "Maharashtra", "Uttar Pradesh", "Gujarat",
        "Rajasthan", "Andhra Pradesh", "Madhya Pradesh", "Karnataka"
    ])
    submitted = st.form_submit_button("🚜 Recommend Equipment")

# Result Handling
if submitted:
    with st.spinner("🤖 Agents are analyzing your data..."):
        result = run_crew(crop, soil, season, region)

        if not result or result.startswith("[Error]"):
            st.error("⚠️ Something went wrong while generating the recommendation.")
            if result:
                st.text(result)
        else:
            pdf_path = generate_pdf(result)

            st.success("✅ Recommendation Ready!")
            st.markdown("### 📋 Recommended Equipment Report")
            st.code(result, language="markdown")

            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Download Full Report (PDF)",
                    data=f,
                    file_name="equipment_report.pdf",
                    mime="application/pdf"
                )

    # Footer
    st.markdown("---")
    st.markdown("📌 *Powered by Farmchain")
