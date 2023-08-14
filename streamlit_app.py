import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

# create the repeatable code block
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
    normalizedSelectedFruit = pandas.json_normalize(fruityvice_response.json())
    return normalizedSelectedFruit


# new Section to display fruityvice api response
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()


streamlit.header("The fruit load list contains:")

#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()


#add a button to load the fruit
if streamlit.button('Get Fruit Load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)


def add_fruit_to_snow_flake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values('"+ new_fruit +"')")
        return "Thank you for adding "+  new_fruit


fruit_choice_add = streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add Fruit into Snow Flake'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_fruit_add = add_fruit_to_snow_flake(fruit_choice_add)
    streamlit.text(my_fruit_add)


