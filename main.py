import streamlit as st

green_amt = 0
brown_amt = 0

def addGreen():
    st.write("Green added")

def main():
    st.set_page_config(page_title="Composted", layout="centered")
    st.button("Greens", on_click=addGreen)

if __name__ == "__main__":
    main()