import streamlit as st
import requests
import base64

URL = st.secrets['API_URL']

st.set_page_config(page_title='NUT-NUT', page_icon='🕵️‍♀️', layout='wide')

"""
# 🌟 Penguin species prediction 🌟
"""

st.image(
    "Pingu_GIF.gif",
    #caption="Penguin classification",
    alt="pingu",
    width = 800
)

# """### gif from url"""
# st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

# """### gif from local file"""
# file_ = open("/home/rzwitch/Desktop/giphy.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

# st.markdown(
#     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
#     unsafe_allow_html=True,
# )


# st.markdown(
#     """
# Remember that there are several ways to output content into your web page...

# Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
# """
# )

# """
# ## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

# 1. Let's ask for:
# - island (the location where the penguin lives: Biscoe, Dream or Torgersen)
# - bill length (in mm)
# - bill depth (in mm)
# - flipper length (in mm)
# - body mass (in g)
# - sex ("Male" or "Female")
# """

# """
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Of course... The `requests` package 💡

# What are the steps to follow in order to call an API ?

# 1. Which url will you use? Save it in a variable so you can easily change it later...

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# """

# Input parameters (controled by user)
## Island
island = st.selectbox('Select an island 🏝️', ['Dream', 'Torgersen', 'Biscoe'])
# st.markdown(
#     """The island you chose:"""
# )
# st.write(island)

## Bill_length, bill_depth, flipper_length, body_mass
bill_length_mm = st.slider('Select a bill length (in mm) 👃📏', min_value = 30.0, max_value = 65.0, step = 0.1)
bill_depth_mm = st.slider('Select a bill depth (in mm) 👃🕳️', min_value = 10.0, max_value = 25.0, step = 0.1)
flipper_length_mm = st.slider('Select a flipper length (in mm) 🪽📏', min_value = 160.0, max_value = 250.0, step = 0.1)
body_mass_g = st.slider('Select a body mass (in g) ⚖️', min_value = 2500, max_value = 6500, step = 1)

## Sex
sex = st.radio('Select a sex 🚹🚺', ('Male', 'Female'))

st.image(
    "gentoo.png",
    #caption="Penguin classification",
    alt="help-input-params",
    width = 650
)

penguins_dict = {
    'island' : island,
    'bill_length_mm' : bill_length_mm,
    'bill_depth_mm' : bill_depth_mm,
    'flipper_length_mm' : flipper_length_mm,
    'body_mass_g' : body_mass_g,
    'sex' : sex
}

# API request

if st.button("Predict species"): # On créé un bouton que l'utilisateur doit activer pour déclencher la préd
    # Autrement a chaque mouvement de slider, ca envoie une requete à l'app pour refaire une prédiction
    response = requests.get(URL, params=penguins_dict)

    if response.status_code == 200:
        species = response.json()['species']
        proba = round(response.json()['probability']*100,3)
        st.success(f"🕵️‍♀️ I think it is .... **{species}** ! But I'm only {proba}% sure 🐧")
    else:
        st.error(f"API error: {response.status_code} - {response.text}")
