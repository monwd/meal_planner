# Meal planner

#### General info

This project is a simple meal planner written in Python 3. It allows you to generate plan for required period of time basing on your standard favourites recipes. It will definetely save your time because you will not waste time thinking about what to cook. 


#### Technologies
Project is created with:
* Python  3
* HTML 


#### Setup
To run this application you need to: 
1. Run the code in your local environment.
2. Provide to your own name of recipes under recipes_base.csv file.
3. The following steps must be performed to get generated planner to specific email address:
    * Open the `sending_emails.py` file
    * Under `send_email` funtion find `email_to =`variable and provide there  required email address (in quotes).