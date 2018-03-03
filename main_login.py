from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

 
class ReusableForm(Form):
        email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        
        password=request.form['password']
        email=request.form['email']
        print  email, " ", password
 
        if form.validate():
            # Save the comment here.
            flash('Thank you for login ')
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('GetLogin_redirectHere.html', form=form)
 
if __name__ == "__main__":
    app.run()

Update the template hello.html with this code:

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
    <head>
        <title>iOT of Medical </title>
       <link rel="stylesheet" media="screen" href ="static/bootstrap.min.css">
       <link rel="stylesheet" href="static/bootstrap-theme.min.css">
       <meta name="viewport" content = "width=device-width, initial-scale=1.0">
 
    </head>
    <body>
 
 
<div class="container">
 
 
  <h2>IOT For Medical</h2>
  <form  action="" method="post" role="form">
    {{ form.csrf }}
    <div class="form-group">
      
      <label for="email">Email:</label>
      <input type="text" class="form-control" id="email" name="email" placeholder="Enter Your EMail id">
      <br>
      <label for="password">Password:</label>
      <input type="password" class="form-control" id="password" name="password" placeholder="Enter a password.">
 
 
    </div>
    <button type="submit" class="btn btn-success">Sign Up</button>
  </form>
 
  <br>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
 
        {% for message in messages %}
            {% if "Error" not in message[1]: %}
                <div class="alert alert-info">
                <strong>Success! </strong> {{ message[1] }}
                </div>
            {% endif %}
 
            {% if "Error" in message[1]: %}
                <div class="alert alert-warning">
                {{ message[1] }}
                </div>
            {% endif %}
        {% endfor %}
            {% endif %}
        {% endwith %}
 
</div>
<br>            
</div>
</div>
</body>
</html>
