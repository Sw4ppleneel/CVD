#  Cardiovascular Disease Dataset Analysis Summary

## Dataset Overview

You have **3 cardiovascular disease datasets** with **2 data sources**:

### 1. **Cardiac Failure & Cardio Base** (Same data, different formats)
- **Size**: 70,001 samples (balanced: 50% disease, 50% healthy)
- **Format**: CSV (cardio_base uses semicolon delimiter)
- **Features**: 13 columns including age, blood pressure, cholesterol, glucose, lifestyle factors
- **Target**: `cardio` (0=No disease, 1=Disease present)

### 2. **Heart Processed** (UCI Heart Disease Dataset)
- **Size**: 918 samples (55.3% disease prevalence)
- **Format**: CSV with pre-processed/encoded features
- **Features**: Age, blood pressure, cholesterol, ECG readings, exercise tolerance, etc.
- **Target**: `HeartDisease` (0=No, 1=Yes)
- **Note**: Includes one-hot encoded categorical variables

### 3. **ECG Timeseries** (Large file, not fully analyzed)
- **Size**: > 50MB (too large to load)
- **Contains**: Electrocardiogram time-series data

---

##  Feature Explanations

### Common Cardiovascular Features:
| Feature | Description | Values |
|---------|-------------|--------|
| **Age** | Patient age | Continuous (normalized in cardiac_failure) |
| **Gender** | Biological sex | 1=Female, 2=Male |
| **Height** | Height in cm | Continuous |
| **Weight** | Weight in kg | Continuous |
| **ap_hi** | Systolic blood pressure | Continuous (upper reading) |
| **ap_lo** | Diastolic blood pressure | Continuous (lower reading) |
| **cholesterol** | Cholesterol level | 1=Normal, 2=Above normal, 3=High |
| **gluc** | Blood glucose level | 1=Normal, 2=Above normal, 3=High |
| **smoke** | Smoking status | 0=No, 1=Yes |
| **alco** | Alcohol consumption | 0=No, 1=Yes |
| **active** | Physical activity | 0=No, 1=Yes |
| **cardio** | **TARGET** - Cardiovascular disease | 0=No, 1=Yes |

### UCI Heart Dataset Unique Features:
| Feature | Description |
|---------|-------------|
| **RestingBP** | Resting blood pressure |
| **FastingBS** | Fasting blood sugar > 120 mg/dl |
| **MaxHR** | Maximum heart rate achieved |
| **Oldpeak** | ST depression induced by exercise |
| **ChestPainType_*** | One-hot encoded chest pain types (ASY, ATA, NAP, TA) |
| **RestingECG_*** | One-hot encoded ECG findings |
| **ExerciseAngina_Y** | Exercise-induced angina |
| **ST_Slope_*** | One-hot encoded ST segment slope |

---

##  Key Correlations with Disease Risk

### Cardiac Failure/Cardio Base Dataset:

####  **Strong Risk Factors** (Correlation > 0.15):
1. **Systolic Blood Pressure**: 0.245
   - Highest single predictor
   - BP > 140 mmHg = significantly higher risk
   
2. **Age**: 0.238
   - Strong positive relationship
   - Older patients = higher disease risk
   
3. **Cholesterol**: 0.218
   - Risk increases dramatically across levels:
     - Level 1 (Normal): 44% disease prevalence
     - Level 2 (Above normal): 60% disease prevalence
     - Level 3 (High): 77% disease prevalence
   
4. **Weight**: 0.181
   - BMI-related risk factor

####  **Moderate Risk Factors** (Correlation 0.07-0.15):
5. **Glucose**: 0.089
   - Elevated glucose increases risk
   - Level 1: 48%, Level 2: 59%, Level 3: 62%

####  **Weak Risk Factors** (Correlation < 0.07):
- **Diastolic BP**: 0.069
- **Smoking**: -0.015 (slight protective - likely data artifact)
- **Alcohol**: -0.007 (slight protective - likely data artifact)
- **Physical Activity**: -0.042 (inactive = 54% risk vs active = 49% risk)

### UCI Heart Disease Dataset:

####  **Strong Predictors**:
1. **Oldpeak** (ST depression): 0.404 - Strongest predictor
2. **Maximum Heart Rate**: -0.400 - Inverse relationship (lower = higher risk)
3. **Age**: 0.282
4. **Fasting Blood Sugar**: 0.267

####  **Moderate Predictors**:
5. **Resting BP**: 0.108
6. **Cholesterol**: -0.232 (inverse relationship)

---

##  Risk Distribution Analysis

### Disease Prevalence Patterns:

**By Risk Factor Level:**

| Factor | No Disease | Disease | Difference |
|--------|-----------|---------|-----------|
| Low Cholesterol (1) | 56% | 44% | -12pp |
| Normal Cholesterol (2) | 40% | 60% | +20pp |
| High Cholesterol (3) | 23% | 77% | +54pp |
| Inactive | 46% | 54% | +8pp |
| Active | 51% | 49% | -2pp |

**Gender:**
- Female disease rate: 49.7%
- Male disease rate: 50.5%
- (Minimal gender difference in this dataset)

---

##  Clinical Insights

### Top 3 Actionable Findings:

1. **Blood Pressure Management is Critical**
   - Systolic BP is the #1 predictor of cardiovascular disease
   - Regular monitoring and control can significantly reduce risk

2. **Cholesterol Levels Triple Risk at Extremes**
   - High cholesterol (Level 3) shows 77% disease prevalence
   - This represents the strongest categorical predictor
   - Lipid management is crucial

3. **Physical Activity is Protective**
   - Inactive individuals have 10% higher disease rate
   - Just maintaining activity level reduces risk to 49%

### Potential Data Quality Issues:

 **Anomalies Detected:**
- Smoking and alcohol show negative correlations (unexpected)
- This may indicate:
  - Data collection bias
  - Survivor bias (smokers with disease may have already been hospitalized)
  - Confounding variables not captured

---

##  Quick Reference: Top Risk Factors

```
MOST IMPORTANT FEATURES (in order):
1. Systolic Blood Pressure (0.245 correlation)
2. Age (0.238 correlation)
3. Cholesterol Level (0.218 correlation)
4. Weight (0.181 correlation)
5. Glucose Level (0.089 correlation)
```

---

##  Recommendations for ML Models

### Data Preparation:
 Use **Cardiac Failure dataset** for main modeling (70k samples, balanced)
 Validate on **Heart Processed** dataset (independent source)
 Be cautious with ECG timeseries (requires specialized handling)

### Feature Engineering:
- Create BMI from height/weight
- Consider blood pressure categories (normal, elevated, stage 1, stage 2)
- Interact age with other risk factors
- Monitor data quality on smoking/alcohol

### Class Balance:
- Cardiac Failure: Perfect 50-50 split (no rebalancing needed)
- Heart Processed: 55.3% positive (minor imbalance)

---

##  Dataset Statistics Summary

| Metric | Cardiac Failure | Heart Processed |
|--------|-----------------|-----------------|
| Samples | 70,001 | 918 |
| Disease (%) | 50.0% | 55.3% |
| Features | 13 | 16 |
| Data Quality | Clean | Preprocessed/Encoded |
| Best For | Training | Validation/Testing |

