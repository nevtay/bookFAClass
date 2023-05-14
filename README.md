# bookFAClass
A python script that automates the class booking process. Requires several inputs from user. Requires the Firefox browser to use.

# Use
- Users should enter `python3 bookFAClass.py *arg1* *arg2* *arg3 (optional)*` in the command line launched from the same folder where this script is located.
  - arg1 is the user's username and is parsed as a string. This input is **mandatory**.
  - arg2 is the user's password and is parsed as a string. This input is **mandatory**.
  - arg3 is the number of days to advance the current booking date by, is parsed as an integer, and is **optional**. For example, if today is Sunday and the user wishes to check the classes on the upcoming Tuesday, a value of "2" should be provided to the input.
- If nothing goes wrong=, the user should see the browser launch and navigate to the login page where it will use the provided username and password to log in. 
- If successfully logged in, the booking page should either move forward by the number of days provided by `arg3`, or stay on the current date if the argument was left blank.
- The terminal should then display all available classes on the current date. Each option should start with a number in square brackets (e.g. `[1]`).
- User will be prompted to enter the number associated with the desired class. Pressing enter with a valid number will cause the browser to open the booking page for that class
- User will then be prompted to either accept or cancel the booking.
