import pandas as pd
import streamlit as st

@st.cache
def load_df(path):
    df = pd.read_csv(path)
    return df

st.title('Netflix App')

df = load_df('movies.csv')

with st.sidebar:
    showAllMovies = st.checkbox('Mostrar todas las peliculas')
    movieSearchTerm = st.text_input('Nombre de pelicula:')
    executeMovieSearch = st.button('Búsqueda')
    directorSearchTerm = st.selectbox('Director', df['director'])
    executeDirectorSearch = st.button('Filtrar director')

if showAllMovies:
    st.write(df)

if executeMovieSearch:
    search_df = df[df['name'].str.lower().str.contains(movieSearchTerm.lower())]
    st.caption('Peliculas encontradas: ' + str(search_df['name'].count()))
    st.write(search_df)

if executeDirectorSearch:
    search_df = df[df['director'].str.lower().str.contains(directorSearchTerm.lower())]
    st.caption('Peliculas encontradas: ' + str(search_df['name'].count()))
    st.write(search_df)