#Importing the necessary libraries
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the Iris dataset
iris = load_iris()
# Creating a DataFrame from the loaded data
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# Adding the species column to the DataFrame
df['species'] = iris.target

# Mapping target numbers to species names
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

try:
    # Displaying the first few rows of the dataset
    print("First few rows of the dataset:")
    print(df.head())

    # Exploring dataset structure
    print("\nData types and missing values:")
    print(df.info())

    # Checking for missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    # Task 2: Basic Data Analysis
    # Displaying the basic statistics of the dataset
    print("\nBasic statistics of the dataset:")
    print(df.describe())

    grouped_data = df.groupby('species')['petal length (cm)'].mean().reset_index()
    print("\nAverage petal length per species:")
    print(grouped_data)

    print("\nInteresting findings:")
    for index, row in grouped_data.iterrows():
        print(f"The average petal length of {row['species']} is {row['petal length (cm)']:.2f} cm.")

    # Task 3: Data Visualization
    sns.set(style="whitegrid")

    # 1. Bar Chart: Average petal length per species
    plt.figure(figsize=(10, 6))
    sns.barplot(x='species', y='petal length (cm)', data=df, estimator='mean', errorbar=None)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.tight_layout()
    plt.show()

    # 2. Histogram: Distribution of sepal length
    plt.figure(figsize=(10, 6))
    sns.histplot(df['sepal length (cm)'], bins=10, kde=True)
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # 3. Scatter Plot: Sepal Length vs. Petal Length
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
    plt.title('Sepal Length vs. Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.tight_layout()
    plt.show()

    # 4. Line Chart: Average Sepal Length per Species
    average_sepal_length = df.groupby('species')['sepal length (cm)'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(average_sepal_length['species'], average_sepal_length['sepal length (cm)'], marker='o', color='g',
             label='Average Sepal Length')
    plt.title('Average Sepal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Sepal Length (cm)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()





except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")
