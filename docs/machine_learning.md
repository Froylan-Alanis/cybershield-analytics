# Machine Learning Module

## Objective

Classify and analyze cybersecurity attack events using supervised learning algorithms.

## Models

### Random Forest

Performance:

* Accuracy: 33.94%
* Precision: 33.95%
* Recall: 33.94%
* F1 Score: 33.91%

Best performing model.

### XGBoost

Performance:

* Accuracy: 32.31%
* Precision: 32.36%
* Recall: 32.31%
* F1 Score: 32.30%

### CatBoost

Performance:

* Accuracy: 32.45%
* Precision: 32.47%
* Recall: 32.45%
* F1 Score: 32.39%

## Pipeline

Dataset
↓
Preprocessing
↓
Feature Engineering
↓
Train/Test Split
↓
Model Training
↓
Model Evaluation
↓
Deployment

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

## Dashboards

### Machine Learning

Provides:

* Best Model KPIs
* Accuracy Comparison
* Precision vs Recall
* Metrics Table

### Model Evaluation

Provides:

* Model Ranking
* Radar Chart
* Leaderboard

## API Endpoints

### Metrics

/ml/metrics

### Best Model

/ml/best-model

## Conclusion

Random Forest achieved the best overall performance and was selected as the primary model for the platform.
