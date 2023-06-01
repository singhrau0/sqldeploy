from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show-customers')
def customer_show():
    conn = sqlite3.connect('mydatabase.db')
    cn = conn.cursor()
    cn.execute("select * from customer")
    data = []
    for i in cn.fetchall():
        customer = {}
        customer['customer_id']= i[0]
        customer['customer_name'] = i[1]
        customer['customer_addr'] = i[2]
        customer['customer_email'] = i[3]
        data.append(customer)
    conn.close()
    return render_template('showcustomers.html',data = data)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = False)