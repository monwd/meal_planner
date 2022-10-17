""" This is a simple meal planner that allows user to generate plan for required period basing on favourites recipes"""

import datetime
import random

breakfast = ['eggs', 'omlet', 'tortilla', 'donut', 'sandwich', 'wafles', 'pancakes']

lunch = ['paella', 'steak with potatoes', 'dumplings', 'creamy chicken', 'roasted steak with tomatos', 'garlic chicken',
         'spaghetti carbonara']

dinner = ['ham and cheese sliders', 'tosts', 'vegetable tarta', 'salmon with vegetables', 'cesar salad', 'sausages',
          'pasta with garlic and tomato']


def recipes(number_of_selected_recipes):  # draw breakfasts, lunches and dinners from list, without repetition
    selected_breakfasts = random.sample(breakfast, number_of_selected_recipes)
    selected_lunches = random.sample(lunch, number_of_selected_recipes)
    selected_dinners = random.sample(dinner, number_of_selected_recipes)

    return selected_breakfasts, selected_lunches, selected_dinners

def get_input(): #error handling when other value than int provided
    try:
        required_number_of_days = int(input("For how many days do you want to plan meals?  \n"))
        return required_number_of_days

    except ValueError:
        raise ValueError("Provide integer value")


def meal_plan():  # print final plan of three meals for every day in required period of time
    required_number_of_days = get_input()
    selected_days = []
    today = datetime.date.today()
    for specific_day in range(1, required_number_of_days + 1):
        selected_days.append((today + datetime.timedelta(days=specific_day)))

    selected_breakfasts, selected_lunches, selected_dinners = recipes(required_number_of_days)
    for i in selected_days:
        print('-----------------')
        print(i.strftime("%A"))
        print('-----------------')
        print('Breakfast: ' + str(selected_breakfasts.pop()))
        print('Lunch: ' + str(selected_lunches.pop()))
        print('Dinner: ' + str(selected_dinners.pop()))


meal_plan()
