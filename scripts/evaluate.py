import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score
from .utils import logger
import torch


def evaluate_model(model, test_loader, device):
    """
    Evaluates the model on the test dataset.

    Args:
        model (nn.Module): The trained neural network model.
        test_loader (DataLoader): DataLoader for the test dataset.
        device (str): Device to perform the evaluation on ('cuda' or 'cpu').

    Returns:
        dict: A dictionary containing the evaluation metrics (accuracy, precision, recall).
    """
    model.eval()  # Set the model to evaluation mode
    y_true = []
    y_pred = []
    print("Evaluating model...")

    with torch.no_grad():  # Disable gradient calculation for evaluation
        for inputs, labels in test_loader:
            print(f"Processing batch: {inputs.shape}")
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)  # Get the index of the max log-probability

            y_true.extend(labels.cpu().numpy())
            y_pred.extend(predicted.cpu().numpy())

    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")

    return {
        "accuracy": accuracy,
        "precision": precision,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
    }

def summarize_privacy_risk(attack_metrics, dp_epsilon):
    print("Summarizing privacy risk...")
    """
    Summarizes the privacy risk based on attack metrics and DP epsilon value.

    Args:
        attack_metrics (dict): A dictionary containing the attack metrics (e.g., recall, precision, accuracy).
        dp_epsilon (float): The epsilon value for differential privacy.

    Returns:
        str: A summary of the privacy risk.
    """
    mia_accuracy = attack_metrics.get("accuracy", 0)
    if mia_accuracy > 0.7 and dp_epsilon < 1.0:
        summary = "High privacy risk: Membership inference attack is successful and DP epsilon is low."
    elif mia_accuracy > 0.5 and dp_epsilon < 5.0:
        summary = "Moderate privacy risk: Membership inference attack has some success and DP epsilon is moderate."
    else:
        summary = "Low privacy risk: Membership inference attack is not very successful or DP epsilon is high."

    print(summary)
    return summary

if __name__ == '__main__':
    # Example Usage (requires a trained model and test data)
    # Assuming you have a trained model 'model' and test_loader
    # metrics = evaluate_model(model, test_loader, device)
    # summary = summarize_privacy_risk(metrics, dp_epsilon=1.0)
    # print(summary)

    # Dummy data for demonstration
    class DummyModel:
        def eval(self):
            pass
        def __call__(self, x):
            return torch.randn(10, 10)  # Dummy output

    class DummyDataLoader:
        def __init__(self, num_batches=5): # Limit the number of batches
            self.num_batches = num_batches
            self.current_batch = 0

        def __iter__(self):
            self.current_batch = 0 # Reset batch counter for new iteration
            return self

        def __next__(self):
            if self.current_batch < self.num_batches:
                self.current_batch += 1
                return torch.randn(10, 784), torch.randint(0, 10, (10,))
            else:
                raise StopIteration # Stop after num_batches

    import torch
    model = DummyModel()
    test_loader = DummyDataLoader()
    device = 'cpu'

    metrics = evaluate_model(model, test_loader, device)
    summary = summarize_privacy_risk(metrics, dp_epsilon=1.0)
    print(summary)
