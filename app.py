__author__ = 'mjholler'

from flask import Flask, render_template
app = Flask(__name__)

import nccmail
from database import Database


@app.route("/")
def index():
    db = Database()
    return render_template('index.html', isup=nccmail.isup(), uptime=db.get_mail_uptime())

if __name__ == "__main__":
    app.run()
