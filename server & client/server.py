# from crypt import methods
from flask import Flask,request,jsonify,render_template
import util

app=Flask(__name__)
app.debug = True

@app.route('/traffic_predictor',methods=['GET','POST'])
def traffic_volume():  #for UI
    print("in")
    holiday=request.form['holiday']
    temperature=float(request.form['temperature'])
    clouds=float(request.form['clouds'])
    weather=request.form['weather']

    time=request.form['time']
    date=request.form['date']
    
    response={
    'estimated_traffic':util.get_estimated_traffic(holiday,weather,time,date,temperature,clouds)
    }
    # response.headers.add('Access-Control-Allow-Origin', '*')
    print(type(response))
    return jsonify(response)

@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')


if __name__=="__main__":
    print("Starting Server fpr model")
    util.load_artifacts() #loading model imp
    app.run(port=5000)