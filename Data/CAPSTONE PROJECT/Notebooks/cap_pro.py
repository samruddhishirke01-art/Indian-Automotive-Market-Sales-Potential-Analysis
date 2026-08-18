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




