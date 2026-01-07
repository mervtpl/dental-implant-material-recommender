import streamlit as st
import pandas as pd
from recommendation import generate_recommendation
from report import generate_txt_report

st.title("AI-Assisted Biomimetric Dental Implant Material Selector")

# =========================
# LOAD PARAMETERS FROM EXCEL
# =========================

EXCEL_PATH = "Literature_Survey.xlsx"

def normalize_text(text):
    if isinstance(text, str):
        return (
            text.replace("\n", " ")
                .replace("\r", " ")
                .replace("  ", " ")
                .strip()
        )
    return text

material_df = pd.read_excel(
    EXCEL_PATH,
    sheet_name="Material_Properties",
    engine="openpyxl"
)

parameter_options = (
    material_df["Parametre"]
    .dropna()
    .apply(normalize_text)
    .unique()
    .tolist()
)

parameter_options.append("I don't know")

# =========================
# PATIENT INFORMATION
# =========================
st.subheader("Patient Information")

age_input = st.text_input("Age", placeholder="Enter age (e.g., 35)")
age = int(age_input) if age_input.isdigit() else None


jaw_region = st.selectbox(
    "Jaw Region",
    ["Mandible (Lower Jaw)", "Maxilla (Upper Jaw)"]
)



allergy = st.selectbox(
    "Metal Sensitivity / Allergy",
    ["I don't know", "None", "Mild", "High"]
)

aesthetic = st.selectbox(
    "Aesthetic Priority",
    ["Low", "Medium", "High"]
)

budget = st.selectbox(
    "Budget Level",
    ["Low", "Medium", "High"]
)

smoking = st.selectbox(
    "Smoking Status",
    ["Non-Smoker", "Smoker"]
)

# =========================
# SPECIAL CONDITIONS
# =========================
st.subheader("Special Clinical Conditions")

diabetes = st.selectbox("Diabetes", ["No", "Yes"])
bruxism = st.selectbox("Bruxism", ["No", "Yes"])

# =========================
# PARAMETER PRIORITIES
# =========================
st.subheader("Literature-Based Parameter Priorities")

selected_parameters = st.multiselect(
    "Select important material parameters(Optional)",
    parameter_options
)

# =========================
# RUN SYSTEM
# =========================
if st.button("Get Recommendation"):
    if age is None:
        st.error("Please enter a valid age.")

    else:
        patient_info = {
            "age": age,
            "jaw_region": jaw_region,
            "smoking": smoking,
            "allergy": allergy,
            "aesthetic": aesthetic,
            "budget": budget,
        }

        special_conditions = {
            "diabetes": diabetes,
            "bruxism": bruxism,
        }

        ai_result = generate_recommendation(
            patient_info,
            special_conditions,
            selected_parameters
        )

        st.subheader("AI Recommendation")
        st.write(ai_result)

        report_text = generate_txt_report(
            patient_info,
            special_conditions,
            selected_parameters,
            ai_result
        )

        st.download_button(
            label="⬇ Download Report (TXT)",
            data=report_text,
            file_name="implant_recommendation_report.txt",
            mime="text/plain",
        )
