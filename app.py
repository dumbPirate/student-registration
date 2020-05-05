from flask import Flask, render_template, request

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

        print(first_name,last_name, email, phone, birthday)
        if first_name == '':
            return render_template('index.html')
        return render_template('success.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
