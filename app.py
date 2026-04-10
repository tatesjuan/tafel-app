import streamlit as st

st.set_page_config(page_title="Tafels Generator", page_icon="📊", layout="centered")

st.title("📊 Tafels Generator")
st.write("Voer een getal in en zie direct de vermenigvuldigingstafels.")

getal = st.number_input("Kies een getal", min_value=1, max_value=100, value=5, step=1)

st.subheader(f"Tafel van {int(getal)}")

cols = st.columns(2)
for i in range(1, 11):
    uitkomst = int(getal) * i
    with cols[0]:
        st.write(f"{int(getal)} × {i}")
    with cols[1]:
        st.markdown(f"**= {uitkomst}**")
