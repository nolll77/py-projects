import requests
import json
import pandas as pd

url = "https://uk.api.just-eat.io/restaurants/bypostcode/E1 7EA"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'referer': 'https://fonts.googleapis.com/'
}
result = requests.get(url, headers=headers)
json_dict = json.loads(result.content.decode()) # method that parses a Json string and converts in a dict

# In json_dict, the main key is 'Restaurants' which contains lots of sub-dictionaries.
# The restaurant_key variable is a list pointing to the 'Restaurants' specific main key.
# This list will be used in different functions to sort out the Names, Ratings and Type of food for every opened restaurants.
restaurant_key = json_dict['Restaurants']

def type_of_cuisine(list):
    """type_of_cuisine first filters restaurants that are opened for delivery - and then returns the
       type of food they serve.

    Args:
        The variable restaurant_key (Type: list) representing the variable json_dictionary (dict)
        that contains descriptive categorized informations (ie: Name, Address, CuisineTypes, etc)
        which are the keys of the dictionaries.

    Returns:
        A list of inner little lists, in which we have dictionaries where the values of those are the types of food. 
    """

    open_for_delivery = []
    
    for i in list:
        if i['IsOpenNowForDelivery'] == True:
            open_for_delivery.append(i['Cuisines'])

    return open_for_delivery

# type_cuisine is a list of inner lists which each ones contain a dictionary
type_cuisine = type_of_cuisine(restaurant_key)

# transform type_cuisine which is a list into a dataframe
df_type_of_cuisine = pd.DataFrame(type_cuisine)

def find_number_of_columns(datafr, list):
    """Because the original extracted JSON string can have a different number of columns each time we execute this Python code, we have to
       know this specific number of columns. Once we know it, we hard-code the names of the columns for the passed dataframe, regarding
       in the meantime the specific number of columns. 

    Args:
        datafr (a dataframe): df_type_of_cuisine is a dataframe in which each column represents the end-dictionary founded in type_cuisine
        list (a list): type_cuisine is a list of inner lists, each inner list contains a dictionary

    Returns:
        A dataframe: It's the same dataframe that has been passed in argument - this returned one has brand clean named columns
    """

    shape_type_of_cuisine = df_type_of_cuisine.shape[1]
    
    for column in datafr:

        if shape_type_of_cuisine == 1:
            datafr = pd.DataFrame(list, columns =['col1'])

        if shape_type_of_cuisine == 2:
            datafr = pd.DataFrame(list, columns =['col1', 'col2'])

        if shape_type_of_cuisine == 3:
            datafr = pd.DataFrame(list, columns =['col1', 'col2', 'col3'])

        if shape_type_of_cuisine == 4:
            datafr = pd.DataFrame(list, columns =['col1', 'col2', 'col3', 'col4'])

        if shape_type_of_cuisine == 5:
            datafr = pd.DataFrame(list, columns =['col1', 'col2', 'col3', 'col4', 'col5'])

        if shape_type_of_cuisine == 6:
            datafr = pd.DataFrame(list, columns =['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

        if shape_type_of_cuisine == 7: # I have seen more than 7 (i.e. 13) but code works idkw 
            datafr = pd.DataFrame(list, columns =['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'])

    return datafr

# Assign a df_type_of_cuisine_numbered variable
df_type_of_cuisine_numbered = find_number_of_columns(df_type_of_cuisine, type_cuisine)

# https://stackoverflow.com/a/55279799
# Flatten the dataframe in order to have consistent columns names
json_struct = json.loads(df_type_of_cuisine_numbered.to_json(orient="records"))
df_flat = pd.json_normalize(json_struct)

list_type_of_cuisine_consistent_names_sorted = sorted(df_flat.columns.values)

def keep_2firts_consistent_names(list):
    """To remove all type-of-cuisine columns names that won't be used when executing the code.
       Because those removed ones are not useful, ie wording has only lower characters or are not well written
       with dash symbols separating the words.
       Purpose is to hold the cleaned and proper type-of-cuisine names.

    Args:
        list (Type: list): list_type_of_cuisine_consistent_names_sorted is a list with the type-of-cuisine
        that a restaurant proposes. The list has sorted consistent names.

    Returns:
        A list: that keeps only the first consistent name and the one called col2.Name
    """
    list_to_keep_2firts_consistent_names =[]

    list_to_keep_2firts_consistent_names.append(list[0])

    for i in list:
        if i == "col2.Name":
            list_to_keep_2firts_consistent_names.append(i)
            
    return list_to_keep_2firts_consistent_names

list_keep_2first = keep_2firts_consistent_names(list_type_of_cuisine_consistent_names_sorted)

# Use a list comprehension in order to keep only the 2 columns in list_keep_2first and remove all others
cols_to_drop = [i for i in list_type_of_cuisine_consistent_names_sorted if i not in list_keep_2first]

# Finally we got our 2 deisired food information for each restaurant!!! 
df_type_of_cuisine_numbered = df_flat.drop(
    cols_to_drop,
    axis=1
)

def restaurants_names(list):
    """restaurants_names() gets back all the names of restaurants who are open-for-delivery
       when executing the code.

    Args:
        The variable restaurant_key (Type: list) representing the origin variable json_dictionary (dict)
        that contains descriptive categorized informations (ie: Name, Address, CuisineTypes, etc)
        which are the keys of the dictionaries.

    Returns:
        A list: that contains all restaurants names.
    """
    list_restaurants_names = []
    
    for i in list:

        if i['IsOpenNowForDelivery'] == True:

            list_restaurants_names.append(f"{i['Name']}")

    return list_restaurants_names

# Assign the returned list of restaurants to a variable
list_of_restaurants_names = restaurants_names(restaurant_key)

# Transform list_of_restaurants_names into a dataframe
df_restaurants_names = pd.DataFrame(list_of_restaurants_names)

def rating_stars(list):
    """rating_stars() gets back all the average notes of restaurants who are open-for-delivery
       when executing the code.

    Args:
        The variable restaurant_key (Type: list) representing the origin variable json_dictionary (dict)
        that contains descriptive categorized informations (ie: Name, Address, CuisineTypes, etc)
        which are the keys of the dictionaries.

    Returns:
        A list: that contains all the average notes.
    """
    average_note = []

    for i in list:
        if i['IsOpenNowForDelivery'] == True:
            average_note.append(f"{i['RatingStars']}")

    return average_note

# Assign the returned average notes to a variable
rating = rating_stars(restaurant_key)

# Transform the variable rating into a dataframe
df_rating = pd.DataFrame(rating)

# Rename the 3 final dataframes with user-friendly names:
# "Restaurant name", "Stars av.", "Spéciality 1", "Spéciality 2 (or Country)"
# If we don't rename properly, the concatenation won't give a good result because of same name for 2 dataframes.
df_restaurants_names = df_restaurants_names.rename(columns = {0:'Restaurant name'})
df_rating = df_rating.rename(columns = {0:'Stars av.'})
df_type_of_cuisine_numbered = df_type_of_cuisine_numbered.rename(columns = {"col1.Name":'Spéciality 1', "col2.Name":'Spéciality 2 (or Country)'})

# Concatenate the 3 dataframes
frames = [df_restaurants_names, df_rating, df_type_of_cuisine_numbered]
result = pd.concat(frames, axis=1)

pd.set_option('display.max_rows', 1000)
print("="*220)
print(f"Hi! We have currently {len(df_restaurants_names.index)} restaurants/groceries opened.")
print("They can't wait to deliver your order at your home or office!!!")
print(result.head(100))