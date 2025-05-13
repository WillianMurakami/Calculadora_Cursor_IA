import streamlit as st
import math
import pandas as pd
from PIL import Image

# Configuração da página
st.set_page_config(
    page_title="Calculadora Python v1.0",
    page_icon="🧮",
    layout="centered",  # Mudado para centered conforme solicitado
    initial_sidebar_state="expanded"
)

# Função para aplicar estilo CSS personalizado
def local_css():
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            margin-top: 1rem;
        }
        .operation-card {
            padding: 1.5rem;
            border-radius: 10px;
            background-color: #f0f2f6;
            margin-bottom: 1rem;
        }
        .result-card {
            padding: 2rem;
            border-radius: 10px;
            background-color: #e6ffe6;
            margin-top: 2rem;
            text-align: center;
        }
        .documentation {
            padding: 1.5rem;
            border-radius: 10px;
            background-color: #f8f9fa;
            margin-bottom: 1rem;
        }
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
        </style>
    """, unsafe_allow_html=True)

# Funções matemáticas
def soma(a, b): return a + b
def subtracao(a, b): return a - b
def multiplicacao(a, b): return a * b
def divisao(a, b): return a / b if b != 0 else "Erro: Divisão por zero!"
def potencia(a, b): return a ** b
def raiz_quadrada(a): return math.sqrt(a) if a >= 0 else "Erro: Raiz de número negativo!"

# Função principal da calculadora
def calculadora():
    # Sidebar com navegação e créditos
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
        
        # Seleção da operação
        operacao = st.selectbox(
            "Escolha a operação:",
            ["Soma (+)", "Subtração (-)", "Multiplicação (×)", "Divisão (÷)", "Potenciação (^)", "Raiz Quadrada (√)"]
        )
        
        # Input dos números
        col1, col2 = st.columns(2)
        
        with col1:
            if operacao != "Raiz Quadrada (√)":
                num1 = st.number_input("Primeiro número", value=0.0)
            else:
                num1 = st.number_input("Número", min_value=0.0, value=0.0)
                
        with col2:
            if operacao != "Raiz Quadrada (√)":
                num2 = st.number_input("Segundo número", value=0.0)
        
        # Cálculo e exibição do resultado
        if st.button("Calcular", use_container_width=True):
            with st.container():
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                
                if operacao == "Soma (+)":
                    resultado = soma(num1, num2)
                    st.markdown(f"### {num1} + {num2} = {resultado}")
                elif operacao == "Subtração (-)":
                    resultado = subtracao(num1, num2)
                    st.markdown(f"### {num1} - {num2} = {resultado}")
                elif operacao == "Multiplicação (×)":
                    resultado = multiplicacao(num1, num2)
                    st.markdown(f"### {num1} × {num2} = {resultado}")
                elif operacao == "Divisão (÷)":
                    resultado = divisao(num1, num2)
                    st.markdown(f"### {num1} ÷ {num2} = {resultado}")
                elif operacao == "Potenciação (^)":
                    resultado = potencia(num1, num2)
                    st.markdown(f"### {num1} ^ {num2} = {resultado}")
                else:  # Raiz Quadrada
                    resultado = raiz_quadrada(num1)
                    st.markdown(f"### √{num1} = {resultado}")
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    elif page == "Sobre o Projeto":
        st.markdown('<h1 class="main-title">📖 Sobre o Projeto</h1>', unsafe_allow_html=True)
        
        st.write("""
        ### A Jornada de Aprendizado com Cursor IA
        
        Este projeto nasceu como uma "brincadeira" durante meu processo de aprendizado da Cursor IA, 
        uma nova e poderosa IDE que integra inteligência artificial ao desenvolvimento de software. 
        A ideia era pegar um dos exercícios mais básicos e tradicionais no aprendizado de programação 
        - a calculadora - e ver até onde poderíamos ir com o auxílio desta ferramenta incrível.
        
        #### 🎯 A Experiência
        O que começou como uma simples calculadora de linha de comando se transformou em uma aplicação 
        web moderna e profissional, demonstrando o poder da integração entre criatividade humana e 
        inteligência artificial.
        
        #### 🛠️ Evolução do Projeto
        1. **Versão Inicial**: Uma calculadora básica em linha de comando
        2. **Exploração do Cursor IA**: Descoberta das capacidades da ferramenta
        3. **Transformação**: Evolução para uma aplicação web com Streamlit
        4. **Refinamento**: Adição de interface moderna e documentação detalhada
        5. **Deploy**: Disponibilização na nuvem através do Streamlit Cloud
        
        #### 💡 Aprendizados
        - Como potencializar o desenvolvimento usando IA
        - Transformação de conceitos básicos em produtos profissionais
        - Integração de diferentes tecnologias modernas
        - Processo completo de desenvolvimento e deploy
        """)
        
    elif page == "Documentação":
        st.markdown('<h1 class="main-title">📚 Documentação</h1>', unsafe_allow_html=True)
        
        st.write("""
        ### O Processo com Cursor IA
        
        Aqui está um registro detalhado de como o projeto evoluiu usando a Cursor IA:
        
        #### 1️⃣ Primeiro Prompt
        ```
        "Crie uma calculadora em Python com operações básicas e interface de linha de comando"
        ```
        Resultado: Obtive um código base funcional com operações matemáticas básicas.
        
        #### 2️⃣ Evolução para Web
        ```
        "Transforme esta calculadora em uma aplicação web moderna usando Streamlit, 
        mantendo todas as funcionalidades existentes"
        ```
        Resultado: A calculadora ganhou uma interface web básica com Streamlit.
        
        #### 3️⃣ Melhorias Visuais
        ```
        "Adicione uma barra lateral para navegação, melhore o layout visual e 
        inclua minha marca pessoal no projeto"
        ```
        Resultado: Interface moderna com navegação, documentação e branding pessoal.
        
        #### 4️⃣ Documentação e Deploy
        ```
        "Crie uma documentação detalhada do processo de desenvolvimento e 
        prepare o projeto para deploy no Streamlit Cloud"
        ```
        Resultado: Documentação completa e projeto pronto para deploy.
        
        ### 🚀 Deploy no Streamlit Cloud
        
        1. Repositório criado no GitHub
        2. Conta configurada no Streamlit Cloud
        3. Conexão estabelecida com o repositório
        4. Deploy realizado com sucesso
        
        ### 📁 Estrutura Final do Projeto
        ```
        Calculadora_Cursor_IA/
        ├── calculadora_app.py    # Aplicação principal
        ├── requirements.txt      # Dependências
        ├── README.md            # Documentação
        └── .gitignore           # Configuração Git
        ```
        """)

# Execução principal
def main():
    local_css()
    calculadora()

if __name__ == "__main__":
    main() 