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


class Meals:
    def __init__(self, type, meals):
        self.type = type
        self.meals = meals


# Allows to select from the csv meal of specific type without repetition
class Cookbook:
    def __init__(self, df_recipes):
        self.df_recipes = df_recipes.copy()

    def draw_meal_type(self, meal_type):
        meal = self.df_recipes.loc[self.df_recipes['Type'] == meal_type].sample()
        self.df_recipes.drop(meal.index[0], inplace=True)
        meal1 = Meal(meal.index[0], meal.Type[0], meal.Category[0], meal.Ingredients[0])
        return meal1.name


# Generates meal plan for one single day
class SingleDayPlan:
    def __init__(self, date):
        self.date = date
        self.breakfast = None
        self.lunch = None
        self.dinner = None

    def draw_day_plan(self, cookbook):
        self.breakfast = cookbook.draw_meal_type('B')
        self.lunch = cookbook.draw_meal_type('L')
        self.dinner = cookbook.draw_meal_type('D')

    def __str__(self):
        return f"\n===================\n" \
               f"{self.date.strftime('%A')}" \
               f"\n===================\n" \
               f"Breakfast: {self.breakfast}\n" \
               f"Lunch: {self.lunch}\n" \
               f"Dinner: {self.dinner}\n" \
               f"==================="


# Generate final meal plans for required number of days
class WeeklyPlan:

    def __init__(self, num_of_days):
        self.num_of_days = num_of_days
        self.list_of_day_plans = None

    def draw_meal_plan(self, cookbook):
        list_of_day_plans = []
        for day_num in range(1, self.num_of_days + 1):
            d = datetime.date.today() + datetime.timedelta(days=day_num)
            day_plan = SingleDayPlan(d)
            day_plan.draw_day_plan(cookbook=cookbook)
            list_of_day_plans.append(day_plan)
        self.list_of_day_plans = list_of_day_plans
        return list_of_day_plans

    def __str__(self):
        return '\n'.join([str(plan) for plan in self.list_of_day_plans])


# Generates final version of table in html
class HtmlGenerator:
    def __init__(self, list_of_day_plans):
        self.list_of_day_plans = list_of_day_plans

    # Generate table
    def create_html_table(self):
        column_names = list(map(lambda plan: plan.date.strftime('%A'), self.list_of_day_plans))
        breakfast = Meals("BREAKFAST", list(map(lambda plan: plan.breakfast, self.list_of_day_plans)))
        lunch = Meals("LUNCH", list(map(lambda plan: plan.lunch, self.list_of_day_plans)))
        dinner = Meals("DINNER", list(map(lambda plan: plan.dinner, self.list_of_day_plans)))
        rows = [breakfast, lunch, dinner]
        return self.generate_table(column_names, rows)

    def generate_table_header(self, column_names):
        header_columns = list(map(lambda name: f"<th>{name}</th>", column_names))
        return f"<tr><th></th>{''.join(header_columns)}</tr>"

    def generate_td(self, values):
        return list(map(lambda value: f"<td >{value}</td>", values))

    def generate_content(self, rows):
        html_rows = list(
            map(lambda row: f"<tr><td class=rowTitle>{row.type} </td>{''.join(self.generate_td(row.meals))}</tr>",
                rows))
        return ''.join(html_rows)

    def generate_table(self, column_names, rows):
        style = '''  <style>
      table {
        border-collapse: collapse;
      }
      th {
        padding: 10px;
        background-color: #00aa8d;
        font-size: 14px;
        font-weight: 700;
      }
      td {
        padding: 10px;
      }
      tr:hover {
        background-color: magenta;
      }
       .rowTitle {
        background-color: #00aa8d;
        font-size: 14px;
        font-weight: 700;
        }
    </style>'''
        table_html = f"""
          <html>
          <head> 
          {style}         
          </head>
          <body>
          <table style="border-collapse: collapse" border="1">
          <caption style="text-align: center; color:red; font-size:20px">MEAL PLANNER</caption>
          {self.generate_table_header(column_names)}
          {self.generate_content(rows)}
          </table>
          </body>
          </html>
           """
        return table_html


# Error handling when other value than int provided for num_of_days
def get_input():
    try:
        num_of_days = int(input("For how many days do you want to plan meals?   \n"))
        return num_of_days

    except ValueError:
        raise ValueError("Provide integer value")


def main():
    df_recipes = pd.read_csv("recipes_base.csv", index_col=0, sep=";")
    cookbook = Cookbook(df_recipes=df_recipes)
    num_of_days = get_input()
    w = WeeklyPlan(num_of_days)
    w.draw_meal_plan(cookbook)
    html_str = HtmlGenerator(w.list_of_day_plans).create_html_table()
    return html_str


if __name__ == "__main__":
    main()
