# Meal planner

### General info

This project is a simple meal planner written in Python 3. It allows you to generate plan for required period of time basing on your standard favourites recipes. It will definetely save your time because you will not waste time thinking about what to cook. 
***

### Technologies

Project is created with:
* Python  3
* HTML 
***

### Setup

To run this application you need to: 
1. Provide to your own recipes under recipes_base.csv file.
2. The following steps must be performed to send generated planner to specific email address:
    * Open the `sending_emails.py` file
    * Under `send_email` funtion find `email_to =`variable and provide there required email address (in quotes).
4. Open the `main.py` script and run the code 
    Note: Make sure the `sending_email_with_planne` is set to `True` so looks in the following way: `main(sending_email_with_planner=True)` (otherwise html version of planner will be printed, but email with planner will not be sent)