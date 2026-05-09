# Customer_Churn_Prediction
Customer Churn Prediction — Machine Learning Project

## Churn Prediction Web App
https://martinsnduka-customer-churn-prediction-app-wzbrli.streamlit.app/

##  Business Overview
This project addresses a telecommunication problem by building a predictive model that identifies customers who are likely to churn — **before they do**.

## Business Objective
 **Predict whether a telecom customer will churn, enabling the business to intervene at the right time with the right offer.**

Key business questions this model answers:
- Which customers are at the highest risk of leaving?
- What customer profile signals imminent churn?
- How can the business prioritize its retention budget effectively?

## Dataset
The dataset captures customer demographics, service usage, and billing information across the following features:
**Age** — The customer's age in years. Helps identify whether older or younger customers are more likely to churn.
**Gender** — Whether the customer is male or female. Used to detect any churn patterns across gender groups.
**Contract Type** — The type of service agreement the customer is on (Month-to-Month, One Year, or Two Year). 
**Monthly Charges** — The amount a customer is billed each month. Higher charges can increase dissatisfaction and likelihood of leaving.
**Tech Support** — Whether the customer has a tech support add-on or not. Customers without support may experience more frustration, influencing churn.
**Tenure** — How long (in months) the customer has been with the company. Longer tenure typically means greater loyalty and lower churn risk

> **Note on feature selection:** `Internet Service` and `Total Charges` were intentionally excluded from model training. `Total Charges` is highly correlated with `Tenure` × `Monthly Charges`, introducing multicollinearity. Removing these features produced a cleaner, more generalisable model without sacrificing predictive power.


## Model Development
Multiple classification algorithms were evaluated to identify the best-performing model. 

### Model Performance Summary
| 1. | **Random Forest Classifier** | **97.00%** |
| 2. | K-Nearest Neighbour (KNN) | 94.00% |
| 3. | Support Vector Classifier (SVC) | 92.67% |
| 4. | Decision Tree Classifier | 92.67% |
| 5. | Logistic Regression | 89.67% |

### Selected Model: Random Forest Classifier

**Why Random Forest for this business problem?**
- Handles a mix of categorical and numerical features effectively
- Provides feature importance scores (useful for business insights)
- Resistant to noise and outliers in billing/demographic data
- Scales well as more customer data is collected over time


## Project Workflow
The followig workflow was sequentially followed :
Data Collection → Exploratory Data Analysis → Feature Selection  → Model Training & Comparison → Evaluation → Deployment-Ready Model
```


##  Key Takeaways

- Customers on **month-to-month contracts** with **short tenure** and **high monthly charges** are the most likely to churn.A strong churn signal **short-term contracts** tend to have higher churn rates.
- The Random Forest model with **97% accuracy** gives the business a highly reliable tool for churn prediction.

**Martins Nduka**
Data Analyst | Data Scientist
 ndukamartins2019@gmail.com | 🔗 [LinkedIn](https://linkedin.com) | 🐙 [GitHub](https://github.com)
