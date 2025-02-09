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
        st.markdown("""
        <style>
            .styled-image {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 300px;
                height: 300px;
                border: 5px solid #4CAF50;  /* Green border */
                border-radius: 15px;  /* Rounded corners */
                box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);  /* Shadow effect */
            }
        </style>

        <img class="styled-image" src="" />
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='text-align: center;'>Yingqi (Cheech) Li</h1>", unsafe_allow_html=True)
        st.markdown("""
        <style>
            .styled-image {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 300px;
                height: 300px;
                border: 5px solid #4CAF50;  /* Green border */
                border-radius: 15px;  /* Rounded corners */
                box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);  /* Shadow effect */
            }
        </style>

        <img class="styled-image" src="images/YingqiLi.jpg" />
        """, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
