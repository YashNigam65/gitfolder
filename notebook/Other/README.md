I am adding notebook related to ML and GenAI.

We have multiple mofule from which we can split test and training data.


Rule of Thumb

Big dataset → train_test_split is usually enough.

Small dataset → use KFold (cross-validation) for reliable evaluation.


1. train_test_split

Splits your dataset into one training set and one test set.

Example: 80% for training, 20% for testing.

Limitation → Model is trained and evaluated only once → performance may depend on which 20% got picked as test data.

Use Case:

When you just want a fast estimate of model performance.

When the dataset is large enough that one train/test split is representative.



2. KFold (K-Fold Cross Validation)

Splits the dataset into k equal folds.

The model is trained k times → each time using (k-1 folds) for training and (1 fold) for testing.

At the end, you take the average accuracy (or other metric) across all folds.

Advantage → Uses the entire dataset for both training & testing (at different times), so performance estimate is more reliable.

Use Case:

When the dataset is small or medium, so you don’t want to “waste” data by leaving a big chunk only for testing.

When you want a more robust accuracy estimate across different subsets.

