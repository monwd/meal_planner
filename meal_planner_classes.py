""" This is a simple meal planner that allows user to generate plan for required period basing on favourites recipes"""

import datetime
import pandas as pd


class Meal:
    def __init__(self, name, meal_type, category, ingredients):
        # name of meal
        self.name = name

        # meal type = Breakfast (B), Lunch (L), Dinner (D)
        self.meal_type = meal_type

        # category = veg, non veg
        self.category = category

        # list of meal ingredients
        self.ingredients = ingredients


class Cookbook:
    def __init__(self, df_recipes):
        self.df_recipes = df_recipes

    def draw_meal_type(self, meal_type):
        meal = self.df_recipes.loc[df_recipes['Type'] == meal_type].sample()
        df_recipes.drop(meal.index[0], inplace=True)
        meal1 = Meal(meal.index[0], meal.Type[0], meal.Category[0], meal.Ingredients[0])
        return meal1.name


class SingleDayPlan:
    def __init__(self, date):
        self.date = date
        self.breakfast = None
        self.lunch = None
        self.dinner = None

    def __str__(self):
        return f"\n===================\n" \
               f"{self.date.strftime('%A')}" \
               f"\n===================\n" \
               f"Breakfast: {self.breakfast}\n" \
               f"Lunch: {self.lunch}\n" \
               f"Dinner: {self.dinner}\n" \
               f"==================="

    def draw_day_plan(self):
        c = Cookbook(df_recipes)
        self.breakfast = c.draw_meal_type('B')
        self.lunch = c.draw_meal_type('L')
        self.dinner = c.draw_meal_type('D')


# Generate final meal plans for required number of days
class WeeklyPlan:

    def __init__(self, num_of_days):
        self.num_of_days = num_of_days
        self.list_of_day_plans = None

    def draw_meal_plan(self):
        list_of_day_plans = []
        for day_num in range(1, self.num_of_days + 1):
            d = datetime.date.today() + datetime.timedelta(days=day_num)
            day_plan = SingleDayPlan(d)
            day_plan.draw_day_plan()
            list_of_day_plans.append(day_plan)
        self.list_of_day_plans = list_of_day_plans
        return list_of_day_plans

    def __str__(self):
        return '\n'.join([str(plan) for plan in self.list_of_day_plans])


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
    w.draw_meal_plan()
    print(w)
