import json
from random import randint
import copy
import sqlite3


def waiting_num(ticket_num, current_num):
    return ticket_num - current_num

number = [0]
current = 0


def store_ticket_num(ticket_num):
    number.append(ticket_num)
    return number


def get_number():
    copy_number = number[:]
    y_number = copy_number.pop()
    y_number_int = int(y_number)
    return y_number_int


def create_current_num():
    global current
    current_num = randint(3, 20)
    current =current_num
    return current

def get_current_num():
    global current
    current +=1
    return current

def alert_message(waiting):
    if waiting == 5:
        return "Det är fem i kön före dig"
    elif waiting == 2:
        return "Det är 2 före dig i kön"
    elif waiting == 1:
        return "Du är nästa i tur"
    else:
        return " "

def find_place(place):
    conn = sqlite3.connect('places1.db')
    c = conn.cursor()
    c.execute("SELECT* FROM places WHERE place=:place", {'place': place})
    our_place= c.fetchone()
    conn.close()
    return our_place

def create_user(email, password):
    con = sqlite3.connect('user1.db')
    c = con.cursor()
    c.execute("SELECT* FROM user WHERE email=:email AND password =:password",{'email':email, 'password':password})
    data = c.fetchone()
    if data == None:
        c.execute("INSERT INTO user (email,password) VALUES (?,?)", (email, password))
        con.commit()
        con.close()
        return 1
    else:
        con.close()
        return 2


def check_user(email, password):
    con = sqlite3.connect('user1.db')
    c = con.cursor()
    c.execute("SELECT* FROM user WHERE email=:email AND password =:password", {'email': email, 'password': password})
    data = c.fetchone()
    con.close()
    return data