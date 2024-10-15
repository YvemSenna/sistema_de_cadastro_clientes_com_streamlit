import streamlit as st

st.title("Cadastro de clientes")
nome = st.text_input("Digite o nome do cliente:")
endereco = st.text_input("Digite seu endereço:")
dt_nasc = st.date_input("Escolha a data de nascimento:")
tipo_cliente = st.selectbox("Tipo de cliente", ["Pessoa Física", "Pessoa Jurídica"])

cadastrar = st.button("Cadastrar cliente")

if cadastrar:
    with open("clentes.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome}, {endereco}, {dt_nasc}, {tipo_cliente}\n")
        st.success("Cliente Cadastrado com sucesso!")