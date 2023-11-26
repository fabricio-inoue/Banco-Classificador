import streamlit as st

from utils import model_utils
from components import components


# Create containers for each page
page_container = st.container()




page_container.title("Teste o modelo")



models = ['Gaussian Naive Bayes','Support Vector Machine (SVM)','Random Forest','k-Nearest Neighbors (KNN)','XGBoost','Logistic Regression']

selected = components.selector(models, "bruh")

page_container.title(str(selected))

# Define the quiz questions
questions = [
    "What is your age?",
    "What is your job?",
    "What is your marital status?",
    "What is your education level?",
    "Do you have any defaults?",
    "Do you own a house?",
    "Do you have a loan?",
    "How were you contacted?",
    "Which month were you contacted?",
    "Which day of the week were you contacted?",
    "What was the duration of the last contact (in seconds)?",
    "How many times have you been contacted during this campaign?",
    "Number of days since the client was last contacted (-1 means client was not contacted before)",
    "Number of contacts performed before this campaign",
    "Outcome of the previous marketing campaign",
    "Employment variation rate",
    "Consumer price index",
    "Consumer confidence index",
    "Euribor 3-month rate",
    "Number of employees"]

# Create a dictionary to store the user's answers
user_answers = {}

# Streamlit app
st.title("Quiz App")
st.write("Answer the following questions:")

for i, question in enumerate(questions):
    st.write(f"**Question {i + 1}:** {question}")
    answer = st.text_input(f"Your answer for Question {i + 1}")
    user_answers[question] = answer

st.write("Your answers:")
st.json(user_answers)

# Map the answers to their respective categories
category_mappings = {
    # Your category mappings here
}

# Encode the answers
encoded_answers = {}

for question, answer in user_answers.items():
    if question in category_mappings['encode']:
        category_mapping = category_mappings['encode'][question]
        encoded_answers[question] = category_mapping.get(answer, None)
    else:
        encoded_answers[question] = answer

st.write("Encoded answers:")
st.json(encoded_answers)


model = model_utils.load_model('src/models/svm.pkl')