__author__ = "Pawan Parackal"
__email__ = "s4792248@student.uq.edu.au"
__date__ = "24/03/2023"

from constants import *


def num_hours() -> float:
    """
    Return the number of hours spent on this spent on this project
    >>num_hours()
    18.3
    """
    hr_spent = 18.3
    return hr_spent


def get_recipe_name(recipe: tuple[str, str]) -> str:
    """
    Return the name of the recipe

    Parameter:
    recipe -> A tuple with two string data

    >>get_recipe_name(('chocolate peanut butter banana shake', '1 large banana,240 ml almond milk'))
    'chocolate peanut butter banana shake'
    """
    # Unpacking tuple to get recipe name
    r_name, r_ingredients = recipe
    # Return the name of the recipe
    return r_name


def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """
    Return the ingredient breakdown from the detail amount, measure and ingredient

    Parameter:
    raw_ingredient_detail -> A string Value with raw ingredient detail

    >>parse_ingredient('0.5 tsp coffee granules')
    (0.5, 'tsp', 'coffee granules')
    """
    # Split the raw ingredient into amount, measure, ingredient using whitespace as the separator
    split_ingredient = raw_ingredient_detail.split()

    # If only amount, ingredient detail in raw_ingredient_detail does not contain measure, assume measure ''
    if len(split_ingredient) == 2:
        amount, *ingredient = split_ingredient
        measure = ''
    # Otherwise we can get the measure if the length greater than 2
    else:
        amount, measure, *ingredient = split_ingredient
        ingredient = ' '.join(ingredient)

    # Converting amount into float
    amount = float(amount)
    # Return tuple
    return amount, measure, ingredient


def create_recipe() -> tuple[str, str]:
    """
    Return a recipe in tuple format in a series of prompting ingredient

    >>create_recipe()
    Please enter the recipe name: peanut butter
    Please enter an ingredient: 300 g peanuts
    Please enter an ingredient: 0.5 tsp salt
    Please enter an ingredient: 2 tsp oil
    Please enter an ingredient:
    ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    """
    name = input("Please enter the recipe name: ")
    ingredients = []
    while True:
        ingredient = input("Please enter an ingredient: ")
        if not ingredient:
            break
        ingredients.append(ingredient)

    ingredients_str = ",".join(ingredients)
    return name, ingredients_str


def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
    """
    Return the ingredients of a recipe amount, measure, ingredients

    Parameter:
    recipe -> A tuple consisting of recipe name and its ingredients

    >> recipe_ingredients[('peanut butter','300 g peanuts,0.5 tsp salt,2 tsp oil'))
    ((300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil')]
    """
    recipe_name, ingredient_strs = recipe
    ingredients = []
    for ingredient_str in ingredient_strs.split(','):
        parts = ingredient_str.strip().split()
        amount = float(parts[0])
        unit = parts[1]
        ingredient = ' '.join(parts[2:])
        ingredients.append((amount, unit, ingredient))
    return tuple(ingredients)


def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]) -> None:
    """
    Returns nothing but adds new recipes to the recipe list

    Parameter:
    new_recipe -> A tuple of recipe needed to be added
    recipe -> A list of recipes
    """
    # Add new recipe to Recipe list
    recipes.append(new_recipe)


def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
    """
    Return either a recipe if it contains otherwise it gives none

    Parameter:
    recipe_name -> A string Value which is recipe name that needed to be found
    recipe -> A list of recipes

    >>recipes = [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    >>find_recipe('peanut butter', recipes)
    ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>find_recipe('cinnamon rolls', recipes)
    >>print(find_recipe('cinnamon rolls', recipes))
    None
    """
    # Finding the recipe name using for loop
    for x in recipes:
        r_name, r_ingredient = x
        if recipe_name == r_name:
            # If the recipe is found Return Recipes
            return x
    # Otherwise return None
    return None


def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """
    Return nothing but remove the recipe from the recipes list.
    If the name is not present in the list it will do nothing.

    Parameter:
    name -> A string Value that needed to be removed from recipes list
    recipes -> A List consisting of tuples


    >>recipes = [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'),
    ('cinnamon rolls', '480 ml almond milk,115 g Nuttelex,50 g sugar,7 g
    active dry yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown
    sugar,2 tbsp cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp
    vanilla extract')]
    >>remove_recipe('brownie', recipes)
    >>recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'), ('cinnamon
    rolls', '480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry
    yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp
    cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp vanilla
    extract')]
    >>remove_recipe('cinnamon rolls', recipes)
    >>recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    """
    # Finding the recipe name and removing it from the recipes
    for recipe in recipes:
        if name == recipe[0]:
            recipes.remove(recipe)
            break
    # Return None
    return


def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float, str]:
    """
    Return the amount and measure of a specific ingredients.
    If there is no ingredient present in the recipe it just return nothing

    Parameter:
    ingredient -> A string Value i.e. the ingredient nae to be find
    recipe -> A tuple consisting of recipe name and its ingredient

    >>recipe = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>get_ingredient_amount('peanuts', recipe)
    (300.0, 'g')
    >>get_ingredient_amount('soy beans', recipe)
    """
    # Unpacking tuple to get amount and measure of ingredient
    ingredient_item = recipe[1]
    amount, measure, ingredient_name = (parse_ingredient(ingredient_item))
    if ingredient == ingredient_name:
        return amount, measure


def add_to_shopping_list(ingredient_details: tuple[float, str, str],
                         shopping_list: list[tuple[float, str, str]] | None) -> None:
    """
    Return Nothing but it adds ingredients to shopping_list. If there is already a ingredient which should be added
    then amount gets combined

    Parameter:
    ingredient_detail -> A tuple consisting of ingredient along with the it's amount and measure
    shopping_list -> It is a list of tuple consisting of items to be bought

    >>shopping_list = [(300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'),
    (2.0, 'tsp', 'oil')]
    >>add_to_shopping_list((1000.0, 'g', 'tofu'), shopping_list)
    >>shopping_list
    [(300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (1000.0, 'g', 'tofu')]
    >>add_to_shopping_list((1200.0, 'g', 'peanuts'), shopping_list)
    >>shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (1000.0, 'g', 'tofu')]
    """
    # Check ingredient already exists in the shopping list
    for i, item in enumerate(shopping_list):
        if item and item[2] == ingredient_details[2]:
            # If it does, combine amounts and update
            amount = item[0] + ingredient_details[0]
            measure = item[1]
            name = item[2]
            shopping_list[i] = (amount, measure, name)
            return

    # If ingredient doesn't exist in the shopping list, add it
    shopping_list.append(ingredient_details)


def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: list) -> None:
    """
    Return a certain amount of ingredient with the given ingredient name from the shopping list

    Parameter:
    ingredient_name -> A String Value
    amount -> Float Value
    shopping_list -> A list consisting of ingredients

    >>shopping_list = [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'),
    (2.0, 'tsp', 'oil'), (9000.0, 'g', 'tofu'), (100.0, 'g', 'sugar'),
    (50.0, 'g', 'tomato sauce'), (120.0, 'g', 'rice'),
    (920.0, 'g', 'ice cream')]
    >>remove_from_shopping_list('ice cream', 500.0, shopping_list)
    >>shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (9000.0, 'g', 'tofu'), (100.0, 'g', 'sugar'), (50.0, 'g', 'tomato
    sauce'), (120.0, 'g', 'rice'), (420.0, 'g', 'ice cream')]
    """
    # Removing ingredient from the shopping list
    for i, item in enumerate(shopping_list):
        if item[2] == ingredient_name:
            remaining_amount = item[0] - amount
            if remaining_amount <= 0:
                shopping_list.pop(i)
            else:
                shopping_list[i] = (remaining_amount, item[1], item[2])
            break


def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    """
    Return a list of ingredients.

    Parameter:
    recipes -> A list of recipes

    >>shopping_list = generate_shopping_list([PEANUT_BUTTER,
    MUNG_BEAN_OMELETTE])
    >>shopping_list
    [(300.0, 'g', 'peanuts'), (1.0, 'tsp', 'salt'), (3.0, 'tsp', 'oil'),
    (1.0, 'cup', 'mung bean'), (0.75, 'tsp', 'pink salt'), (0.25, 'tsp',
    'garlic powder'), (0.25, 'tsp', 'onion powder'), (0.125, 'tsp',
    'pepper'), (0.25, 'tsp', 'turmeric'), (1.0, 'cup', 'soy milk')]
    """
    # Create an empty dictionary to store the quantity of each ingredient
    ingredients_dict = {}

    # Loop through each recipe and extract the ingredients and their quantities
    for recipe in recipes:
        ingredients = recipe[1].split(',')  # Split the ingredients string into a list
        for ingredient in ingredients:
            quantity, measure, name = ingredient.split()  # Split each ingredient into its quantity, measure and name
            quantity = float(quantity)  # Convert the quantity to a float
            # Add the quantity to the dictionary, if the ingredient already exists, add the quantity to its value
            if name in ingredients_dict:
                ingredients_dict[name] += quantity
            else:
                ingredients_dict[name] = quantity, measure

    # Create a list of tuples from the dictionary, with each tuple representing an ingredient
    shopping_list = [(quantity, measure, name) for name, (quantity, measure) in ingredients_dict.items()]

    return shopping_list


def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """
    Prints the shopping list in sorted order.

    Parameter:
    shopping_list -> A list of ingredients

    >>display_ingredients([(1.0, 'large', 'banana'), (0.5, 'cup', 'ice'),])
    | 1.0 | large | banana |
    | 0.5 | cup | ice |
    >>display_ingredients([(1.0, 'large', 'banana'),
    (2.0, 'tbsp', 'peanut butter'),
    (2.0, 'pitted', 'dates'),
    (1.0, 'tbsp', 'cacao powder'),
    (240.0, 'ml', 'almond milk'),
    (0.5, 'cup', 'ice'),
    (1.0, 'tbsp', 'cocao nibs'),
    (1.0, 'tbsp', 'flax seed')])
    | 1.0   | large  | banana        |
    | 2.0   | tbsp   | peanut butter |
    | 2.0   | pitted | dates         |
    | 1.0   | tbsp   | cacao powder  |
    | 240.0 | ml     | almond milk   |
    | 0.5   | cup    | ice           |
    | 1.0   | tbsp   | cocao nibs    |
    | 1.0   | tbsp   | flax seed     |
    """
    max_amount_len = max(len(str(item[0])) for item in shopping_list)
    max_measure_len = max(len(item[1]) for item in shopping_list)
    max_ingredient_len = max(len(item[2]) for item in shopping_list)
    print('| {} | {} | {} |'.format('amount'.center(max_amount_len), 'measure'.center(max_measure_len),
                                    'ingredient'.center(max_ingredient_len)))
    # Print the list in sorted order
    for item in sorted(shopping_list, key=lambda x: x[2]):
        print('| {} | {} | {} |'.format(str(item[0]).rjust(max_amount_len), item[1].center(max_measure_len),
                                        item[2].center(max_ingredient_len)))


def sanitise_command(command: str) -> str:
    """
    Return a standardised command to all lower-case and no leading or trailing white spaces removing
    any numbers from the string.

    Parameter:
    command -> A string value

    >>sanitise_command('add chocolate brownies')
    'add chocolate brownies'
    >>sanitise_command('add c4hocolate Brownies')
    'add chocolate brownies'
    """
    # Convert command to lower case and strips the leading/trailing white spaces
    command = command.lower().strip()

    # Remove if any digits from the command is there
    command = ''.join([i for i in command if not i.isdigit()])

    # Strip white spaces
    command = command.strip()

    return command


def main() -> None:
    """Coordinates the overall interaction with the user."""
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE,
        BROWNIE,
        SEITAN,
        CINNAMON_ROLLS,
        PEANUT_BUTTER,
        MUNG_BEAN_OMELETTE
    ]
    # shopping list
    shopping_list = []
    # shopping cart
    shopping_cart = []

    while True:
        command = input("Please enter a command: ")
        if command.lower() == 'h':
            print("H or h: Help"
                  "\nmkrec: creates a recipe, add to cook book."
                  "\nadd {recipe}: adds a recipe to the collection."
                  "\nrm {recipe}: removes a recipe from the collection."
                  "\nrm -i {ingredient_name} {amount}: removes ingredient from shopping list."
                  "\nls: list all recipes in shopping cart."
                  "\nls -a: list all available recipes in cook book."
                  "\nls -s: display shopping list."
                  "\ng or G: generates a shopping list."
                  "\nQ or q: Quit.")
        elif sanitise_command(command) == 'mkrec':
            add_recipe(create_recipe(), recipe_collection)
        elif command.startswith('add'):
            recipe_name = sanitise_command(command[4:])
            if recipe_name is None:
                print(f"Recipe '{recipe_name}' not found.")
            else:
                shopping_cart.append(find_recipe(recipe_name, recipe_collection))
                shopping_list = generate_shopping_list(shopping_cart)
        elif command.startswith('rm'):
            if command.startswith('rm -i'):
                amount = ''.join(i for i in command[-1:-len(command)+6:-1] if i.isdigit())[::-1]
                ingredient_name = command[6:len(command)-len(amount)]
                remove_from_shopping_list(sanitise_command(ingredient_name), float(amount), shopping_list)
            else:
                recipe_name = sanitise_command(command[2:])
                if recipe_name is None:
                    print(f"Recipe '{recipe_name}' not found.")
                else:
                    remove_recipe(recipe_name, shopping_cart)
                    shopping_list = generate_shopping_list(shopping_cart)
        elif command == 'ls':
            print(shopping_cart)
        elif command == 'ls -a':
            for recipes in recipe_collection:
                get_recipe_name(recipes)
        elif command == 'ls -s':
            display_ingredients(shopping_list)
        elif command.lower() == 'g':
            if not shopping_list:
                return None
            else:
                display_ingredients(shopping_list)
        elif command.lower() == 'q':
            break


if __name__ == "__main__":
    main()
