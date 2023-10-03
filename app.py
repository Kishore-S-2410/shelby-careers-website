from flask import Flask,render_template,jsonify

app = Flask(__name__,template_folder="C:\\Users\\Kishore\\Documents\\Backend")

jobs =[
    {
        
        'id':1,
        'title':'Data Analyst',
        'location':'Bangalore',
        'salary':'10 LPA'
    },
    {
        'id':2,
        'title':'Support Engineer',
        'location':'Hydrebad',
        'salary':'8 LPA'

    },
    {
        
        'id':3,
        'title':'Frontend Developer',
        'location':'Remote',
        'salary':'10 LPA'
    },
    {
        'id':4,
        'title':'Software Engineer',
        'location':'Bangalore'
    },
    {
        'id':5,
        'title':'Data Engineer',
        'location':'Chennai',
        'salary':'9 LPA'
    }
]

@app.route("/")
def hello():
    return render_template('main.html',jobs=jobs,company='Shelby')

@app.route("/api/jobs")
def job_list():
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)