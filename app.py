import streamlit as st
import pandas as pd
import pickle
import requests
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------------------------------
# Load Data + TF-IDF Model (CORRECT LOADING)
# -------------------------------------------------------

anime_data = pd.read_pickle("pkl/anime_data.pkl")              # Full anime dataframe
anime_indices = pd.read_pickle("pkl/anime_index_lower.pkl")          # Mapping: title → index

with open("pkl/tfidf_model.pkl", "rb") as f:                   # Load tuple (tfidf, matrix)
    tfidf, tfidf_matrix = pickle.load(f)

# -------------------------------------------------------
# Fetch Poster from Jikan API
# -------------------------------------------------------

@st.cache_data
def fetch_poster(title):
    base_url = "https://api.jikan.moe/v4/anime"
    response = requests.get(base_url, params={"q": title, "limit": 1})

    try:
        data = response.json()["data"][0]
        return data["images"]["jpg"]["image_url"], data["score"], data["synopsis"]
    except:
        return None, None, None

# -------------------------------------------------------
# Recommend Function (FIXED VERSION)
# -------------------------------------------------------

def recommend_content(title, top_n=5):
    title_key = title.strip().lower()

    if title_key not in anime_indices:
        return ["Anime not found"]

    idx = anime_indices[title_key]

    query_vec = tfidf_matrix[idx]
    sims = cosine_similarity(query_vec, tfidf_matrix).flatten()

    similar_indices = sims.argsort()[-top_n-1:-1][::-1]

    return anime_data.iloc[similar_indices]


# -------------------------------------------------------
# Streamlit UI
# -------------------------------------------------------

st.set_page_config(page_title="Anime Recommendation System", layout="wide")

st.title("🎌 Anime Recommendation System")
st.write("Find similar anime instantly using **TF-IDF + Cosine Similarity**")

search = st.text_input("Search Anime", "")

if st.button("Recommend"):
    if search.strip() == "":
        st.warning("Please enter an anime name.")
    else:
        results = recommend_content(search)

        if isinstance(results, list):
            st.error("Anime not found!")
        else:
            st.subheader(f"Recommendations similar to **{search}**")

            cols = st.columns(3)

            for i, (_, row) in enumerate(results.iterrows()):
                poster, score, synopsis = fetch_poster(row["name"])

                with cols[i % 3]:
                    if poster:
                        st.image(poster, width=220)
                    else:
                        st.write("No Image")

                    st.markdown(f"### {row['name']}")
                    st.markdown(f"⭐ **Score:** {score if score else 'N/A'}")
                    st.markdown(f"🎭 **Genres:** {row['genre']}")

                    st.markdown(
                        f"<p style='font-size:14px'>{(synopsis[:250] + '...') if synopsis else 'No synopsis available.'}</p>",
                        unsafe_allow_html=True
                    )
