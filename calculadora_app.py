import streamlit as st
import math
import pandas as pd
from PIL import Image

# Configuração da página
st.set_page_config(
    page_title="Calculadora Python v1.0",
    page_icon="🧮",
    layout="centered",
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
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
            background-color: transparent;
            border: 1px solid #e0e0e0;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #f0f2f6;
            transform: translateX(5px);
        }
        .stButton>button:active {
            background-color: #e6f3ff;
            border-right: 3px solid #1E88E5;
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
        .step-box {
            padding: 1rem;
            border-left: 3px solid #1E88E5;
            background-color: #f8f9fa;
            margin: 1rem 0;
        }
        .highlight-text {
            color: #1E88E5;
            font-weight: 500;
        }
        div[data-testid="stSidebarNav"] {
            margin-top: -1rem;
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
        
        # Criando uma variável de sessão para controlar a navegação se não existir
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "Calculadora"
        
        # Botões de navegação usando st.button
        if st.button("🧮 Calculadora", key="calc_btn", use_container_width=True):
            st.session_state.current_page = "Calculadora"
            st.experimental_rerun()
            
        if st.button("📖 Sobre o Projeto", key="sobre_btn", use_container_width=True):
            st.session_state.current_page = "Sobre"
            st.experimental_rerun()
        
        # Link do desenvolvedor
        st.markdown(
            '<div class="sidebar-text">Projeto desenvolvido por '
            '<a href="https://www.linkedin.com/in/willian-murakami/" target="_blank">Willian Murakami</a></div>',
            unsafe_allow_html=True
        )

    # Lógica de exibição baseada na página atual
    if st.session_state.current_page == "Calculadora":
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
    
    elif st.session_state.current_page == "Sobre":
        st.markdown('<h1 class="main-title">📖 Sobre o Projeto</h1>', unsafe_allow_html=True)
        
        st.write("""
        ### A Jornada de Aprendizado com Cursor IA
        
        Este projeto nasceu como uma "brincadeira" durante meu processo de aprendizado da 
        [**_Cursor IA_**](https://cursor.sh), uma nova e poderosa IDE que integra inteligência 
        artificial ao desenvolvimento de software. A ideia era pegar um dos exercícios mais básicos 
        e tradicionais no aprendizado de programação - a calculadora - e ver até onde poderíamos 
        ir com o auxílio desta ferramenta incrível.
        
        #### 🎯 A Experiência
        
        O que começou como uma simples calculadora de linha de comando se transformou em uma aplicação 
        web moderna e profissional, demonstrando o poder da integração entre criatividade humana e 
        inteligência artificial. Veja abaixo como foi essa evolução:
        """)
        
        # Primeiro Prompt
        st.markdown("""
        <div class="step-box">
        <h4>1️⃣ Versão Inicial</h4>
        <p><strong>Prompt utilizado:</strong></p>
        <code>"Crie uma calculadora em Python com operações básicas e interface de linha de comando"</code>
        <p><em>Resultado:</em> Desenvolvimento de uma calculadora funcional em terminal, implementando 
        operações matemáticas básicas com interface simples e intuitiva.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Segundo Prompt
        st.markdown("""
        <div class="step-box">
        <h4>2️⃣ Exploração do Cursor IA</h4>
        <p><strong>Prompt utilizado:</strong></p>
        <code>"Transforme esta calculadora em uma aplicação web moderna usando Streamlit, 
        mantendo todas as funcionalidades existentes"</code>
        <p><em>Resultado:</em> A calculadora ganhou uma interface web moderna, mantendo todas as 
        funcionalidades originais e adicionando novos recursos visuais.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Terceiro Prompt
        st.markdown("""
        <div class="step-box">
        <h4>3️⃣ Refinamento Visual</h4>
        <p><strong>Prompt utilizado:</strong></p>
        <code>"Adicione uma barra lateral para navegação, melhore o layout visual e 
        inclua minha marca pessoal no projeto"</code>
        <p><em>Resultado:</em> Implementação de navegação intuitiva, melhorias significativas no 
        design e adição de elementos de marca pessoal.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quarto Prompt
        st.markdown("""
        <div class="step-box">
        <h4>4️⃣ Documentação e Deploy</h4>
        <p><strong>Prompt utilizado:</strong></p>
        <code>"Crie uma documentação detalhada do processo de desenvolvimento e 
        prepare o projeto para deploy no Streamlit Cloud"</code>
        <p><em>Resultado:</em> Criação de documentação completa e preparação para disponibilização 
        online através do Streamlit Cloud.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        #### 💡 Principais Aprendizados
        
        Durante este projeto, foram adquiridos diversos conhecimentos importantes:
        
        - **Desenvolvimento Ágil com IA**: Aprendi como a _Cursor IA_ pode acelerar significativamente 
          o processo de desenvolvimento, sugerindo código relevante e ajudando na resolução de problemas.
          
        - **Integração de Tecnologias**: Experiência prática com a combinação de diferentes tecnologias:
          - _Python_ para a lógica de programação
          - _Streamlit_ para a interface web
          - _Git_ para controle de versão
          - _Streamlit Cloud_ para deploy
          
        - **Melhores Práticas**: Desenvolvimento de código limpo, documentação clara e interface 
          intuitiva para usuários técnicos e não técnicos.
          
        #### 🚀 Deploy e Disponibilização
        
        O projeto está disponível online através do Streamlit Cloud, seguindo estas etapas:
        
        1. Repositório criado no GitHub
        2. Configuração da conta no Streamlit Cloud
        3. Conexão com o repositório
        4. Deploy e disponibilização online
        
        #### 📁 Estrutura do Projeto
        ```
        Calculadora_Cursor_IA/
        ├── calculadora_app.py    # Aplicação principal
        ├── requirements.txt      # Dependências
        ├── README.md            # Documentação
        └── .gitignore           # Configuração Git
        ```
        
        ---
        
        > **Nota**: Este projeto é um exemplo prático de como ferramentas modernas de IA, como a 
        > _Cursor IA_, podem transformar exercícios básicos de programação em aplicações profissionais 
        > e funcionais.
        """)

# Execução principal
def main():
    local_css()
    calculadora()

if __name__ == "__main__":
    main()