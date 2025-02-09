import streamlit as st
from PIL import Image

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
        img = Image.open("images/YingqiLi.jpg")
        st.image(img, caption="Yingqi (Cheech) Li", use_container_width=True)

        # Apply custom CSS styles using st.markdown without breaking the image
        st.markdown("""
            <style>
                img {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 300px;  /* Set the image width */
                    height: 300px;  /* Set the image height */
                    border: 5px solid #4CAF50;  /* Green border */
                    border-radius: 15px;  /* Rounded corners */
                    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);  /* Shadow effect */
                    transition: transform 0.3s ease-in-out;
                }

                img:hover {
                    transform: scale(1.1);  /* Hover effect to scale the image */
                }
            </style>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='text-align: center;'>Yingqi (Cheech) Li</h1>", unsafe_allow_html=True)
        # Display image using st.image()
        img = Image.open("images/YingqiLi.jpg")
        st.image(img, caption="Yingqi (Cheech) Li", use_container_width=True)

        # Apply custom CSS styles using st.markdown without breaking the image
        st.markdown("""
            <style>
                img {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 200;  /* Set the image width */
                    height: 200;  /* Set the image height */
                    border: 5px solid #4CAF50;  /* Green border */
                    border-radius: 15px;  /* Rounded corners */
                    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);  /* Shadow effect */
                    transition: transform 0.3s ease-in-out;
                }

                img:hover {
                    transform: scale(1.1);  /* Hover effect to scale the image */
                }
            </style>
        """, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
