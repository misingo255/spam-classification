import joblib
from flask import Flask,request,render_template,jsonify
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")
    


@app.route("/classify", methods = ["POST"])
def classification():

    contents = request.json["message"]

    model = joblib.load("./models/spam-detection-model.pkl")

    vectorizer = joblib.load("./preprocessing/count-vectorizer.pkl")

    results = model.predict(vectorizer.transform([contents])[0])

    prediction = str(results[0])

    if prediction == "0":
        return jsonify({"message": "The given message is not a spam"})
    else:
        return jsonify({"message": "The given message is a spam"})
        
    



if __name__ == "__main__":
    app.run(debug=True)