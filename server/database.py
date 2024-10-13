#!/opt/homebrew/bin/python3

"""
Upload the predicted output to firebase.
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

# Fetch the service account key JSON file contents
cred = credentials.Certificate('keys.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})


def upload(output):
    # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference()
    databaseRef = ref.child(datetime.now().strftime("%d-%m-%Y") )
    # todays date in dd/mm/YY format

    databaseRef.push().set({
        'attacker': output,
    })
    #print(ref.get())