import streamlit as st
import pandas as pd
import pickle
import requests

# ------------------------------
# Load saved model + data
# ------------------------------

anime_data = pd.read_pickle("anime_data.pkl")
anime_indices = pd.read_pickle("anime_index.pkl")

with open("similarity.pkl", "rb") as f:
    cosine_sim = pickle.load(f)

# ------------------------------
# Fetch Anime Poster (via Jikan API)
# ------------------------------

@st.cache_data
def fetch_poster(title):
    base_url = "https://api.jikan.moe/v4/anime"
    response = requests.get(base_url, params={"q": title, "limit": 1})

    try:
        data = response.json()["data"][0]
        return data["images"]["jpg"]["image_url"], data["score"], data["synopsis"]
    except:
        return None, None, None

# ------------------------------
# Recommend Function
# ------------------------------

def recommend_content(title, top_n=5):
    if title not in anime_indices:
        return ["Anime not found"]

    idx = anime_indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    recommended_indices = [i[0] for i in sim_scores]
    return anime_data.iloc[recommended_indices]

# ------------------------------
# UI
# ------------------------------

st.set_page_config(page_title="Anime Recommender", layout="wide")

st.title("🎌 Anime Recommendation System")
st.write("Find similar anime instantly based on genres using TF-IDF + Cosine Similarity!")

# Search Input
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

                poster, score, synopsis = fetch_poster(row['name'])

                with cols[i % 3]:

                    st.image(poster, width=220) if poster else st.write("No Image")

                    st.markdown(f"### {row['name']}")
                    st.markdown(f"⭐ **Score:** {score if score else 'N/A'}")
                    st.markdown(f"🎭 **Genres:** {row['genre']}")
                    st.markdown(
                        f"<p style='font-size:14px'>{synopsis[:250]+'...' if synopsis else 'No synopsis available.'}</p>",
                        unsafe_allow_html=True
                    )
