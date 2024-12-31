# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from datetime import datetime

# # Configuração inicial da aplicação
# st.title("Sistema de Gestão Financeira Pessoal")
# st.sidebar.title("Opções")
# st.markdown("Gerencie suas receitas e despesas de forma simples e visualize seus dados com gráficos.")

# # Inicializar ou carregar os dados
# if "dados" not in st.session_state:
#     st.session_state["dados"] = pd.DataFrame(columns=["Data", "Tipo", "Categoria", "Valor"])

# # Função para adicionar receita ou despesa
# def adicionar_dado(tipo, categoria, valor):
#     nova_linha = {"Data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Tipo": tipo, "Categoria": categoria, "Valor": float(valor)}
#     st.session_state["dados"] = pd.concat([st.session_state["dados"], pd.DataFrame([nova_linha])], ignore_index=True)

# # Sidebar para entrada de dados
# st.sidebar.header("Adicionar Dados")

# # Seleção das categorias com botões
# if st.sidebar.radio("Tipo de Receita", ["Receita", "Despesa"]) == "Receita":
#     categoria_receita = st.sidebar.radio("Escolha a Categoria de Receita:", ["Estágio", "Bolsa", "Outros"])
#     valor_receita = st.sidebar.text_input("Valor da Receita (R$):")
    
#     # Verificar se o valor é válido para receitas
#     if st.sidebar.button("Adicionar Receita"):
#         try:
#             valor_float = float(valor_receita)
#             if valor_float > 0:  # Verifica se o valor é positivo
#                 if categoria_receita:
#                     adicionar_dado("Receita", categoria_receita, valor_receita)
#                     st.sidebar.success("Receita adicionada com sucesso!")
#                 else:
#                     st.sidebar.error("Por favor, selecione uma categoria de receita.")
#             else:
#                 st.sidebar.error("Por favor, insira um valor positivo para a receita.")
#         except ValueError:
#             st.sidebar.error("Por favor, insira um valor numérico válido.")
# else:
#     categoria_despesa = st.sidebar.radio("Escolha a Categoria de Despesa:", ["Alimentação", "Aluguel", "Transporte", "Lazer", "Academia", "Outros"])
#     valor_despesa = st.sidebar.text_input("Valor da Despesa (R$):")
    
#     # Verificar se o valor é válido para despesas
#     if st.sidebar.button("Adicionar Despesa"):
#         try:
#             valor_float = float(valor_despesa)
#             if valor_float > 0:  # Verifica se o valor é positivo
#                 if categoria_despesa:
#                     adicionar_dado("Despesa", categoria_despesa, valor_despesa)
#                     st.sidebar.success("Despesa adicionada com sucesso!")
#                 else:
#                     st.sidebar.error("Por favor, selecione uma categoria de despesa.")
#             else:
#                 st.sidebar.error("Por favor, insira um valor positivo para a despesa.")
#         except ValueError:
#             st.sidebar.error("Por favor, insira um valor numérico válido.")

# # Exibir tabela com os dados
# st.header("Tabela de Dados")
# st.dataframe(st.session_state["dados"])

# # Análise dos dados
# receitas = st.session_state["dados"][st.session_state["dados"]["Tipo"] == "Receita"]["Valor"].sum()
# despesas = st.session_state["dados"][st.session_state["dados"]["Tipo"] == "Despesa"]["Valor"].sum()
# diferenca = receitas - despesas

# st.write(f"**Receitas Totais:** R$ {receitas:.2f}")
# st.write(f"**Despesas Totais:** R$ {despesas:.2f}")
# st.write(f"**Saldo Final (Receitas - Despesas):** R$ {diferenca:.2f}")

# # Opção de visualização de gráficos
# st.header("Gráficos")
# tipo_grafico = st.selectbox("Escolha o tipo de gráfico:", ["Linha (Curva S)", "Barras (Montante Total)"])

# # Definir orçamento
# orçamento_receitas = st.sidebar.number_input("Orçamento para Receitas (R$):", min_value=0.0, format="%.2f")
# orçamento_despesas = st.sidebar.number_input("Orçamento para Despesas (R$):", min_value=0.0, format="%.2f")

# st.write(f"**Orçamento de Receitas:** R$ {orçamento_receitas:.2f}")
# st.write(f"**Orçamento de Despesas:** R$ {orçamento_despesas:.2f}")

# # Gráfico de Linha (Curva S) com meta de orçamento
# if tipo_grafico == "Linha (Curva S)":
#     if not st.session_state["dados"].empty:
#         fig, ax = plt.subplots()
#         dados_acumulados = st.session_state["dados"].copy()
#         dados_acumulados["Acumulado Receita"] = dados_acumulados[dados_acumulados["Tipo"] == "Receita"]["Valor"].cumsum()
#         dados_acumulados["Acumulado Despesa"] = dados_acumulados[dados_acumulados["Tipo"] == "Despesa"]["Valor"].cumsum()

#         ax.plot(
#             dados_acumulados["Data"],
#             dados_acumulados["Acumulado Receita"].fillna(method="ffill"),
#             label="Receitas Acumuladas",
#             color="green",
#         )
#         ax.plot(
#             dados_acumulados["Data"],
#             dados_acumulados["Acumulado Despesa"].fillna(method="ffill"),
#             label="Despesas Acumuladas",
#             color="red",
#         )
#         # Adicionando linha de meta de orçamento
#         if orçamento_receitas > 0:
#             ax.axhline(y=orçamento_receitas, color='darkgreen', linestyle='--', label="Meta de Receita")
#         if orçamento_despesas > 0:
#             ax.axhline(y=orçamento_despesas, color='darkred', linestyle='--', label="Meta de Despesa")

#         ax.set_title("Gráfico de Linha (Curva S)")
#         ax.set_xlabel("Data")
#         ax.set_ylabel("Valor (R$)")
#         ax.legend()
#         plt.xticks(rotation=45)
#         st.pyplot(fig)
#     else:
#         st.warning("Não há dados suficientes para gerar o gráfico.")

# # Gráfico de Barras (Montante Total) com meta de orçamento
# elif tipo_grafico == "Barras (Montante Total)":
#     if not st.session_state["dados"].empty:
#         fig, ax = plt.subplots()
#         categorias = ["Receitas", "Despesas"]
#         valores = [receitas, despesas]
#         barras = ax.bar(categorias, valores, color=["green", "red"])
#         ax.set_title("Gráfico de Barras (Montante Total)")
#         ax.set_ylabel("Valor (R$)")

#         # Adicionando rótulos de dados nas barras
#         for barra in barras:
#             altura = barra.get_height()  # Obtém o valor da barra
#             ax.text(
#                 barra.get_x() + barra.get_width() / 2,  # Posição horizontal
#                 altura + 3,  # Posição vertical (um pouco acima da barra)
#                 f"R$ {altura:.2f}",  # Formatação do valor
#                 ha='center',  # Alinha o texto no centro
#                 va='bottom'  # Posiciona o texto acima da barra
#             )

#         # Adicionando linha de meta de orçamento
#         if orçamento_receitas > 0:
#             ax.axhline(y=orçamento_receitas, color='darkgreen', linestyle='--', label="Meta de Receita")
#         if orçamento_despesas > 0:
#             ax.axhline(y=orçamento_despesas, color='darkred', linestyle='--', label="Meta de Despesa")

#         st.pyplot(fig)
#     else:
#         st.warning("Não há dados suficientes para gerar o gráfico.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Configuração inicial da aplicação (modo escuro)
st.set_page_config(page_title="Sistema de Gestão Financeira Pessoal", page_icon="💰", layout="wide", initial_sidebar_state="expanded")

st.title("Sistema de Gestão Financeira Pessoal")
st.sidebar.title("Opções")
st.markdown("Gerencie suas receitas e despesas de forma simples e visualize seus dados com gráficos.")

# Alterar o tema para "dark" manualmente
st.markdown("""
    <style>
        body {
            background-color: #2e2e2e;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: #333333;
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .stTextInput>div>input {
            background-color: #444444;
            color: white;
        }
        .stSelectbox>div>div>input {
            background-color: #444444;
            color: white;
        }
        .stDataFrame {
            background-color: #444444;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Inicializar ou carregar os dados
if "dados" not in st.session_state:
    st.session_state["dados"] = pd.DataFrame(columns=["Data", "Tipo", "Categoria", "Valor"])

# Função para adicionar receita ou despesa
def adicionar_dado(tipo, categoria, valor):
    nova_linha = {"Data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Tipo": tipo, "Categoria": categoria, "Valor": float(valor)}
    st.session_state["dados"] = pd.concat([st.session_state["dados"], pd.DataFrame([nova_linha])], ignore_index=True)

# Sidebar para entrada de dados
st.sidebar.header("Adicionar Dados")

# Seleção das categorias com botões
if st.sidebar.radio("Tipo de Receita", ["Receita", "Despesa"]) == "Receita":
    categoria_receita = st.sidebar.radio("Escolha a Categoria de Receita:", ["Estágio", "Bolsa", "Outros"])
    valor_receita = st.sidebar.text_input("Valor da Receita (R$):")
    
    # Verificar se o valor é válido para receitas
    if st.sidebar.button("Adicionar Receita"):
        try:
            valor_float = float(valor_receita)
            if valor_float > 0:  # Verifica se o valor é positivo
                if categoria_receita:
                    adicionar_dado("Receita", categoria_receita, valor_receita)
                    st.sidebar.success("Receita adicionada com sucesso!")
                else:
                    st.sidebar.error("Por favor, selecione uma categoria de receita.")
            else:
                st.sidebar.error("Por favor, insira um valor positivo para a receita.")
        except ValueError:
            st.sidebar.error("Por favor, insira um valor numérico válido.")
else:
    categoria_despesa = st.sidebar.radio("Escolha a Categoria de Despesa:", ["Alimentação", "Aluguel", "Transporte", "Lazer", "Academia", "Outros"])
    valor_despesa = st.sidebar.text_input("Valor da Despesa (R$):")
    
    # Verificar se o valor é válido para despesas
    if st.sidebar.button("Adicionar Despesa"):
        try:
            valor_float = float(valor_despesa)
            if valor_float > 0:  # Verifica se o valor é positivo
                if categoria_despesa:
                    adicionar_dado("Despesa", categoria_despesa, valor_despesa)
                    st.sidebar.success("Despesa adicionada com sucesso!")
                else:
                    st.sidebar.error("Por favor, selecione uma categoria de despesa.")
            else:
                st.sidebar.error("Por favor, insira um valor positivo para a despesa.")
        except ValueError:
            st.sidebar.error("Por favor, insira um valor numérico válido.")

# Exibir tabela com os dados
st.header("Tabela de Dados")
st.dataframe(st.session_state["dados"])

# Análise dos dados
receitas = st.session_state["dados"][st.session_state["dados"]["Tipo"] == "Receita"]["Valor"].sum()
despesas = st.session_state["dados"][st.session_state["dados"]["Tipo"] == "Despesa"]["Valor"].sum()
diferenca = receitas - despesas

st.write(f"**Receitas Totais:** R$ {receitas:.2f}")
st.write(f"**Despesas Totais:** R$ {despesas:.2f}")
st.write(f"**Saldo Final (Receitas - Despesas):** R$ {diferenca:.2f}")

# Opção de visualização de gráficos
st.header("Gráficos")
tipo_grafico = st.selectbox("Escolha o tipo de gráfico:", ["Linha (Curva S)", "Barras (Montante Total)"])

# Definir orçamento
orçamento_receitas = st.sidebar.number_input("Orçamento para Receitas (R$):", min_value=0.0, format="%.2f")
orçamento_despesas = st.sidebar.number_input("Orçamento para Despesas (R$):", min_value=0.0, format="%.2f")

st.write(f"**Orçamento de Receitas:** R$ {orçamento_receitas:.2f}")
st.write(f"**Orçamento de Despesas:** R$ {orçamento_despesas:.2f}")

# Gráfico de Linha (Curva S) com meta de orçamento
if tipo_grafico == "Linha (Curva S)":
    if not st.session_state["dados"].empty:
        fig, ax = plt.subplots()
        dados_acumulados = st.session_state["dados"].copy()
        dados_acumulados["Acumulado Receita"] = dados_acumulados[dados_acumulados["Tipo"] == "Receita"]["Valor"].cumsum()
        dados_acumulados["Acumulado Despesa"] = dados_acumulados[dados_acumulados["Tipo"] == "Despesa"]["Valor"].cumsum()

        ax.plot(
            dados_acumulados["Data"],
            dados_acumulados["Acumulado Receita"].fillna(method="ffill"),
            label="Receitas Acumuladas",
            color="green",
        )
        ax.plot(
            dados_acumulados["Data"],
            dados_acumulados["Acumulado Despesa"].fillna(method="ffill"),
            label="Despesas Acumuladas",
            color="red",
        )
        # Adicionando linha de meta de orçamento
        if orçamento_receitas > 0:
            ax.axhline(y=orçamento_receitas, color='darkgreen', linestyle='--', label="Meta de Receita")
        if orçamento_despesas > 0:
            ax.axhline(y=orçamento_despesas, color='darkred', linestyle='--', label="Meta de Despesa")

        ax.set_title("Gráfico de Linha (Curva S)")
        ax.set_xlabel("Data")
        ax.set_ylabel("Valor (R$)")
        ax.legend()
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("Não há dados suficientes para gerar o gráfico.")

# Gráfico de Barras (Montante Total) com meta de orçamento
elif tipo_grafico == "Barras (Montante Total)":
    if not st.session_state["dados"].empty:
        fig, ax = plt.subplots()
        categorias = ["Receitas", "Despesas"]
        valores = [receitas, despesas]
        barras = ax.bar(categorias, valores, color=["green", "red"])
        ax.set_title("Gráfico de Barras (Montante Total)")
        ax.set_ylabel("Valor (R$)")

        # Adicionando rótulos de dados nas barras
        for barra in barras:
            altura = barra.get_height()  # Obtém o valor da barra
            ax.text(
                barra.get_x() + barra.get_width() / 2,  # Posição horizontal
                altura + 3,  # Posição vertical (um pouco acima da barra)
                f"R$ {altura:.2f}",  # Formatação do valor
                ha='center',  # Alinha o texto no centro
                va='bottom'  # Posiciona o texto acima da barra
            )

        # Adicionando linha de meta de orçamento
        if orçamento_receitas > 0:
            ax.axhline(y=orçamento_receitas, color='darkgreen', linestyle='--', label="Meta de Receita")
        if orçamento_despesas > 0:
            ax.axhline(y=orçamento_despesas, color='darkred', linestyle='--', label="Meta de Despesa")

        st.pyplot(fig)
    else:
        st.warning("Não há dados suficientes para gerar o gráfico.")
