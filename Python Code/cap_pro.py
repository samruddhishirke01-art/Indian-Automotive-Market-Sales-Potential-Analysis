import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore")

indian_data=pd.read_excel(r"C:\Users\Samruddhi Shirke\OneDrive\CAPSTONE PROJECT\Data\Indian Dataset.xlsx")
jap_data=pd.read_excel(r"C:\Users\Samruddhi Shirke\OneDrive\CAPSTONE PROJECT\Data\Japanese Dataset.xlsx")

print(indian_data.head())
print(jap_data.head())

print(indian_data.tail())
print(jap_data.tail())

print("Indian DataShape",indian_data.shape)
print("Japanese Datashape",jap_data.shape)

print("Indian Dataset Rows",indian_data.shape[0])
print("Indian Dataset Columna",indian_data.shape[1])

print("Japanese Dataset Rows ",jap_data.shape[0])
print("Japanese Dataset Columns",jap_data.shape[1])

print("Indian Dataset Columns",indian_data.columns)
print("Japanese Dataset Columns",jap_data.columns)

print("Indian Dataset Info",indian_data.info())
print("Japanese Dataset Info",jap_data.info())

print("Indian Data Description",indian_data.describe())
print("Japanese Data Descripton",jap_data.describe())

print("Indian Dataset Missing Values",indian_data.isnull().sum())
print("Japanese Dataset Misiing Values",jap_data.isnull().sum())

print("Indian Dataset Duplicated Values",indian_data.duplicated().sum())
print("Japanases Dataset Duplicated Values",jap_data .duplicated().sum())

print("Unique Values in Gender(India)",indian_data["GENDER"].unique())
print("Unique Values in Gender(Japan)",jap_data["GENDER"].unique())

print("Number of Unique Values in Gender(India)",indian_data["GENDER"].nunique())
print("Number of Values in Gender(Japan)",jap_data["GENDER"].nunique())

print("Print Indian Dataset Data types",indian_data.dtypes)
print("Japanases Dataset Data types",jap_data.dtypes)

print("Random 5 sample Rows(India)",indian_data.sample(5))
print("Random 5 Sample Rows(Japan)",jap_data.sample(5))

print("Memory Usage(India)",indian_data.memory_usage())
print("Memory Usage(Japan)",jap_data.memory_usage())

print("Basic Dataset SUmmary")

print("Indian Dataset Rows",indian_data.shape[0])
print("Indian Dataset Columna",indian_data.shape[1])

print("Japanese Dataset Rows ",jap_data.shape[0])
print("Japanese Dataset Columns",jap_data.shape[1])

print("Indian Dataset Missing Values",indian_data.isnull().sum())
print("Japanese Dataset Misiing Values",jap_data.isnull().sum())

print("Indian Dataset Duplicated Values",indian_data.duplicated().sum())
print("Japanases Dataset Duplicated Values",jap_data .duplicated().sum())

# Create copy of Dataset

japan=jap_data.copy()
indian=indian_data.copy()

print("Japanese Datset")
print("Missing Values",japan.isnull().sum())

print("Inidan Dataset")
print("Missing Values",indian.isnull().sum())

missing_japan=((japan.isnull().sum())/len(japan))*100
missing_india=((indian.isnull().sum())/len(indian))*100

print("Japan Missing Values Percentage",missing_japan)
print("Indian Missing Values Percentage",indian_data)

print("Japan duplicate values",japan.duplicated().sum())
print("Indian Missing Values",indian.duplicated().sum())

japan.drop_duplicates(inplace=True)
indian.drop_duplicates(inplace=True)

print("Successfully removed duplicated")

# verify shape

print(japan.shape)
print(indian.shape)


print("Data type",japan.dtypes)
print("Data type",indian.dtypes)

# Unique Values
print(japan["GENDER"].unique())
print(indian["GENDER"].unique())

# Count Unique Values

print(japan["GENDER"].value_counts())
print(indian["GENDER"].value_counts())

japan.columns=japan.columns.str.strip()
indian.columns=indian.columns.str.strip()

print(japan.columns)
print(indian.columns)

# Check Numeric Column
print(japan.select_dtypes(include=np.number).columns)
print(indian.select_dtypes(include=np.number).columns)

# Check Categorical Data
print(japan.select_dtypes(include="object").columns)
print(indian.select_dtypes(include="object").columns)

japan.to_csv(r"C:\Users\Samruddhi Shirke\OneDrive\CAPSTONE PROJECT\Data\japan_clean.csv",index=False)
indian.to_csv(r"C:\Users\Samruddhi Shirke\OneDrive\CAPSTONE PROJECT\Data\indian_dataset.csv",index=False)

print("Cleaned Dataset Saved Successfully")

# Copy of cleaned dataset

japan_fe=japan.copy()
indian_fe=indian.copy()

# First Five Rows

print("="*60)
print("Japanese Dataset")
print(japan_fe.head())

print("="*60)
print("Indian Dataset")
print(indian_fe.head())

# Data Type

print("="*60)
print("Data Type of Japanese Dataset")
print(japan_fe.dtypes)

print("\n")

print("="*60)
print("Data Type of Indian Dataset")
print(indian_fe.dtypes)

indian_fe["DT_MAINT"]=pd.to_datetime(indian_fe["DT_MAINT"])

print("\n")
print("="*60)
print("Data Type of Indian Dataset after Conversion")
print(indian_fe.dtypes)

# Calculate Age Car

reference_date=pd.Timestamp("2019-07-01")
print("Reference Date:-",reference_date)

indian_fe["AGE_CAR"]=(reference_date-indian_fe["DT_MAINT"]).dt.days

# Verify Age car

print("\n")
print("="*60)
print("Age_car created successfully")
print("="*60)

print(indian_fe[["DT_MAINT","AGE_CAR"]].head(10))

print("="*60)
print("Age Car Summary")
print("="*60)

print(indian_fe["AGE_CAR"].describe())

# Check Negative Values

negative_values=(indian_fe["AGE_CAR"]<0).sum()
print("Negative Age Car Values",negative_values)

# Create Age Car Segment

bins=[-1,199,360,500,np.inf]
labels=[
    "Segment 1",
    "Segement 2",
    "Segment 3",
    "Segement 4"
]

indian_fe["AGE_CAR_SEGMENT"]=pd.cut(
    indian_fe["AGE_CAR"],
    bins=bins,
    labels=labels
)

print("\n")
print("Verify Age Car Segment")
print("="*60)

print(indian_fe[["AGE_CAR","AGE_CAR_SEGMENT"]].head(20))

# Count age car segment Indian
print("\n")
print("="*60)
print("Age Car Segement count")
print("="*60)

print(indian_fe["AGE_CAR_SEGMENT"].value_counts())

# Create Age Car segment Japan

japan_fe["AGE_CAR_SEGMENT"]=pd.cut(
    japan_fe["AGE_CAR"],
    bins=bins,
    labels=labels
)

# Very Age car segment India

print("="*60)
print("Age Car Segment Japan")
print("="*60)

print(japan_fe[["AGE_CAR","AGE_CAR_SEGMENT"]].head())

# Count Age Car Segement Count

print("="*60)
print("Count Age Car Segment")
print("="*60)

print(japan_fe["AGE_CAR_SEGMENT"].value_counts())

# Check Missing Values 

print("\n")
print("Missing Values-Japan")
print("="*60)

print(japan_fe.isnull().sum())

print("\n")
print("Missing Values-India")
print("="*60)

print(indian_fe.isnull().sum())

# Check Duplicates

print("="*60)
print("Data Type-Japan")
print("="*60)

print(japan_fe.dtypes)

print("\n")
print("="*60)
print("Data Type-India")
print("="*60)

print(indian_fe.dtypes)

# Check Shape Again

print("="*60)
print("Final Shape")
print("="*60)

print("Japan:",japan_fe.shape)
print("India:",indian_fe.shape)

japan_fe.to_csv(r"C:\Users\Samruddhi Shirke\OneDrive\CAPSTONE PROJECT\Data\Featured_Engineering_Japan.csv",index=False)
indian_fe.to_csv(r"C:\Users\Samruddhi Shirke\OneDrive\CAPSTONE PROJECT\Data\Featured_Engineering_India.csv",index=False)

print("\n")
print("="*60)
print("Featured Engineering Completed Successfully")
print("="*60)

print("Featured_Engineering_Japan.csv Saved Successfully")
print("Featured_Engineering_India.csv Saved Successfully")

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"]=(8,5)


print("="*60)
print("Purchase Value Counts")
print("="*60)

print(japan_fe["PURCHASE"].value_counts())

plt.figure(figsize=(8,5))

sns.countplot(
    data=japan_fe,
    x="PURCHASE",
    palette="Set2"
)

plt.title("Number of Distribution")
plt.xlabel("Purchase")
plt.ylabel("Number of Customers")
plt.show()

# Puchase Percent 

purchase_percent=(japan_fe["PURCHASE"].value_counts(normalize=True)*100)

print("="*60)
print("Purchase Percent")
print("="*60)

print(purchase_percent)

# Gender Distribution

print("="*60)
print("Gender Distribution")
print("="*60)

print(japan_fe["GENDER"].value_counts())

plt.figure(figsize=(8,5))

sns.countplot(
    data=japan_fe,
    x="GENDER",
    palette="Pastel1"
)

plt.title("Gender Disribution")
plt.xlabel("GENDER")
plt.ylabel("Count")

plt.show()

# Gender Distribution Percentage

gender_percentage=(japan_fe["GENDER"].value_counts(normalize=True)*100)

print("="*60)
print("Gender Percentage")
print("="*60)

print(gender_percentage)

# Current Age Distribution

print("="*60)
print("Current Age Distirbution")
print("="*60)

print(japan_fe["CURR_AGE"].describe())

plt.figure(figsize=(8,5))

sns.histplot(
    data=japan_fe,
    x="CURR_AGE",
    bins=20,
    kde=True,
    color="skyblue"
)

plt.title("Current Age Distribution")
plt.xlabel("CURRENT AGE")
plt.ylabel("Frequency")

plt.show()

# Annual Income Distribution

print("="*60)
print("Annual Income Distribution")
print("="*60)

print(japan_fe["ANN_INCOME"].describe())

plt.figure(figsize=(8,5))

sns.histplot(
    data=japan_fe,
    x="ANN_INCOME",
    bins=20,
    kde=True,
    color="skyblue"
)

plt.title("Annual Income Distribution")
plt.xlabel("ANNual INCOME")
plt.ylabel("Frequency")
plt.show()


# Unique  Values

print("="*60)
print("Unique Vaues")
print("="*60)

print("Unique Gender",japan_fe["GENDER"].unique())
print("Unique Purchase",japan_fe["PURCHASE"].unique())

# Numerical Summary

print("="*60)
print("Numerical Summary")
print("="*60)

print(japan_fe[
    [
        "CURR_AGE",
        "ANN_INCOME",
        "AGE_CAR"
    ]
].describe()
      )
# Check Distribution

print("="*60)
print("SKEWNESS")
print("="*60)

print(japan_fe[
    [
        "CURR_AGE",
        "ANN_INCOME",
        "AGE_CAR"
    ]
].skew()
      )

print("="*60)
print("KURTOSIS")
print("="*60)

print(japan_fe[
    [
        "CURR_AGE",
        "ANN_INCOME",
        "AGE_CAR"
    ]
].kurt()
      )

# Age Car Summary 

print("="*60)
print("Age Car Summary")
print("="*60)

print(japan_fe["AGE_CAR"].describe())

plt.figure(figsize=(8,5))

sns.histplot(
    data=japan_fe,
    x="AGE_CAR",
    bins=20,
    kde=True,
    color="green"
)

plt.title("Age Car Summary")
plt.xlabel("Age Car(No. of Days)")
plt.ylabel("Frequency")
plt.show()

# Age Car segment Distribution
print("="*60)
print("Age Car Segment Distribution")
print("="*60)

print(japan_fe["AGE_CAR_SEGMENT"].value_counts())

plt.figure(figsize=(8,5))

sns.countplot(
    data=japan_fe,
    x="AGE_CAR_SEGMENT",
    palette="viridis",
    order=japan_fe["AGE_CAR_SEGMENT"].value_counts().index
)

plt.title("Age Car Segement Distribution")
plt.xlabel("Age Car Segment")
plt.ylabel("Number of Customers")
plt.show()

# Pie Chart of AGE CAR SEGEMENT

segment_count=japan_fe["AGE_CAR_SEGMENT"].value_counts()

plt.figure(figsize=(8,5))

plt.pie(
    segment_count,
    labels=segment_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Percentage of Age Car Segment")
plt.show()

# Boxplt of Current Age

plt.figure(figsize=(8,5))

sns.boxplot(
    x=japan_fe["CURR_AGE"],
    color="skyblue"
)
plt.title("Box Plot of Current Age")
plt.show()

# Boxplot of Annual Income
plt.figure(figsize=(8,5))

sns.boxplot(
    x=japan_fe["ANN_INCOME"],
    color="orange"
)
plt.title("Boxplot of Annual Income")
plt.show()

# Boxplot of Age Car

plt.figure(figsize=(8,5))

sns.boxplot(
    x=japan_fe["AGE_CAR"],
    color="lightgreen",
    
)

plt.title("Boxplot of Age Car")
plt.show()

# Outliers

Q1= japan_fe["ANN_INCOME"].quantile(0.25)
Q3= japan_fe["ANN_INCOME"].quantile(0.75)

IQR=Q3-Q1

lower_limit=Q1-1.5*IQR
upper_limit=Q3+1.5*IQR

print("="*60)
print("Outliers Information")
print("="*60)

print(Q1)
print(Q3)
print(IQR)
print("Lower Limit",lower_limit)
print("Upper Limit",upper_limit)

# Display Outliers

income_outliers=japan_fe[
    (japan_fe["ANN_INCOME"]<lower_limit)|
    (japan_fe["ANN_INCOME"]>upper_limit)
]

print("Number Of Outliers",len(income_outliers))

print("First 5 Outliers")

print(income_outliers.head())

segement_percentage=japan_fe["AGE_CAR_SEGMENT"].value_counts(normalize=True)*100
print("Percentage")
print(segement_percentage)

# Summary Table 

summary=japan_fe[
    [
        "CURR_AGE",
        "AGE_CAR",
        "ANN_INCOME"
    ]
].agg(
    [
        "min",
        "max",
        "median",
        "mean",
        "std"
    ]
)

print("="*60)
print("Summary Table")
print("="*60)

print(summary)

# Bivariate Analysis and Business Insights

print("="*60)
print("Dataset Information")
print("="*60)

print("Number of Rows:",japan_fe.shape[0])
print("Number of Columns",indian_fe.shape[1])

print("\n")
print("="*60)
print("Purchase v/s Gender")
print("="*60)

purchase_gender=pd.crosstab(
    japan_fe["PURCHASE"],
    japan_fe["GENDER"]
)

print(purchase_gender)

print("\n")
print("Purchase Rate by Gender")
print("="*60)

purchase_rate_gender=pd.crosstab(
    japan_fe["PURCHASE"],
    japan_fe["GENDER"],
    normalize=True
)*100

print(purchase_rate_gender)

# Visualise purchase and gender

plt.figure(figsize=(8,5))

sns.countplot(
    data=japan_fe,
    x="GENDER",
    hue="PURCHASE"
)

plt.title("Distribution of Purchase")
plt.xlabel("GENDER")
plt.ylabel("Number of Customers")

plt.legend(
    title="Purchase",
    labels=["No Purchase","Purchase"]
)

plt.show()

# Puchase v/s Current Age 

plt.figure(figsize=(8,5))

sns.boxplot(
    data=japan_fe,
    x="PURCHASE",
    y="CURR_AGE"
)

plt.title("Distribution Of Current Age")
plt.xlabel("PURCHASE")
plt.ylabel("Current Age")

plt.show()

# Average Age by Purchase 

average_rate_purchase=(japan_fe.groupby("PURCHASE")["CURR_AGE"].mean())

print("="*60)
print("Average age by purchase")
print("="*60)
print(average_rate_purchase)

# Purchase v/s Annual Income

plt.figure(figsize=(8,5))

sns.boxplot(
    data=japan_fe,
    x="PURCHASE",
    y="ANN_INCOME"
)

plt.title("Purchase v/s Annual Income")
plt.xlabel("PURCHASE")
plt.ylabel("Annual Income")
plt.show()

# Averaage Income by Puchase

avg_income_pur=(japan_fe.groupby("PURCHASE")["ANN_INCOME"].mean())

print("="*60)
print("Average income by purchase")
print("="*60)

print(avg_income_pur)

# Purchase V/s Age Car

plt.figure(figsize=(8,5))

sns.boxplot(
    data=japan_fe,
    x="PURCHASE",
    y="AGE_CAR"
)

plt.title("Distribution of Age Car and Purchase")
plt.xlabel("PURCHASE")
plt.ylabel("Age Of Car")
plt.show()

# Average Age by Purchase

avg_age_pur=(japan_fe.groupby("PURCHASE")["AGE_CAR"].mean())

print("="*60)
print("Average Age Car by Purchase")
print("="*60)

print(avg_age_pur)

# Purchase V/s age car

print("="*60)
print("PURCHASE V/S AGE_CAR_SEGMENT")
purchase_agecar=pd.crosstab(
    japan_fe["PURCHASE"],
    japan_fe["AGE_CAR_SEGMENT"]
)

print(purchase_agecar)

# Purchase v/s age car segment

plt.figure(figsize=(8,5))

sns.countplot(
    data=japan_fe,
    x="PURCHASE",
    hue="AGE_CAR_SEGMENT"
)

plt.title("Purchase decision by age car segment Age Car Segemnt")
plt.xlabel("PURCHASE")
plt.ylabel("AGE CAR SEGMENT")
plt.show()

# Average age car segment by purchase

age_car_seg_avg=pd.crosstab(japan_fe["PURCHASE"],
                            japan_fe["AGE_CAR_SEGMENT"],normalize=True)*100

print("="*60)
print("Avg age car segment")
print("="*60)

print(age_car_seg_avg)

# Income Distribution by Gender

plt.figure(figsize=(8,5))

sns.boxplot(
    data=japan_fe,
    x="GENDER",
    y="ANN_INCOME"
)

plt.title("Annual Income Distribution by Gender")
plt.xlabel("GENDER")
plt.ylabel("Annual Income")
plt.show()

# Age Distribution by gender

plt.figure(figsize=(8,5))

sns.boxplot(
    data=japan_fe,
    x="GENDER",
    y="CURR_AGE"
)
plt.title("Age Distribution by Gender")
plt.xlabel("GENDER")
plt.ylabel("Current Age")
plt.show()

# Correlation Matrix

numeric_columns=[
    "CURR_AGE",
    "ANN_INCOME",
    "AGE_CAR",
    "PURCHASE"
]

correlation_matrix=japan_fe[numeric_columns].corr()

print("="*60)
print("Correlation Matrix")
print("="*60)

print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.show()

# Purchase rate Summary

total_purchase_summary=(japan_fe["PURCHASE"].mean())*100

print("="*60)
print("Purchase Rate")
print("="*60)
print(round(total_purchase_summary,2),"%")

# Highest Purchase by Gender

pur_by_gen=(
    japan_fe.groupby("GENDER")["PURCHASE"].mean().mul(100).sort_values(ascending=False)
)

print("="*60)
print("Purchasse by gender")
print("="*60)

print(pur_by_gen)

segment_purchase_summary = (
    japan_fe
    .groupby("AGE_CAR_SEGMENT", observed=True)["PURCHASE"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\n")
print("=" * 60)
print("PURCHASE RATE BY CAR AGE SEGMENT")
print("=" * 60)

print(segment_purchase_summary)

# Machine Learning Data Oreparation

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Availabel Dataset Information

print("="*60)
print("Availabel Dataset Column")
print("="*60)
print(japan_fe.columns.to_list())

# Check Target Variable 

print("="*60)
print("Target Variable- PURCHASE")
print("="*60)

print(japan_fe["PURCHASE"].value_counts())

print("Purchase Percentage")
print(japan_fe["PURCHASE"].value_counts(normalize=True)*100)

# Select Features and target column

features=[
    "CURR_AGE",
    "ANN_INCOME",
    "AGE_CAR_SEGMENT",
    "GENDER"
]

target="PURCHASE"

# Create X and Y 
X=japan_fe[features].copy()
y=japan_fe[target].copy()

# Feature Data
print("\n")
print("="*60)
print("Feature Data-X")
print("="*60)

print(X.head())
print("Feature shape",X.shape)

# Target Data
print("="*60)
print("Target Data-y")
print("="*60)

print(y.head())
print("Target Shape",y.shape)

# Check Data Types
print("="*60)
print("Data Type of Features")
print("="*60)
print(X.dtypes)

print("="*60)
print("Missing Values in X")
print(X.isnull().sum())

print("Missing Values in Y")
print(y.isnull().sum())

# Encode Categorical Variables

X_encoded=pd.get_dummies(
    X,
    columns=[
        "GENDER",
        "AGE_CAR_SEGMENT"
    ],
    drop_first=True
)

# Check Encoded Data
print("="*60)
print("Encoded Features")
print("="*60)
print(X_encoded.head())

print("Encoded Columns")
print(X_encoded.columns.to_list())

# Check Encoded datatypes
print("="*60)
print("Features Data Types")
print("="*60)

print(X_encoded.dtypes)

# Convert Boolean Columns to integer

X_encoded=X_encoded.astype(int)

# Final Feature Check

print("="*60)
print("Final Feature Check")
print("="*60)

print(X_encoded.head())
print(X_encoded.shape)

# Train Test Split
X_train,X_test,y_train,y_test=train_test_split(
    X_encoded,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Check Training Data

print("="*60)
print("Training Data")
print("="*60)

print("Shape of X Training Data",X_train.shape)
print("Shape of Y Training Data",y_train.shape)

print("="*60)
print("Testing Data")
print("="*60)

print("Shape of X testing data",X_test.shape)
print("Shape of y testing data",y_test.shape)

# Check Purchase Distribution
print("\n")
print("=" * 60)
print("PURCHASE DISTRIBUTION")
print("=" * 60)

print("Training data:")
print(y_train.value_counts(normalize=True)*100)

print("\nTesting data:")
print(y_test.value_counts(normalize=True) * 100)

print("Original Features",X.shape)
print("Encoded Features",X_encoded.shape)
print("Training Rows",X_train.shape[0])
print("Testing Rows",X_test.shape[0])

# Import Logstic Regression

from sklearn.linear_model import LogisticRegression

# Create the model
logistic_model=LogisticRegression(
    max_iter=1000,
    random_state=42
)

# Train The model

print("="*60)
print("Training Logistic Regression Model")
print("="*60)

logistic_model.fit(
    X_train,
    y_train
)

print("Model Trained Successfully")

# Make predictions on test data
y_pred=logistic_model.predict(X_test)

# Compare Actual and predicted values
print("="*60)
print("Actual v/s Predicted Values")
print("="*60)

comparison=pd.DataFrame({
    "Actual":y_test.values,
    "Predicted":y_pred
})

print(comparison.head(20))

# Check Number of Prediction
print("="*60)
print("Prediction Information")
print("="*60)

print("Number of test records",len(X_test))
print("Number of predictions",len(y_pred))

# Predicted Class Distribution
print("="*60)
print("Predicted Class Distribution")
print("="*60)

print(
    pd.Series(y_pred).value_counts()
)

# Display Model Ceeficients

print("="*60)
print("Model Coefficients")
print("="*60)

coefficients=pd.DataFrame({
    "Features":X_train.columns,
    "Coeficients":logistic_model.coef_[0]
})

print(coefficients)

# Display Intercept

print("="*60)
print("Intercept Information")
print("="*60)

print(logistic_model.intercept_[0])

# Model Evaluatio

from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
    
)

accuracy=accuracy_score(
    y_test,
    y_pred
)

precision=precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall=recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1=f1_score(
    y_test,
    y_pred,
    zero_division=0
)

print("="*60)
print("Logistic Regression-Model Performance")
print("="*60)

print("Accuracy:",round(accuracy*100,2))
print("Precision:",round(precision*100,2))
print("Recall:",round(recall*100,2))
print("F1-score:",round(f1*100,2))


print("="*60)
print("Classification Report")
print("="*60)

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "No Purchase",
            "Purchase"
        ],
        zero_division=0
        
    )
    
)

# Model results

model_results=pd.DataFrame({
    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1-score"
    ],
    "Score":[
        accuracy,
        precision,
        recall,
        f1
    ]
    
})

# Peformance summary

print("="*60)
print("Performance Summary")
print("="*60)

print(model_results)

plt.figure(figsize=(8,5))

sns.barplot(
    data=model_results,
    x="Metric",
    y="Score"
)

plt.ylim(0,1)
plt.title("Logistic Regression Performance")
plt.xlabel("Evaluation Metric")
plt.ylabel("Score")
plt.show()

# Confusion Matrix

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

cm=confusion_matrix(
    y_test,
    y_pred
)

print("="*60)
print("Confusion Matrix Values")
print("="*60)

print(cm)

TN, FP, FN, TP = cm.ravel()


print("="*60)
print("CONFUSION MATRIX COMPONENT")
print("="*60)
print("True Negative",TN)
print("False Psitive",FP)
print("True Positive",TP)
print("False Negative",FN)


# Display Labeled Confusion Matrix

print("="*60)
print("Labeled Confusion Matrix")
print("="*60)

cm_table=pd.DataFrame(
    cm,
    index=["Actual:No Purchase ", "Actual: Purchase"],
    columns=["Predicted:No Purchase","Predicted:Purchase"]
    )

print(cm_table)

# Visualise Confusion Matrix

plt.figure(figsize=(8,5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Purchase","Purchase"],
    yticklabels=["No Purchase","Purchase"]
)

plt.title("Confusion Matrix-Logistic regression")
plt.xlabel("Predicted Label")
plt.ylabel("Actual label")
plt.show()

# Calculate error Counts

total_correct=TN+TP
total_incorrect=FN+FP

print("="*60)
print("Prediction Summary")
print("="*60)
print("Correct Prediction",total_correct)
print("Incorrect Prediction",total_incorrect)
print("Total Prediction",len(y_test))


# Calculate error Rate

error_rate=(
    total_incorrect/len(y_test)*100
)
print("Error Rate",round(error_rate),2)

print("\n")
print("=" * 60)
print("BUSINESS INTERPRETATION")
print("=" * 60)

print(
    "Potential buyers correctly identified (TP) :",
    TP
)

print(
    "Potential buyers missed by the model (FN) :",
    FN
)

print(
    "Customers incorrectly classified as buyers (FP) :",
    FP
)

print(
    "Customers correctly classified as non-buyers (TN) :",
    TN)


from sklearn.metrics import (roc_curve,roc_auc_score)

y_probability=logistic_model.predict_proba(X_test)[:,1]

# Predicted Purchase Probabilities
print(y_probability[:10])

# Calculate Roc probabilitie
fpr,tpr,thresholds=roc_curve(
    y_test,
    y_probability
)

# Calculate AUC curve
auc_score=roc_auc_score(
    y_test,
    y_probability
)

print("="*60)
print("AUC",round(auc_score,4))

# Visualization
plt.figure(figsize=(8,6))

plt.plot(
    fpr,
    tpr,
    label=f"Logistic Regression (AUC = {auc_score:.2f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random Classifier"
)

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve - Logistic Regression")

plt.legend()

plt.grid(True)

plt.show()

roc_table=pd.DataFrame(
    {
        "thresholds:":thresholds,
        "False Positive Rate":fpr,
        "True Positive Rate":tpr
        
    }
)

print(roc_table.head(10))

print("\n")
print("=" * 60)
print("AUC INTERPRETATION")
print("=" * 60)

if auc_score >= 0.90:
    print("Excellent discrimination")
elif auc_score >= 0.80:
    print("Good discrimination")
elif auc_score >= 0.70:
    print("Acceptable discrimination")
elif auc_score >= 0.60:
    print("Weak discrimination")
else:
    print("Poor discrimination")


# Feature Importance and Model Iterpretation

coefficients=logistic_model.coef_[0]

# Feature Importance
feature_imp=pd.DataFrame(
    {
        "Feature":X_train.columns,
        "coefficients":coefficients
    }
)

feature_imp["Absolute_Importance"]=(feature_imp["coefficients"].abs())

feature_imp=feature_imp.sort_values(by="Absolute_Importance",ascending=False)

print("="*60)
print("Feature Importance")
print("="*60)
print(feature_imp)

positive_features=feature_imp[
    feature_imp["coefficients"]>0
    ].sort_values(by="coefficients",ascending=False)

print("="*60)
print("Positive Features")
print("="*60)

print(positive_features)

negative_features=feature_imp[
    feature_imp["coefficients"]<0
    ].sort_values(by="coefficients",ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(
    data=feature_imp,
    x="coefficients",
    y="Feature"
)

plt.axvline(
    x=0,
    linestyle="--"
)

plt.title("Feature importance")
plt.xlabel("Coefficients")
plt.ylabel("Features")

plt.show()

# Display Most influential Features

print("="*60)
print("Most Influential Features")
print("="*60)

print(
    feature_imp[["Feature","coefficients"]].head(10)
)

# create Random forest classifier

from sklearn.ensemble import RandomForestClassifier

random_forest_model=RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

print("="*60)
print("Train Random Forest Model")
print("="*60)

random_forest_model.fit(
    X_train,
    y_train
)

print("Random forest Training Completed Successfully")

rf_pred=random_forest_model.predict(
    X_test
)

rf_probability=random_forest_model.predict_proba(X_test)[:,1]

print("="*60)
print("Random Forest Prediction")
print("="*60)

print(rf_pred[:20])

rf_comparison=pd.DataFrame(
    {
        "Actutal":y_test.values,
        "Predicted":rf_pred
    }
)

print(rf_comparison.head())

print("="*60)
print("Random Forest Information")
print("="*60)

print("Number of trees:",random_forest_model.n_estimators)
print("Number of Features used:",X_train.shape[1])

print("Random Forest Class Distribution")
print(pd.Series(rf_pred).value_counts())


rf_feature_importance=pd.DataFrame({
    "Features":X_train.columns,
    "Importance":random_forest_model.feature_importances_}
)

print("Random Forest Information")
print(rf_feature_importance)

plt.figure(figsize=(8,5))

sns.barplot(
    data=rf_feature_importance,
    x="Importance",
    y="Features"
)

plt.title("Random Forest Information Distribution")

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()

baseline_results = pd.DataFrame({
    "Model": [
        "Logistic Regression"
    ],
    "Accuracy": [
        accuracy
    ],
    "Precision": [
        precision
    ],
    "Recall": [
        recall
    ],
    "F1-Score": [
        f1
    ],
    "ROC-AUC": [
        auc_score
    ]
})

print("\n")
print("=" * 60)
print("BASELINE MODEL")
print("=" * 60)

print(baseline_results)


# Random Forest Model Evaluation

rf_accuracy=accuracy_score(
    y_test,
    y_pred
)

rf_precision=precision_score(
    y_test,
    rf_pred,
    zero_division=0
)

rf_f1=f1_score(
    y_test,
    rf_pred,
    zero_division=0
)

rf_recall=recall_score(
    y_test,
    rf_pred,
    zero_division=0
)

rf_auc=roc_auc_score(
    y_test,
    rf_probability
)

print("=" * 60)
print("RANDOM FOREST MODEL PERFORMANCE")
print("=" * 60)

print("Accuracy  :", round(rf_accuracy * 100, 2), "%")
print("Precision :", round(rf_precision * 100, 2), "%")
print("Recall    :", round(rf_recall * 100, 2), "%")
print("F1-Score  :", round(rf_f1 * 100, 2), "%")
print("ROC-AUC   :", round(rf_auc, 4))


print("="*60)
print("Random Forest Classification Report")
print("="*60)

print(classification_report(
    y_test,
    rf_pred,
    target_names=[
        "No Purchase",
        "Purchase"
    ],
    zero_division=0
))

# Random Forest Confusion Matrix

print("="*60)
print("Random Forest Confusion Matrix")
print("="*60)

rf_cm=confusion_matrix(
    y_test,
    rf_pred
)
print(rf_cm)

rf_TN, rf_FP, rf_FN, rf_TP = rf_cm.ravel()

print("\n")
print("=" * 60)
print("RANDOM FOREST CONFUSION MATRIX COMPONENTS")
print("=" * 60)

print("True Negative  (TN) :", rf_TN)
print("False Positive (FP) :", rf_FP)
print("False Negative (FN) :", rf_FN)
print("True Positive  (TP) :", rf_TP)

rf_results=pd.DataFrame({
    "Model":[random_forest_model],
    "Accuracy":[rf_accuracy],
    "Precision":[rf_precision],
    "Recall":[rf_precision],
    "F1":[rf_f1],
    "Roc_Auc":[rf_auc]
})

print("="*60)
print("Random Forest Model Results")
print("="*60)

print(rf_results)

# Model Comparison

model_comparison=pd.concat(
    [
        baseline_results,
        rf_results
    ],
    ignore_index=True
)

print("="*60)
print("Model Performance Comparison")
print("="*60)

print(model_comparison)

model_comparison_display=model_comparison.copy()

model_comparison_display[
["Accuracy","Precision","Recall","F1","ROC-AUC"]
]=model_comparison_display[
["Accuracy","Precision","Recall","F1","ROC-AUC"]
].round(4)

print("Rounded Model Comaprison")
print(model_comparison_display) 

# Create Comparison Bar Chart

comparison_plot=model_comparison.set_index(
    "Model"
)   
    
comparison_plot[["Accuracy","Precision","Recall","F1","ROC-AUC"]].plot(
    kind="bar",
    figsize=(8,5)
)    

plt.title("Model Comparison Bar")
plt.xlabel("Model")
plt.ylabel("Score")
plt.ylim(0, 1)

plt.xticks(rotation=0)

plt.legend(
    title="Metrics",
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.grid(axis="y")

plt.tight_layout()
plt.show()


metrics=["Accuracy","Precision","Recall","F1","ROC-AUC"]

for metric in metrics:  
    best_model=model_comparison.loc[
    model_comparison[metric].idxmax(),
    "Model"
]
    best_score=model_comparison[metric].max()
    
    print(metric,"->",best_model,round(best_score,4))
    
    
model_comparison["Average_Score"]=model_comparison[metrics].mean(axis=1)

print("\n")
print("=" * 70)
print("OVERALL MODEL SCORE")
print("=" * 70)

print(
    model_comparison[
        ["Model", "Average_Score"]
    ].sort_values(
        by="Average_Score",
        ascending=False
    )
)

best_model_row=model_comparison.loc[
    model_comparison["Average_Score"].idxmax()
]    

best_model_name=best_model_row["Model"]

print("\n")
print("=" * 70)
print("MODEL SELECTION")
print("=" * 70)

print("Best overall model based on average metric score:")
print(best_model_name)

final_model_name = best_model_name


# ==========================================================
#  FINAL MODEL SELECTION & MODEL SAVING
# ==========================================================

import joblib


# ==========================================================
# STEP 1 : SELECT FINAL MODEL
# ==========================================================

if final_model_name == "Logistic Regression":

    final_model = logistic_model

else:

    final_model = random_forest_model


# ==========================================================
# STEP 2 : DISPLAY SELECTED MODEL
# ==========================================================

print("=" * 60)
print("FINAL MODEL SELECTION")
print("=" * 60)

print("Selected Model :", final_model_name)


# ==========================================================
# STEP 3 : DISPLAY FINAL MODEL PERFORMANCE
# ==========================================================

final_model_row = model_comparison[
    model_comparison["Model"] == final_model_name
]

print("\n")
print("=" * 60)
print("FINAL MODEL PERFORMANCE")
print("=" * 60)

print(
    final_model_row[
        [
            "Model",
            "Accuracy",
            "Precision",
            "Recall",
            "F1-Score",
            "ROC-AUC"
        ]
    ]
)


# ==========================================================
# STEP 4 : SAVE THE FINAL MODEL
# ==========================================================

model_filename = "final_purchase_prediction_model.pkl"

joblib.dump(
    final_model,
    model_filename
)

print("\n")
print("=" * 60)
print("MODEL SAVED")
print("=" * 60)

print(
    "Model saved as:",
    model_filename
)


# ==========================================================
# STEP 5 : SAVE FEATURE/COLUMN INFORMATION
# ==========================================================

feature_columns = list(X_train.columns)

joblib.dump(
    feature_columns,
    "model_features.pkl"
)

print(
    "Feature information saved as:",
    "model_features.pkl"
)


# ==========================================================
# STEP 6 : VERIFY MODEL FILE
# ==========================================================

loaded_model = joblib.load(
    model_filename
)

print("\n")
print("=" * 60)
print("MODEL VERIFICATION")
print("=" * 60)

print("Saved model loaded successfully!")


# ==========================================================
# STEP 7 : TEST LOADED MODEL
# ==========================================================

loaded_predictions = loaded_model.predict(
    X_test
)

verification_accuracy = accuracy_score(
    y_test,
    loaded_predictions
)

print(
    "Accuracy of loaded model :",
    round(verification_accuracy * 100, 2),
    "%"
)


# ==========================================================
# STEP 8 : FINAL PROJECT SUMMARY
# ==========================================================

print("\n")
print("=" * 60)
print("FINAL MODEL SUMMARY")
print("=" * 60)

print("Final Model :", final_model_name)

print(
    "Accuracy :",
    round(
        float(final_model_row["Accuracy"].iloc[0]) * 100,
        2
    ),
    "%"
)

print(
    "Precision :",
    round(
        float(final_model_row["Precision"].iloc[0]) * 100,
        2
    ),
    "%"
)

print(
    "Recall :",
    round(
        float(final_model_row["Recall"].iloc[0]) * 100,
        2
    ),
    "%"
)

print(
    "F1-Score :",
    round(
        float(final_model_row["F1-Score"].iloc[0]) * 100,
        2
    ),
    "%"
)

print(
    "ROC-AUC :",
    round(
        float(final_model_row["ROC-AUC"].iloc[0]),
        4
    )
)





# ==========================================================
#  POTENTIAL CUSTOMER PREDICTION
# ==========================================================

print("=" * 60)
print("POTENTIAL CUSTOMER PREDICTION")
print("=" * 60)


# ----------------------------------------------------------
# STEP 1 : CHECK FINAL MODEL
# ----------------------------------------------------------

print("\nFinal Model:")
print(final_model)


# ----------------------------------------------------------
# STEP 2 : USE THE COMPLETE ENCODED DATA
# ----------------------------------------------------------

# X_encoded contains all customers after encoding
# The final model was trained using X_train from X_encoded

print("\nEncoded Feature Shape:", X_encoded.shape)

print("\nEncoded Features:")
print(X_encoded.columns.tolist())


# ----------------------------------------------------------
# STEP 3 : PREDICT PURCHASE FOR ALL CUSTOMERS
# ----------------------------------------------------------

all_predictions = final_model.predict(X_encoded)


# ----------------------------------------------------------
# STEP 4 : PREDICT PURCHASE PROBABILITY
# ----------------------------------------------------------

all_probabilities = final_model.predict_proba(
    X_encoded
)[:, 1]


# ----------------------------------------------------------
# STEP 5 : CREATE PREDICTION DATAFRAME
# ----------------------------------------------------------

prediction_df = japan_fe.copy()


prediction_df["Predicted_Purchase"] = all_predictions


prediction_df["Purchase_Probability"] = all_probabilities


# ----------------------------------------------------------
# STEP 6 : CONVERT PROBABILITY TO PERCENTAGE
# ----------------------------------------------------------

prediction_df["Purchase_Probability_Percent"] = (
    prediction_df["Purchase_Probability"] * 100
).round(2)


# ----------------------------------------------------------
# STEP 7 : CREATE POTENTIAL CUSTOMER STATUS
# ----------------------------------------------------------

prediction_df["Potential_Customer"] = (
    prediction_df["Predicted_Purchase"]
    .map({
        0: "No",
        1: "Yes"
    })
)


# ----------------------------------------------------------
# STEP 8 : DISPLAY SAMPLE
# ----------------------------------------------------------

print("\n")
print("=" * 60)
print("PREDICTION SAMPLE")
print("=" * 60)


print(
    prediction_df[
        [
            "ID",
            "CURR_AGE",
            "GENDER",
            "ANN_INCOME",
            "AGE_CAR",
            "PURCHASE",
            "Predicted_Purchase",
            "Purchase_Probability_Percent",
            "Potential_Customer"
        ]
    ].head(20)
)


# ----------------------------------------------------------
# STEP 9 : COUNT POTENTIAL CUSTOMERS
# ----------------------------------------------------------

potential_customers = (
    prediction_df["Predicted_Purchase"] == 1
).sum()


total_customers = len(prediction_df)


potential_customer_rate = (
    potential_customers / total_customers
) * 100


print("\n")
print("=" * 60)
print("POTENTIAL CUSTOMER SUMMARY")
print("=" * 60)


print(
    "Total Customers        :",
    total_customers
)


print(
    "Potential Customers    :",
    potential_customers
)


print(
    "Potential Customer Rate:",
    round(potential_customer_rate, 2),
    "%"
)


# ----------------------------------------------------------
# STEP 10 : SORT CUSTOMERS BY PURCHASE PROBABILITY
# ----------------------------------------------------------

top_potential_customers = prediction_df.sort_values(
    by="Purchase_Probability",
    ascending=False
)


# ----------------------------------------------------------
# STEP 11 : DISPLAY TOP 20 POTENTIAL CUSTOMERS
# ----------------------------------------------------------

print("\n")
print("=" * 60)
print("TOP 20 POTENTIAL CUSTOMERS")
print("=" * 60)


print(
    top_potential_customers[
        [
            "ID",
            "CURR_AGE",
            "GENDER",
            "ANN_INCOME",
            "AGE_CAR",
            "Purchase_Probability_Percent",
            "Potential_Customer"
        ]
    ].head(20)
)


# ----------------------------------------------------------
# STEP 12 : CREATE POTENTIAL CUSTOMER LIST
# ----------------------------------------------------------

potential_customer_list = prediction_df[
    prediction_df["Predicted_Purchase"] == 1
].copy()


potential_customer_list = (
    potential_customer_list
    .sort_values(
        by="Purchase_Probability",
        ascending=False
    )
)


# ----------------------------------------------------------
# STEP 13 : SAVE POTENTIAL CUSTOMER LIST
# ----------------------------------------------------------

potential_customer_list.to_csv(
    "potential_customers.csv",
    index=False
)


# ----------------------------------------------------------
# STEP 14 : SAVE COMPLETE PREDICTION DATA
# ----------------------------------------------------------

prediction_df.to_csv(
    "customer_purchase_predictions.csv",
    index=False
)





print("\nFiles created:")

print("1. potential_customers.csv")

print("2. customer_purchase_predictions.csv")

# ==========================================================
# POTENTIAL CUSTOMER ANALYSIS
# ==========================================================

print("=" * 60)
print("POTENTIAL CUSTOMER ANALYSIS")
print("=" * 60)


# ----------------------------------------------------------
# 1. POTENTIAL CUSTOMERS BY GENDER
# ----------------------------------------------------------

potential_by_gender = (
    potential_customer_list
    .groupby("GENDER")
    .size()
    .reset_index(name="Potential_Customers")
)


print("\n")
print("=" * 60)
print("POTENTIAL CUSTOMERS BY GENDER")
print("=" * 60)

print(potential_by_gender)


# ----------------------------------------------------------
# 2. POTENTIAL CUSTOMERS BY CAR AGE SEGMENT
# ----------------------------------------------------------

potential_by_car_age = (
    potential_customer_list
    .groupby("AGE_CAR_SEGMENT")
    .size()
    .reset_index(name="Potential_Customers")
)


print("\n")
print("=" * 60)
print("POTENTIAL CUSTOMERS BY CAR AGE SEGMENT")
print("=" * 60)

print(potential_by_car_age)


# ----------------------------------------------------------
# 3. AVERAGE AGE
# ----------------------------------------------------------

average_age_potential = (
    potential_customer_list["CURR_AGE"]
    .mean()
)


print("\n")
print("=" * 60)
print("AVERAGE AGE OF POTENTIAL CUSTOMERS")
print("=" * 60)

print(
    "Average Age:",
    round(average_age_potential, 2)
)


# ----------------------------------------------------------
# 4. AVERAGE INCOME
# ----------------------------------------------------------

average_income_potential = (
    potential_customer_list["ANN_INCOME"]
    .mean()
)


print("\n")
print("=" * 60)
print("AVERAGE INCOME OF POTENTIAL CUSTOMERS")
print("=" * 60)

print(
    "Average Annual Income:",
    round(average_income_potential, 2)
)


# ----------------------------------------------------------
# 5. TOP 10 POTENTIAL CUSTOMERS
# ----------------------------------------------------------

top_10_potential_customers = (
    potential_customer_list[
        [
            "ID",
            "CURR_AGE",
            "GENDER",
            "ANN_INCOME",
            "AGE_CAR",
            "AGE_CAR_SEGMENT",
            "Purchase_Probability_Percent"
        ]
    ]
    .head(10)
)


print("\n")
print("=" * 60)
print("TOP 10 POTENTIAL CUSTOMERS")
print("=" * 60)

print(top_10_potential_customers)


# ----------------------------------------------------------
# 6. SAVE RESULTS
# ----------------------------------------------------------

potential_by_gender.to_csv(
    "potential_customers_by_gender.csv",
    index=False
)


potential_by_car_age.to_csv(
    "potential_customers_by_car_age_segment.csv",
    index=False
)


top_10_potential_customers.to_csv(
    "top_10_potential_customers.csv",
    index=False
)


# ==========================================================
#  INDIAN MARKET PREDICTION
# ==========================================================

print("=" * 60)
print("INDIAN MARKET POTENTIAL CUSTOMER PREDICTION")
print("=" * 60)


# ----------------------------------------------------------
# STEP 1 : CHECK INDIAN DATA
# ----------------------------------------------------------

print("\nIndian Dataset Shape:")
print(indian_fe.shape)

print("\nIndian Dataset Columns:")
print(indian_fe.columns.tolist())

# ----------------------------------------------------------
# STEP 2 : CREATE INDIAN MODEL FEATURES
# ----------------------------------------------------------

indian_model = indian_fe.copy()

# Keep only the variables used by the model
indian_model = indian_model[
    [
        "CURR_AGE",
        "GENDER",
        "ANN_INCOME",
        "AGE_CAR",
        "AGE_CAR_SEGMENT"
    ]
].copy()

print("\nIndian Model Features:")
print(indian_model.head())

print("\nIndian Model Feature Shape:")
print(indian_model.shape)

# ----------------------------------------------------------
# STEP 3 : ENCODE INDIAN CATEGORICAL VARIABLES
# ----------------------------------------------------------

# Convert categorical variables into dummy/indicator variables
indian_encoded = pd.get_dummies(
    indian_model,
    columns=["GENDER", "AGE_CAR_SEGMENT"],
    drop_first=True
)

print("\nIndian Encoded Features:")
print(indian_encoded.head())

print("\nIndian Encoded Shape:")
print(indian_encoded.shape)

# ----------------------------------------------------------
# STEP 4 : MATCH INDIAN FEATURES WITH MODEL FEATURES
# ----------------------------------------------------------

# Make Indian columns exactly the same as the columns
# used while training the model

indian_encoded = indian_encoded.reindex(
    columns=X_encoded.columns,
    fill_value=0
)

print("\nFinal Indian Model Input Shape:")
print(indian_encoded.shape)

print("\nFinal Indian Model Columns:")
print(indian_encoded.columns.tolist())


# ----------------------------------------------------------
# STEP 5 : PREDICT INDIAN CUSTOMER PURCHASE BEHAVIOUR
# ----------------------------------------------------------

# Generate purchase predictions
indian_predictions = final_model.predict(indian_encoded)

# Generate purchase probabilities
indian_probabilities = final_model.predict_proba(indian_encoded)[:, 1]


print("\nPrediction completed successfully!")

print("\nFirst 10 Predictions:")
print(indian_predictions[:10])

print("\nFirst 10 Purchase Probabilities:")
print(indian_probabilities[:10])


# ----------------------------------------------------------
# STEP 6 : ADD PREDICTIONS TO INDIAN DATASET
# ----------------------------------------------------------

indian_predictions_df = indian_fe.copy()

indian_predictions_df["Predicted_Purchase"] = indian_predictions

indian_predictions_df["Purchase_Probability"] = indian_probabilities

indian_predictions_df["Purchase_Probability_Percent"] = (
    indian_probabilities * 100
)

print("\nIndian Prediction Dataset:")
print(indian_predictions_df.head())

print("\nPrediction Dataset Shape:")
print(indian_predictions_df.shape)


# ----------------------------------------------------------
# STEP 7 : CREATE POTENTIAL CUSTOMER FLAG
# ----------------------------------------------------------

indian_predictions_df["Potential_Customer"] = np.where(
    indian_predictions_df["Predicted_Purchase"] == 1,
    "Yes",
    "No"
)

print("\nPotential Customer Distribution:")
print(
    indian_predictions_df["Potential_Customer"].value_counts()
)


# ----------------------------------------------------------
# STEP 8 : CALCULATE POTENTIAL CUSTOMERS IN INDIA
# ----------------------------------------------------------

# Count potential customers
potential_customers = (
    indian_predictions_df["Potential_Customer"] == "Yes"
).sum()

# Count total Indian customers
total_indian_customers = len(indian_predictions_df)

# Calculate potential customer percentage
potential_customer_rate = (
    potential_customers / total_indian_customers
) * 100


print("\n" + "=" * 60)
print("INDIAN MARKET POTENTIAL CUSTOMER RESULTS")
print("=" * 60)

print(f"Total Indian Customers       : {total_indian_customers:,}")
print(f"Potential Customers          : {potential_customers:,}")
print(f"Potential Customer Rate      : {potential_customer_rate:.2f}%")
print("=" * 60)



# ==========================================================
# STEP 10 : CREATE FINAL INDIAN TABLEAU DATASET
# ==========================================================

indian_tableau = indian_predictions_df.copy()

# Save the complete Indian analysis dataset
indian_tableau.to_csv(
    "indian_tableau_data.csv",
    index=False
)

print("\n" + "=" * 60)
print("INDIAN TABLEAU DATASET CREATED")
print("=" * 60)

print("Rows:", len(indian_tableau))
print("Columns:", len(indian_tableau.columns))

print("\nColumns available for Tableau:")
print(indian_tableau.columns.tolist())

print("\nFile saved as:")
print("indian_tableau_data.csv")

# ==========================================================
# LOGISTIC REGRESSION COEFFICIENT ANALYSIS
# ==========================================================

# Get the feature names used by the Logistic Regression model
feature_names = X_encoded.columns

# Get the coefficients
coefficients = logistic_model.coef_[0]

# Create a DataFrame containing feature names and coefficients
coefficient_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

# Sort coefficients from most negative to most positive
coefficient_df = coefficient_df.sort_values(
    by="Coefficient"
)

# Display all coefficients
print("=" * 60)
print("LOGISTIC REGRESSION COEFFICIENTS")
print("=" * 60)

print(coefficient_df.to_string(index=False))


# ----------------------------------------------------------
# MOST NEGATIVE COEFFICIENT
# ----------------------------------------------------------

most_negative = coefficient_df.iloc[0]

print("\n" + "=" * 60)
print("MOST NEGATIVE COEFFICIENT")
print("=" * 60)

print("Feature:", most_negative["Feature"])
print("Coefficient:", round(most_negative["Coefficient"], 4))


# ----------------------------------------------------------
# MOST POSITIVE COEFFICIENT
# ----------------------------------------------------------

most_positive = coefficient_df.iloc[-1]

print("\n" + "=" * 60)
print("MOST POSITIVE COEFFICIENT")
print("=" * 60)

print("Feature:", most_positive["Feature"])
print("Coefficient:", round(most_positive["Coefficient"], 4))