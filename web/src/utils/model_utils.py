import pickle

# Function to load a .pkl model
def load_model(model_path):
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model
    except FileNotFoundError:
        print(f"Model file {model_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the model: {str(e)}")
        return None

# Function to make predictions using a loaded model
def predict_with_model(model, data):
    if model is not None:
        try:
            predictions = model.predict(data)
            return predictions
        except Exception as e:
            print(f"An error occurred while making predictions: {str(e)}")
            return None
    else:
        print("Model not loaded. Please load the model first.")
        return None
