########## Importing necessary libraries ##########
from flask import Flask, render_template, request, Response
from threading import Thread
import firebase_admin, datetime, time, os
from firebase_admin import credentials, firestore

########## Initializing app ##########
app = Flask(__name__)
picfolder = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = picfolder

########## 1. Route for HOME PAGE ##########
@app.route('/', methods=['GET'])
def login():
	########## Read CREDENTIALS.txt ##########
    with open('credentials.txt', 'r') as f:
        cred = f.read().split(",")
        NAME = cred[0]
    if request.method == 'GET':
        home1 = os.path.join(app.config['UPLOAD_FOLDER'], 'home.png')
        home2 = os.path.join(app.config['UPLOAD_FOLDER'], 'compuser.jpg')
        return (render_template('home.html', message=NAME, home1=home1, home2=home2))

########## 2. Route for SETTINGs ##########
@app.route('/setting', methods=['GET', 'POST'])
def setting():
    if request.method == 'GET': ########## GET method only ##########
        setting1 = os.path.join(app.config['UPLOAD_FOLDER'], 'setting.jpg')
        return (render_template('login.html', setting1=setting1))
    elif request.method == 'POST' : ########## POST method only ##########

    ########## Read CREDENTIALS.txt ##########
        with open('credentials.txt', 'r') as f:
            cred = f.read().split(",")
            NAME = cred[0]
            EMAIL = cred[1]
            KEY = cred[2]
            PASS = cred[3]
            CODE = cred[4]

        name = request.form["name"]
        email = request.form["email"]
        key_name = request.form["key"]
        pass_word = request.form["password"]
        old_auth_code = request.form["oldauthcode"]
        new_auth_code = request.form["newauthcode"]
		
        if old_auth_code == CODE: ########## Correct Authentication Code ##########
            if name =="":
                name = NAME
            if email == "":
                email = EMAIL
            if key_name == "":
                key_name = KEY
            if pass_word == "":
                pass_word = PASS

            if (email != EMAIL) or (new_auth_code != ""):
                with open('credentials.txt', 'w') as f:
                    if new_auth_code == "":
                        text = name+","+email+","+key_name+","+pass_word+","+old_auth_code
                    else:
                        text = name+","+email+","+key_name+","+pass_word+","+new_auth_code
                    f.write(text)
            result = os.path.join(app.config['UPLOAD_FOLDER'], 'update.png')
            return (render_template('result.html', message1="AUTHENTICATED.", message2='SUCCESSfully UPDATEd SETTINGs', result=result, color='#28a62a'))
        else: ########## Incorrect Authentication code ##########
            result = os.path.join(app.config['UPLOAD_FOLDER'], 'code.png')
            return (render_template('result.html', message1="NOT authenticated.", message2="Authentication code that you gave is incorrect.", result=result, color='#c43745'))
	
    else: ########## PUT / DELETE methods ##########
        return ("Access DENIED")


########## Initial setups for Firebase Data Transmission ##########
cred = credentials.Certificate('key.json') # Capture certificate
firebase_admin.initialize_app(cred) # Initialize connection
db = firestore.client() # Created the object

# Processed data ; JN ----------> FS

stop_run = False

def my_function(uid, pass_word, key_name, name):
    global stop_run
    while not stop_run:
        ##### 1. Capture video frames from Posture and Stress Cameras #####
        ##### 2. 3D skeleton detection from Postural Camera #####
        ##### 3. RULA assess from 3D skeletons #####
        ##### 4. Stress feature extraction from Stress Camera #####
        ##### 5. Multi output regression model results #####
        ##### 6. Send data to firestore <- bad/good, 4scores, 6outputs, NASA_TLX, ..... #####
        now = str(datetime.datetime.now())
        data_docs = db.collection('data').document(uid) # Creating Main Collection
        data_posture = data_docs.collection("POSTURE").document(now) # Creating POSTURE Document
        data_posture.set({'time':now, 'pass_word': pass_word, 'ssid': key_name}) # Sending POSTURE Document
        data_stress = data_docs.collection("STRESS").document(now) # Creating STRESS Document
        data_stress.set({'time':now, 'pass_word': pass_word, 'name':name}) # Sending STRESS Document
        time.sleep(3)
        print("Sending...")

def manual_run(uid, pass_word, key_name, name):
    t = Thread(target=my_function, args=(uid, pass_word, key_name, name))
    t.start()
    return "Processing"


########## 3. Route for START ##########
@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
        startting = os.path.join(app.config['UPLOAD_FOLDER'], 'startting.png')
        return (render_template('startting.html', startting=startting))
    elif request.method == 'POST':
        with open('credentials.txt', 'r') as f:
            cred = f.read().split(",")
            AUTH = cred[-1]
            email = cred[1]
            pass_word = cred[-2]
            key_name = cred[-1]
            name = cred[0]
        if AUTH == request.form['authcode']:
            global stop_run
            stop_run = False

            # Connect to Wi-Fi <- Subprocess to run commands in command prompt {key_name, pass_word}
            ##### 0. If success then below ##### ----->
            
            users_docs = db.collection('users').stream()
            time.sleep(1)
            uid = ''
            for doc in users_docs:
                field = doc.to_dict()
                if 'email' in field.keys():
                    if field['email'] == email:
                        uid = doc.id
                
            if uid == '':
                result = os.path.join(app.config['UPLOAD_FOLDER'], 'email.png')
                return (render_template('result.html', message1="AUTHENTICATED.", message2='EMAIL address is NOT found in FireStore', result=result, color='#f041e4'))
                
            else:
                print ("###################### Here we go ######################")
                return Response(manual_run(uid, pass_word, key_name, name), mimetype="text/html")

            ##### 0. If fail then this ##### -----> 
            #return (render_template('result.html', message1="AUTHENTICATED.", message2='Invalid Wi-Fi key or password or Router not powered yet.'))

        else:
            result = os.path.join(app.config['UPLOAD_FOLDER'], 'code.png')
            #return ("Wrong AUTHENTICATION code.....")
            return (render_template('result.html', message1="NOT authenticated..", message2='Authentication code that you gave is incorrect.', result=result, color='#c43745'))

########## 4. Route for END ##########
@app.route('/end', methods=['GET', 'POST'])
def end():
    if request.method == 'GET':
        stopping = os.path.join(app.config['UPLOAD_FOLDER'], 'stopping.png')
        return (render_template('stopping.html', stopping=stopping))
    elif request.method == 'POST':
        with open('credentials.txt', 'r') as f:
            cred = f.read().split(",")
            AUTH = cred[-1]
        if AUTH == request.form['authcode']:
            global stop_run
            stop_run = True

            stop = os.path.join(app.config['UPLOAD_FOLDER'], 'stop.png')
            return ("You have STOPped processing.....")
        else:
            result = os.path.join(app.config['UPLOAD_FOLDER'], 'code.png')
            return (render_template('result.html', message1="NOT authenticated..", message2='Authentication code that you gave is incorrect.', result=result, color='#c43745'))

########## Run App ##########
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2397)