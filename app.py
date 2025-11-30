import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

st.title("🎓 学生生活方式类型预测小测试")

st.write("根据你的习惯和生活方式，看看你属于哪种类型的学生!")

# 7 个变量名（与你的 dataset 一模一样）
cols = [
    "Study_Hours_Per_Day",
    "Extracurricular_Hours_Per_Day",
    "Sleep_Hours_Per_Day",
    "Social_Hours_Per_Day",
    "Physical_Activity_Hours_Per_Day",
    "GPA",
    "Stress_Level"
]

# 让用户输入自己的数据
st.subheader("👉 输入你的生活方式信息：")

study = st.slider("每天学习小时数", 0.0, 12.0, 3.0, 0.5)
extra = st.slider("每天课外活动小时数", 0.0, 10.0, 1.0, 0.5)
sleep = st.slider("每天睡眠小时数", 0.0, 12.0, 8.0, 0.5)
social = st.slider("每天社交时间（小时）", 0.0, 10.0, 2.0, 0.5)
activity = st.slider("每天运动时间（小时）", 0.0, 5.0, 0.5, 0.1)
gpa = st.slider("GPA", 0.0, 4.0, 3.0, 0.1)

stress_level = st.selectbox("压力等级", ["Low", "Moderate", "High"])
stress_map = {"Low": 1, "Moderate": 2, "High": 3}
stress = stress_map[stress_level]

# 用户输入组合成一行
new_row = pd.DataFrame([[study, extra, sleep, social, activity, gpa, stress]], columns=cols)

# 读取你的 dataset，用来 fit scaler 和 KMeans
df = pd.read_csv("student_lifestyle_dataset.csv")

# 压力等级转换
df["Stress_Level"] = df["Stress_Level"].map(stress_map)

# 取出训练数据
X = df[cols]

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
new_scaled = scaler.transform(new_row)

# 训练 KMeans（k=3）
kmeans = KMeans(n_clusters=3, random_state=42, n_init="auto")
kmeans.fit(X_scaled)

# 预测结果
cluster = int(kmeans.predict(new_scaled)[0])

# 可以给 cluster 起人话名字（你可以自己改）
cluster_name = {
    0: "📚 自律学霸型",
    1: "🎉 社交活跃型",
    2: "😴 摆烂摸鱼型"
}

if st.button("✨ 查看结果"):
    st.success(f"你属于：Cluster {cluster} - {cluster_name.get(cluster, '未命名类型')}")
    st.write("（根据你的 7 个输入特征，通过 K-Means 预测。）")





