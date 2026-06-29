from flask import Flask, render_template
from config_db import get_db_connection

app = Flask(__name__)

def load_jobs():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    print(jobs)

    cursor.close()
    db.close()

    return jobs

@app.route("/")
def home():
    jobs = load_jobs()
    return render_template(
        "home.html",
        jobs=jobs,
        company_name="Company Careers"
    )

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)