import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
df = pd.read_csv("customer_churnNew1.csv")

# Features and label
X = df[["Gender","Age","Tenure","MonthlyCharges","TotalCharges","PaymentMethod","ContractType","InternetService","StreamingServices","TechSupport"]]
y = df["Churn"]  # Target column (binary classification)

# Train Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

