from flask import Flask,render_template,jsonify,request, url_for, redirect
import pickle
app= Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html') 

@app.route("/predict", methods=['POST','GET'])
def predict():
    
    N=request.form["N"]
    P=request.form["P"]
    K=request.form["K"]
    temperature=float(request.form["temperature"])
    humidity=float(request.form["humidity"])
    ph=float(request.form["ph"])
    rainfall=float(request.form["rainfall"])

    prediction=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    pred=prediction[0]
                 
    out='Error'
    crop=['apple','banana','blackgram','chickpea','coconut','coffee','cotton','grape','jute','kidneybeans','lentil','maize','mango',
           'mothbeans','mungbean','muskmelon','orange','papaya','pigeonpeas','pomegranat','rice','watermelon']
    apple='apple.jpg'
    coffee='coffee.jpg'
    img=[apple,coffee]  

    for i in range(0,22):
        if (pred==i):
            out=crop[i] 
            
                         
    return render_template('after.html',results= "You should grow '{}' in your farm".format(out))
   
if __name__== "__main__":
    app.run(debug=True)