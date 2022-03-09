from flask import Flask,flash, redirect, render_template, request, session, abort
import joblib
import os

app = Flask(__name__)
#@app.route('/')
#def index():
    #return render_template('hw2.html')
@app.route("/", methods=['GET', 'POST'])

def test():
    if request.method == "POST":
        age = request.form['Ag']
        weight = request.form['Weigh']
        model =joblib.load("regr.pkl")
        x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
        pred = model.predict(x)[0]
        pred_str = str(pred)
        #output = f"{pred_str}"
        return render_template('hw2.html', output=pred_str)
    else:
        return render_template('hw2.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))