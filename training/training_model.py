from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle
import csv
import os

# transactions = [
#   "Purchase at Amazon",
#   "Dinner at ABC Restaurant",
#   "Gas station purchase",
#   "Online payment to ABC Corp",
#   "Grocery shopping at XYZ Mart",
# ]

# categories = [
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Unknown"
# ]

# transactions = [
#     "Purchase at Amazon",
#     "Dinner at ABC Restaurant",
#     "Gas station purchase",
#     "Online payment to ABC Corp",
#     "Grocery shopping at XYZ Mart",
#     "Clothes shopping at H&M",
#     "Lunch at McDonald's",
#     "Electricity bill payment",
#     "Movie ticket purchase",
#     "Furniture purchase at IKEA",
#     "Coffee at Starbucks",
#     "Car insurance payment",
#     "Music streaming subscription",
#     "Train ticket booking",
#     "Pharmacy purchase",
#     "Subscription to Netflix",
#     "Hardware store purchase",
#     "Magazine subscription renewal",
#     "Dinner at Italian restaurant",
#     "Mobile phone bill payment",
#     "Online course subscription",
#     "Gym membership renewal",
#     "Shopping at Walmart",
#     "Coffee machine purchase",
#     "Dinner at Chinese restaurant",
#     "Gas bill payment",
#     "Gaming console purchase",
#     "Taxi ride",
#     "Book purchase at Barnes & Noble",
#     "Payment to utility company",
#     "Lunch at Subway",
#     "Online software subscription",
#     "Bedding purchase",
#     "Dinner at Mexican restaurant",
#     "Payment to credit card company",
#     "Shoe shopping at Nike",
#     "Concert ticket purchase",
#     "Payment to internet service provider",
#     "Grocery shopping at Target",
#     "Haircut at local salon",
#     "Subscription to Spotify",
#     "Laptop purchase",
#     "Breakfast at Denny's",
#     "Payment to streaming service",
#     "Clothing alteration",
#     "Online donation to charity",
#     "Car wash",
#     "Dinner at sushi restaurant",
#     "Payment to phone company",
#     "Art supplies purchase"
# ]

# categories = [
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Online Payment",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Online Payment",
#     "Online Payment",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Online Payment",
#     "Unknown",
#     "Online Payment",
#     "Online Payment",
#     "Online Payment"
# ]


# Define the file name
csv_file = 'data.csv'

transactions = []
categories = []
    
# Read the CSV file
def read_csv(filename):
    # Get the path to the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Construct the full path to the CSV file
    csv_file = os.path.join(script_dir, filename)

    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row['Transaction Description'])
            categories.append(row['Category'])
    return transactions, categories
  
read_csv(csv_file)
# Create a pipeline with CountVectorizer and MultinomialNB
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(transactions, categories)

# Get the current directory (a directory)
current_root_directory = os.getcwd()

# Specify the path to the 'transactify' directory relative to the root directory
transactify_dir = os.path.join(current_root_directory, 'transactify')

# Define the path to save the pickle file in the transactify directory
transactify_model_file_path = os.path.join(transactify_dir, 'transactify_model.pkl')

# Save the trained model to a pickle file
with open(transactify_model_file_path, 'wb') as file:
  pickle.dump(model, file)