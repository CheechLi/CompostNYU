import streamlit as st

def main():
    st.set_page_config(page_title="Composted", layout="wide")
    st.markdown("<h1 style='text-align: center; font-size: 150px; color: #90EE90'>CompostED</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 50px;'>Composting is the cornerstone of food sustainability</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Explore the benefits of composting with our composting simulator and chatbot!</h3>", unsafe_allow_html=True)
    st.page_link("pages/2_Composting_Chatbot.py", label="Simulator", icon="➡️>")

if __name__ == "__main__":
    main()
