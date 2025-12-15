class PredictionValidator:
    """
    Validates AI/ML model predictions before production usage.
    Ensures predictions are numeric and within expected range.
    """

    def __init__(self, min_value=0.0, max_value=1.0):
        self.min_value = min_value
        self.max_value = max_value
        self.valid_predictions = []
        self.invalid_predictions = []

    def process(self, records):
        """
        Process prediction records.
        Each record format: user_id,prediction_score
        """
        for record in records:
            try:
                user_id, score = record.split(",")
                score = float(score)

                if self.min_value <= score <= self.max_value:
                    self.valid_predictions.append(
                        {"user_id": user_id, "score": score}
                    )
                else:
                    raise ValueError("Prediction out of allowed range")

            except Exception as error:
                self.invalid_predictions.append(
                    {"record": record, "error": str(error)}
                )

