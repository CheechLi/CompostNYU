import streamlit as st
import random

def set_state(i):
    st.session_state.stage = i

if 'stage' not in st.session_state:
    st.session_state.stage = 0

greens = ["fruits/vegetables", "coffee grounds", "eggshells", "grass clippings", "leaves", "tea bags", "weeds", "yard trimmings", "flowers"]
browns = ["cardboard", "newspaper", "organic paper", "paper straw", "wood chips", "sawdust", "hay", "egg cartons", "toilet paper rolls"]
not_allowed = ["dairy", "meat", "bones", "fish", "grease", "oil", "glossy paper", "pet waste", "weeds with seeds", "diseased plants", "inorganic material"]

if(st.session_state.stage == 0):
    choices = random.sample(greens + browns + not_allowed, 10)

st.title("Composting Simulator")

st.write("Welcome to the Composting Simulator! Let's see if you can correctly identify which items can be composted.")
options = st.multiselect("Select the items that can be composted:", choices, on_change=set_state, args=[1])
st.write(options)

# def main():
#     st.set_page_config(page_title="Composted", layout="centered")
#     st.button("Greens", on_click=addGreen)

# if __name__ == "__main__":
#     main()

# import streamlit as st

# if 'stage' not in st.session_state:
#     st.session_state.stage = 0

# def set_state(i):
#     st.session_state.stage = i

# if st.session_state.stage == 0:
#     st.button('Begin', on_click=set_state, args=[1])

# if st.session_state.stage >= 1:
#     name = st.text_input('Name', on_change=set_state, args=[2])

# if st.session_state.stage >= 2:
#     st.write(f'Hello {name}!')
#     color = st.selectbox(
#         'Pick a Color',
#         [None, 'red', 'orange', 'green', 'blue', 'violet'],
#         on_change=set_state, args=[3]
#     )
#     if color is None:
#         set_state(2)

# if st.session_state.stage >= 3:
#     st.write(f':{color}[Thank you!]')
#     st.button('Start Over', on_click=set_state, args=[0])