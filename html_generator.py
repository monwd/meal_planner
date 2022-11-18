from typing import List

from pydantic import BaseModel

import meal_planner_classes


class Meals(BaseModel):
    type: str
    meals: List[str] = []

    # def __init__(self, type, meals):
    #     self.type = type
    #     self.meals = meals


# Generates final version of table in html
class HtmlGenerator(BaseModel):
    list_of_day_plans: List[meal_planner_classes.SingleDayPlan] = []

    # def __init__(self, list_of_day_plans):
    #     self.list_of_day_plans = list_of_day_plans

    # Generate table
    def create_html_table(self):
        column_names = list(map(lambda plan: plan.date.strftime('%A'), self.list_of_day_plans))
        breakfast = Meals(type="BREAKFAST", meals=list(map(lambda plan: plan.breakfast, self.list_of_day_plans)))
        lunch = Meals(type="LUNCH", meals=list(map(lambda plan: plan.lunch, self.list_of_day_plans)))
        dinner = Meals(type="DINNER", meals=list(map(lambda plan: plan.dinner, self.list_of_day_plans)))
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
        background-color: red;
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


def creation_of_html_table():
    meal_plan = meal_planner_classes.creation_of_weekly_plan()
    html_str = HtmlGenerator(list_of_day_plans=meal_plan).create_html_table()
    return html_str


if __name__ == "__main__":
    creation_of_html_table()
