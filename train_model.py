import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

MODEL_PATH = "model.pkl"

def train_and_save_model():
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print("Model trained and saved as model.pkl")

if __name__ == "__main__":
    train_and_save_model()

