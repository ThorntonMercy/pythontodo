This beginner python task was to create a simple to-do application.

Requirements included: 
1. Options for adding, viewing, deleting tasks
2. Option for quitting the app
3. Error handling to avoid improper / invalid input
4. Test to catch edge cases like empty lists


I think this program reminded me of something similar that we did back in python pre-work, where we were asking for input on pizza toppings. 
So the approach here was similar and relatively familiar. 

Since there's no webpage or things of the sort, I just jumped on in to create the menu. I wanted the necessary options and a relatively plain 
menu. 
The menu options are tied to their specific functions using if/elif/else statements. 
Each option requires it's own function for better readability
and for easier programming, so each menu option has a coordinating function related exclusively to it.
Each function has it's own try/except/else/finally statements.

The program will notify in the event that user input is invalid or doesn't exist, such as:
1. Not inputting anything.
2. Trying to delete something that doesn't exist.
3. Trying to view a list that has nothing on it.
4. Trying to do an option that doesn't actually exist (eg. selecting 6 on a menu of 1-5)
