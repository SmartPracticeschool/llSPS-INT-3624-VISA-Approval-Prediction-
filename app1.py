from flask import Flask,render_template,request

import pickle
import numpy as np

model = pickle.load(open('case.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/prediction',methods=['POST'])
def prediction():
    '''    #
    For rendering results on HTML GUI
    '''
    #x_test = [[str(x) for x in request.form.values()]]
    a = request.form['FULL_TIME_POSITION']
    if (a == "Yes"):
        a = 0
    if (a == "No"):
        a = 1
    m = request.form['PREVAILING_WAGE']
    n = request.form['YEAR']

    b = request.form['NEW_EMPLOYER']
    if (b == "University"):
        b = 1
    if (b == "Non University"):
        b = 0

    c = request.form['OCCUPATION']
    if (c == "Advance Sciences"):
        c = 0
    if (c == "Architecture & Engineering"):
        c = 1
    if (c == "Business Occupation"):
        c = 2
    if (c == "Financial Occupation"):
        c = 3
    if (c == "Management Occupation"):
        c = 4
    if (c == "Marketing Occupation"):
        c = 5
    if (c == "Medical Occupations"):
        c = 6
    if (c == "Others"):
        c = 7
    if (c == "computer occupations"):
        c = 8
    d = request.form['STATE']
    if (d == "MICHIGAN"):
        d = 28
    if (d == "TEXAS"):
        d = 42
    if (d == "JERSEY"):
        d = 20
    if (d == "COLORADO"):
        d = 6
    if (d == "FLORIDA"):
        d = 11
    if (d == "CALIFORNIA"):
        d = 4
    if (d == "PENNSYLVANIA"):
        d = 39
    if (d == "MASSACHUSETTS"):
        d = 26
    if (d == "VIRGINIA"):
        d = 45
    if (d == "WISCONSIN"):
        d = 47
    
    total = [[int(a),int(b),int(m),int(n),int(c),int(d)]]
    prediction_1 = model.predict(total)
    print(prediction_1)
    output=prediction_1[0]
    if(output==0):
        pred="Visa CERTIFIED"
    else:
        pred="Visa DENIED"
    return render_template('base.html', showcase=pred)

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    For direct API calls trought request
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
    '''

if __name__ == "__main__":
    app.run(debug=True)
