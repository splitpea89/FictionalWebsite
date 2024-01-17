from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    address = request.args.get('address')
    props = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
    }
    with open('contacts.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, address])
    return render_template("confirmation.html", data=props)



if __name__ == '__main__':
    app.run(debug=True)