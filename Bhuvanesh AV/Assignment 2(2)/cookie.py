from flask import *
app = Flask(__name__)
@app.route('/')
def keys():
    res = make_response("Cookie was inserted successfully :)")
    res.set_cookie('IBM','Assignment2')
    return res
if __name__=='__main__':
    app.run(debug = True)