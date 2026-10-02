const form =
    document.getElementById(
        "predictionForm"
    );


const button =
    document.getElementById(
        "predictBtn"
    );


const results =
    document.getElementById(
        "results"
    );


const error =
    document.getElementById(
        "error"
    );


function getValue(id) {

    return document
        .getElementById(id)
        .value;

}


function money(value) {

    return new Intl.NumberFormat(
        "en-IN",
        {
            style: "currency",
            currency: "INR",
            maximumFractionDigits: 2
        }
    ).format(value);

}


form.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        error.innerText = "";


        button.innerText =
            "Predicting...";


        button.disabled = true;


        const data = {

            age:
                Number(
                    getValue("age")
                ),

            gender:
                getValue("gender"),

            plan_type:
                getValue("plan_type"),

            tenure_months:
                Number(
                    getValue(
                        "tenure_months"
                    )
                ),

            monthly_usage_hours:
                Number(
                    getValue(
                        "monthly_usage_hours"
                    )
                ),

            support_tickets:
                Number(
                    getValue(
                        "support_tickets"
                    )
                ),

            satisfaction_score:
                Number(
                    getValue(
                        "satisfaction_score"
                    )
                ),

            monthly_charges:
                Number(
                    getValue(
                        "monthly_charges"
                    )
                ),

            data_usage_gb:
                Number(
                    getValue(
                        "data_usage_gb"
                    )
                ),

            payment_delay_days:
                Number(
                    getValue(
                        "payment_delay_days"
                    )
                ),

            contract_months:
                Number(
                    getValue(
                        "contract_months"
                    )
                ),

            avg_login_days:
                Number(
                    getValue(
                        "avg_login_days"
                    )
                ),

            service_count:
                Number(
                    getValue(
                        "service_count"
                    )
                ),

            discount_percent:
                Number(
                    getValue(
                        "discount_percent"
                    )
                )

        };


        try {

            const response =
                await fetch(
                    "/predict",
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(
                                data
                            )

                    }
                );


            const result =
                await response.json();


            if (!result.success) {

                throw new Error(
                    result.error
                );

            }


            // Display predictions

            document.getElementById(
                "linear"
            ).innerText =
                money(
                    result.linear_regression
                );


            document.getElementById(
                "tree"
            ).innerText =
                money(
                    result.decision_tree
                );


            document.getElementById(
                "forest"
            ).innerText =
                money(
                    result.random_forest
                );


            document.getElementById(
                "svr"
            ).innerText =
                money(
                    result.svr
                );


            document.getElementById(
                "average"
            ).innerText =
                money(
                    result.average
                );


            // Show result section

            results.style.display =
                "block";


            results.scrollIntoView({
                behavior: "smooth"
            });


        }

        catch (err) {

            error.innerText =
                "Error: " +
                err.message;

        }


        finally {

            button.innerHTML =
                'Predict Annual Value <span>→</span>';

            button.disabled = false;

        }

    }
);