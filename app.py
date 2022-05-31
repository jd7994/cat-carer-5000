from application import app, db
from flask import Flask
import os


app.config['SECRET_KEY'] = #os.getenv('YOUR_SECRET_KEY')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

