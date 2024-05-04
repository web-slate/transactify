import pickle

# Load the trained model from the pickle file
with open('transactify_model.pkl', 'rb') as file:
    model = pickle.load(file)

# TODO: will be passed as parameter.
new_transactions = [
    "Book purchase from Bookstore ABC",
    "Lunch at Cafe XYZ",
    "Book movie ticket in website"
]

# Predict categories for new transactions
predicted_categories = model.predict(new_transactions)

# Output the predicted categories
for transaction, category in zip(new_transactions, predicted_categories):
    print(f"Transaction: {transaction} --> Predicted Category: {category}")
