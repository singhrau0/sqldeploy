from flask import Flask, jsonify, request, render_template, g
import sqlite3
import pyodbc

app = Flask(__name__)





# server = '192.168.50.68,1433'
# database = 'newims'
# username = 'AMAN\singh'
# password = '752952'


# # connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'
# connection_string = 'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
# conn = pyodbc.connect(connection_string)



# customer_name = 'rtf'
# customer_addr = 'hyd'
# customer_email = 'rtf@gmail.com'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show-customers')
def customer_show():
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
    
    return render_template('showcustomers.html',data = data)

@app.route('/show-product')
def product_show():
    cn = conn.cursor()
    cn.execute("select * from product")
    data = []
    for i in cn.fetchall():
        product = {}
        product['product_id']= i[0]
        product['product_name'] = i[1]
        product['product_stock'] = i[2]
        product['product_price'] = i[3]
        product['product_supplierid'] = i[4]
        data.append(product)
    print(data)
    
    return render_template('showproduct.html',data = data)
@app.route('/add-customer',methods = ['GET','POST'])
def addcustomer():
    if request.method=='POST':
        cn = conn.cursor()
        customername = request.form.get('name')
        customeraddr = request.form.get('address')
        customeremail = request.form.get('email')
        cn.execute(f"insert into customer(customer_name,customer_addr,customer_email) values('{customername}','{customeraddr}','{customeremail}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addcustomer.html')

@app.route("/update-customer", methods = ['GET','POST'])
def updatecustomer():
    if request.method=='POST':
        cn = conn.cursor()
        customerid = request.form.get('customerid')
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        cn.execute(f"update customer set {change} = '{newvalue}' where customer_id = '{customerid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatecustomer.html')

if __name__ == '__main__':
    app.run()