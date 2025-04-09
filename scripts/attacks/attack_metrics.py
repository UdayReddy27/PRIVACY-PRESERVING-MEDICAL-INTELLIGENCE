def print_attack_results(metrics):
    """
    Nicely formats and prints attack metrics line by line for readability.

    Args:
        metrics (dict): A dictionary containing the attack metrics.
    """
    print("Attack Results:")
    print(f"  True Positives: {metrics['true_positives']}")
    print(f"  False Positives: {metrics['false_positives']}")
    print(f"  Recall: {metrics['recall']:.2f}")
    print(f"  Precision: {metrics['precision']:.2f}")
    print("Attack Results:")
    print(f"  True Positives: {metrics['true_positives']}")
    print(f"  False Positives: {metrics['false_positives']}")
    print(f"  Recall: {metrics['recall']:.2f}")
    print(f"  Precision: {metrics['precision']:.2f}")
    print(f"  Accuracy: {metrics['accuracy']:.2f}")
