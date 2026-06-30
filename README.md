# 🛍️ Customer Segmentation using K-Means Clustering

An end-to-end Machine Learning project that segments customers into different groups using the **K-Means Clustering** algorithm. The project also includes an interactive **Streamlit web application** that allows users to upload a dataset, visualize customer segments, and download the clustered results.

---

## 📌 Project Overview

Customer segmentation is a technique used by businesses to divide customers into groups based on their purchasing behavior and characteristics. This project applies the **K-Means Clustering** algorithm to identify customer groups based on:

* Annual Income
* Spending Score

The interactive Streamlit application enables users to upload a CSV file, perform clustering, visualize the results, and download the processed dataset.

---

## ✨ Features

* Upload customer dataset (CSV)
* Interactive dataset preview
* Automatic feature selection
* Elbow Method to determine the optimal number of clusters
* Customer segmentation using K-Means Clustering
* Interactive cluster visualization
* Download clustered dataset
* User-friendly Streamlit interface

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Jupyter Notebook

---

## 📂 Project Structure

```text
Customer_Segmentation/
│
├── app.py
├── customer_segmentation.ipynb
├── Mall_Customers.csv
├── segmented_customers.csv
├── requirements.txt
├── README.md

```

---

## 📊 Machine Learning Workflow

1. Load the customer dataset.
2. Perform basic data exploration.
3. Select Annual Income and Spending Score as features.
4. Use the Elbow Method to determine the optimal number of clusters.
5. Train the K-Means clustering model.
6. Visualize customer segments.
7. Generate a new dataset with cluster labels.
8. Download the segmented customer data.

---

## 📈 Project Output

The application provides:

* Dataset preview
* Elbow Method graph
* Customer segmentation scatter plot
* Clustered dataset with a new **Cluster** column
* Download option for the processed CSV file

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Customer-Segmentation.git
```

### 2. Navigate to the project folder

```bash
cd Customer-Segmentation
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py


```


## 💼 Business Use Cases

This project can help businesses:

* Understand customer purchasing behavior
* Identify high-value customers
* Design targeted marketing campaigns
* Improve customer retention
* Support data-driven business decisions

---

## 📌 Future Improvements

* Automatic feature detection
* Cluster description and naming
* Interactive dashboard with additional charts
* Customer insights and recommendations
* Deployment on Streamlit Community Cloud

---

## 👨‍💻 Author

**Aniket Chavan**

If you found this project useful, consider giving it a ⭐ on GitHub.
