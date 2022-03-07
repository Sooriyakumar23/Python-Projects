# Function

1. User authentication for modifying user details using a code & the authentication code also can be changed
    * Name
    * Gmail address
    * Wi-Fi SSID
    * Wi-Fi password
    * Authentication Code
2. Start sending data from local to Firestore in Firebse
    * Initialize an object to send data to Firestore using configuration file ['key.json']  
    * A function defined for getting and preparing data to send
    * Another function :- Threading the above function
    * BASE_URL/start route will open the page for sending data
    * Data will be sending when correct authentication code put and pressed SUBMIT button
3. Stop sending data from local to Firestore in Firebse
    * BASE_URL/start route will open the page to end sending data
    * Data will not be sending when correct authentication code put and pressed SUBMIT button
4. Exception handling for following cases
    * Wrong authentication code
    * Wrong gmail address when starting

# How to use ?
- Create new folder and open cmd/terminal in that folder
- https://firebase.google.com/ - Click this url
- Create an account and click "Get started"
- Create your project
- Go to your : Firebase portal --> Project Settings --> Service accounts --> Generate new private key {https://clemfournier.medium.com/how-to-get-my-firebase-service-account-key-file-f0ec97a21620}
- Rename this json file as 'key.json' & shift this to the project folder that we created first of all
- git clone https://github.com/Sooriyakumar23/Flask-FireStore.git
- Run "pip install -r requirements.txt" in the terminal
- Run "python server.py" in the terminal
- Copy and paste the following urls for particular operations

    BASE_URL = https://192.168._.___:2397
    1. Homepage : Just a page with 2 pictures and welcome message with the user name
        BASE_URL/
    2. Settings page : Setting page to modify username, gmail address, Wi-Fi SSID, Wi-Fi password, Authentication code
        BASE_URL/setting
    3. Start page : Start passing data from local server/computer to Firestore in Firebase
        BASE_URL/start
    4. End page : End passing data from local server/computer to Firestore in Firebase
        BASE_URL/end

# Techs used
1. Python - programming language
2. Flask - micro web framework
3. Firestore - Database in firebase
4. Html
5. Threading
6. Sublime text - IDE