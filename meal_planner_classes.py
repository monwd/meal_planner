""" This is a simple meal planner that allows user to generate plan for required period basing on favourites recipes"""

import datetime
import pandas as pd
from IPython.display import display, HTML


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

    def draw_day_plan(self):
        c = Cookbook(df_recipes)
        self.breakfast = c.draw_meal_type('B')
        self.lunch = c.draw_meal_type('L')
        self.dinner = c.draw_meal_type('D')

    def __str__(self):
        return f"\n===================\n" \
               f"{self.date.strftime('%A')}" \
               f"\n===================\n" \
               f"Breakfast: {self.breakfast}\n" \
               f"Lunch: {self.lunch}\n" \
               f"Dinner: {self.dinner}\n" \
               f"==================="

    def html_date(self):
        html_date_template = f"""
         <table style="border-collapse: collapse; width: 100%;" border="1">
         <tbody>
         <tr valign="top">
         <td style="width: 100%;text-align: left">{self.date.strftime('%A')}</td>
         </tr>
         </tbody>
         </table>
         """
        return html_date_template

    def html_meal(self, meal):
        html_meal_template = f"""
         <table style="border-collapse: collapse; width: 100%;" border="1">
         <tbody>
         <tr>
         <td style="width: 100%; text-align: left"> {meal}</td>
         </tr>
 
         </tbody>
         </table>
         """

        return html_meal_template


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

    def create_html_table(self):
        w1 = WeeklyPlan(num_of_days)
        plans = self.list_of_day_plans
        days_str = f"{'</th><th>'.join(list(map(lambda plan: plan.html_date(), plans)))}"
        html_row_breakfasts = f"{'</td><td>'.join(list(map(lambda plan: plan.html_meal(meal=plan.breakfast), plans)))}"
        html_row_lunch = f"{'</td><td>'.join(list(map(lambda plan: plan.html_meal(meal=plan.lunch), plans)))}"
        html_row_dinner = f"{'</td><td>'.join(list(map(lambda plan: plan.html_meal(meal=plan.dinner), plans)))}"

        table_html = f"""
        
        <table>
        <tbody>
        <th></th>
        <th>{days_str}</th>
        <tr>
        <td style="width: 10%; height: 18px; text-align: left;"><strong>BREAKFAST</strong></span></td>
        <td>{html_row_breakfasts}</td>
        <tr>
        <td style="width: 10%; height: 18px; text-align: left;"><strong>LUNCH</strong></span></td>
        <td>{html_row_lunch}</td>
        </tr>
        <tr>
        <td style="width: 10; height: 18px; text-align: left;"><strong>DINNER</strong></span></td>
        <td>{html_row_dinner}</td>
        </tr>
        </tbody>
        </table>
        
         """
        return table_html

    def display_html(self, html_str):
        display(HTML(html_str))

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
    html_str = w.create_html_table()
    w.display_html(html_str)
