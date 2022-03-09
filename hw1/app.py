from flask import Flask,flash, redirect, render_template, request, session, abort
import joblib

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
        pred = model.predict(age,weight)
        pred_str = str(pred)
        output = f"{pred_str}"
        return render_template('hw2.html', output=output)
    else:
        return render_template('hw2.html')

if __name__ == "__main__":
    app.run()