import streamlit as st
import base64
import os
import csv

# Funktion för att lägga till en bakgrundsbild
def add_background(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/webp;base64,{encoded_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    h1 {{
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        font-size: 2.5em;
        text-align: center; /* Centrera rubriken */
    }}
    label {{
        color: black; /* Textfärg för etiketter */
        background-color: rgba(255, 255, 255, 0.8); /* Ljus bakgrund för etiketter */
        padding: 5px;
        border-radius: 5px;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.8);
        font-size: 1.2em;
    }}
    .stTextInput {{
        background-color: rgba(255, 255, 255, 0.85);
        color: black;
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }}
    .stButton {{
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
        border-radius: 10px;
        padding: 12px;
        margin-top: 5px;
        transition: background-color 0.3s;
        font-size: 1.1em; /* Öka storleken på texten i knappar */
    }}
    .stButton:hover {{
        background-color: rgba(0, 0, 0, 0.9);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# Sökväg till din bild
image_path = "Dallansgolf.webp"  # Se till att detta filnamn är korrekt

# Anropa funktionen för att sätta bakgrundsbild
add_background(image_path)

# Skapa CSV-fil om den inte redan finns
file_name = "inventering.csv"
if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Produktnamn", "Kvantitet", "Plats", "Datum"])

# Lägga till produkt i CSV
def add_product(produktnamn, kvantitet, plats, datum):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([produktnamn, kvantitet, plats, datum])

# Huvudgränssnitt med Streamlit
st.title("Dallans Inventeringsprogram")

# Inmatningsfält
produktnamn = st.text_input("Spoltyp")
kvantitet = st.number_input("Kvantitet", min_value=0)
plats = st.text_input("Plats (Maskin/Linje)")
datum = st.text_input("Datum (ÅÅÅÅ-MM-DD)")

# Knapp för att lägga till produkt
if st.button("Lägg till"):
    add_product(produktnamn, kvantitet, plats, datum)
    st.success(f"{produktnamn} har lagts till i inventeringen!")

# Knapp för att visa inventeringen
if st.button("Visa inventering"):
    st.write("Nuvarande inventering:")
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            st.write(", ".join(row))

# Knapp för att ladda ner CSV-fil
if st.button("Ladda ner CSV-fil"):
    with open(file_name, 'rb') as f:
        st.download_button('Ladda ner CSV', f, file_name)


