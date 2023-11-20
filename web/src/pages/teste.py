import streamlit as st

from utils import model_utils
from components import components


# Create containers for each page
page_container = st.container()




page_container.title("Teste o modelo")



models = ['Gaussian Naive Bayes','Support Vector Machine (SVM)','Random Forest','k-Nearest Neighbors (KNN)','XGBoost','Logistic Regression']

selected = components.selector(models, "bruh")

page_container.title(str(selected))

model = model_utils.load_model('src/models/svm.pkl')