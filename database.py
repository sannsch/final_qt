import sqlite3


con = sqlite3.connect('user1.db')
c = con.cursor()
# c.execute('CREATE TABLE user(email text, password text)')





# c.execute("INSERT INTO places VALUES ('arbetsförmedligen')")

# c.execute("INSERT INTO user (email,password) VALUES (?,?)", ('lisa', 'skittunge'))
# con.commit()


c.execute("SELECT* FROM user WHERE email=:email AND password =:password",{'email':'lisa', 'password':'skittunge'})
print(c.fetchone())


