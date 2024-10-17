import streamlit as st
import base64

# Funktion för att lägga till en bakgrundsbild
def add_background(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Ange sökvägen till din bild
image_path = ".github/githubBakgrundsbild"

# Lägg till bakgrundsbilden
add_background(image_path)

# Huvudgränssnitt med Streamlit
st.title("Inventeringsprogram")

# Resten av din app-kod
file_name = "inventering.csv"

# Skapa CSV-fil om den inte redan finns
if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Produktnamn", "Kvantitet", "Plats", "Datum"])

# Lägga till produkt i CSV
def add_product(produktnamn, kvantitet, plats, datum):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([produktnamn, kvantitet, plats, datum])

# Inmatningsfält
produktnamn = st.text_input("Produktnamn")
kvantitet = st.number_input("Kvantitet", min_value=0)
plats = st.text_input("Plats (linje/avdelning)")
datum = st.text_input("Datum (ÅÅÅÅ-MM-DD)")

# Knapp för att lägga till produkt
if st.button("Lägg till produkt"):
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

