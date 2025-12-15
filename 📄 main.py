from src.processor import PredictionValidator

def main():
    # Simulated model prediction output
    prediction_records = [
        "u1,0.85",
        "u2,1.2",     # invalid
        "u3,0.45",
        "u4,-0.1"     # invalid
    ]

    validator = PredictionValidator()
    validator.process(prediction_records)

    print("\nValid Predictions:")
    for item in validator.valid_predictions:
        print(item)

    print("\nInvalid Predictions:")
    for item in validator.invalid_predictions:
        print(item)

if __name__ == "__main__":
    main()

