import pickle
import numpy as np

model = pickle.load(open("car_price_model.pkl", "rb"))

def predict_price(year, kms, fuel, trans):
    fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4}
    trans_map = {'Manual': 0, 'Automatic': 1}
    x = np.array([[year, kms, fuel_map[fuel], trans_map[trans]]])
    return model.predict(x)[0]

# Example usage:
price = predict_price(2017, 30000, 'Petrol', 'Manual')
print(f"Predicted Price: ₹{price:,.2f}")
