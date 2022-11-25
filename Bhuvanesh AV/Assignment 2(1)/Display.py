from flask import Flask, render_template, request
app = Flask(__name__,template_folder = 'template')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login' , methods = ["POST"])
def login():
    if request.method=="POST":
        n=request.form.get('name')
        e=request.form.get('email')
        p=request.form.get('pass')
        return render_template("display.html",y=n,x=e,z=p)
if __name__=='__main__':
    app.run(debug = True)