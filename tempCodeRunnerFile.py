from flask import *
from flask_mysqldb import MySQL

app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'portfolio contact form'
 
mysql=MySQL(app)



@app.route('/',methods=['POST','GET'])
def home():
    if request.method =='POST':
        name=request.form["nm"]
        email=request.form["eml"]
        mobile=request.form["mn"]
        subject=request.form["sub"]
        message=request.form["msg"]

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO new_table(name,email,mobile,subject,message) VALUES (%s,%s, %s,%s, %s)",(name,email,mobile,subject,message))
        mysql.connection.commit()
        cur.close()

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
            cur=mysql.connection.cursor()
            cur.execute("SELECT * FROM new_table")
            contacts = cur.fetchall()
            cur.close()
            
            return render_template('adminportal.html',contacts=contacts)
    
    return redirect(url_for("home")) 


   

if __name__== '__main__':
    app.run(debug=True)
    