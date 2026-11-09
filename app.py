import streamlit as st

#inicializacao das variaveis de estado 
st.title("sistema de cadastro")
 if "pagina" not in st.session_state:
   st.session_state.pagina = "Menu"
#tela de menu

if st.session_state.pagina == "menu":
    st.title("Menu principal")
    st.write("escolha uma opcao: ")

#tela de cadastro
#tela de login
