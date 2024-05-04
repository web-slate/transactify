from predict_category import predict_categories

new_transactions = [
    "Book purchase from Bookstore ABC",
    "Lunch at Cafe XYZ",
    "Book movie ticket in website"
]

# Predict categories for new transactions
predicted_categories = predict_categories(new_transactions)

for transaction, category in zip(new_transactions, predicted_categories):
    print(f"Transaction: {transaction} --> Predicted Category: {category}")