from flask import Flask, render_template, request
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        birthday = request.form['birthday']
        gender = request.form['gender']
        state = request.form['state']
        city = request.form['city']
        pincode = request.form['pincode']
        uni_name = request.form['uni_name']
        field = request.form['field']
        year = request.form['year']



        fields = [first_name,last_name, email, phone, birthday, gender, 
                 state, city, pincode, uni_name, field, year]
        
        with open(r'data.csv', 'a') as data:
            writer = csv.writer(data)
            writer.writerow(fields)

        if first_name == '':
            return render_template('index.html', message = 'enter required fields')
        return render_template('success.html')


@app.route("/data")
def show_tables():
    a = pd.read_csv("data.csv")
    html_file = a.to_html()
    return render_template('data.html', data=html_file)


@app.route("/toedit")
def to_edit():
    return render_template('toedit.html')



@app.route('/edit', methods = ['POST'])
def edit_data():
    if request.method == 'POST':
        f_name = request.form['f_name']
        a = pd.read_csv("data.csv")
        b = list(a)
        c = a[a['first_name']==f_name].values.tolist()[0]
        d = dict(zip(b, c))
        r = a[a['first_name']== f_name].index
        a.drop(r, inplace = True)
        a.to_csv('data.csv', index = False)

    return render_template('edit.html', variable = d)


if __name__ == '__main__':
    app.debug = True
    app.run()
