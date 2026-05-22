import os
from flask import Flask, request, render_template, redirect, session, flash
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.user import User
from lib.space import Space
from lib.booking_repository import BookingRepository
from lib.booking import Booking

app = Flask(__name__)

app.secret_key = "makersbnb_secret"

@app.route('/', methods=['GET'])
def get_index():
    user_email = session.get("user_email")

    if user_email:
        return redirect('/spaces')
    
    return render_template('index.html')

@app.route('/spaces/new', methods=['GET'])
def get_spaces_new():

    if 'user_email' not in session:
        return redirect('/login')
    
    return render_template('new_space.html')

@app.route('/spaces', methods = ['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)

    if 'user_email' not in session:
        return redirect('/login')

    space_name = request.form['space_name']
    space_location = request.form['space_location']
    space_description = request.form['space_description']
    price_per_night = request.form['price_per_night']
    available_from = request.form['available_from']
    available_to = request.form ['available_to']

    new_space_test = Space(
        None, 
        session["user_id"],
        space_name,
        space_location,
        space_description,
        price_per_night,
        available_from,
        available_to
    )

    repository.create(new_space_test)
    return redirect('/spaces')

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces.html', spaces=spaces)

@app.route('/signup', methods=['GET'])
def get_signup_form():
    return render_template('signup.html')

@app.route('/users', methods=['POST'])
def create_user():
    db = get_flask_database_connection(app)
    repository = UserRepository(db)

    email = request.form["email"]
    password = request.form["password"]

    user = User(email, password)

    repository.create(user)

    session["user_email"] = user.email
    session["user_id"] = user.id

    return redirect('/spaces')


@app.route('/login', methods=['GET'])
def get_login_form():
    return render_template("login.html")


@app.route('/sessions', methods=['POST'])
def create_session():
    db = get_flask_database_connection(app)
    repository = UserRepository(db)

    email = request.form["email"]
    password = request.form["password"]

    user = repository.find_by_email(email)

    if user is None or user.password != password:
        flash("Invalid email or password")
        return redirect('/login')
    
    session["user_email"] = user.email
    session["user_id"] = user.id
    return redirect("/spaces")


@app.route('/logout', methods=['POST'])
def logout():
    session.pop("user_email", None)
    return redirect('/')    

@app.route('/spaces/<id>', methods=['GET'])
def get_single_space(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template("space.html", space = space)


@app.route('/requests', methods=['POST'])
def create_request():

    if 'user_email' not in session:
        return redirect('/login')

    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)

    booking_start = request.form['booking_start']
    booking_end = request.form['booking_end']
    space_id = request.form['space_id']

    booking = Booking(
        None,
        space_id,
        None,
        session["user_id"],
        session["user_email"],
        booking_start,
        booking_end,
        'Pending'
    )

    repository.create(booking)

    return redirect('/requests')


@app.route('/requests', methods=['GET'])
def get_requests():

    if 'user_email' not in session:
        return redirect('/login')

    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)

    booking_made = repository.booking_requests_made(session["user_id"])
    booking_received = repository.booking_requests_received(session["user_id"])

    return render_template(
        'requests.html',
        booking_made=booking_made,
        booking_received=booking_received
    )


@app.route('/requests/<id>/approve', methods=['POST'])
def approve_request(id):

    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)

    repository.update_status(id, 'Confirmed')

    return redirect('/requests')


@app.route('/requests/<id>/deny', methods=['POST'])
def deny_request(id):

    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)

    repository.update_status(id, 'Denied')

    return redirect('/requests')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))