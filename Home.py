import streamlit as st

def main():
    st.set_page_config(page_title="Composted", layout="wide")
    st.markdown("""
    <style>
    .stApp {
        background-color: #f9f1f1;
        color: #90EE90;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center;'>Eugene Hwang</h1>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='text-align: center;'>Yingqi (Cheech) Li</h1>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()
