import pytest

from transactify import predict_categories
# from .predict_category import predict_categories

new_transactions = [
    "Book purchase from Bookstore ABC",
    "Lunch at Cafe XYZ",
    "Book movie ticket in website",
    "Online order from Etsy",
    "Airline ticket booking",
    "Subscribed to digital magazine for monthly issues",
    "Renewed annual subscription to video streaming service"
]

# Predict categories for new transactions
predicted_categories = predict_categories(new_transactions)

for transaction, category in zip(new_transactions, predicted_categories):
    print(f"Transaction: {transaction} --> Predicted Category: {category}")