from src.processor import PredictionValidator

def test_valid_prediction():
    validator = PredictionValidator()
    validator.process(["u1,0.75"])

    assert len(validator.valid_predictions) == 1
    assert len(validator.invalid_predictions) == 0

def test_invalid_prediction_out_of_range():
    validator = PredictionValidator()
    validator.process(["u2,1.5"])

    assert len(validator.valid_predictions) == 0
    assert len(validator.invalid_predictions) == 1

