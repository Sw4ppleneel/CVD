# CVD

Cardiovascular Disease Prediction Using Classical Machine Learning and Neural Networks
1. Problem Framing
Cardiovascular diseases (CVDs) are among the leading causes of mortality worldwide. Early identification of individuals at elevated cardiovascular risk is critical for preventive intervention and public health planning. This project addresses a binary classification problem: predicting the presence or absence of cardiovascular disease using structured patient data.
The dataset consists of demographic, physiological, and lifestyle-related features such as age, blood pressure, glucose levels, smoking status, alcohol intake, and physical activity indicators. The target variable is binary, indicating whether a patient has cardiovascular disease.
From a machine learning perspective, this is a low-dimensional tabular classification task with a mix of continuous and categorical (one-hot encoded) variables. Such datasets are known to favor models capable of learning nonlinear threshold-based decision rules.
The primary objective of this work is:
•	to evaluate multiple modeling paradigms on the same dataset,
•	to understand how model inductive bias affects performance on tabular medical data,
•	and to select a model that balances predictive performance, robustness, and interpretability.
 
2. Data and Preprocessing
The dataset contains 16 input features, grouped as follows:
•	Continuous features:
age, height, weight, systolic blood pressure (ap_hi), diastolic blood pressure (ap_lo)
•	Categorical / binary features (one-hot encoded):
gender, glucose levels, smoking status, alcohol intake, and physical activity indicators
Preprocessing steps included:
•	Standardization of continuous variables using z-score normalization.
•	Retaining binary features in their original {0,1} representation to preserve semantic meaning.
•	Splitting the data into training and test sets.
•	Addressing class imbalance through appropriate evaluation metrics and, where applicable, class weighting.
All models were trained and evaluated using identical splits to ensure fair comparison.
 
3. Methods
Multiple modeling approaches were explored to benchmark performance across different inductive biases.
3.1 Logistic Regression, SVM, and Gaussian Naive Bayes
These models served as classical baselines:
•	Logistic Regression provided a linear decision boundary.
•	Support Vector Machines offered margin-based classification.
•	Gaussian Naive Bayes assumed conditional independence between features.
While computationally efficient and interpretable, these models are limited in capturing complex nonlinear feature interactions.
 
3.2 Random Forest Classifier
A Random Forest classifier was trained with a large number of trees and constrained depth to control overfitting. Random Forests aggregate predictions from multiple decision trees, reducing variance while capturing nonlinear relationships.
This model also provided feature importance estimates, offering insights into which clinical features contributed most to prediction.
 
3.3 XGBoost Classifier
XGBoost (Extreme Gradient Boosting) was used as the primary gradient-boosted tree ensemble method. The model was trained with:
•	a low learning rate,
•	a large number of estimators,
•	and moderate tree depth (approximately 5–8 levels).
This configuration allows the model to incrementally correct errors made by previous trees, making it particularly effective for structured tabular data.
 
3.4 Neural Network (PyTorch MLP)
A fully connected neural network was implemented using PyTorch:
•	Architecture: 16 → 32 → 1
•	Activation: ReLU
•	Loss function: Binary Cross Entropy with Logits
•	Optimizer: AdamW
The network outputs a single logit per sample, which is converted to a probability via the sigmoid function during inference.
Despite careful implementation and regularization, the neural network was intentionally kept simple to avoid overfitting and to reflect realistic tabular deep learning practices.
 
4. Evaluation Metrics
Models were evaluated primarily using classification accuracy on the held-out test set. Accuracy was chosen for consistency across models, while acknowledging that additional metrics such as ROC-AUC and recall are also relevant in medical contexts.
Cross-validation and controlled hyperparameter tuning were applied to tree-based models to ensure robust estimates.
 
5. Results
Model	Test Accuracy (approx.)
XGBoost Classifier	~73%
Random Forest	~72%
PyTorch MLP	~65%
Logistic Regression / SVM / GNB	~62%
Key observations:
•	XGBoost achieved the highest performance, outperforming all other models.
•	Random Forest closely followed, confirming the strength of tree-based ensembles.
•	The neural network slightly outperformed linear baselines but failed to match tree-based models.
•	Linear and naive models served as useful lower bounds.
 
6. Discussion
The results strongly highlight the importance of model–data alignment. The dataset is low-dimensional, largely categorical, and driven by threshold-based clinical signals. These characteristics favor tree-based methods, which naturally learn decision rules such as:
“If systolic blood pressure is high and physical activity is low, risk increases.”
Neural networks, by contrast, are better suited to learning smooth, high-dimensional representations and require significantly more data to outperform trees on tabular problems. Even with tuning, the MLP struggled to match ensemble methods due to its less suitable inductive bias.
Importantly, the underperformance of neural networks does not indicate flawed implementation, but rather reinforces a well-established empirical pattern in tabular machine learning.
 
7. Conclusion
This study demonstrates that for structured cardiovascular health data:
•	Gradient-boosted decision trees provide superior predictive performance.
•	Neural networks offer limited advantages and are not the optimal primary model.
•	Careful benchmarking against classical methods is essential before adopting deep learning.
The final recommended model for this task is XGBoost, due to its accuracy, robustness, and compatibility with interpretability tools such as feature importance and SHAP values.
 
8. Future Work
Future improvements may include:
•	Incorporating ROC-AUC and recall-focused optimization.
•	Adding explainability analysis to support clinical interpretation.
•	Exploring calibrated probability outputs for risk stratification.
•	Testing model generalization on external or longitudinal datasets.

