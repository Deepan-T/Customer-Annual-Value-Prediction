from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)


# ==============================
# LOAD MODELS
# ==============================

with open("model1.pkl", "rb") as file:
    m1 = pickle.load(file)

with open("model2.pkl", "rb") as file:
    m2 = pickle.load(file)

with open("model3.pkl", "rb") as file:
    m3 = pickle.load(file)

with open("model4.pkl", "rb") as file:
    m4 = pickle.load(file)


# ==============================
# LOAD LABEL ENCODERS
# ==============================

with open("gender_encoder.pkl", "rb") as file:
    l1 = pickle.load(file)

with open("plan_encoder.pkl", "rb") as file:
    l2 = pickle.load(file)


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():

    genders = list(l1.classes_)
    plans = list(l2.classes_)

    return render_template(
        "index.html",
        genders=genders,
        plans=plans
    )


# ==============================
# PREDICTION API
# ==============================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get data from webpage
        data = request.get_json()

        # --------------------------
        # Get input values
        # --------------------------

        age = int(data["age"])

        gender = data["gender"]

        plan_type = data["plan_type"]

        tenure_months = int(data["tenure_months"])

        monthly_usage_hours = float(
            data["monthly_usage_hours"]
        )

        support_tickets = int(
            data["support_tickets"]
        )

        satisfaction_score = float(
            data["satisfaction_score"]
        )

        monthly_charges = float(
            data["monthly_charges"]
        )

        data_usage_gb = float(
            data["data_usage_gb"]
        )

        payment_delay_days = int(
            data["payment_delay_days"]
        )

        contract_months = int(
            data["contract_months"]
        )

        avg_login_days = float(
            data["avg_login_days"]
        )

        service_count = int(
            data["service_count"]
        )

        discount_percent = float(
            data["discount_percent"]
        )


        # ==============================
        # LABEL ENCODING
        # ==============================

        Gender = l1.transform([gender])[0]

        Plan_Type = l2.transform([plan_type])[0]


        # ==============================
        # CREATE DATAFRAME
        # ==============================

        input_data = pd.DataFrame([[
            age,
            Gender,
            Plan_Type,
            tenure_months,
            monthly_usage_hours,
            support_tickets,
            satisfaction_score,
            monthly_charges,
            data_usage_gb,
            payment_delay_days,
            contract_months,
            avg_login_days,
            service_count,
            discount_percent

        ]], columns=[

            "Age",
            "Gender",
            "Plan_Type",
            "Tenure_Months",
            "Monthly_Usage_Hours",
            "Support_Tickets",
            "Satisfaction_Score",
            "Monthly_Charges",
            "Data_Usage_GB",
            "Payment_Delay_Days",
            "Contract_Months",
            "Avg_Login_Days",
            "Service_Count",
            "Discount_Percent"

        ])


        # ==============================
        # PREDICTIONS
        # ==============================

        result1 = m1.predict(input_data)[0]

        result2 = m2.predict(input_data)[0]

        result3 = m3.predict(input_data)[0]

        result4 = m4.predict(input_data)[0]


        # ==============================
        # AVERAGE
        # ==============================

        average = (
            result1 +
            result2 +
            result3 +
            result4
        ) / 4


        # ==============================
        # SEND RESPONSE
        # ==============================

        return jsonify({

            "success": True,

            "linear_regression": round(
                float(result1), 2
            ),

            "decision_tree": round(
                float(result2), 2
            ),

            "random_forest": round(
                float(result3), 2
            ),

            "svr": round(
                float(result4), 2
            ),

            "average": round(
                float(average), 2
            )

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)

        }), 400


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":

    app.run(
        debug=True,port=5001
    )