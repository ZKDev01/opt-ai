import streamlit as st 


st.set_page_config(
  page_title='Service Bot',
  layout='wide'
)


about = """
- Resolver problemas de optimización 
- Responder a preguntas sobre datos no estructurados como videos e imágenes
"""

def main ( ) -> None:
  with st.expander (label="**Capacidades**", expanded=False):
    st.markdown (about)

if __name__ == '__main__':
  st.title ( "Service Bot" )
  main ( )
