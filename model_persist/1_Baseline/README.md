# Summary of 1_Baseline

[<< Go back](../README.md)


## Baseline Classifier (Baseline)
- **n_jobs**: -1
- **num_class**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

0.2 seconds

### Metric details
|           |         0 |   1 |   2 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----------:|----:|----:|-----------:|------------:|---------------:|----------:|
| precision |  0.333333 |   0 |   0 |   0.333333 |    0.111111 |       0.111111 |   1.09861 |
| recall    |  1        |   0 |   0 |   0.333333 |    0.333333 |       0.333333 |   1.09861 |
| f1-score  |  0.5      |   0 |   0 |   0.333333 |    0.166667 |       0.166667 |   1.09861 |
| support   | 10        |  10 |  10 |   0.333333 |   30        |      30        |   1.09861 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |
|:-------------|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |               10 |                0 |                0 |
| Labeled as 1 |               10 |                0 |                0 |
| Labeled as 2 |               10 |                0 |                0 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
