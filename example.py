from flask import Flask, render_template  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

app = Flask(__name__, template_folder = ".") 
# We created a Flask object and set template_folder to the current folder.
# We then assigned the Flask object into app variable.
app.config['SECRET_KEY'] = "longandrandomsecretkey"
# We added SECRET_KEY to our app object's configuration.
# The SECRET_KEY is commonly used for encryption with database connections and browser sessions. 
# WTForms will use the SECRET_KEY as a salt to create a CSRF token.
class CreateUserForm(FlaskForm):
    username = StringField(label=('Username'), validators=[DataRequired(), Length(max=64)])
    email = StringField(label=('Email'), Validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField(label=('Password'), validators=[DataRequired(),Length(min=8, message="Password should be atleast %(min)d characters long")])
    confirm_password = PasswordField(label=('Confirm Password'), Validators=[DataRequired(message="*Required"), EqualTo('password', message="Both Password fields must be equal!") ])
    receive_emails = BooleanField(label=("Receive marketting emails?"))
    submit = SubmitField(label=('Submit'))

# GreetUserForm class contains a StringField. As the name implies, this field expects and 
# will return a string value.
# The name of the field is username, and we'll use this name to access data of the form element.
# The label paremeters are what will be rendered on our page so that users would understand
# what data a form element captures. 
# We also have a submit button, which will try to submit the form if all fields pass our validation criteria.
# We are passing the validators parameter as a list. 
# This tells us that we can have multiple validators for each field.
# DataRequired():The username field will not be validated if there is no input data
# If you inspect the form element, you'll see that WTForms automatically added the required attribute to the input field:
# WTForms adds a basic front-end validation to our form field.
# To set a validation rule that only allows characters that are 5 characters and 60 characters long
# Use Length() validator with min and max parameters.
# PasswordField hides the password text on the front-end.
# BooleanField renders as a checkbox on the front-end since it only contains either 
# True (Checked) or False (Unchecked) values.
@app.route('/', methods=["GET", "POST"]) #A route displays and processes our form
def index():
    form = GreetUserForm()
    if form.validate_on_submit():
        return f"<h1> Welcome {form.username.data} </h1>" 
    return render_template("index.html", form=form)
# Our route has GET and POST methods. The GET method displays the form, whereas the POST method processes 
# the form data on submission. 
# We set the URL path to /, or the root URL, so it will appear as our web app's home page.
# if form.validate_on_submit():This rule says 'if the request method is POST and if the form 
# field(s) are valid, then proceed. If our form input passes our validation criteria, on the 
# next page a simple greet message will be rendered with the user's name.
# we used field name (username) to access input data.
