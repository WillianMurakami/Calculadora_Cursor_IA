import streamlit as st
import math

# Configuração da página
st.set_page_config(
    page_title="Calculadora Python v1.0",
    page_icon="🧮",
    layout="centered"
)

# Estilo CSS personalizado
st.markdown("""
    <style>
    .sidebar-text {
        font-size: 0.8em;
        color: #888;
        margin-top: 20px;
        text-align: center;
    }
    .main-title {
        text-align: center;
        color: #1E88E5;
        margin-bottom: 30px;
    }
    .operation-section {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Navegação")
    page = st.radio(
        "Ir para:",
        ["Calculadora", "Sobre o Projeto", "Documentação"]
    )
    
    # Link do desenvolvedor
    st.markdown(
        '<div class="sidebar-text">Projeto desenvolvido por '
        '<a href="https://www.linkedin.com/in/willian-murakami/" target="_blank">Willian Murakami</a></div>',
        unsafe_allow_html=True
    )

if page == "Calculadora":
    st.markdown('<h1 class="main-title">🧮 Calculadora Python v1.0</h1>', unsafe_allow_html=True)
    
    operacao = st.selectbox(
        "Escolha a operação:",
        ["Soma", "Subtração", "Multiplicação", "Divisão", "Potenciação", "Raiz Quadrada"]
    )
    
    if operacao != "Raiz Quadrada":
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Primeiro número", value=0.0)
        with col2:
            num2 = st.number_input("Segundo número", value=0.0)
    else:
        num1 = st.number_input("Digite o número", value=0.0)
    
    if st.button("Calcular"):
        try:
            if operacao == "Soma":
                resultado = num1 + num2
                st.success(f"{num1} + {num2} = {resultado}")
            elif operacao == "Subtração":
                resultado = num1 - num2
                st.success(f"{num1} - {num2} = {resultado}")
            elif operacao == "Multiplicação":
                resultado = num1 * num2
                st.success(f"{num1} × {num2} = {resultado}")
            elif operacao == "Divisão":
                if num2 == 0:
                    st.error("Erro: Divisão por zero!")
                else:
                    resultado = num1 / num2
                    st.success(f"{num1} ÷ {num2} = {resultado}")
            elif operacao == "Potenciação":
                resultado = num1 ** num2
                st.success(f"{num1} ^ {num2} = {resultado}")
            elif operacao == "Raiz Quadrada":
                if num1 < 0:
                    st.error("Erro: Não é possível calcular raiz quadrada de número negativo!")
                else:
                    resultado = math.sqrt(num1)
                    st.success(f"√{num1} = {resultado}")
        except Exception as e:
            st.error(f"Erro: {str(e)}")

elif page == "Sobre o Projeto":
    st.markdown('<h1 class="main-title">📖 Sobre o Projeto</h1>', unsafe_allow_html=True)
    
    st.write("""
    ### A Jornada de Aprendizado com Cursor IA
    
    Este projeto nasceu de uma ideia simples: transformar um dos exercícios mais básicos e tradicionais 
    no aprendizado de programação - a calculadora - em algo mais robusto e profissional utilizando 
    ferramentas modernas de desenvolvimento.
    
    #### 🎯 Objetivo
    O objetivo principal foi explorar as capacidades da IDE Cursor IA, demonstrando como uma ferramenta
    de IA pode potencializar o desenvolvimento de software, mesmo em projetos aparentemente simples.
    
    #### 🛠️ Evolução do Projeto
    1. **Versão Inicial**: Começamos com uma calculadora básica em linha de comando
    2. **Transformação**: Utilizamos o Cursor IA para evoluir o projeto para uma aplicação web
    3. **Melhorias**: Adicionamos interface gráfica, tratamento de erros e documentação
    4. **Deploy**: Disponibilizamos a aplicação na nuvem através do Streamlit Cloud
    
    #### 💡 Aprendizados
    - Integração de IA no processo de desenvolvimento
    - Boas práticas de programação
    - Desenvolvimento de interfaces web com Streamlit
    - Processo de deploy e disponibilização de aplicações
    """)

elif page == "Documentação":
    st.markdown('<h1 class="main-title">📚 Documentação</h1>', unsafe_allow_html=True)
    
    st.write("""
    ### Exemplos de Prompts Utilizados
    
    1. **Criação da Base**:
    ```
    "Crie uma calculadora em Python com operações básicas e interface de linha de comando"
    ```
    
    2. **Transformação para Streamlit**:
    ```
    "Transforme a calculadora em uma aplicação web usando Streamlit, mantendo todas as funcionalidades"
    ```
    
    3. **Melhorias Visuais**:
    ```
    "Adicione uma barra lateral para navegação e melhore o layout visual da aplicação"
    ```
    
    ### Deploy no Streamlit Cloud
    
    1. Crie uma conta no Streamlit Cloud
    2. Conecte seu repositório GitHub
    3. Selecione o repositório da calculadora
    4. Configure as variáveis de ambiente (se necessário)
    5. Deploy!
    
    ### Estrutura do Projeto
    ```
    📁 Calculadora_Cursor_IA/
    ├── 📄 app.py
    ├── 📄 requirements.txt
    ├── 📄 README.md
    └── 📄 .gitignore
    ```
    """)

    st.info("""
    **Nota**: Este projeto está disponível no GitHub e pode ser usado como referência para 
    aprender sobre desenvolvimento com Cursor IA e Streamlit.
    """) 