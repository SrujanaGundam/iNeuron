# from crypt import methods
from flask import Flask,request,jsonify,render_template
import util

app=Flask(__name__)
app.debug = True

@app.route('/',methods=['GET','POST'])
def traffic_volume():  #for UI
    #print("in")
    if request.method == "POST":
        holiday=request.form.get("holiday")
        temperature=float(request.form.get("temperature"))
        clouds=float(request.form.get("clouds"))
        weather=request.form.get("weather")

        time=request.form.get("time")
        date=request.form.get("date")

        response=util.get_estimated_traffic(holiday,weather,time,date,temperature,clouds)

        #print(type(response))

        return "Estimated Traffic is: "+ str(response[0])
    return render_template('index.html')
    # response.headers.add('Access-Control-Allow-Origin', '*')
    #print(type(response))
    #return jsonify(response)

''''@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')'''


if __name__=="__main__":
    print("Starting Server for model")
    util.load_artifacts() #loading model imp
    app.run(port=5000)