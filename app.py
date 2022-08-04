#Creating a dictionary for birthstone activity 
# Alternate: Create nultiple HTML
# Creating new rout results
# Create function
# Conditionals (If/Else)
# Import images/text stating "your birth month is"

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import birth_calc


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# rout that corresponds to form action
# POST request
# store the user information
  
@app.route('/results', methods=['GET', 'POST'])
def results():
  # great way to debug - prints an ImmutableMultiDict to console
  # can make sure form is handling info properly to find bugs elsewhere
  # form_results = request.form
  # print(form_results)
  # return("BIRTHSTONE")

  user_info = request.form
  birthstone = birth_calc(user_info['birth_month'])
  user_birth = {
    'first_name': user_info['name'],
    'birthstone': birthstone
  }
  # first user birth is what is called in the template, second is from here
  return render_template('results.html', user_birth=user_birth)

app.run(host='0.0.0.0', port=81, debug=True)