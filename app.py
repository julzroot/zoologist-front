import streamlit as st

"""
# Zoologist front
"""

URL = 'http://localhost:8501/'

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

"""
## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

1. Let's ask for:
- island (the location where the penguin lives: Biscoe, Dream or Torgersen)
- bill length (in mm)
- bill depth (in mm)
- flipper length (in mm)
- body mass (in g)
- sex ("Male" or "Female")
"""

"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""

# penguins_dict = {
#     'island' : island,
#     'bill_length_mm' : bill_length_mm,
#     'bill_depth_mm' : bill_depth_mm,
#     'flipper_length_mm' : flipper_length_mm,
#     'body_mass_g' : body_mass_g,
#     'sex' : sex
# }

# Selection of input parameters
## Island
island = st.selectbox('Select an island', ['Dream', 'Torgersen', 'Biscoe'])
st.markdown(
    """The island you chose:"""
)
st.write(island)

## Bill_length, bill_depth, flipper_length, body_mass
bill_length_mm = st.slider('Select a bill length (in mm)', min_value = 30, max_value = 100, step = 3)
bill_depth_mm = st.slider('Select a bill depth (in mm)', min_value = 10, max_value = 50, step = 2)
flipper_length_mm = st.slider('Select a flipper length (in mm)', min_value = 150, max_value = 300, step = 5)
body_mass_kg = st.slider('Select a body mass (in g)', min_value = 3500, max_value = 4500, step = 50)

## Sex
sex = st.radio('Select a sex', ('Male', 'Female'))
