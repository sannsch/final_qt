

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
    if place in places:
        return render_template('add_ticket.html')
    else:
        flash('Butiken du har valt finns inte i listan för tillgängliga butiker')
        return render_template('place.html')


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


if __name__ == '__main__':
    app.run(debug=True, port=8080)
