# 🧹 Text Data Cleaning & Preprocessing (IMDB Sentiment Analysis)

# ==============================
# 📦 Importing Required Libraries
# ==============================
import pandas as pd
import numpy as np
import re
import string
import nltk
import emoji
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# ==============================
# 📂 Load Dataset
# ==============================
df = pd.read_csv('/content/drive/MyDrive/IMDB Dataset.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# ==============================
# 🧠 1. Convert Text to Lowercase
# ==============================
df['review'] = df['review'].str.lower()

# ==============================
# 🧼 2. Remove HTML Tags
# ==============================
def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)

df['review'] = df['review'].apply(remove_html_tags)

# ==============================
# 🔗 3. Remove URLs
# ==============================
def remove_url(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', text)

df['review'] = df['review'].apply(remove_url)

# ==============================
# 🔠 4. Remove Punctuation
# ==============================
exclude = string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', exclude))

df['review'] = df['review'].apply(remove_punctuation)

# ==============================
# 💬 5. Replace Chatwords (Short forms)
# ==============================
chatwords = {
    "LOL": "Laughing out loud",
    "IMHO": "In My Honest Opinion",
    "TTYL": "Talk To You Later",
    "BRB": "Be Right Back",
    "BTW": "By The Way",
    "IDC": "I don't care",
    "OMG": "Oh My God",
    "FYI": "For Your Information",
    "WTF": "What The F...",
    "ROFL": "Rolling On The Floor Laughing",
    "LMAO": "Laughing My A.. Off",
    "ILY": "I Love You",
    "BAE": "Before Anyone Else",
    "GN": "Good Night",
    "CU": "See You",
    "GM": "Good Morning",
    "BFF": "Best Friends Forever",
    "JK": "Just Kidding"
}

def chat_conversation(text):
    new_text = []
    for word in text.split():
        if word.upper() in chatwords:
            new_text.append(chatwords[word.upper()])
        else:
            new_text.append(word)
    return " ".join(new_text)

df['review'] = df['review'].apply(chat_conversation)

# ==============================
# ✍️ 6. Spelling Correction
# ==============================
def spell_correction(text):
    text_correct = TextBlob(text)
    return text_correct.correct().string

# ⚠️ Note: Spell correction is slow. Uncomment to run.
# df['review'] = df['review'].apply(spell_correction)

# ==============================
# 🚫 7. Remove Stopwords
# ==============================
nltk.download('stopwords')
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    return " ".join([word for word in text.split() if word not in stop_words])

df['review'] = df['review'].apply(remove_stopwords)

# ==============================
# 😊 8. Handle Emojis
# ==============================
def replace_emojis(text):
    return emoji.demojize(text)

df['review'] = df['review'].apply(replace_emojis)

# ==============================
# ✂️ 9. Tokenization
# ==============================
nltk.download('punkt')
def tokenization(text):
    return word_tokenize(text)

df['review'] = df['review'].apply(tokenization)

# ==============================
# 🌱 10. Stemming & Lemmatization
# ==============================
ps = PorterStemmer()
def stem_words(text):
    return [ps.stem(word) for word in text]

df['review'] = df['review'].apply(stem_words)

# Lemmatization
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
def lemmatize_text(text):
    return [lemmatizer.lemmatize(token) for token in text]

df['review'] = df['review'].apply(lemmatize_text)

# ==============================
# 💾 Save Cleaned Data
# ==============================
df.to_csv('/content/drive/MyDrive/IMDB_Cleaned.csv', index=False)
print("✅ Data Cleaning Completed and Saved Successfully!")

