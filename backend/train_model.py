import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
url = "https://raw.githubusercontent.com/gauravpurohit28/Breast-Cancer/main/data.csv"
df = pd.read_csv(url)

# Drop irrelevant or problematic columns
df = df.drop([
    'id','texture_se','area_se','area_mean','area_worst',
    'fractal_dimension_se','fractal_dimension_worst','Unnamed: 32',
    'concave points_worst','fractal_dimension_mean','concavity_mean',
    'symmetry_worst','perimeter_mean','concave points_mean',
    'concavity_se','symmetry_se','concave points_se','perimeter_se',
    'compactness_worst','concavity_worst','smoothness_worst','perimeter_worst'
], axis=1)

# Clean dataset
df = df.dropna()

# Split features and target
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

print("Training started...")

# Train model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Model saved as model.pkl")
