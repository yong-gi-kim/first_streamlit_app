import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner2')

streamlit.header('💀Breakfast Menu')
streamlit.text('🎉Omega 3 & Blueberry Oatmeal')
streamlit.text('🥭Kale, Spnach & Rocket Smoothie')
streamlit.text('🍋Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

fruit_apple = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple'])
fruit_apple_toShow = my_fruit_list.loc[fruit_apple]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.dataframe(fruit_apple_toShow)

streamlit.dataframe(my_fruit_list.loc['Grapes'])