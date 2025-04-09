import torch
import torch
from .core import model_wrapper
from .core import data_sanitizer
from .defenses import pii_redaction, differential_privacy
from .utils import logger, visualizer, file_encryptor, config
from .attacks import shadow_model, simulate_mia, attack_metrics
from . import evaluate
from . import intrusion_detection
import os

def main():
    """Main entry point for the secure medical data project."""

    # 0. Configuration
    model_path = config.MODEL_PATH
    noise_multiplier = config.NOISE_MULTIPLIER
    l2_norm_clip = config.L2_NORM_CLIP
    log_file = config.LOG_FILE

    # 1. Load a dummy model
    logger.log_message("Loading dummy model...")
    logger.log_event("Loading dummy model...")
    model_wrapper_instance = model_wrapper.ModelWrapper(model_path)

    # 2. Take a dummy input string (e.g., medical record with PII)
    medical_record = "Patient Name: John Doe, Patient ID: 12345, Diagnosis: Flu, Email: johndoe@example.com, Phone: 123-456-7890"
    logger.log_message(f"Original medical record: {medical_record}")
    logger.log_event(f"Original medical record: {medical_record}")

    # 3. Sanitize the input
    logger.log_message("Sanitizing input...")
    logger.log_event("Sanitizing input...")
    sanitized_record = data_sanitizer.sanitize_input(medical_record)
    logger.log_message(f"Sanitized medical record: {sanitized_record}")
    logger.log_event(f"Sanitized medical record: {sanitized_record}")

    # 4. Call a function to redact PII from it
    logger.log_message("Redacting PII...")
    logger.log_event("Redacting PII...")
    redacted_record = pii_redaction.redact_pii(sanitized_record)
    logger.log_message(f"Redacted medical record: {redacted_record}")
    logger.log_event(f"Redacted medical record: {redacted_record}")

    # 5. Pass the redacted text to a dummy model predict function
    logger.log_message("Predicting with redacted record...")
    logger.log_event("Predicting with redacted record...")
    prediction = model_wrapper_instance.predict(redacted_record)
    logger.log_message(f"Prediction: {prediction}")
    logger.log_event(f"Prediction: {prediction}")

    # 6. Train shadow models
    logger.log_message("Training shadow models...")
    logger.log_event("Training shadow models...")
    member_confidences, non_member_confidences = shadow_model.train_shadow_models()
    logger.log_message(f"Member confidences: {member_confidences}")
    logger.log_event(f"Non-member confidences: {non_member_confidences}")

    # 7. Perform membership inference attack
    logger.log_message("Performing membership inference attack...")
    logger.log_event("Performing membership inference attack...")
    attack_metrics_results = simulate_mia.perform_membership_inference_attack(member_confidences, non_member_confidences)
    logger.log_message(f"Attack metrics: {attack_metrics_results}")
    logger.log_event(f"Attack metrics: {attack_metrics_results}")

    # 8. Print attack results
    logger.log_message("Printing attack results...")
    logger.log_event("Printing attack results...")
    attack_metrics.print_attack_results(attack_metrics_results)

    # 9. Evaluate model (dummy implementation)
    logger.log_message("Evaluating model...")
    logger.log_event("Evaluating model...")
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

    model = DummyModel()
    test_loader = DummyDataLoader()
    device = 'cpu'

    model_evaluation_results = evaluate.evaluate_model(model, test_loader, device)

    # 10. Summarize privacy risk
    logger.log_message("Summarizing privacy risk...")
    logger.log_event("Summarizing privacy risk...")
    privacy_summary = evaluate.summarize_privacy_risk(attack_metrics_results, dp_epsilon=1.0)
    logger.log_message(f"Privacy summary: {privacy_summary}")
    logger.log_event(f"Privacy summary: {privacy_summary}")

    # 11. Visualize attack results
    logger.log_message("Visualizing attack results...")
    logger.log_event("Visualizing attack results...")
    # Corrected path relative to the execution directory
    visualizer.plot_attack_results(attack_metrics_results, filename="results/attack_results.png")

    # 12. Encrypt sensitive files (example)
    logger.log_message("Encrypting sensitive files...")
    logger.log_event("Encrypting sensitive files...")
    # Corrected path relative to the execution directory
    try:
        file_encryptor.encrypt_file("data/raw/README.md", file_encryptor.generate_key())
    except FileNotFoundError as e:
        logger.log_message(f"Error encrypting file: {e}", level="error") # Log error instead of crashing

    logger.log_message("End of data flow.")
    logger.log_event("End of data flow.")

    # Simulate intrusion detection
    logger.log_message("Simulating intrusion detection...")
    logger.log_event("Simulating intrusion detection...")
    intrusion_detection.detect_suspicious_login("testuser", "wrongpassword")
    intrusion_detection.detect_unusual_access_time()


if __name__ == "__main__":
    main()
