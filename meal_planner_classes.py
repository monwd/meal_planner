""" This is a simple meal planner that allows user to generate plan for required period basing on favourites recipes"""

import datetime
import pandas as pd


# Generate meal plan for one single day
class SingleDayPlan:

    def __init__(self):
        self.breakfast = None
        self.lunch = None
        self.dinner = None
        self.date = None

    def draw_meal_type(self, meal_type):
        meal = df_recipes.loc[df_recipes['Meal_type'] == meal_type].sample()
        df_recipes.drop(meal.index[0], inplace=True)
        return meal.index[0]

    def __str__(self):
        rep = f"\n===================\n{self.date}\n===================\n" \
              f"Breakfast: {self.breakfast}\nLunch: {self.lunch}\nDinner: {self.dinner}\n==================="
        return rep

    def draw_day_plan(self, date):
        self.date = date
        self.breakfast = self.draw_meal_type('B')
        self.dinner = self.draw_meal_type('L')
        self.lunch = self.draw_meal_type('D')


# Generate final meal plans for required number of days
class WeeklyPlan:

    def __init__(self, num_of_days):
        self.num_of_days = num_of_days
        self.list_of_day_plans = None
        self.selected_days = None

    def meal_plan(self):
        list_of_day_plans = []
        for day_num in range(1, self.num_of_days + 1):
            day_plan = SingleDayPlan()
            day_plan.draw_day_plan((datetime.date.today() + datetime.timedelta(days=day_num)).strftime("%A"))
            list_of_day_plans.append(day_plan)
        self.list_of_day_plans = list_of_day_plans
        return list_of_day_plans

    #     def list_of_days(self):
    #         today = datetime.date.today()
    #         selected_days = [(today + datetime.timedelta(days=specific_day)) for specific_day in
    #                          range(1, self.num_of_days + 1)]
    #         self.selected_days = selected_days
    #         return selected_days

    def generate_plan(self):
        self.meal_plan()
        for plan in self.list_of_day_plans:
            print(plan)


# Error handling when other value than int provided for num_of_days
def get_input():
    try:
        num_of_days = int(input("For how many days do you want to plan meals?  \n"))
        return num_of_days

    except ValueError:
        raise ValueError("Provide integer value")


if __name__ == "__main__":
    df_recipes = pd.read_csv("recipes_base.csv", index_col=0, sep=";")
    num_of_days = get_input()
    w = WeeklyPlan(num_of_days)
    w.generate_plan()
