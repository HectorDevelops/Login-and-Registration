from flask import Flask

app = Flask(__name__)

# Secret key needed for SESSION
app.secret_key = "Que viva la Republica Dominicana"

DATABASE = "login_and_registration_schema"