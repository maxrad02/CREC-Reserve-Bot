# CREC-Reserve-Bot

This bot will automatically reserve a time slot for the city rec at which ever time you chose.

Important Note: You will recieve a duo push at 12 pm every time you want to reserve, you must accept this before it timeouts after 1 minute
Other Important Note: For mac users, good luck. You are gonna have to find a different way to schedule tasks

# Installation:
If unsure on any of these steps, follow this link: https://selenium-python.readthedocs.io/installation.html

  1. You must install python if you do not already have it 
    - Download link: https://www.python.org/downloads/
  
  2. Once done installing, you must run the command "pip install selenium" in command prompt

  3. You must download the chrome webdriver for the current version of chrome that you have
    - You can find this by:
      a. Click on the Menu icon in the upper right corner of the screen.
      b. Click on Help, and then About Google Chrome.
      c. Your Chrome browser version number can be found here.
    - Download link: https://sites.google.com/a/chromium.org/chromedriver/downloads
    (**You will need to remember the path of where you store this)

# Setup:

  1. Change the username and password variables to your nuid and password

  2. Edit the time you want to reserve for by changing the reserveTime variable

  3. Change the executable_path to the path that you stored the chrome webdriver

# Setting it up to run at 12pm every day:

  1. Open Task Scheduler for windows

  2. Create new task

  3. Edit name, change to run whether or not user is logged in, and check box to run with highest priviledges

  4. Create a new trigger that repeats when you want it to repeat that starts at 12:00:30 PM. I recommend creating two different tasks, one that runs sunday which runs a copy of the python script but with the time changed to 6:00 pm and another task that repeats monday, wednesday, thursday with the script set to reserve at 3:00 pm. This may be confusing, if you actually are setting this up, just dm me

  5. Create an action that runs the script at the location you stored it

  6. Check the box in conditions that says wake the computer up to run this task

  7. (optional) Change if the task fails, to restart every 10 minutes with a max of 3 times


If you have any questions or want any help setting this up, dm me
