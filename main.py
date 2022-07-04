from flask import Flask , render_template, request
app = Flask(__name__)
import pickle

# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')
clf= pickle.load(file)
file.close() 


@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        fever = int(myDict['fever'])
        age = int(myDict['age'])
        Pain = int(myDict['Pain'])
        runnyNose = int(myDict['runnyNose'])
        dryCough = int(myDict['dryCough'])
        tiredness = int(myDict['tiredness'])
        diffBreath = int(myDict['diffBreath'])
        headache= int(myDict['headache']) 
        sneezing = int(myDict['sneezing'])
        conjunctivitis = int(myDict['conjunctivitis'])
        diarrhea = int(myDict['diarrhea'])
        skinRashes = int(myDict['skinRashes'])
        vomting = int(myDict['vomting'])
        soreThroat = int(myDict['soreThroat'])
        loss_of_test_or_smell = int(myDict['loss_of_test_or_smell'])



        inputFeatures =[fever, Pain, age, runnyNose, dryCough, tiredness, diffBreath, headache, sneezing, conjunctivitis, diarrhea, skinRashes, vomting, soreThroat,loss_of_test_or_smell]
        infProb= clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
        return render_template('show.html', inf=round(infProb*100))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)