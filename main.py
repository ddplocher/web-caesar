from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
  <head>
    <style>
      form {{
      background-color: #eee;
      padding: 20px;
      margin: 0 auto;
      width: 540px;
      font: 16px sans-serif;
      border-radius: 10px;
      }}
      textarea {{
          margin: 10px 0;
          width: 540px;
          height: 120px;
      }}

      </style>
    </head>
<body>
  <form action = "/" method= "POST"/>
  <label for = rot/>
  
  Rotate by:
  
  <input type = "text" name = "rot"/>
 
  <textarea name = "text">{0}</textarea>

 <input type = "submit" />
  

"""

@app.route("/")
def index():
    
    return form.format(" ")

@app.route("/", methods= ["POST"])
def encrypt():
   
    new_rot = request.form["rot"]
    new_text = request.form['text']
    new_message = rotate_string(str(new_text), int(new_rot))
    
   
    return form.format(new_message)
    

app.run()