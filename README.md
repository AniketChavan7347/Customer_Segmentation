# 🛍️ Customer Segmentation using K-Means Clustering

An end-to-end Machine Learning project that segments customers into different groups using the **K-Means Clustering** algorithm. The project includes an interactive **Streamlit** web application that allows users to upload a dataset, visualize customer segments, and download the clustered results.

## 🔗 Live Demo

**Streamlit App:**  customersegmentation-bzpql8vkcbb2adcbqqf6fa.streamlit.app

---

## 📌 Project Overview

Customer segmentation is a business strategy used to group customers based on similar characteristics and purchasing behavior. This project applies the **K-Means Clustering** algorithm to identify customer groups using:

* Annual Income
* Spending Score

The application provides an interactive interface where users can upload a customer dataset, perform clustering, visualize the results, and download the segmented data.

---

## ✨ Features

* 📂 Upload customer dataset (CSV)
* 📊 Preview uploaded dataset
* 📌 Select features for clustering
* 📈 Elbow Method to determine the optimal number of clusters
* 🤖 Customer Segmentation using K-Means Clustering
* 📉 Interactive cluster visualization
* ⬇️ Download clustered dataset
* 💻 User-friendly Streamlit interface

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

## 🤖 Machine Learning Algorithm

This project uses the **K-Means Clustering** algorithm, an unsupervised machine learning technique that groups customers with similar characteristics into different clusters based on **Annual Income** and **Spending Score**.

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
├── dashboard.png
├── elbow_method.png
├── customer_segments.png
└── clustered_data.png
```

---

## 📷 Project Screenshots

### Dashboard
 dashboard.png
---

### Elbow Method
elbow_method.png
---

### Customer Segments
 customer_segments.png
---

### Clustered Dataset
clustered_data.png
---

## 📊 Machine Learning Workflow

1. Load the customer dataset.
2. Perform data exploration.
3. Select Annual Income and Spending Score as features.
4. Apply the Elbow Method to determine the optimal number of clusters.
5. Train the K-Means Clustering model.
6. Assign cluster labels to each customer.
7. Visualize customer segments.
8. Download the segmented dataset.

---

## 📈 Project Output

The application generates:

* Dataset Preview
* Elbow Method Graph
* Customer Segmentation Scatter Plot
* Clustered Dataset with a **Cluster** column
* Downloadable CSV file

---

## 🚀 How to Run the Project

### Clone the Repository

```bash
git clone https: https://github.com/AniketChavan7347/Customer_Segmentation
```

### Navigate to the Project Folder

```bash
cd Customer-Segmentation
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 💼 Business Use Cases

* Customer Segmentation
* Targeted Marketing Campaigns
* Customer Behavior Analysis
* Customer Retention Strategies
* Personalized Product Recommendations
* Business Decision Support

---

## 📌 Future Improvements

* Automatic feature selection
* Cluster naming (Premium, Budget, Standard, etc.)
* More interactive visualizations
* Customer insights and recommendations
* Enhanced dashboard design

---

## 👨‍💻 Author

**Aniket Chavan**

GitHub: http://github.com/AniketChavan7347

LinkedIn: https://www.linkedin.com/in/aniket-chavan-b494ab255

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.
