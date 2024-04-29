from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("homepage.html")
    else:
        return redirect("/symptoms")

@app.route("/symptoms", methods=["GET", "POST"])
def symptoms():
    if request.method == "GET":
        return render_template("symptoms.html")
    else:
        return redirect("/predict")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        
        # The symptoms will be stored in a variable and sent here 
        symptom_1 = request.form.get("symptom_1")
        symptom_2 = request.form.get("symptom_2")
        symptom_3 = request.form.get("symptom_3")
        symptom_4 = request.form.get("symptom_4")


        # Use the symptoms along with an API to get prediction data
        # For example:
        # symptoms = request.form.getform("symptoms")
        # prediction = some_api_function(symptoms)
        # Replace some_api_function with your actual function
        # Return the prediction to the template
        prediction = "Prediction Data"  # Replace with actual prediction data
        return render_template("Predictions.html", prediction=prediction)
    else:
        return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)

