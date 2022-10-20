""" This is a simple meal planner that allows user to generate plan for required period basing on favourites recipes"""

import datetime
# import random
# import xlrd
import csv
import pandas as pd
from pprint import pprint

df_recipes = pd.read_csv("recipes_base.csv", index_col=0, sep=";")


# num_of_days = int(input("For how many days do you want to plan meals?  \n"))

def get_input():  # error handling when other value than int provided
    try:
        num_of_days = int(input("For how many days do you want to plan meals?  \n"))
        return num_of_days

    except ValueError:
        raise ValueError("Provide integer value")


num_of_days = get_input()


# Generate meal plan for one single day
class SingleDayPlan:

    def __init__(self):
        self.breakfast = None
        self.lunch = None
        self.dinner = None

    def draw_meal_type(self, meal_type):
        meal = df_recipes.loc[df_recipes['Meal_type'] == meal_type].sample()
        df_recipes.drop(meal.index[0], inplace=True)
        return meal.index[0]

    def __str__(self):
        rep = f"\n===================\nBreakfast: {self.breakfast}\nLunch: {self.lunch}\nDinner: {self.dinner}\n==================="
        return rep

    def draw_day_plan(self):
        self.breakfast = self.draw_meal_type('B')
        self.dinner = self.draw_meal_type('L')
        self.lunch = self.draw_meal_type('D')

#Generate final meal plan for required number of days
class WeeklyPlan:

    def __init__(self, num_of_days):
        self.num_of_days = num_of_days
        self.list_of_day_plans = None
        self.selected_days = None

    def meal_plan(self):
        list_of_day_plans = []
        for day_num in range(self.num_of_days):
            day_plan = SingleDayPlan()
            day_plan.draw_day_plan()
            list_of_day_plans.append(day_plan)
        self.list_of_day_plans = list_of_day_plans
        return list_of_day_plans

    def list_of_days(self):
        selected_days = []
        today = datetime.date.today()
        for specific_day in range(1, self.num_of_days + 1):
            selected_days.append((today + datetime.timedelta(days=specific_day)))
        self.selected_days = selected_days
        return selected_days

    def generate_plan(self):
        self.meal_plan()
        self.list_of_days()
        for day, plan in zip(self.selected_days, self.list_of_day_plans):
            print(day.strftime("%A"), plan)


w = WeeklyPlan(num_of_days)
w.generate_plan()
