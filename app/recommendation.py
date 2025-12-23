import pandas as pd
from gemini import ask_gemini

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


def generate_recommendation(patient_info, special_conditions, selected_parameters):

    # =========================
    # LOAD EXCEL
    # =========================
    material_df = pd.read_excel(
        EXCEL_PATH,
        sheet_name="Material_Properties",
        engine="openpyxl"
    )

    special_df = pd.read_excel(
        EXCEL_PATH,
        sheet_name="Special_Clinical_Conditions",
        engine="openpyxl"
    )

    # =========================
    # NORMALIZE MATERIAL PARAMETERS
    # =========================
    material_df["Parametre_clean"] = material_df["Parametre"].apply(normalize_text)

    selected_parameters_clean = [
        normalize_text(p) for p in selected_parameters
    ]

    material_subset = material_df[
        material_df["Parametre_clean"].isin(selected_parameters_clean)
    ]

    material_table_text = material_subset.fillna("").to_markdown(index=False)

    # =========================
    # NORMALIZE SPECIAL CONDITIONS (TEXT MODE)
    # =========================
    special_df_clean = special_df.fillna("").applymap(normalize_text)
    special_table_text = special_df_clean.to_markdown(index=False)

    # =========================
    # GEMINI PROMPT
    # =========================
    prompt = f"""
You are an AI-based, literature-driven decision support system
for dental implant material selection.

IMPORTANT RULE:
If any patient information is marked as "I don't know",
do NOT penalize or exclude materials based on that factor.

PATIENT CONTEXT
---------------
Age: {patient_info['age']}
Bone Type: {patient_info['bone_type']}
Jaw Region: {patient_info['jaw_region']}
Bone Density: {patient_info['bone_density']}
Smoking Status: {patient_info['smoking']}
Allergy Risk: {patient_info['allergy']}
Aesthetic Priority: {patient_info['aesthetic']}
Budget Level: {patient_info['budget']}

SPECIAL CLINICAL CONDITIONS
---------------------------
Diabetes: {special_conditions['diabetes']}
Bruxism: {special_conditions['bruxism']}

GENERAL MATERIAL PROPERTIES (FROM LITERATURE)
---------------------------------------------
{material_table_text}

SPECIAL CLINICAL CONDITIONS (FROM LITERATURE)
---------------------------------------------
{special_table_text}

TASK
----
Using the literature tables above:
1. use just the providen links in the tables.
2. Explain how the selected parameters influence material choice briefly.
3. Consider special clinical conditions only if they are present.
4. Provide ONE final recommended material with clear justification at the beginning.
"""

    return ask_gemini(prompt)
