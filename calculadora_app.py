import streamlit as st
import math
import pandas as pd
from PIL import Image

# Configuração da página
st.set_page_config(
    page_title="Calculadora Python",
    page_icon="🧮",
    layout="wide",
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
    st.title("🧮 Calculadora Python")
    
    # Tabs para navegação
    tab1, tab2 = st.tabs(["Calculadora", "Documentação"])
    
    with tab1:
        st.markdown("### Realize seus cálculos de forma simples e rápida!")
        
        # Seleção da operação
        operacao = st.selectbox(
            "Escolha a operação desejada:",
            [
                "Soma (+)",
                "Subtração (-)",
                "Multiplicação (×)",
                "Divisão (÷)",
                "Potenciação (^)",
                "Raiz Quadrada (√)"
            ]
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
    
    with tab2:
        st.markdown("## Sobre o Projeto")
        
        st.markdown("""
        ### 📝 Descrição
        
        Esta calculadora foi desenvolvida como parte do curso de Python, utilizando tecnologias modernas
        e práticas de desenvolvimento profissionais. O projeto demonstra a aplicação prática de conceitos
        de programação e a criação de interfaces web interativas.
        
        ### 🛠️ Tecnologias Utilizadas
        
        - **Python**: Linguagem de programação principal
        - **Streamlit**: Framework para criação de aplicações web
        - **Cursor IDE**: Ambiente de desenvolvimento integrado com IA
        - **Git**: Sistema de controle de versão
        
        ### 💡 Funcionalidades
        
        - Operações matemáticas básicas
        - Interface intuitiva e responsiva
        - Tratamento de erros
        - Documentação integrada
        
        ### 🤖 Desenvolvimento com IA
        
        O projeto foi desenvolvido com o auxílio do Cursor IDE, que utiliza inteligência artificial para:
        
        1. **Sugestões de código**: Autocompletar e sugerir melhores práticas
        2. **Debugging**: Identificação e correção de erros
        3. **Documentação**: Geração de comentários e documentação
        4. **Refatoração**: Sugestões de melhorias no código
        
        ### 📊 Estrutura do Projeto
        
        ```
        calculadora/
        ├── calculadora_app.py    # Aplicação principal
        ├── requirements.txt      # Dependências
        └── README.md            # Documentação
        ```
        
        ### 🎯 Objetivos Alcançados
        
        1. Criar uma interface amigável para usuários leigos
        2. Implementar todas as operações matemáticas básicas
        3. Fornecer feedback claro sobre erros
        4. Documentar o processo de desenvolvimento
        
        ### 🔄 Processo de Desenvolvimento
        
        1. **Planejamento**: Definição de requisitos e funcionalidades
        2. **Desenvolvimento**: Implementação com auxílio de IA
        3. **Testes**: Verificação de funcionalidades e usabilidade
        4. **Documentação**: Registro do processo e instruções de uso
        
        ### 🌟 Próximos Passos
        
        - Adicionar mais operações matemáticas
        - Implementar histórico de cálculos
        - Adicionar temas personalizáveis
        - Criar versão mobile
        """)

# Execução principal
def main():
    local_css()
    calculadora()

if __name__ == "__main__":
    main() 