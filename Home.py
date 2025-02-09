import streamlit as st
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3

def main():
    st.set_page_config(page_title="Composted", layout="wide", page_icon="🌱")
    st.markdown("""
    <style>
    .stApp {
        background-color: #f9f1f1;
        color: #000000;
    }xs
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 150px; color: #006400'>CompostED</h1>", unsafe_allow_html=True)
    st.image("images/compost_bin.jpg")
    st.markdown("<h2 style='text-align: center; font-size: 50px'>Composting is the cornerstone of food sustainability.</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center'>Composting is an environmentally friendly way to recycle organic waste, reducing the amount of trash that ends up in landfills and returning valuable nutrients to the earth. ​Explore the benefits of composting with our composting simulator and chatbot!</h3>", unsafe_allow_html=True)
    # st.markdown("<a href='pages/1_About.py'>About</a>", unsafe_allow_html=True)
    # st.markdown("<a href='pages/2_Composting_Chatbot.py'>Chat</a>", unsafe_allow_html=True)
    # st.markdown("<a href='pages/3_Composting_Simulator.py'>Simulator</a>", unsafe_allow_html=True)

    st.page_link("pages/1_About.py", label="About", icon="ℹ️")
    st.page_link("pages/2_Composting_Chatbot.py", label="Chat", icon="💬")
    st.page_link("pages/3_Composting_Simulator.py", label="Simulator", icon="🔄")

if __name__ == "__main__":
    main()
