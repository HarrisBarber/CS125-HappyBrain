# CS125-HappyBrain

to run the program, run the python file health_state.py
if it fails to run due to missing libraries, run pip -r install on requirements.txt to install the necessary python libraries

The main files that we wrote are:
guidance.py
prompt.py
questionaire.py
health_state.py
fitbit_data.py

prompt.py displays a tkinter window with text boxes for inputting the user's name and their answer to the question "do you want to do the questionaire?"

questionaire.py displays a tkinter window with questions that each have a coresponding dropdown menu with possible values between 0 and 9 inclusive

health_state.py calls prompt.py to start up and display it's window.  if the user has said that they want to fill in the questionaire, then if the user's name has already been recorded by the system before starting (they are a returning user) then an existing state txt file is read from, otherwise the program prepares a new file to be created.  questionaire.py is then told to display its window and the answers to the questions are recorded into the file (calculating the new average if it's a returning user).  After that, guidance.py is told to display itself

guidance.py displays a tkinter window populated with various messages and buttons to open relevant text links based on the values gathered from the user's questionaire answers and from the data gathered about calories, sleep, stepcout, and heartrate from fitbit_data.py

fitbit_data.py uses the fitbit api to access data from the fitbit account assiciated with the CLIENT_SECRET and CLIENT_ID. The file can get the amount of sleep, the heartrate, the calories burned, and the number of steps taken
