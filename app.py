import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Segmentation App", layout="wide")

st.title("🛍️ Customer Segmentation using K-Means Clustering")
st.write("Upload your dataset and explore customer segments easily.")


# Upload CSV

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")

    # Show data
    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    # Rename columns if needed
    if st.checkbox("Auto Rename Columns"):
        df.columns = df.columns.str.replace(" ", "_")

  
    # Feature Selection
  
    st.subheader("📌 Feature Selection")

   # remove useless columns from selection
    usable_columns = df.columns.drop("Cluster", errors="ignore")

    income_col = st.selectbox("Select Income Column", usable_columns)
    score_col = st.selectbox("Select Spending Score Column", usable_columns)

    if income_col == score_col:
     st.error("Please select two different columns!")
     st.stop()

    X = df[[income_col, score_col]]

  
    # Elbow Method
  
    st.subheader("📈 Elbow Method (Find Optimal K)")

    wcss = []
    K_range = range(1, 11)

    for i in K_range:
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    fig, ax = plt.subplots()
    ax.plot(K_range, wcss, marker='o')
    ax.set_xlabel("Number of Clusters")
    ax.set_ylabel("WCSS")
    ax.set_title("Elbow Method")
    st.pyplot(fig)

  
    # K Means Model

    k = st.slider("Select Number of Clusters", 2, 10, 5)

    kmeans = KMeans(n_clusters=k, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X)

    st.subheader("🎯 Clustered Data")
    st.dataframe(df.head())

    # Visualization
  
    st.subheader("📊 Customer Segments Visualization")

    fig2, ax2 = plt.subplots()

    sns.scatterplot(
        x=X.iloc[:, 0],
        y=X.iloc[:, 1],
        hue=df["Cluster"],
        palette="Set1",
        ax=ax2
    )

    ax2.set_xlabel(income_col)
    ax2.set_ylabel(score_col)
    ax2.set_title("Customer Segments")

    st.pyplot(fig2)

    # Download Result
    
    st.subheader("⬇️ Download Results")

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "Download Segmented Data",
        data=csv,
        file_name="segmented_customers.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a CSV file to start analysis.")