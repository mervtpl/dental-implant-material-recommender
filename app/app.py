import streamlit as st

st.title("AI Dental Implant Material Selector")

st.subheader("Enter Patient Information")

# AGE INPUT
age_input = st.text_input("Age", placeholder="Enter age (e.g., 35)")
age = None
if age_input.isdigit():
    age = int(age_input)
else:
    if age_input != "":
        st.warning("Please enter a valid numeric age.")

# BONE TYPE
bone_type = st.selectbox("Bone Type", ["Type I", "Type II", "Type III", "Type IV"])

# JAW REGION
jaw_region = st.selectbox("Jaw Region", ["Mandible (Lower Jaw)", "Maxilla (Upper Jaw)"])

# BONE DENSITY
bone_density = st.selectbox("Bone Density", ["Low", "Medium", "High"])

# ALLERGY RISK
allergy = st.selectbox("Metal Sensitivity / Allergy", ["None", "Mild", "High"])

# AESTHETIC PRIORITY
aesthetic = st.selectbox("Aesthetic Priority", ["Low", "Medium", "High"])

# BUDGET
budget = st.selectbox("Budget Level", ["Low", "Medium", "High"])

# SMOKING
smoking = st.selectbox("Smoking Status", ["Non-Smoker", "Smoker"])

# PROCESS BUTTON
if st.button("Get Recommendation"):
    if age is None:
        st.error("Please enter a valid age before continuing.")
    else:
        result = f"""
Recommended Material: Titanium

Why:
- Strong osseointegration suitable for {jaw_region.lower()} and {bone_type}.
- Performs well in {bone_density.lower()} bone density cases.
- Biocompatible even with mild allergy risks.
- Aesthetic priority: {aesthetic}.
- Good choice for long-term durability.
- Budget level: {budget}.
- Smoking status considered: {smoking}.
"""

        st.subheader("Recommendation")
        st.write(result)

        # TXT REPORT CONTENT
        report_text = f"""
AI Dental Implant Recommendation Report
----------------------------------------

Patient Information:
- Age: {age}
- Bone Type: {bone_type}
- Jaw Region: {jaw_region}
- Bone Density: {bone_density}
- Metal Sensitivity: {allergy}
- Aesthetic Priority: {aesthetic}
- Budget Level: {budget}
- Smoking Status: {smoking}

Recommendation:
Titanium implant is suggested.

Reasoning:
- Strong biocompatibility
- High osseointegration rate
- Long-term durability
- Supported by clinical literature
"""

        st.download_button(
            label="⬇ Download Report (TXT)",
            data=report_text,
            file_name="implant_recommendation_report.txt",
            mime="text/plain",
        )
