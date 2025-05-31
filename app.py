from flask import *
import sqlite3



app=Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



@app.route('/',methods=['POST','GET'])
def home():
    if request.method =='POST':
        name=request.form["nm"]
        email=request.form["eml"]
        mobile=request.form["mn"]
        subject=request.form["sub"]
        message=request.form["msg"]

        conn = get_db_connection()
        conn.execute('INSERT INTO posts (name,email,mobile,subject,message) VALUES (?,?,?,?,?)',
                         (name,email,mobile,subject,message))
        conn.commit()
        conn.close()        

    return render_template('index.html')



@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/adminportal",methods=['POST','GET'])
def adminportal():
    if request.method == 'POST':
        email = request.form['em']
        password = request.form['pswd']
        if email == "lovishchaudhary098@gmail.com" and password == "admin123": 
            conn = get_db_connection()
            contacts = conn.execute('SELECT * FROM posts').fetchall()
            conn.close()
                      
            return render_template('adminportal.html',contacts=contacts)
        
            
    return redirect(url_for("home")) 


   

if __name__== '__main__':
    app.run(debug=True)
    