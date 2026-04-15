import pyrebase

# Exact configuration extracted from strings.xml
config = {
    "apiKey": "AIzaSyAXsK0qsx4RuLSA9C8IPSWd0eQ67HVHuJY",
    "authDomain": "firestorm-9d3db.firebaseapp.com",
    "databaseURL": "https://firestorm-9d3db-default-rtdb.firebaseio.com",
    "storageBucket": "firestorm-9d3db.appspot.com",
    "projectId": "firestorm-9d3db"
}

# Initialize Firebase connection
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Credentials
email = "TK757567@pwnsec.xyz"

# IMPORTANT: Replace this string with the exact password your Frida script generated
password = "C7_dotpsC7t7f_._In_i.IdttpaofoaIIdIdnndIfC" 

try:
    # 1. Authenticate with Firebase
    print("[*] Attempting to authenticate with Firebase...")
    user = auth.sign_in_with_email_and_password(email, password)
    print("[+] Authentication successful. Token retrieved.")

    # 2. Access the database using the auth token
    db = firebase.database()
    flag_data = db.get(user['idToken'])
    
    # 3. Print the flag
    print("\n[+] FLAG Recovered:")
    print(flag_data.val())
    
except Exception as e:
    print("\n[-] Authentication Error. Did you paste the correct Frida password?")
    print(e)
