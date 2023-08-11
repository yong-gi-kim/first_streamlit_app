import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner2')

streamlit.header('💀Breakfast Menu')
streamlit.text('🎉Omega 3 & Blueberry Oatmeal')
streamlit.text('🥭Kale, Spnach & Rocket Smoothie')
streamlit.text('🍋Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(
    my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")


# # write your own comment -what does the next line do? I will get the json displayed as "Pandas Table"
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # write your own comment - what does this do? -> in a dataframe
# streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
# streamlit.dataframe(fruityvice_response)
normalizedSelectedFruit = streamlit.text(fruityvice_response.json())

streamlit.dataframe(normalizedSelectedFruit)