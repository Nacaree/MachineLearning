



import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the required lexicon (only needed once)
nltk.download('vader_lexicon')

# Initialize the analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    # Calculate sentiment polarity scores
    scores = analyzer.polarity_scores(text)
    
    # Extract the compound score (ranges from -1 to 1)
    compound = scores['compound']
    
    # Classify based on standard VADER thresholds
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return sentiment, scores

# Test the function
sample_text = """Cambodia,[a] officially the Kingdom of Cambodia,[b] is a country in Mainland Southeast Asia. It is bordered by Thailand to the northwest, Laos to the north, and Vietnam to the east, and has a coastline along the Gulf of Thailand in the southwest. It spans an area of about 181,035 km2 (69,898 sq mi), dominated by a low-lying plain and the confluence of the Mekong river and Tonlé Sap, Southeast Asia's largest lake. It is dominated by a tropical climate. Cambodia has a population of about 17 million people,[8] the majority of which are ethnically Khmer. Its capital and most populous city is Phnom Penh, followed by Siem Reap and Battambang.[15]

In 802 AD, Jayavarman II declared himself king, uniting the warring Khmer princes of Chenla under the name "Kambuja".[16] This marked the beginning of the Khmer Empire. The Indianised kingdom facilitated the spread of first Hinduism and then Buddhism to Southeast Asia and undertook religious infrastructural projects throughout the region, the most famous of which is Angkor Wat. In the 15th century, it began a decline in power until, in 1863, Cambodia became a French protectorate. Following Japanese occupation during World War II, Cambodia declared independence from France in 1953. The Vietnam War embroiled the country in civil war during the 1960s, culminating in a 1970 coup which installed the U.S.-aligned Khmer Republic and the takeover of the communist Khmer Rouge in 1975. The Khmer Rouge ruled the country and carried out the Cambodian genocide from 1975 until 1979, until they were ousted during the Cambodian–Vietnamese War. Peace was restored by the 1991 Paris Peace Accords and subsequent United Nations peacekeeping mission, establishing a new constitution, holding the 1993 general election, and ending long-term insurgencies. The 1997 coup d'état consolidated power under Prime Minister Hun Sen and the Cambodian People's Party (CPP)."""
sentiment, detailed_scores = analyze_sentiment(sample_text)

# Split the sentense into single words
words = sample_text.lower().split()

print("--- Analyzing Words inside the Sentence ---")
for word in words:
    # Clean basic punctuation from the word
    clean_word = word.strip(".,!?\"'")
    
    # Get score from VADER's dictionary (defaults to 0.0 if neutral)
    score = analyzer.lexicon.get(clean_word, 0.0)
    
    print(f"Word: '{clean_word:<10}' | VADER Score: {score}")


print(f"Text: {sample_text}")
print(f"Predicted Sentiment: {sentiment}")
print(f"Full Score Breakdown: {detailed_scores}")







"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the required lexicon dataset
nltk.download('vader_lexicon')

# Initialize the analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze a sample sentence
text = "Why Apple is looking at buying U.K. startup for $1 billion ?"
scores = analyzer.polarity_scores(text)

print(scores)
"""
