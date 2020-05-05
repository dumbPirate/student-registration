from flask import Flask, render_template, request
import csv

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
        address = request.form['address']
        state = request.form['state']
        city = request.form['city']
        pincode = request.form['pincode']
        uni_name = request.form['uni_name']
        field = request.form['field']
        year = request.form['year']



        fields = [first_name,last_name, email, phone, birthday, gender,
                 address, state, city, pincode, uni_name, field, year]
        
        with open(r'data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        # if first_name == '':
        #     return render_template('index.html', message = 'enter required fields')
        return render_template('success.html')

# fields=['first_name','last_name','email','phone', 'birthday']




if __name__ == '__main__':
    app.debug = True
    app.run()
