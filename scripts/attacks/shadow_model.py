def train_shadow_models():
    """
    Simulates the training of two shadow models, one on member data and one on non-member data.

    Returns:
        tuple: A tuple containing two lists:
            - member_confidences: Model confidences on member data.
            - non_member_confidences: Model confidences on non-member data.
    """
    print("Simulating training of shadow models...")

    # Simulate training on member data
    member_confidences = [0.95, 0.90, 0.88, 0.92]
    print(f"Member confidences: {member_confidences}")

    # Simulate training on non-member data
    non_member_confidences = [0.60, 0.58, 0.62, 0.55]
    print(f"Non-member confidences: {non_member_confidences}")

    return member_confidences, non_member_confidences
