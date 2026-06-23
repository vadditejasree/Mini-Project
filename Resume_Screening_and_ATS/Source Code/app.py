import streamlit as st
from resume_parser import extract_text
from skill_extractor import extract_skills
from ats_score import calculate_score

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

job_description = st.text_area("Paste Job Description")

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    st.subheader("Resume Text")
    st.write(text)

    skills = extract_skills(text)

    st.subheader("Detected Skills")
    st.write(skills)

    score = calculate_score(text, job_description)

    st.subheader("ATS Match Score")
    st.write(str(score) + "%")