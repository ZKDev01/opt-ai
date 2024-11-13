import streamlit as st 


about = """
- Resolver Problemas de Optimizacion 
- Permite preguntar sobre el contenido de un documento pdf
"""

def main ( ) -> None:
  with st.expander (label="**Capacidades**", expanded=False):
    st.markdown (about)

if __name__ == '__main__':
  st.title ( "Service Bot" )
  main ( )
