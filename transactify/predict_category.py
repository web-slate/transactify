import pickle
import pkg_resources

class TransactionCategorizer:
    def __init__(self, model_path=None):
        if model_path is None:
            # Load the model file from the package's data directory
            model_path = pkg_resources.resource_filename(__name__, 'transactify_model.pkl')
        self.model_path = model_path
        self.load_model()

    def load_model(self):
        with open(self.model_path, 'rb') as file:
            self.model = pickle.load(file)

    def predict_categories(self, transactions):
        predicted_categories = self.model.predict(transactions)
        return predicted_categories

def predict_categories(transactions):
    categorizer = TransactionCategorizer()
    return categorizer.predict_categories(transactions)