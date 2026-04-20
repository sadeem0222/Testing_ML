import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import joblib

# توليد بيانات أكبر
np.random.seed(42)

data = {
    "api_calls": np.random.randint(1, 20, 200),
    "response_time": np.random.randint(100, 800, 200),
    "previous_failures": np.random.randint(0, 5, 200),
}

df = pd.DataFrame(data)

# تحديد النتيجة
df["result"] = (
    (df["response_time"] > 400) |
    (df["previous_failures"] >= 3)
).astype(int)

# تقسيم البيانات
X = df[["api_calls", "response_time", "previous_failures"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# تدريب النموذج
model = RandomForestClassifier()

model.fit(X_train, y_train)

# حفظ النموذج
joblib.dump(model, "model.pkl")

print("Model saved successfully")