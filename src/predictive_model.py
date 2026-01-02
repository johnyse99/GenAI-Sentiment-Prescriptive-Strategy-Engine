"""
Module: Predictive Model
Description: Sentiment classification using NLP logic.
Inputs: Validated Dataframe from Phase 1.
Outputs: Sentiment labels (Positive, Negative, Neutral).
"""

from textblob import TextBlob
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class SentimentPredictor:
    def __init__(self):
        self.results: pd.DataFrame = pd.DataFrame()

    def analyze_sentiment(self, df: pd.DataFrame) -> pd.DataFrame:
        """Predicts sentiment polarity for each review."""
        try:
            logger.info("Starting sentiment prediction...")
            
            def get_label(text: str) -> str:
                analysis = TextBlob(text)
                if analysis.sentiment.polarity > 0.1:
                    return "Positive"
                elif analysis.sentiment.polarity < -0.1:
                    return "Negative"
                else:
                    return "Neutral"

            df['sentiment'] = df['review_text'].apply(get_label)
            df['score'] = df['review_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
            
            self.results = df
            return df
        except Exception as e:
            logger.error(f"Prediction failed: {e}")
            return pd.DataFrame()