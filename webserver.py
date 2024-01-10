from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

redstatus = True
yellowstatus = True
greenstatus = True

@app.route("/")
def hello_world():
    status = f"""
Red : {redstatus}<br>
Yellow : {yellowstatus}<br>
Green : {greenstatus}<br>"""
    return render_template("index.html",status=status)

@app.route("/post",methods=["POST"])
def post():
    data = request.form.to_dict(flat=False)
    global redstatus
    global yellowstatus
    global greenstatus
    try:
        data["toggle1"]
        redstatus=True
    except KeyError:
        redstatus=False
    
    try:
        data["toggle2"]
        yellowstatus=True
    except KeyError:
        yellowstatus=False
        
    
    try:
        data["toggle3"]
        greenstatus=True
    except KeyError:
        greenstatus=False
    print(redstatus,yellowstatus,greenstatus)
    return redirect("/",302)


@app.route("/data.json")
def jsoner():
    return {
        "red": redstatus,
        "yellow": yellowstatus,
        "green": greenstatus,
    }
app.run(debug=True)