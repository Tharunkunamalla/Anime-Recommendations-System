# 🎌 Anime Recommendation System

A content-based anime recommendation system that suggests similar anime titles based on genre similarities using TF-IDF vectorization and cosine similarity. The system features an interactive web interface built with Streamlit and fetches real-time anime data including posters, ratings, and synopses from the Jikan API.

## 🌟 Features

- **Content-Based Filtering**: Recommends anime based on genre similarities using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
- **Interactive Web Interface**: User-friendly Streamlit application for easy anime search and recommendations
- **Real-Time Data**: Fetches anime posters, ratings, and synopses from the Jikan API (MyAnimeList)
- **Comprehensive Dataset**: Uses a dataset of 12,000+ anime titles with ratings from 7.8 million+ users
- **Fast Similarity Matching**: Utilizes cosine similarity for efficient recommendation generation

## 🛠️ Technology Stack

- **Python 3.x**: Core programming language
- **Streamlit**: Web framework for the interactive UI
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning library (TF-IDF vectorization and cosine similarity)
- **Requests**: HTTP library for API calls
- **Jikan API**: MyAnimeList API for fetching anime metadata

## 📊 Dataset

The system uses two main datasets:

- **anime.csv**: Contains 12,294 anime entries with information including:
  - anime_id: Unique identifier
  - name: Anime title
  - genre: Comma-separated genres
  - type: Type (TV, Movie, OVA, etc.)
  - episodes: Number of episodes
  - rating: Average rating
  - members: Number of community members

- **rating.csv**: Contains 7,813,737 user ratings for collaborative filtering (optional)

Dataset source: [Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Tharunkunamalla/Anime-Recommendations-System.git
cd Anime-Recommendations-System
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure the following pre-processed files are present:
   - `anime_data.pkl`: Processed anime dataframe
   - `anime_index_lower.pkl`: Lowercase title-to-index mapping
   - `tfidf_model.pkl`: TF-IDF vectorizer and matrix

## 💻 Usage

### Running the Streamlit Application

Start the web application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### How to Use

1. Enter an anime title in the search box
2. Click the "Recommend" button
3. View recommended anime with:
   - Poster images
   - Ratings
   - Genres
   - Synopsis

### Example

Search for "Naruto" to get recommendations for similar action/adventure anime titles.

## 📸 Application Interface & Results

### Initial Interface
![Application Interface](https://github.com/user-attachments/assets/b7c8054f-560c-4b37-8a97-643e914dbdfa)

The application features a clean, intuitive interface where users can:
- Enter an anime title in the search box
- Click the "Recommend" button to get similar anime suggestions
- View recommendations with poster images, ratings, genres, and synopses displayed in a grid layout

### Sample Output

When you search for an anime (e.g., "Naruto"), the system generates recommendations based on genre similarity:

**Example: Recommendations for "Naruto"**

| # | Anime Title | Type | Rating | Genres |
|---|------------|------|--------|--------|
| 1 | Naruto Shippuuden: Sunny Side Battle | Special | 7.26 | Action, Comedy, Martial Arts, Shounen, Super Power |
| 2 | Naruto: Shippuuden Movie 4 - The Lost Tower | Movie | 7.53 | Action, Comedy, Martial Arts, Shounen, Super Power |
| 3 | Boruto: Naruto the Movie | Movie | 8.03 | Action, Comedy, Martial Arts, Shounen, Super Power |
| 4 | Naruto: Shippuuden | TV | 7.94 | Action, Comedy, Martial Arts, Shounen, Super Power |
| 5 | Naruto: Shippuuden Movie 3 - Hi no Ishi wo Tsugu Mono | Movie | 7.50 | Action, Comedy, Martial Arts, Shounen, Super Power |

Each recommendation is displayed with:
- **Poster Image**: Fetched in real-time from the Jikan API
- **Rating**: Current MyAnimeList score
- **Genres**: Comma-separated genre tags
- **Synopsis**: Brief description of the anime (truncated to 250 characters)

## 📁 Project Structure

```
Anime-Recommendations-System/
│
├── app.py                          # Main Streamlit application
├── Anime_recomendation_system.ipynb # Jupyter notebook for data processing
├── anime.csv                        # Raw anime dataset
├── rating.csv                       # User ratings dataset
├── anime_data.pkl                   # Processed anime dataframe
├── anime_index.pkl                  # Title-to-index mapping
├── anime_index_lower.pkl            # Lowercase title-to-index mapping
├── tfidf_model.pkl                  # TF-IDF vectorizer and matrix
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## 🔍 How It Works

### 1. Data Processing
- Loads anime dataset from CSV
- Handles missing genre values
- Creates title-to-index mappings for efficient lookups

### 2. Feature Extraction
- Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization on genre text
- Converts genre strings into numerical feature vectors
- Each anime is represented as a vector in high-dimensional space

### 3. Similarity Calculation
- Computes cosine similarity between anime vectors
- Measures how similar anime genres are to each other
- Higher similarity scores indicate more similar anime

### 4. Recommendation Generation
- Takes user input (anime title)
- Finds the anime in the dataset
- Calculates similarity scores with all other anime
- Returns top-N most similar anime

### 5. Data Enrichment
- Fetches real-time data from Jikan API
- Retrieves poster images, current ratings, and synopses
- Enhances recommendations with visual and descriptive information

## 🔧 Development

### Processing the Data

If you need to regenerate the pickle files, use the included Jupyter notebook:

1. Open `Anime_recomendation_system.ipynb`
2. Run all cells to:
   - Load and clean the data
   - Create TF-IDF model
   - Generate pickle files for the application

### API Rate Limiting

The Jikan API has rate limits. The application includes caching (`@st.cache_data`) to minimize API calls and improve performance.

## 🌐 Live Demo

The application is hosted at: [www.anime-recommendations-system.com](https://anime-recommendations-system.streamlit.app/)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Add collaborative filtering using user ratings
- [ ] Implement hybrid recommendation system (content + collaborative)
- [ ] Add user authentication and personalized recommendations
- [ ] Include more features (year, rating, type) in similarity calculation
- [ ] Add anime watchlist functionality
- [ ] Implement advanced filters (year, rating range, type)
- [ ] Add anime comparison feature

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Dataset from [Kaggle - Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database)
- Anime data and images from [MyAnimeList](https://myanimelist.net/) via [Jikan API](https://jikan.moe/)
- Built with [Streamlit](https://streamlit.io/)

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: This is an educational project demonstrating content-based recommendation systems and web application development with Python.
