import streamlit as st


# Create a sidebar navigation menu
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Introduction", "Modelos", "Model Testing"], format_func=lambda x: x)

# Create containers for each page
page_container = st.container()

# Create a session state to store data
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# Define content for each page
if page == "Introduction":

    page_container.title("Project Introduction")
    
    # Add text spaces for your project introduction
    introduction_text = """
    Welcome to our project! This is a brief introduction to what we are working on.
    
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Vestibulum ac tellus eu ligula sollicitudin laoreet. 
    Nulla facilisi. Sed ut nisi et velit posuere feugiat. 
    
    Feel free to add more details about your project here.
    """
    page_container.write(introduction_text)

elif page == "Modelos":

    page_container.title("Machine Learning Model Evaluation")

    models = [
        'Gaussian Naive Bayes',
        'Support Vector Machine (SVM)',
        'Random Forest',
        'k-Nearest Neighbors (KNN)',
        'XGBoost',
        'Logistic Regression',
    ]


    # Navigation bar
    page = st.sidebar.selectbox("Select a model", [model for model in models])

    # Display selected model's information
    st.subheader(f'Model: {page}')

elif page == "Model Testing":
    page_container.title("Model Testing")
    



