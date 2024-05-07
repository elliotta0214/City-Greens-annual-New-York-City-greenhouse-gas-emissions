# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import json


app = Flask(__name__, static_url_path="", static_folder="static")


@app.route("/")
def index():
    return redirect("/about", code=302)




@app.route("/about")
def about():
    f = open("data/stateemissions.json", "r")
    data = json.load(f)
    f.close()
    states = []
    for st in data.keys():
        if st != "Total":
            states.append(st)
    return render_template("about.html", states=states)

@app.route("/macro")
def macro():
    dict = {}
    f = open("data/stateemissions.json", "r")
    data = json.load(f)
    f.close()
    min = 10000000000
    for key in data.keys():
        if len(key) == 2:
            dict[key] = data[key]["emissions"]
            if data[key]["emissions"] < min:
                min = data[key]["emissions"]
    states = []
    for st in data.keys():
        if st != "Total":
            states.append(st)
            
    return render_template("macro.html", states=states, dict=dict)

@app.route("/micro")
def micro():
    f = open("data/stateemissions.json", "r")
    data = json.load(f)
    f.close()
    state = request.args.get("state")
    types = data[state].keys()
    sources = []
    vals = []
    for key in types:
        if key != "emissions":
            vals.append(data[state][key])
            sources.append(key)
    emissions = data[state]["emissions"]
    usTypes = data["Total"].keys()
    usSources = []
    usVals = []
    states = []
    for st in data.keys():
        if st != "Total":
            states.append(st)
    for key in usTypes:
        if key != "Total":
            usVals.append(data["Total"][key] / 50)
            usSources.append(key)
    usTotal = data["Total"]["emissions"] / 50
    comp = ""
    if emissions < usTotal:
        comp = "less"
    else:
        comp = "more"
    return render_template("micro.html", sources=sources, vals=vals, state=state, emissions=emissions, usTypes=usTypes, usSources = usSources, usVals=usVals, usTotal=usTotal, states=states, comp=comp)

app.run(debug=True)