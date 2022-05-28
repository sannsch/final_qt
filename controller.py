from flask import Flask, request, render_template, redirect, flash
from model import waiting_num, store_ticket_num, get_number, create_current_num, get_current_num, alert_message, \
    find_place


app = Flask(__name__)
app.secret_key = 'the random string'


@app.route('/')
def home():
    return render_template('place.html')


places = ['postnord', 'coop']


@app.route('/add_place', methods=['POST'])
def add_place():
    place = request.form['place']
    place_lower = place.lower()
    our_place = find_place(place_lower)
    if our_place == None:
        flash('Butiken du har valt finns inte i listan för tillgängliga butiker')
        return render_template('place.html')
    else:
        return render_template('add_ticket.html')


@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    current_num = create_current_num()
    ticket_num = request.form['ticket_num']
    store_ticket_num(ticket_num)
    ticket = get_number()
    if ticket < current_num:
        flash('Det här numret har redan passerat')
        return render_template('add_ticket.html')
    else:
        return redirect('/show_ticket')


@app.route('/show_ticket')
def show_ticket():
    your_number = get_number()
    current = get_current_num()
    waiting = waiting_num(your_number, current)
    message = alert_message(waiting)
    flash(message)
    if waiting < 0:
        return render_template('place.html')
    else:
        return render_template('ticket_page.html', your_number=your_number, current=current,
                               waiting=waiting, message=message)


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    answer = check_user(email, password)
    if answer == None:
        flash('Kontot finns inte')
        return render_template('login.html')
    else:
        flash('Du är inloggad')
        return render_template('place.html')



@app.route('/log_out', methods=['POST'])
def log_out():
    return render_template('sign_out.html')

@app.route('/sign_up', methods=['POST'])
def sign_up():
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    if len(email) < 5:
        flash('Du behöver ett längre email')
        return render_template('sign_up.html')
    elif len(password1) < 7:
        flash('Du har för kort lösenord. Det behöver vara minst 7 tecken')
        return render_template('sign_up.html')
    elif password2 != password1:
        flash('Dina lösenord matchar inte')
        return render_template('sign_up.html')
    else:
        answer= create_user(email, password1)
        if answer == 2:
            flash('Kontot finns redan')
            return render_template('sign_up.html')
        else:
            flash('Konto skapat!')
            return render_template('sign_up.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080)
