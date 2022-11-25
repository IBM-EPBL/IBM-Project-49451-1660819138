from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
app = Flask(__name__,template_folder = 'template')
@app.route('/')
def file():
    return render_template('resume.html')
@app.route('/upload', methods=['GET','POST'])
def folk_up():
    if request.method=='POST':
        a = request.form.get('name')
        b = request.form.get('dob')
        c=request.form.get('email')
        d=request.form.get('clg')
        e=request.form.get('deg')
        f=request.form.get('cgpa')
        g=request.form.get('year')
        h=request.form.get('lan')
        name = request.files['file']
        name.save(secure_filename(name.filename))
        
        
    
        

    return render_template("displayResume.html",a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,y=name.filename)
if __name__=='__main__':
    app.run(debug = True)