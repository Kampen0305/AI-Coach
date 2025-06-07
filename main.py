import streamlit as st
import requests
from fpdf import FPDF
from datetime import datetime
import os

# --- Configuratie ---
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct:free"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# --- Functie: Advies opvragen via OpenRouter ---
def vraag_ai_advies(vak, niveau, doel):
    prompt = (
        f"Ik geef les in het vak {vak} op niveau {niveau}."
        f" Hoe kan ik AI inzetten om het volgende doel te behalen: {doel}?"
        " Geef een concrete suggestie voor een AI-toepassing, een prompt die ik kan gebruiken,"
        " en een praktische werkvorm."
    )

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Fout bij ophalen advies: {response.status_code} - {response.text}"

# --- Functie: PDF genereren ---
def genereer_pdf(vak, niveau, doel, advies):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="AI Coach Adviesrapport", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Datum: {datetime.today().strftime('%d-%m-%Y')}", ln=True)
    pdf.ln(10)

    pdf.multi_cell(0, 10, txt=f"Vak: {vak}\nNiveau: {niveau}\nDoel: {doel}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=f"Advies:\n{advies}")

    pdf_path = "/tmp/advies.pdf"
    pdf.output(pdf_path)
    return pdf_path

# --- Streamlit UI ---
st.set_page_config(page_title="AI Coach voor Docenten", layout="centered")
st.title("🧠 AI Coach voor Docenten")

with st.form("ai_form"):
    vak = st.text_input("Vakgebied", placeholder="Bijv. Engels, Burgerschap")
    niveau = st.selectbox("Onderwijsniveau", ["Niveau 2", "Niveau 3", "Niveau 4"])
    doel = st.text_area("Wat wil je bereiken met je les?", placeholder="Bijv. Kritisch denken stimuleren")
    submitted = st.form_submit_button("Vraag advies aan")

if submitted:
    with st.spinner("AI Coach denkt na..."):
        advies = vraag_ai_advies(vak, niveau, doel)
        st.subheader("📘 Advies")
        st.write(advies)

        pdf_path = genereer_pdf(vak, niveau, doel, advies)
        with open(pdf_path, "rb") as file:
            st.download_button(
                label="📄 Download als PDF",
                data=file,
                file_name="AI_Advies.pdf",
                mime="application/pdf"
            )
