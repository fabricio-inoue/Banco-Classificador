

import streamlit as st

import pickle

# Função para codificar os dados categóricos
# def encode_data(data, category_mappings):
#     encoded_data = {}
#     for key, value in data.items():
#         if key in category_mappings['encode']:
#             encoded_data[key] = category_mappings['encode'][key].get(value, None)
#         else:
#             encoded_data[key] = value
#     return encoded_data

def encode_data(data, category_mappings):
    encoded_data = []
    for key in sorted(data.keys()):  # Ordenando as chaves para garantir a ordem consistente dos dados
        value = data[key]
        if key in category_mappings['encode']:
            encoded_value = category_mappings['encode'][key].get(value, None)
            encoded_data.append(encoded_value)
        else:
            encoded_data.append(value)
    return encoded_data


def load_model(model_name):
    with open(model_name, 'rb') as file:
        return pickle.load(file)

# Mapeamentos de categorias
category_mappings = {'decode':{
    'job': {
        0: 'administrador',
        2: 'empreendedor',
        1: 'trabalhador manual',
        4: 'gerência',
        6: 'autônomo',
        5: 'aposentado',
        3: 'empregada doméstica',
        8: 'estudante',
        7: 'serviços',
        9: 'técnico',
        10: 'desempregado',

    },
    'marital': {
        0: 'divorciado',
        2: 'solteiro',
        1: 'casado',

    },
    'education': {
        0: 'fundamental 4 anos',
        1: 'fundamental 6 anos',
        2: 'fundamental 9 anos',
        3: 'ensino médio',
        4: 'analfabeto',
        5: 'curso profissionalizante',
        6: 'ensino superior',

    },
    'default': {
        0: 'não',
        1: 'sim',

    },
    'housing': {
        0: 'não',
        1: 'sim',

    },
    'loan': {
        0: 'não',
        1: 'sim',

    },
    'contact': {
        0: 'celular',
        1: 'telefone'
    },
    'month': {
        0: 'abr',
        1: 'ago',
        2: 'dez',
        3: 'jul',
        4: 'jun',
        5: 'mar',
        6: 'mai',
        7: 'nov',
        8: 'out',
        9: 'set'
    },
    'day_of_week': {
        0: 'sex',
        1: 'seg',
        2: 'qui',
        3: 'ter',
        4: 'qua'
    },
    'poutcome': {
        0: 'fracasso',
        1: 'sucesso',

    },
    'y': {
        0: 'não',
        1: 'sim'
    }
},
'encode': {
    'job': {
        'administrador': 0,
        'empreendedor': 2,
        'trabalhador manual': 1,
        'gerência': 4,
        'autônomo': 6,
        'aposentado': 5,
        'empregada doméstica': 3,
        'estudante': 8,
        'serviços': 7,
        'técnico': 9,
        'desempregado': 10,

    },
    'marital': {
        'divorciado': 0,
        'solteiro': 2,
        'casado': 1,

    },
    'education': {
        'fundamental 4 anos': 0,
        'fundamental 6 anos': 1,
        'fundamental 9 anos': 2,
        'ensino médio': 3,
        'analfabeto': 4,
        'curso profissionalizante': 5,
        'ensino superior': 6,

    },
    'default': {
        'não': 0,
        'sim': 1,

    },
    'housing': {
        'não': 0,
        'sim': 1,

    },
    'loan': {
        'não': 0,
        'sim': 1,

    },
    'contact': {
        'celular': 0,
        'telefone': 1
    },
    'month': {
        'abr': 0,
        'ago': 1,
        'dez': 2,
        'jul': 3,
        'jun': 4,
        'mar': 5,
        'mai': 6,
        'nov': 7,
        'out': 8,
        'set': 9
    },
    'day_of_week': {
        'sex': 0,
        'seg': 1,
        'qui': 2,
        'ter': 3,
        'qua': 4
    },
    'poutcome': {
        'fracasso': 0,
        'sucesso': 1,

    },
    'y': {
        'não': 0,
        'sim': 1
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
        
        models = {
            "Gaussian Naive Bayes": "GaussianNB_model.pkl",
            "K-Nearest Neighbors (KNN)": "KNN_model.pkl",
            "Logistic Regression": "LogisticRegression_model.pkl",
            "Random Forest": "RandomForest_model.pkl",
            "Support Vector Machine (SVM)": "SVM_model.pkl",
            "XGBoost": "XGBoost_model.pkl"
        }

        selected_model_name = st.selectbox("Escolha um modelo de ML", list(models.keys()))


        # Descrição e intervalos para cada entrada em português
        user_data = {}
        user_data['age'] = st.number_input("Idade", min_value=18, max_value=100, help="Digite sua idade (18-100 anos).")

        job_options = list(category_mappings['decode']['job'].values())
        user_data['job'] = st.selectbox("Profissão", options=job_options, help="Selecione sua profissão da lista.")

        marital_options = list(category_mappings['decode']['marital'].values())
        user_data['marital'] = st.selectbox("Estado Civil", options=marital_options, help="Selecione seu estado civil.")

        education_options = list(category_mappings['decode']['education'].values())
        user_data['education'] = st.selectbox("Educação", options=education_options, help="Selecione seu nível de educação.")

        default_options = list(category_mappings['decode']['default'].values())
        user_data['default'] = st.selectbox("Inadimplência", options=default_options, help="Você possui inadimplência? (sim/não)")

        housing_options = list(category_mappings['decode']['housing'].values())
        user_data['housing'] = st.selectbox("Moradia", options=housing_options, help="Você possui moradia própria? (sim/não)")

        loan_options = list(category_mappings['decode']['loan'].values())
        user_data['loan'] = st.selectbox("Empréstimos", options=loan_options, help="Você possui empréstimos pessoais? (sim/não)")

        contact_options = list(category_mappings['decode']['contact'].values())
        user_data['contact'] = st.selectbox("Tipo de Contato", options=contact_options, help="Qual o tipo de contato preferencial? (celular/telefone)")

        month_options = list(category_mappings['decode']['month'].values())
        user_data['month'] = st.selectbox("Mês", options=month_options, help="Selecione o mês atual.")

        day_of_week_options = list(category_mappings['decode']['day_of_week'].values())
        user_data['day_of_week'] = st.selectbox("Dia da Semana", options=day_of_week_options, help="Selecione o dia da semana.")

        user_data['duration'] = st.number_input("Duração do Último Contato (em segundos)", min_value=0, help="Digite a duração, em segundos, do último contato.")

        user_data['campaign'] = st.number_input("Número de Contatos Nesta Campanha", min_value=0, help="Digite o número de contatos realizados nesta campanha.")

        user_data['pdays'] = st.number_input("Dias Após Último Contato da Campanha Anterior", min_value=0, help="Digite o número de dias desde o último contato da campanha anterior.")

        user_data['previous'] = st.number_input("Contatos Antes Desta Campanha", min_value=0, help="Digite o número de contatos realizados antes desta campanha.")

        poutcome_options = list(category_mappings['decode']['poutcome'].values())
        user_data['poutcome'] = st.selectbox("Resultado da Campanha Anterior", options=poutcome_options, help="Selecione o resultado da campanha anterior.")

        user_data['emp.var.rate'] = st.number_input("Taxa de Variação do Emprego", step=0.1, help="Digite a taxa de variação do emprego.")

        user_data['cons.price.idx'] = st.number_input("Índice de Preços ao Consumidor", step=0.1, help="Digite o índice de preços ao consumidor.")

        user_data['cons.conf.idx'] = st.number_input("Índice de Confiança do Consumidor", step=0.1, help="Digite o índice de confiança do consumidor.")

        user_data['euribor3m'] = st.number_input("Taxa Euribor de 3 Meses", step=0.1, help="Digite a taxa Euribor de 3 meses.")

        user_data['nr.employed'] = st.number_input("Número de Empregados", step=1.0, help="Digite o número de empregados.")

        # # Botão para codificar e mostrar dados
        # if st.button("Codificar e Mostrar Dados"):
        #     try:
        #         encoded_data = encode_data(user_data, category_mappings)
        #         st.write(encoded_data)
        #     except Exception as e:
        #         st.error(f"Ocorreu um erro ao processar os dados: {e}")

            
        if st.button("Prever"):
            try:
                encoded_data = encode_data(user_data, category_mappings)
                model = load_model(models[selected_model_name])
                prediction = model.predict([encoded_data])

                if prediction[0] == 0:
                    st.success("Previsão: Não")

                elif prediction[0] == 1:
                    st.success("Previsão: Sim")

                else:
                    st.error("Ocorreu um erro ao realizar a previsão.")
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")



if __name__ == "__main__":
    main()

