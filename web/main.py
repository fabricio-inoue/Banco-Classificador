

import streamlit as st

# Função para codificar os dados categóricos
def encode_data(data, category_mappings):
    encoded_data = {}
    for key, value in data.items():
        if key in category_mappings['encode']:
            encoded_data[key] = category_mappings['encode'][key].get(value, None)
        else:
            encoded_data[key] = value
    return encoded_data

# Mapeamentos de categorias
category_mappings = {'decode':{
    'job': {
        0: 'admin.',
        2: 'entrepreneur',
        1: 'blue-collar',
        4: 'management',
        6: 'self-employed',
        5: 'retired',
        3: 'housemaid',
        8: 'student',
        7: 'services',
        9: 'technician',
        10: 'unemployed',
        11: None  # Represents missing data
    },
    'marital': {
        0: 'divorced',
        2: 'single',
        1: 'married',
        3: None
    },
    'education': {
        0: 'basic.4y',
        1: 'basic.6y',
        2: 'basic.9y',
        3: 'high.school',
        4: 'illiterate',
        5: 'professional.course',
        6: 'university.degree',
        7: None
    },
    'default': {
        0: 'no',
        1: 'yes',
        2: None
    },
    'housing': {
        0: 'no',
        1: 'yes',
        2: None
    },
    'loan': {
        0: 'no',
        1: 'yes',
        2: None
    },
    'contact': {
        0: 'cellular',
        1: 'telephone'
    },
    'month': {
        0: 'apr',
        1: 'aug',
        2: 'dec',
        3: 'jul',
        4: 'jun',
        5: 'mar',
        6: 'may',
        7: 'nov',
        8: 'oct',
        9: 'sep'
    },
    'day_of_week': {
        0: 'fri',
        1: 'mon',
        2: 'thu',
        3: 'tue',
        4: 'wed'
    },
    'poutcome': {
        0: 'failure',
        1: 'success',
        2: None
    },
    'y': {
        0: 'no',
        1: 'yes'
    }
},
'encode': {
    'job': {
        'admin.': 0,
        'entrepreneur': 2,
        'blue-collar': 1,
        'man`age`ment': 4,
        'self-employed': 6,
        'retired': 5,
        'housemaid': 3,
        'student': 8,
        'services': 7,
        'technician': 9,
        'unemployed': 10,
        None: 11
    },
    'marital': {
        'divorced': 0,
        'single': 2,
        'married': 1,
        None: 3
    },
    'education': {
        'basic.4y': 0,
        'basic.6y': 1,
        'basic.9y': 2,
        'high.school': 3,
        'illiterate': 4,
        'professional.course': 5,
        'university.degree': 6,
        None: 7
    },
    'default': {
        'no': 0,
        'yes': 1,
        None: 2
    },
    'housing': {
        'no': 0,
        'yes': 1,
        None: 2
    },
    'loan': {
        'no': 0,
        'yes': 1,
        None: 2
    },
    'contact': {
        'cellular': 0,
        'telephone': 1
    },
    'month': {
        'apr': 0,
        'aug': 1,
        'dec': 2,
        'jul': 3,
        'jun': 4,
        'mar': 5,
        'may': 6,
        'nov': 7,
        'oct': 8,
        'sep': 9
    },
    'day_of_week': {
        'fri': 0,
        'mon': 1,
        'thu': 2,
        'tue': 3,
        'wed': 4
    },
    'poutcome': {
        'failure': 0,
        'success': 1,
        None: 2
    },
    'y': {
        'no': 0,
        'yes': 1
    }
}

}

def main():
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Escolha uma página", ["Introdução", "Modelos", "Teste de Modelo"])

    if page == "Introdução":
        st.title("Introdução")
        st.write("Bem-vindo ao nosso projeto de Machine Learning! Aqui você pode testar diferentes modelos de ML e ver como eles funcionam com dados reais.")

    elif page == "Modelos":
        st.title("Modelos de Machine Learning")
        model = st.selectbox("Escolha um modelo", ['Gaussian Naive Bayes', 'Support Vector Machine (SVM)', 'Random Forest', 'k-Nearest Neighbors (KNN)', 'XGBoost', 'Logistic Regression'])
        
        # Textos explicativos para cada modelo
        model_texts = {
            'Gaussian Naive Bayes': 'O Gaussian Naive Bayes é um classificador probabilístico baseado no Teorema de Bayes com a suposição de independência entre os preditores.',
            'Support Vector Machine (SVM)': 'SVM é um modelo poderoso para tarefas de classificação e regressão. Ele cria um hiperplano ou conjunto de hiperplanos em um espaço de alta ou infinita dimensão.',
            'Random Forest': 'Random Forest é um método de aprendizado conjunto para classificação, regressão e outras tarefas. Ele opera construindo uma infinidade de árvores de decisão.',
            'k-Nearest Neighbors (KNN)': 'KNN é um algoritmo simples que armazena todos os casos disponíveis e classifica novos casos com base em uma medida de similaridade.',
            'XGBoost': 'XGBoost é uma implementação otimizada de gradient boosting que é eficiente, flexível e portátil.',
            'Logistic Regression': 'A regressão logística é um modelo de regressão usado para prever a probabilidade de uma variável dependente categórica.'
        }
        st.write(model_texts[model])

    elif page == "Teste de Modelo":
        st.title("Teste de Modelo")
        user_data = {}
        user_data['age'] = st.number_input("Idade", min_value=0, max_value=120)
        user_data['job'] = st.selectbox("Trabalho", list(category_mappings['decode']['job'].values()))
        user_data['marital'] = st.selectbox("Estado Civil", list(category_mappings['decode']['marital'].values()))
        user_data['education'] = st.selectbox("Educação", list(category_mappings['decode']['education'].values()))
        user_data['default'] = st.selectbox("Inadimplente", list(category_mappings['decode']['default'].values()))
        user_data['housing'] = st.selectbox("Moradia", list(category_mappings['decode']['housing'].values()))
        user_data['loan'] = st.selectbox("Empréstimo", list(category_mappings['decode']['loan'].values()))
        user_data['contact'] = st.selectbox("Contato", list(category_mappings['decode']['contact'].values()))
        user_data['month'] = st.selectbox("Mês", list(category_mappings['decode']['month'].values()))
        user_data['day_of_week'] = st.selectbox("Dia da Semana", list(category_mappings['decode']['day_of_week'].values()))
        user_data['duration'] = st.number_input("Duração", min_value=0)
        user_data['campaign'] = st.number_input("Campanha", min_value=0)
        user_data['pdays'] = st.number_input("Pdias", min_value=0)
        user_data['previous'] = st.number_input("Anterior", min_value=0)
        user_data['poutcome'] = st.selectbox("Resultado da Campanha Anterior", list(category_mappings['decode']['poutcome'].values()))
        user_data['emp.var.rate'] = st.number_input("Taxa de Variação de Emprego", step=0.1)
        user_data['cons.price.idx'] = st.number_input("Índice de Preços ao Consumidor", step=0.1)
        user_data['cons.conf.idx'] = st.number_input("Índice de Confiança do Consumidor", step=0.1)
        user_data['euribor3m'] = st.number_input("Euribor 3 Meses", step=0.1)
        user_data['nr.employed'] = st.number_input("Número de Empregados", step=0.1)

        if st.button("Codificar e Mostrar Dados"):
            encoded_data = encode_data(user_data, category_mappings)
            st.write(encoded_data)

if __name__ == "__main__":
    main()

