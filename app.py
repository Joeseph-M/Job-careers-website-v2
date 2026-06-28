from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Singapore',
        'salary': '$3,500'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Singapore',
        'salary': '$7,500' 
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'location': 'Remote',
        'salary': '$5,500'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'North Carolina, USA',
        'salary': '$6,500'
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Company")


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)