# Customer Personality Analysis

Welcome to the **Customer Personality Analysis** repository! This project aims to explore and analyze customer data by segmenting them based on various attributes. The goal is to derive actionable insights for targeted marketing strategies. Using Exploratory Data Analysis (EDA) and clustering techniques, we identify distinct customer groups, leveraging Python and key data science libraries for in-depth analysis and visualization.

---

## Table of Contents

- [Dataset Overview](#dataset-overview)
- [Project Workflow](#project-workflow)
  - [Data Preprocessing](#data-preprocessing)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Clustering Techniques](#clustering-techniques)
  - [Cluster Evaluation](#cluster-evaluation)
  - [Conclusion & Insights](#conclusion--insights)
  - [Streamlit App](#streamlit-app)
- [Requirements](#requirements)
- [Analysis Conclusion](#Analysis Conclusion)

---

## Dataset Overview

The **Customer Personality Analysis** dataset, available on [Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis), provides comprehensive customer data, ideal for segmentation and analysis. It includes various customer attributes such as demographic information and purchasing behavior, including:

- **ID**: Unique customer identifier
- **Year_Birth**: Customer's birth year
- **Education**: Education level
- **Marital_Status**: Marital status
- **Income**: Annual income
- **Kidhome**: Number of small children at home
- **Teenhome**: Number of teenagers at home
- **Dt_Customer**: Date of customer enrollment
- **Recency**: Number of days since the last purchase
- **Spending categories**: Amounts spent across various product categories
- **Response**: Customer response to the latest marketing campaign

---

## Project Workflow

### 1. Data Preprocessing
   - **Data Cleaning**: Handling missing values, encoding categorical variables, and performing feature engineering.
   - **Feature Scaling**: Normalizing numerical features to improve clustering results.

### 2. Exploratory Data Analysis (EDA)
   - Visualizing distributions of customer attributes.
   - Investigating correlations between features.
   - Identifying outliers and analyzing data distribution.

### 3. Clustering Techniques
   - **K-means Clustering**:
     - Using the Elbow Method to determine the optimal number of clusters.
     - Evaluating the quality of clusters using the Silhouette Score.
   - **Hierarchical Clustering**:
     - Creating a dendrogram to visualize hierarchical relationships among clusters.
   - **Alternative Clustering Methods (Optional)**:
     - Exploring DBSCAN or Gaussian Mixture Models for comparison.

### 4. Cluster Evaluation
   - Analyzing the characteristics of each cluster.
   - Visualizing clusters using dimensionality reduction techniques like PCA or t-SNE to better understand cluster separations.
   - Deriving business insights based on the cluster analysis.

### 5. Conclusion & Insights
   - Summarizing the findings from clustering analysis.
   - Providing actionable recommendations for targeted marketing and customer relationship management.

### 6. Streamlit App
   - A user-friendly interface to interact with the clustering results and visualize customer segments.

---

## Requirements

To run the code and reproduce the results, you need the following Python libraries:

```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit

## Analysis Conclusion

After thoroughly analyzing the clustering results, we observed a significant overlap in the characteristics of Cluster 1 and Cluster 2 when the number of clusters was set to 3 (n_clusters = 3). This overlap suggests that differentiating between these two clusters does not provide additional insights into customer segmentation. 

Additionally, the silhouette score, which measures the cohesion and separation of clusters, was found to be the highest when n_clusters = 2. This supports the decision that two clusters offer the most meaningful segmentation and reflect distinct customer groups.

Consequently, the optimal number of clusters for this segmentation problem is 2 (n_clusters = 2). Below, we provide a detailed profile of these two clusters, highlighting the key characteristics that differentiate them.

### Profiling Customers

| Feature               | Cluster 0                             | Cluster 1                             |
|-----------------------|---------------------------------------|---------------------------------------|
| **Income & Spending** | Individuals with low to average income and low spending | Individuals with average to high income, and moderate to high spending |
| **Education Level**   | Majority are Graduate/Postgraduate, with a very small percentage of Undergraduates | Majority are Graduate/Postgraduate |
| **Response Rate**     | Low response rate                     | Higher response rate                  |
| **Number of Children**| Majority have more than 1 child       | Majority have no children or have 1 child |
| **Total Purchases**   | Fewer purchases                       | Higher number of purchases            |
| **Amount Spent**      | Lowest spending                       | Highest spending                      |
| **Income**            | Lowest income                         | Highest income                        |
| **Age**               | Median: 42.0                          | Median: 48.0                          |

