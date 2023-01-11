import joblib
from flask import Flask,request,render_template,jsonify
import warnings
warnings.filterwarnings("ignore")

application = Flask(__name__)

@application.route("/", methods = ["GET"])
def home():
    return render_template("index.html")
    


@application.route("/classify", methods = ["POST"])
def classification():

    #contents = request.json["message"]

    contents = request.form["text_contents"]

    model = joblib.load("./models/spam-detection-model.pkl")

    vectorizer = joblib.load("./preprocessing/count-vectorizer.pkl")

    results = model.predict(vectorizer.transform([contents])[0])

    prediction = str(results[0])

    # if prediction == "0":
    #     return jsonify({"message": "The given message is not a spam"})
    # else:
    #     return jsonify({"message": "The given message is a spam"})

    if prediction == "0":
        good_results = prediction
        return render_template("index.html", good_results = good_results)
    else:
        bad_results = prediction
        return render_template("index.html", bad_results = bad_results)
        
    



# if __name__ == "__main__":
#     application.run(debug=True)