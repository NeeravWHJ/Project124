from flask import Flask,jsonify,request

app = Flask(__name__)
tasks = [
    {
        "id":1,
        "contact": '9869280752',
        "name": 'raju',
        "done": False,
    },

    {
        "id":1,
        "contact": '9869581752',
        "name": 'ram',
        "done": False,
    }
]

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task ={
        "id":tasks[-1]["id"]+1,
        "contact":request.json["contact"],
        "name":request.json.get("name",''),
        "done":False
    } 
    tasks.append(task)
    return jsonify(
        {
            "status":"succes",
            "message":"tasks added succesfully"
        }
    )
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
    
if(__name__ == "__main__"):
    app.run(debug = True)
