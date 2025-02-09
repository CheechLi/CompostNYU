import streamlit as st
import random
import simulator.choices as choices

st.title("Composting Simulator")

def set_state(i):
    st.session_state.stage = i

if 'stage' not in st.session_state:
    st.session_state.stage = 0

greens = ["fruits/vegetables", "coffee grounds", "eggshells", "grass clippings", "leaves", "tea bags", "weeds", "yard trimmings", "flowers"]
browns = ["cardboard", "newspaper", "organic paper", "paper straw", "wood chips", "sawdust", "hay", "egg cartons", "toilet paper rolls"]
not_allowed = ["dairy", "meat", "bones", "fish", "grease", "oil", "glossy paper", "pet waste", "weeds with seeds", "diseased plants", "inorganic materials"]
col1, col2 = st.columns([1, 3])

if("greens" not in st.session_state):
    st.session_state.greens = 0
if("browns" not in st.session_state):
    st.session_state.browns = 0

def addGreen():
    st.session_state.greens += 1

def addBrown():
    st.session_state.browns += 1

if("ch" not in st.session_state):
    st.session_state.ch = choices.getChoices()

with col2:
    if(st.session_state.stage == 0):
        chSubmit = st.button("Submit")
        st.write("You now have the following items that you're considering to compost. Choose the items that can be composted:")
        options = st.multiselect("Select the items that can be composted:", st.session_state.ch, disabled=chSubmit)
        
        if chSubmit:
            for c in st.session_state.ch:
                if(c in not_allowed and c in options):
                    st.write("You realized that you can't compost " + c + ". You discarded it.")
                if(c not in not_allowed and c not in options):
                    st.write("You realized that you should have composted " + c + ". You added it to the compost pile.")
                if(c in greens and c in options):
                    st.session_state.greens += 1
                if(c in browns and c in options):
                    st.session_state.browns += 1
            set_state(1)
    if(st.session_state.stage == 1):
        if 2 > st.session_state.browns/st.session_state.greens:
            st.write("Because you don't have enough browns, the compost pile is way too wet and starts to smell. Add more browns to balance it out.")
        elif st.session_state.browns/st.session_state.greens > 3:
            st.write("Because you don't have enough greens, the compost pile is too dry and composting too slowly. Add more greens to balance it out.")
        else:
            st.write("Your compost pile is balanced! Make sure to keep a ratio between 2:1 and 3:1 browns to greens.")
            st.button("Next", on_click=set_state, args=[2])
        
        st.button("Add Browns", on_click=addBrown)
        st.button("Add Greens", on_click=addGreen)
    if(st.session_state.stage == 2):
        

with col1:
    st.write("Greens: " + str(st.session_state.greens))
    st.write("Browns: " + str(st.session_state.browns))
    if(st.session_state.greens == 0):
        st.write("B/G Ratio: " + str(st.session_state.browns))
    else:
        st.write("B/G Ratio: " + str(st.session_state.browns / st.session_state.greens))



# def main():
#     st.set_page_config(page_title="Composted", layout="centered")
#     st.button("Greens", on_click=addGreen)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import random

# operation = st.selectbox(
#     "Which type of operation shall we do for the numbers 1 and 2?",
#     ["add", "subtract", "multiply", "divide"],
# )

# if "rand_num1" not in st.session_state:
#     st.session_state["rand_num1"] = random.randint(0, 20)

# if "rand_num2" not in st.session_state:
#     st.session_state["rand_num2"] = random.randint(0, 20)

# if st.toggle("Randomly generate my numbers"): # I think this looks nicer than a checkbox here
#     if st.button("regenerate numbers"):
#         st.session_state["rand_num1"] = random.randint(0, 20)
#         st.session_state["rand_num2"] = random.randint(0, 20)
#     num1 = st.session_state["rand_num1"]
#     num2 = st.session_state["rand_num2"]
#     st.write(f"Your random numbers are: `{num1}` and `{num2}`.")


# else:
#     num1 = st.number_input(
#         "What is the first number?", min_value=0, max_value=20, key="num1"
#     )

# if st.button("Do math"):
#     if operation == "add":
#         num = num1 + num2
#     elif operation == "subtract":
#         num = num1 - num2
#     elif operation == "multiply":
#         num = num1 * num2
#     elif operation == "divide":
#         num = num1 / num2

#     st.write(f"With the operation {operation}, your result is {num}.")