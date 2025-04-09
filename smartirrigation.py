# smart_irrigation.py

import random
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Train the model (only once)
def train_model():
    X = [
        [0, 35],  # dry & hot → irrigate
        [0, 25],  # dry & mild → irrigate
        [1, 25],  # wet & mild → no need
        [1, 30],  # wet & warm → no need
    ]
    y = [1, 1, 0, 0]  # 1 = Irrigate, 0 = Don't

    model = DecisionTreeClassifier()
    model.fit(X, y)
    joblib.dump(model, 'irrigation_model.pkl')
    print("🌱 ML model trained and saved.")


def load_model():
    if not os.path.exists("irrigation_model.pkl"):
        train_model()
    return joblib.load("irrigation_model.pkl")

def get_sensor_data():
    soil_moisture = random.choice([0, 1])  # 0 = dry, 1 = wet
    temperature = random.randint(20, 40)
    return soil_moisture, temperature

def main():
    model = load_model()
    moisture, temp = get_sensor_data()

    print(f"🌡️ Temperature: {temp}°C")
    print(f"🌾 Soil Moisture: {'Dry' if moisture == 0 else 'Wet'}")

    prediction = model.predict([[moisture, temp]])[0]

    if prediction == 1:
        print("🚨 Irrigation Needed! Send alert to farmer.")
    else:
        print("✅ Soil conditions are good. No irrigation needed.")

if __name__ == "__main__":
    main()
