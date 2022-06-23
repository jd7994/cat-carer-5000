from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import cryptography


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{os.getenv("MYSQL_ROOT_PASSWORD")}@sql:3306/flask-db'
app.config['SECRET_KEY'] = os.getenv('YOUR_SECRET_KEY')

db = SQLAlchemy(app)
db.create_all()

import routes

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

