"""
Notice1:
col"*".Name and col"*".SeoName have same values,
so delete col"*".SeoName in order to keep name values starting with Capital

Notice 2:
Can remove col3."*" to col6."*" ; 
because values are poor

Notice3:
Originally create the Dataframe with 6 columns because certain rows had up to 6 ;
had to go to this limit - shame

"""

col1.Name
['Pizza' 'Chicken' 'Breakfast' 'Burgers' 'Groceries' 'Italian'
 'Fish & Chips' 'Desserts' 'Lebanese' 'Kebab' 'Greek' 'Mediterranean'
 'Brunch' 'Sandwiches' 'Middle Eastern' 'Caribbean' 'American' 'Japanese'
 'Doughnuts' 'Turkish' 'Indian' 'Iranian' 'Coffee' 'Lunch' 'Bakery'
 'Healthy' 'Bagels' 'Crepes' 'Café' 'Korean' 'Ukrainian' 'Vegan' 'Wraps'
 'Asian' 'Seafood' 'Thai' 'Vietnamese' 'Alcohol' 'British' 'Smoothies'
 'Ice Cream']

col1.SeoName
['pizza' 'chicken' 'breakfast' 'burgers' 'groceries' 'italian'
 'fish-and-chips' 'desserts' 'lebanese' 'kebabs' 'greek' 'mediterranean'
 'brunch' 'sandwiches' 'middle-eastern' 'caribbean' 'american' 'japanese'
 'doughnuts' 'turkish' 'indian' 'iranian' 'coffee' 'lunch' 'bakery'
 'healthy' 'bagels' 'crepes' 'cafe' 'korean' 'ukrainian' 'vegan' 'wraps'
 'asian' 'seafood' 'thai' 'vietnamese' 'alcohol' 'british' 'smoothies'
 'icecream']

col2.Name
['Italian' 'Burgers' 'American' 'Sandwiches' 'Café' 'Chicken' 'Drinks'
 'Breakfast' 'Alcohol' 'British' 'Brunch' 'Coffee' 'Mediterranean' 'Lunch'
 'Peri Peri' 'Lebanese' 'Supermarkets' 'Brazilian food' 'Kebab'
 'Vegetarian' 'Turkish' 'Healthy' 'Sushi' 'Indian' 'Grill' 'Pasta' 'Curry'
 'Burritos' 'Persian' 'Middle Eastern' 'Salads' 'Gourmet' 'Smoothies'
 'Bakery' 'Vegan' 'Tapas' 'Desserts' 'Portuguese' 'Low Delivery Fee'
 'Malaysian' 'Baguettes' 'Crepes' 'Milkshakes' 'Groceries' 'Cakes'
 'Arabic' 'Mexican' 'Pizza']

col2.SeoName
['italian' 'burgers' 'american' 'sandwiches' 'cafe' 'chicken' 'drinks'
 'breakfast' 'alcohol' 'british' 'brunch' 'coffee' 'mediterranean' 'lunch'
 'peri-peri' 'lebanese' 'supermarkets' 'brazilian-food' 'kebabs'
 'vegetarian' 'turkish' 'healthy' 'sushi' 'indian' 'grill' 'pasta' 'curry'
 'burritos' 'persian' 'middle-eastern' 'salads' 'gourmet' 'smoothies'
 'bakery' 'vegan' 'tapas' 'desserts' 'portuguese' 'low-delivery-fee'
 'malaysian' 'baguettes' 'crepes' 'milkshakes' 'groceries' 'cakes'
 'arabic' 'mexican' 'pizza']

col3.Name
[nan 'Halal' 'Low Delivery Fee' 'Breakfast' 'Sandwiches']

col3.SeoName
[nan 'halal' 'low-delivery-fee' 'breakfast' 'sandwiches']

col4.Name
[nan 'Low Delivery Fee' 'Sandwiches' 'Breakfast']

col4.SeoName
[nan 'low-delivery-fee' 'sandwiches' 'breakfast']

col5.Name
[nan 'Low Delivery Fee' 'Sandwiches']

col5.SeoName
[nan 'low-delivery-fee' 'sandwiches']

col6.Name
[nan 'Low Delivery Fee']

col6.SeoName
[nan 'low-delivery-fee']
