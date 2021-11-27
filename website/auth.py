from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data=request.form
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("/")

@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstName) < 3:
            flash('Invalid First Name',category='error')
        elif len(lastName) <3:
            flash('Invalid Last Name',category='error')
        elif len(email) < 4:
            flash('Invalid Email ',category='error')
        elif password1!=password2:
            flash('Passwords Do Not Match!!',category='error')
        elif len(password1)<7:
            flash('Please enter a password atleast 7 characters in length',category='error')
        else:
            flash('Credentials Accepted',category='success')
    return render_template("signup.html")

    