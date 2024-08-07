from flask import Flask,request,render_template,url_for
import joblib
import sqlite3
import re

mnb = joblib.load('./models/multinomialNB.lb')
bnb = joblib.load('./models/bernoulliNB.lb')
countVectorizer = joblib.load('./models/countvectorizer.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/prediction',methods=['POST','GET'])
def prediction():
    if request.method == 'POST':
        conn = sqlite3.connect('userData.db')
        messege = request.form['messege']
        lowerCaseMessege = messege.lower()
        final_messege = re.sub("[^a-zA-Z ]","",lowerCaseMessege)
        final_messege_array = countVectorizer.transform([final_messege]).toarray()

        label = {1:'HAM!',0:'SPAM!'}

        prediction = bnb.predict(final_messege_array)[0]

        prediction = label[prediction]

        databaseMessege = (messege,prediction)

        insertionQuerry = """
        insert into email values(?,?)
        """
        cur = conn.cursor()
        cur.execute(insertionQuerry,databaseMessege)
        conn.commit()
        print('data stored in database successfully!')
        cur.close()
        conn.close()

        return render_template('result.html',output = str(prediction))

if __name__=="__main__":
    app.run(debug=True)