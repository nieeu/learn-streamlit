# Import libraries

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app

st.title("Palmer's Penguins")
st.markdown('Use this Streamlit to make my own scatterplot about penguins!')

# selected_species = st.selectbox('What species would you like to visualize?',['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the x variable to be?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
                                                                         'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm','body_mass_g'])

# Import dataset
penguins_df = pd.read_csv('penguins.csv')
st.write(penguins_df.head())
# penguins_df = penguins_df[penguins_df['species'] == selected_species]

# Visualization
sns.set_style('darkgrid')

fig, ax = plt.subplots()
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
ax = sns.scatterplot(data = penguins_df, x = selected_x_var, y = selected_y_var, hue = 'species', markers = markers, style = 'species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
st.pyplot(fig)