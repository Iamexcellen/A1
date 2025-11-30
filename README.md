#<h1>**Student Lifestyle Clustering App**</h1>
---
#This project uses **K-Means clustering** to classify different types of student lifestyles based on daily habits and academic indicators.␣␣

👉 **Live Demo（right now it is in Chinese version)␣␣
Here is the link for experiencing
https://genesisthebeginning.streamlit.app/

##The technology that I used:␣␣
- Python
- Streamlit
- scikit-learn（KMeans, StandardScaler）
- pandas, numpy

##The introduction of the dataset:␣␣
"student_lifestyle_dataset.csv" is the dataset that I am using.␣␣
The main variables are:␣␣
- Study_Hours_Per_Day  
- Extracurricular_Hours_Per_Day  
- Sleep_Hours_Per_Day  
- Social_Hours_Per_Day  
- Physical_Activity_Hours_Per_Day  
- GPA  
- Stress_Level（Low / Moderate / High change to 1 / 2 / 3）

##The function of the project:␣␣
-Users could choose their own lifestyle indicators
- The project automatically standardizes inputs using **StandardScaler**  
- A **K-Means model (k = 3)** is used to classify the lifestyle type  
- The app returns a cluster label representing different student lifestyle categories  

##Purpose␣␣
This web app provides a simple and interactive demonstration of how machine learning can be used to cluster behavioral patterns.  
