from flask import Flask, render_template, request
import util

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html',result="",msg="")

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        region = request.form.get('region')
        gender = request.form.get('gender')
        smoker = request.form.get('smoker')
        result=""
        if region == "choose" or gender == "choose" or smoker=="choose" or age<=0 or bmi<=0:
           return render_template('index.html',result="",msg="Choose something positive!")
        if gender=="female":
            if smoker=="yes":
                if region=="northeast":
                    result = util.get_estimated_price(age, bmi,1,0,1,0,0,0,0,1)
                elif region=="northwest":
                    result = util.get_estimated_price(age, bmi, 1, 0, 0, 1, 0, 0, 0, 1)
                elif region=="southeast":
                    result = util.get_estimated_price(age, bmi, 1, 0, 0, 0, 1, 0, 0, 1)
                else:
                    result = util.get_estimated_price(age, bmi, 1, 0, 0, 0, 0, 1, 0, 1)
            else:
                if region=="northeast":
                    result = util.get_estimated_price(age, bmi,1,0,1,0,0,0,1,0)
                elif region=="northwest":
                    result = util.get_estimated_price(age, bmi, 1, 0, 0, 1, 0, 0, 1, 0)
                elif region=="southeast":
                    result = util.get_estimated_price(age, bmi, 1, 0, 0, 0, 1, 0, 1, 0)
                else:
                    result = util.get_estimated_price(age, bmi, 1, 0, 0, 0, 0, 1, 1, 0)
        else:
            if smoker=="yes":
                if region=="northeast":
                    result = util.get_estimated_price(age, bmi,0,1,1,0,0,0,0,1)
                elif region=="northwest":
                    result = util.get_estimated_price(age, bmi, 0, 1, 0, 1, 0, 0, 0, 1)
                elif region=="southeast":
                    result = util.get_estimated_price(age, bmi, 0, 1, 0, 0, 1, 0, 0, 1)
                else:
                    result = util.get_estimated_price(age, bmi, 0, 1, 0, 0, 0, 1, 0, 1)
            else:
                if region=="northeast":
                    result = util.get_estimated_price(age, bmi,0,1,1,0,0,0,1,0)
                elif region=="northwest":
                    result = util.get_estimated_price(age, bmi, 0, 1, 0, 1, 0, 0, 1, 0)
                elif region=="southeast":
                    result = util.get_estimated_price(age, bmi, 0, 1, 0, 0, 1, 0, 1, 0)
                else:
                    result = util.get_estimated_price(age, bmi, 0, 1, 0, 0, 0, 1, 1, 0)
        return render_template('index.html', result=result,msg="")
if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)