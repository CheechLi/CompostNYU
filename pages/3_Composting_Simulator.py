import streamlit as st
import random
import numpy as np
import pandas as pd
import simulator.choices as choices

st.title("Composting Simulator")

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if 'weeks' not in st.session_state:
    st.session_state.weeks = 0

st.subheader("Week " + str(st.session_state.weeks + 1))

greens = ["fruits/vegetables", "coffee grounds", "eggshells", "grass clippings", "leaves", "tea bags", "weeds", "yard trimmings", "flowers"]
browns = ["cardboard", "newspaper", "organic paper", "paper straw", "wood chips", "sawdust", "hay", "egg cartons", "toilet paper rolls"]
not_allowed = ["dairy", "meat", "bones", "fish", "grease", "oil", "glossy paper", "pet waste", "weeds with seeds", "diseased plants", "inorganic materials"]
col1, col2, col3 = st.columns([1, 3, 1])

if("greens" not in st.session_state):
    st.session_state.greens = 0
if("browns" not in st.session_state):
    st.session_state.browns = 0

def addGreen():
    st.session_state.plotdata.iloc[st.session_state.weeks + 1, 1] += 1
    st.session_state.greens += 1

def addBrown():
    st.session_state.plotdata.iloc[st.session_state.weeks + 1, 2] += 1
    st.session_state.browns += 1

if("ch" not in st.session_state):
    st.session_state.ch = choices.getChoices()

# st.subheader(str(st.session_state.stage))
if("plotdata" not in st.session_state):
    st.session_state.plotdata = pd.DataFrame(np.array([[0, 0, 0]]), columns=["Weeks", "Greens", "Browns"])

with col2:
    # print(st.session_state.plotdata)
    st.progress(st.session_state.weeks/15, text="Week " + str(st.session_state.weeks + 1) + " of 15")
    st.line_chart(
        st.session_state.plotdata,
        x="Weeks",
        y=["Greens", "Browns"],
        color=["#964B00", "#00FF00"])

with col3:
    if(st.session_state.stage == 0):
        if(len(st.session_state.plotdata) != st.session_state.weeks + 2):
            newrow = pd.DataFrame(np.array([[st.session_state.weeks + 1, st.session_state.greens, st.session_state.browns]]), columns=["Weeks", "Greens", "Browns"])
            st.session_state.plotdata = pd.concat([st.session_state.plotdata, newrow], ignore_index=True)
        chSubmit = st.button("Submit")
        st.write("You now have the following items that you're considering to compost. Choose the items that can be composted:")
        options = st.multiselect("Select the items that can be composted:", st.session_state.ch, disabled=chSubmit)
        
        if chSubmit:
            for c in st.session_state.ch:
                if(c in not_allowed and c in options):
                    st.write("You realized that you can't compost " + c + ". You discarded it.")
                if(c not in not_allowed and c not in options):
                    st.write("You realized that you should have composted " + c + ". You added it to the compost pile.")
                    if(c in greens):
                        addGreen()
                    if(c in browns):
                        addBrown()
                if(c in greens and c in options):
                    addGreen()
                if(c in browns and c in options):
                    addBrown()
                
            set_state(1)
    if(st.session_state.stage == 1):

        if 2 > st.session_state.browns/st.session_state.greens:
            st.write("Because you don't have enough browns, the compost pile is way too wet and starts to smell. Add more browns to balance it out.")
        elif st.session_state.browns/st.session_state.greens > 3:
            st.write("Because you don't have enough greens, the compost pile is too dry and composting too slowly. Add more greens to balance it out.")
        else:
            st.write("Your compost pile is balanced! Make sure to keep a ratio between 2:1 and 3:1 browns to greens.")
            if(st.session_state.browns/st.session_state.greens > 3):
                st.button("Next", on_click=set_state, args=[random.choice([2, 3])])
            else:
                st.button("Next", on_click=set_state, args=[random.choice([2, 4])])
            # st.button("Next", on_click=set_state, args=[2])

        st.button("Add Browns", on_click=addBrown)
        st.button("Add Greens", on_click=addGreen)
    if(st.session_state.stage == 2):
        if("moisture" not in st.session_state):
            st.session_state.moisture = random.choice([random.randint(0, 30), random.randint(70, 100)])
        if(st.session_state.moisture < 30):
            st.write("Your pile is too dry! Add more greens to balance it out.")
        elif(st.session_state.moisture > 70):
            st.write("Your pile is too wet because it rained a lot! Add more browns to balance it out.")
        else:
            st.write("Your pile is at a good moisture level. Keep it up!")
            if(st.session_state.browns/st.session_state.greens > 3):
                st.button("Next", on_click=set_state, args=[3])
            else:
                st.button("Next", on_click=set_state, args=[4])

        def addGreenMoisture():
            if(st.session_state.moisture <= 90):
                addGreen()
                st.session_state.moisture += 10
            else:
                st.warning("Your pile is too wet! Add more browns to balance it out.")
        def addBrownMoisture():
            if(st.session_state.moisture >= 10):
                addBrown()
                st.session_state.moisture -= 10
            else:
                st.warning("Your pile is too dry! Add more greens to balance it out.")
        
        st.button("Add Greens", on_click=addGreenMoisture)
        st.button("Add Browns", on_click=addBrownMoisture)
        st.write("Moisture Level: " + str(st.session_state.moisture) + "%")

    if(st.session_state.stage == 3):
        if("temperature" not in st.session_state):
            st.session_state.temperature = random.randint(60, 90)
        if(st.session_state.temperature < 90):
            st.write("Your pile is too cold! Add more greens to heat it up between 90 to 150 degrees Fahrenheit.")
        else:
            st.write("Your pile is at a good temperature. Keep it up!")
            st.button("Next", on_click=set_state, args=[4])

        def addGreenTemperature():
            if(st.session_state.temperature <= 140):
                addGreen()
                st.session_state.temperature += 10
            else:
                st.warning("Your pile will only get hotter if the pile gets larger. The optimal temperature is between 90 and 150 degrees Fahrenheit. You cannot add any more greens for now.")
        
        st.button("Add Greens", on_click=addGreenTemperature)
        st.write("Temperature: " + str(st.session_state.temperature) + "°F") 

    if(st.session_state.stage == 4):
        st.write("Time to turn! It is crucial to allow for oxygen to reach the center of the pile. This will help the microorganisms break down the materials through aerobic decomposition.")
        if st.button("Turn Pile"):
            del st.session_state.ch
            if("moisture" in st.session_state):
                del st.session_state.moisture
            if("temperature" in st.session_state):
                del st.session_state.temperature
            st.session_state.weeks += 1
            set_state(0)
            if(st.session_state.weeks == 15):
                set_state(5)

if(st.session_state.stage == 5):
    st.header("Congratulations! You have successfully composted for 15 weeks. Your compost is now ready to be used in your virtual garden. Now, you are ready to compost in real life!")

with col1:
    st.write("Greens: " + str(st.session_state.greens))
    st.write("Browns: " + str(st.session_state.browns))
    if(st.session_state.greens == 0):
        st.write("B/G Ratio: " + str(st.session_state.browns))
    else:
        st.write("B/G Ratio: " + str(st.session_state.browns / st.session_state.greens))
