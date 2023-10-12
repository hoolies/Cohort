#!/usr/bin/env python3
"""This is a flask app that will create a random alphanum and give you a link"""
from flask import Flask, render_template
from random import choice
from sqlite3 import connect
from datetime import datetime


# Set the app
app = Flask(__name__)

# Creating password.db in the local directory
con = connect("tempass.db", check_same_thread=False)

# In order to run SQL we need to create a cursor
cur = con.cursor()

# Query the db tp see of tje table exists
res = cur.execute("SELECT name FROM sqlite_master")

# If does not exists ot exist, create the table
if res.fetchone() is None:
    cur.execute("Create Table tempass(Token, Password, Time)")


def alphanumeric_generator(length: int = 14, complexity: int = 4) -> str:
    """This function will generate a random alphanum according to lenght and complexity criteria"""
    # Set lists with Uppercase, Lowercase, Numbers and Symbols
    lowercase = [chr(i) for i in range(97,123)]
    uppercase = [chr(i) for i in range(65,91)]
    numbers = [chr(i) for i in range(48,58)]
    symbols = [chr(i) for i in range(33,48)] + [chr(i) for i in range(58,65)] + [chr(i) for i in range(91,97)] + [chr(i) for i in range(123,127)]
    # Create conditions for the complexity level
    if complexity == 1:
        alphanumlist = [choice(lowercase) for _ in range(length)]
    elif complexity == 2:
        alphanumlist = [choice(lowercase + uppercase) for _ in range(length)]
    elif complexity == 3:
        alphanumlist = [choice(lowercase + uppercase + numbers) for _ in range(length)]
    elif complexity == 4:
        alphanumlist = [choice(lowercase + uppercase + numbers + symbols) for _ in range(length)]
    # Catch the error in case complexity is not between 1 - 4
    else:
        print("Invalid complexity level, please choose between 1 - 4")
    # Convert the list to a string and return it
    alphanum = "".join(alphanumlist)
    return alphanum


@app.route('/') # type: ignore
def root_response():
    """Returns the index page"""
    return render_template("index.html")


@app.route('/generate/')
def generate_password_uri() -> str: # type: ignore
    """API call to generate password and link"""
    # Creating password.db in the local directory
    password = alphanumeric_generator()
    uri = alphanumeric_generator(length = 10, complexity = 3)
    # Transforms timw to epoch
    now = int(datetime.now().timestamp())
    two_days_old = now - 172800
    cur.execute(
    f"""
    INSERT INTO tempass(Token, Password, Time) 
    VALUES (?,?,?);
    """, (uri, password, now)
    )
    con.commit()
    # cur.execute(f"""    
    # DELETE FROM "tempass" WHERE Time<'{two_days_old}'
    # """)
    con.commit()
    return render_template("token.html", uri=uri)


@app.route('/password/<uri>', methods=['GET', 'POST'])
def uri_response(uri: str) -> str:
    """Return the password"""
    # Connects to the database
    query_con = connect("tempass.db")
    query_cur = query_con.cursor()
    # Run a query to get the password
    password = list(query_cur.execute(f"""
    SELECT Password FROM tempass WHERE Token='{uri}'
    """))
    # Delete the row with the uri and the corresponding password from the database
    query_cur.execute(f"""    
    DELETE FROM tempass WHERE token='{uri}'
    """)
    query_con.commit()
    return render_template("password.html", password=password[0][0])
