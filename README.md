Instructions on how to use this script:
Abstract:
This is code is designed to automate the process of changing variables for testing purposes. As Senior Design becomes more complicated and more variables in our code need to be changed, it's nice for all our variables to stay consistant. 

Step 1: Download Google Drive for desktop https://www.google.com/drive/download/ so the senior design project is in your local drive.

Step 2: Once you have working script and want to automate it, create a copy of the file and maybe rename it with vars, open up the data.xlsx file and change the variable names of the copy that need changing to $NAME. It must be consistant with the names on the data.xlsx. It also seems to take a minute for the local file to update with the drive. 

Step 3: Setup python through Anaconda which is the easiest method.

Step 4: Open terminal, go to the Automation directory, and enter:
python main.py --file=NAME_OF_THE_FILE

Just looking at the original_vars.py, I changed the names of the variables according to the data.xlsx 

I enter in terminal:
python main.py --file=original_vars.py

The main.py file will create and run a temporary file. Notice how as I change the variables in data.xlsx, the numbers in the temp file change as well. 