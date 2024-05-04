# transactify
A Python module for predicting transaction categorization


## Step 1: Install Transactify

```
pip install transactify
```

## Add Simple Transaction List.

```
from transactify import predict_categories


new_transactions = [
    "Book purchase from Bookstore ABC",
    "Lunch at Cafe XYZ",
    "Book movie ticket in website"
]

# Predict categories for new transactions
predicted_categories = predict_categories(new_transactions)

for transaction, category in zip(new_transactions, predicted_categories):
    print(f"Transaction: {transaction} --> Predicted Category: {category}")

```

## Expected output

```
Transaction: Book purchase from Bookstore ABC --> Predicted Category: Online Payment
Transaction: Lunch at Cafe XYZ --> Predicted Category: Unknown
Transaction: Book movie ticket in website --> Predicted Category:  Online Payment
```

## Demo

![transactify-demo](https://github.com/web-slate/transactify/assets/1652629/4537ff3a-2572-4037-a541-41150ab21f0f)

