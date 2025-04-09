def perform_membership_inference_attack(member_scores, non_member_scores):
    """
    Simulates a membership inference attack based on model confidence scores.

    Args:
        member_scores (list): Model confidence scores on member (training) data.
        non_member_scores (list): Model confidence scores on non-member data.

    Returns:
        dict: A dictionary containing the attack metrics:
            - true_positives (int): Number of correctly identified member data points.
            - false_positives (int): Number of incorrectly identified member data points.
            - recall (float): Recall of the attack.
            - precision (float): Precision of the attack.
            - accuracy (float): Accuracy of the attack.
    """
    print("Performing membership inference attack...")

    # Threshold for classifying as member
    threshold = 0.8

    # Initialize counters
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    true_negatives = 0

    # Classify member data
    for score in member_scores:
        if score > threshold:
            true_positives += 1
        else:
            false_negatives += 1

    # Classify non-member data
    for score in non_member_scores:
        if score > threshold:
            false_positives += 1
        else:
            true_negatives += 1

    # Compute metrics
    total_members = len(member_scores)
    total_non_members = len(non_member_scores)

    recall = true_positives / total_members if total_members else 0
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) else 0
    accuracy = (true_positives + true_negatives) / (total_members + total_non_members) if (total_members + total_non_members) else 0

    print(f"True Positives: {true_positives}")
    print(f"False Positives: {false_positives}")
    print(f"Recall: {recall}")
    print(f"Precision: {precision}")
    print(f"Accuracy: {accuracy}")

    return {
        "true_positives": true_positives,
        "false_positives": false_positives,
        "recall": recall,
        "precision": precision,
        "accuracy": accuracy,
    }
