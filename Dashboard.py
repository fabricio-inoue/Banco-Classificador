import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

st.set_page_config(page_title='Dashboard_Bank', layout='centered')

df = pd.read_csv('bank-additional-full.csv', sep=';')

selected_page = st.sidebar.selectbox("Selecione a página", ["Descrição do Projeto", "Dataframe", "Identificando valores NaN", "Gráficos", "Modelo de Random Forest Treinado"])
if selected_page == "Descrição do Projeto":
    text_content = """
    ## Descrição do Projeto
    Estamos lidando com dados de marketing uma instituição de banco portuguesa, mais especificamente, ligações efetuadas entre Maio de 2008 e Novembro de 2010. Estes dados serão utilizados para que ligações e ofertas de marketing possam ter alvos melhores, de modo em que diminua o número de chamadas que não fecharão um negócio.
    Utilizando Machine Learning, faremos uma análise das chamadas efetuadas e quais conseguiram fechar um negócio, para otimizarmos as chamadas e os clientes escolhidos, assim aumentando a chance de sucesso do banco.
    """

    # Display the text content using Streamlit
    st.markdown(text_content)

elif selected_page == "Dataframe":
    st.write('## Dataframe sobre a campanha')
    df
    text_content = """
    ## Variáveis Bancárias

    **age (Idade):** Variável numérica que representa a idade do cliente.

    **job (Emprego):** Variável categórica que descreve o emprego do cliente, com categorias como 'admin.', 'blue-collar', 'entrepreneur', etc.

    **marital (Status Conjugal):** Variável categórica que indica o estado conjugal do cliente, com categorias como 'divorced', 'married', 'single', etc. (Nota: 'divorced' representa divorciado ou viúvo).

    **education (Escolaridade):** Variável categórica que descreve a escolaridade do cliente, com categorias como 'basic.4y', 'basic.6y', 'basic.9y', etc.

    **default (Inadimplente):** Variável categórica que indica se o cliente é inadimplente, com categorias 'no', 'yes' e 'unknown'.

    **housing (Financiamento Imobiliário):** Variável categórica que descreve se o cliente possui financiamento imobiliário, com categorias 'no', 'yes' e 'unknown'.

    **loan (Empréstimo Pessoal):** Variável categórica que descreve se o cliente possui empréstimo pessoal, com categorias 'no', 'yes' e 'unknown'.


    ## Variáveis Campanha

    **contact (Canal de Contato):** Variável categórica que indica o canal de contato utilizado, com categorias 'cellular' e 'telephone'.

    **month (Mês de Contato):** Variável categórica que descreve o mês em que o cliente foi contatado, com valores como 'jan', 'feb', 'mar', etc.

    **day_of_week (Dia da Semana):** Variável categórica que indica o dia da semana em que o cliente foi contatado, com valores como 'mon', 'tue', 'wed', etc.

    **duration(s) (Duração em Segundos):** Variável numérica que representa a duração do contato em segundos.

    **campaign (Número de Contatos):** Variável numérica que indica o número de contatos realizados durante esta campanha para este cliente.

    **pdays (Dias desde o Último Contato):** Variável numérica que indica o número de dias desde o último contato da campanha anterior (999 significa que o cliente não foi contatado anteriormente).

    **previous (Contatos Anteriores):** Variável numérica que representa o número de contatos realizados antes desta campanha para este cliente.

    **poutcome (Resultado da Campanha Anterior):** Variável categórica que descreve o resultado da campanha de marketing anterior, com categorias como 'fracasso', 'inexistente' e 'sucesso'.


    ## Variáveis Contexto Socioeconômicas

    **emp.var.rate (Taxa de Variação de Emprego):** Variável numérica que representa a taxa de variação do emprego.

    **cons.price.idx (Índice de Preços ao Consumidor):** Variável numérica que representa o índice de preços ao consumidor.

    **cons.conf.idx (Índice de Confiança do Consumidor):** Variável numérica que representa o índice de confiança do consumidor.

    **euribor3m (Taxa de Juros a 3 Meses):** Variável numérica que representa a taxa de juros média dos empréstimos interbancários a 3 meses.

    **n°.empregados (Número de Empregados):** Variável numérica que indica o número de empregados.

    ## Target

    **y (O Cliente Aderiu ao Produto?):** Variável binária que indica se o cliente aderiu ao produto, com valores 'yes' (sim) e 'no' (não).
    """

    # Display the text content using Streamlit
    st.markdown(text_content)

elif selected_page == 'Identificando valores NaN':
    search_values = [np.nan, 'unknown', 'nonexistent']
    for value in search_values:
        st.subheader(f'Histograma para "{value}"')
        
        # Initialize a count for each column
        counts = []
        
        # Iterate through columns
        for column in df.columns:
            # Count occurrences of the value in the column
            count = df[column].apply(lambda x: x == value).sum()
            counts.append(count)
        
        # Create a bar plot for the counts
        plt.figure(figsize=(8, 4))
        plt.title(f'Histograma para "{value}"')
        sns.barplot(x=counts, y=df.columns)
        plt.xlabel('Count')
        plt.ylabel('Columns')
        
        # Display the plot in Streamlit
        st.pyplot(plt)
        text_content = """
        Com os histogramas, conseguimos ver que apesar de não termos nenhum valor "NaN", temos outros termos que também representam a 
        ausência de um valor, mostrando que as nomenclaturas não estão padronizadas, dificultando o manuseio dos dados
    """

    # Display the text content using Streamlit
    st.markdown(text_content)

elif selected_page == "Gráficos":
    chart_container = st.container()

    with chart_container:
        st.write('#### Gráfico de barras demonstra uma distribuição desequilibrada dos dados, concentrados na faixa dos 30 aos 40 anos.')
        col1, col2 = st.columns(2)
        fig_hist = px.histogram(df, x='age', title='Histograma de Idade')
        col1.plotly_chart(fig_hist)

    with chart_container:
        st.write('#### Gráfico de pizza demonstra que a maioria dos clientes nesse dataset são casados, com uma parte considerável de solteiros e divorciados.')
        col3, col4 = st.columns(2)
        df['marital_counts'] = df['marital'].value_counts()
        fig_marital = px.pie(df, names='marital', title='Distribuição Marital')
        col3.plotly_chart(fig_marital)

    with chart_container:
        st.write('#### Gráfico de pizza demonstra que os clientes predominantes nesse dataset são estudantes de nível básico, com número significativos de universitários e de ensino médio.')
        col3, col4 = st.columns(2)
        df['education'] = df['education'].replace(['basic.9y', 'basic.6y', 'basic.4y'], 'basic')
        df['education_counts'] = df['education'].value_counts()
        fig_marital = px.pie(df, names='education', title='Distribuição da educação')
        col3.plotly_chart(fig_marital)

elif selected_page == "Modelo de Random Forest Treinado":
    # Split the data and train the model
    X = df.drop(columns=['y'])
    y = df['y']
    X = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Calculate accuracy
    accuracy = rf_model.score(X_test, y_test)
    st.write(f'Accuracy on the test set: {accuracy:.2f}')

    # Plot feature importance
    feature_importance = rf_model.feature_importances_
    sorted_idx = feature_importance.argsort()

    fig, ax = plt.subplots(figsize=(15, 9))
    ax.barh(range(X.shape[1]), feature_importance[sorted_idx])
    ax.set_yticks(range(X.shape[1]))
    ax.set_yticklabels(X.columns[sorted_idx])
    ax.set_xlabel('Feature Importance')
    ax.set_title('Random Forest Feature Importance')
    # Show the plot using st.pyplot
    st.pyplot(fig)

    # Split the data and train the model
    X = df.drop(columns=['y', 'duration'])
    y = df['y']
    X = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Calculate accuracy
    accuracy = rf_model.score(X_test, y_test)
    st.write(f'Accuracy on the test set: {accuracy:.2f}')

    # Plot feature importance
    feature_importance = rf_model.feature_importances_
    sorted_idx = feature_importance.argsort()

    fig, ax = plt.subplots(figsize=(15, 9))
    ax.barh(range(X.shape[1]), feature_importance[sorted_idx])
    ax.set_yticks(range(X.shape[1]))
    ax.set_yticklabels(X.columns[sorted_idx])
    ax.set_xlabel('Feature Importance')
    ax.set_title('Random Forest Feature Importance')
    # Show the plot using st.pyplot
    st.pyplot(fig)


