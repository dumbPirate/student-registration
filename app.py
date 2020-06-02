from flask import Flask, render_template, request
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')

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

        df = pd.read_csv("data.csv", index_col=0)
        reg_num = df.index[-1] + 1


        fields = [reg_num, first_name,last_name, email, phone, birthday, gender, 
                 state, city, pincode, uni_name, field, year]
        
        with open(r'data.csv', 'a') as data:
            writer = csv.writer(data)
            writer.writerow(fields)

        a = pd.read_csv("data.csv")
        b = a[a['reg_num'] == reg_num]
        hf = b.to_html(index = False)

        # if first_name == '':
        #     return render_template('index.html', message = 'enter required fields')
        return render_template('success.html', variable = reg_num, data = hf)


@app.route("/data")
def show_tables():
    a = pd.read_csv("data.csv")
    html_file = a.to_html(index = False)
    return render_template('data.html', data=html_file)


@app.route("/toedit")
def to_edit():
    return render_template('toedit.html')

@app.route('/todelete')
def to_delete():
    return render_template('todelete.html')

@app.route('/delete', methods = ['POST'])
def delete_user():
    if request.method == 'POST':
        r_num = int(request.form['r_num'])

        a = pd.read_csv("data.csv", index_col=0)
        a.drop(r_num, inplace = True)
        a.to_csv('data.csv')

    return render_template('deletion.html', variable = r_num)



@app.route('/edit', methods = ['POST'])
def edit_data():
    if request.method == 'POST':
        r_num = int(request.form['r_num'])
        
        a = pd.read_csv("data.csv")
        b = list(a)
        c = a[a['reg_num']==r_num].values.tolist()[0]
        d = dict(zip(b, c))
        r = a[a['reg_num']== r_num].index
        # a.drop(r, inplace = True)
        # a.to_csv('data.csv')

    return render_template('edit.html', variable = d)

@app.route('/resubmit', methods = ['POST'])
def resubmit():
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
        reg_num = int(request.form['dis'])


        fields = [first_name,last_name, email, phone, birthday, gender, 
                 state, city, pincode, uni_name, field, year]

        fields_n = ['first_name',' last_name', ' email', ' phone', ' birthday', ' gender', 
                 ' state', ' city', ' pincode', ' uni_name', ' field', ' year']
        
        first = pd.Series(fields, fields_n)
        print(first)
        print(type(reg_num))
        a = pd.read_csv("data.csv", index_col=0)
        a.loc[reg_num] = first
        a.to_csv('data.csv')
        c = pd.read_csv("data.csv")
        b = c[c['reg_num'] == reg_num]
        hf = b.to_html(index = False)

        return render_template('resuccess.html', variable = reg_num, data = hf)




if __name__ == '__main__':
    app.debug = True
    app.run()
