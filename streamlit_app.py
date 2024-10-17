import streamlit as st
from PIL import Image


ww=0
levainpct=0

def bread(flour, hydration, ww=0, levainpct=.25):
    salt = 0
    levain = 0
    water = 0
    salt = round(flour * .02)
    levain = round(flour * (levainpct/100))
    start = levain/2
    water = round(((start+flour)*(hydration+ww)-start)/100)
    return "Flour: "+ str(flour) +"g", "Salt: "+str(salt)+"g", 'Levain: '+str(levain)+"g", 'Water: '+str(water)+"g"


st.title('Sourdough Hydration Calculator')

image = Image.open('hojicha.JPG')
st.image(image, caption='Hojicha Infused Sourdough, 75% hydration', use_column_width=True)

st.markdown("Welcome to the sourdough hydration calculator.  I created this calculator to help me adjust my sourdough bread recipes for both size and hydration levels.  This calulator uses basic baker's percentages to allow you to customize the size of your loaf, as well as the amount of water needed for a target hydration level.  ")
st.markdown("I've always been a fan of big open airy crumbs, and higher hydration helps me get there.  To get you started, standard sourdough loaves start at around 65% hydration, and go all the way to 120%.")
st.markdown("Move the sliders to adjust flour weight, and hydration percentage and the calculator will return the needed starter(25%), salt(2%), and water for your recipe.")
st.markdown("Note, this includes the flour and water in your starter, assuming you are using a 50/50 Flour/Water starter")
st.markdown("I've included a whole wheat modifier.  If you've got a smidge of whole wheat in your dough, you can use the default option, but anything more than 20% and you should use the Less than 50% option.  Less than 50% adds 10% to your hydration automatically.  More than 50% adds 15% to your hydration.  Remember to autolyse for 2 hours if you're using WW!" )
# In[6]:
wwheat = st.radio(
    "Whole Wheat?",
    ('All white, maybe some WW', 'Less than 50%', 'More than 50%'))

if wwheat == 'Less than 50%':
    ww = .10
elif wwheat == 'More than 50%':
    ww = .15

levainpct = st.slider("Levain/Starter Percentage? (default is 25%)", 10, 50, 25, 1, format="%d%%")
st.write(levainpct, '%')
flours = st.slider("Flour by gram", 200, 1000, 200, 10)
st.write(flours)

hydrations = st.slider("Target hydration", 30, 120, 50, 1, format="%d%%")
st.write(hydrations, '%')

st.write(bread(flours, hydrations, ww, levainpct))


st.balloons()
