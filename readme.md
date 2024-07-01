---------------------------------------------------------------------------
Created By-
    Pavan M
    1KS20CS071
    mpavan2313@gmail.com
    8951219613
---------------------------------------------------------------------------
For adminstration login - username = admin , password = admin
User Login info is user's input but has no encryption.
---------------------------------------------------------------------------

Implements a meeting room booking system using Flask. 
It uses a database to store data.

Features:

->Administration and user Login
->Room Management by adminstrator
->Booking Rooms (specify date, time, duration)
->Conflict Detection (prevents overlapping bookings)

Limitations:

->Security: Storing user credentials directly in memory might not be secure.

Getting Started:

Prerequisites: Python 3, Flask (install using pip install Flask)
Clone the Repository: Clone this repository or download the files.
Run the Application:
Navigate to the project directory in your terminal.
Run python create_database.py to create a database.
Then Run python main.py to start the development server.
Access the application in your web browser at http://127.0.0.1:5000/ (default Flask development port).

User Guide:
For adminstration login - username = admin , password = admin
First navigate to administration and create rooms
Then you can login as user to book the available room

