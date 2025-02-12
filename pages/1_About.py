import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Composted", layout="wide")
    st.markdown("""
    <style>
    .stApp {
        background-color: #f9f1f1;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center;'>Eugene Hwang</h1>", unsafe_allow_html=True)
        img = Image.open("images/eugene_hwang.jpg")
        st.image(img, use_container_width=False)

        # Apply custom CSS styles using st.markdown without breaking the image
        st.markdown("""
            <style>
                img {
                    display: block;
                    width: 100%;
                    height: 100%;
                    border: 5px solid #4CAF50;  /* Green border */
                    border-radius: 15px;  /* Rounded corners */
                    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);  /* Shadow effect */
                    transition: transform 0.3s ease-in-out;
                    text-align: center;
                }

                img:hover {
                    transform: scale(1.1);  /* Hover effect to scale the image */
                }
            </style>
        """, unsafe_allow_html=True)
        st.markdown(
            '''
            <div style="text-align: center;">
                <a href="https://www.linkedin.com/in/eugene-hwang-93b8842a6/" target="_blank" 
                style="color: blue; text-decoration: none; font-size: 24px;">
                Connect with me
                </a>
            </div>
            ''',
            unsafe_allow_html=True
        )
        st.markdown("<p>I am a senior in Fort Lee High School. I have been passionate for computer science since I learned coding from my father during elementary school and participated in numerous computer competitions since entering middle school. Recently, I have become interested in hackathons, being the lead organizer for a local game jam and attending HackNYU as my first hackathon. I am also passionate for sustainability and am the founding president of a student composting organization named ComposTogether at my town.</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='text-align: center;'>Yingqi (Cheech) Li</h1>", unsafe_allow_html=True)
        # Display image using st.image()
        img = Image.open("images/yingqi_li.jpg")
        st.image(img, use_container_width=False)

        # Apply custom CSS styles using st.markdown without breaking the image
        st.markdown("""
            <style>
                img {
                    display: block;
                    width: 100%;
                    height: 100%;
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
        st.markdown(
            '''
            <div style="text-align: center;">
                <a href="https://www.linkedin.com/in/yingqili/" target="_blank" 
                style="color: blue; text-decoration: none; font-size: 24px;">
                Connect with me
                </a>
            </div>
            ''',
            unsafe_allow_html=True
        )
        st.markdown("<p>Hello! My name is Yingqi (Cheech) Li and I am a current junior at Fort Lee High School. HackNYU was my first ever official in-person hackathon after co-hosting Counterspell with my friend Eugene as apart of a branch of Hack Club in Bergen County. Currently, I serve as my school's class president, student council vice president, computer club president, and general manager of model United Nations. In the future, I am interested in studying a niche of computer science and government.</p>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()
