from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Lagos, Nigeria',
    'salary': 'N100,000'
  },
  {
      'id':2,
      'title': 'Data Scientist',
      'location': 'Ondo, Nigeria',
      'salary': 'N100,000'
    },
  {
    'id':3,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': 'N100,000'
  },
  {
    'id':4,
    'title': 'Data Analyst',
    'location': 'Delta, Nigeria',
    'salary': 'N100,000'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='CareerWoman')

if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)