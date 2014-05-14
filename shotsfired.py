'''
Your assignment is to use the boilerplate app we've been building in class to produce JSON from
a new database, in this case of Medicare payments to doctors in Columbia. Specifically, you should
create a function that returns all of the data from the "doctors" table when someone visits the 
"/doctors" route in your application.

Most of the code below is boilerplate that you won't have to modify. You should only be changing
two areas: first, change the appropriate setting to connect the application to the "medicare.sqlite"
database (which is included in the repository). Second, write a function that produces the JSON.
'''

########## IMPORTS (DON'T CHANGE THESE) ##########

import os
# import sqlite3
import json
from flask import Flask, g, render_template, make_response



app = Flask(__name__)
app.config.from_object(__name__)

########## SETTINGS (CHANGE THESE AS APPROPRIATE) ##########

# DATABASE = 'data/medicare.sqlite'
# USERNAME = ''
# PASSWORD = ''

########## DATABASE CONNECTION BOILERPLATE (DO NOT CHANGE THIS) ##########

# Load default config and override config from an environment variable
# app.config.update(dict(
#     DATABASE=os.path.join(app.root_path, DATABASE),
#     DEBUG=True,
#     SECRET_KEY='',
#     USERNAME=USERNAME,
#     PASSWORD=PASSWORD
# ))

# def connect_db():
#     """Connects to the specific database."""
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv

# def get_db():
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db

# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()

########## APP CODE (YOUR FUNCTION GOES HERE) ##########

#to display an index page, do not name it index in the decorator, simply list the address by slash. duh.  labelling it index will throw an error and drive you nuts.

@app.route('/')
def index():
    return 'Index Page'

# @app.route("/doctors")
# def combine_latlong():    
#     db = get_db()
#     cur = db.execute('select Date,"day of week", "incident time", "nature code", Address, formatted_latitude, formated_longitude, formatted_zip  from combine_latlong;')

#     combine_latlong = []
#     for row in cur.fetchall():
#         combine_latlong.append(dict(row))

#     template = json.dumps(combine_latlong)

#     response = make_response(template)
#     response.headers["Content-Type"] = "application/json"
#     return response

# @app.route("/crosslet")
# def crosslet_shotsfired():    
#     db = get_db()
#     cur = db.execute('select change, date, year, month, day, time, hour, addr, lon, lat, zip, nature  from crosslet_shotsfired;')

#     crosslet_shotsfired = []
#     for row in cur.fetchall():
#         crosslet_shotsfired.append(dict(row))

#     template = json.dumps(crosslet_shotsfired)

#     response = make_response(template)
#     response.headers["Content-Type"] = "application/json"
#     return response

# @app.route("/crosslet2")
# def crosslet_shotsfired2():    
#     db = get_db()
#     cur = db.execute('select change, date, year, month, day, time, hour, addr, lon, lat, zip, nature, all2  from crosslet_shotsfired2;')

#     crosslet_shotsfired2 = []
#     for row in cur.fetchall():
#         crosslet_shotsfired2.append(dict(row))

#     template = json.dumps(crosslet_shotsfired2)

#     response = make_response(template)
#     response.headers["Content-Type"] = "application/json"
#     return response

@app.route("/dcjs")
def dcjs():    
    #template here
    return render_template("/html/index.html")

@app.route("/sf")
def sf():    
    #template here
    return render_template("/sf/index.html")


    

# @app.route("/topten")
# def topten():    
#     db = get_db()
#     cur = db.execute('select nppes_provider_first_name, nppes_provider_last_org_name, npi, count(*) from procedures group by 3 order by 4 desc limit 10;')

#     topten = []
#     for row in cur.fetchall():
#         topten.append(dict(row))

#     template = json.dumps(topten)

#     response = make_response(template)
#     response.headers["Content-Type"] = "application/json"
#     return response





########## EXECUTION BOILERPLATE (ALSO DON'T CHANGE THIS) ##########

if __name__ == "__main__":
    app.run(debug=True)