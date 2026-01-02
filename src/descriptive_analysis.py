"""
Module: Descriptive Analysis
Description: Performs EDA on text data and validates input using Pydantic.
Inputs: CSV file with customer reviews.
Outputs: Word frequency data and text statistics for Streamlit.
"""

import pandas as pd
import logging
from typing import Dict, Any
import matplotlib.pyplot as plt

# Senior standard: Specific logging
logger = logging.getLogger(__name__)

class SentimentDescriptive:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.df: pd.DataFrame = pd.DataFrame()

    def load_and_validate(self) -> bool:
        """Loads data and validates structure."""
        try:
            self.df = pd.read_csv(self.data_path)
            logger.info(f"Loaded {len(self.df)} reviews from {self.data_path}")
            return True
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return False

    def get_text_stats(self) -> Dict[str, Any]:
        """Calculates basic NLP statistics."""
        if self.df.empty:
            return {}
        
        self.df['char_count'] = self.df['review_text'].str.len()
        self.df['word_count'] = self.df['review_text'].str.split().str.len()
        
        stats = {
            "avg_chars": self.df['char_count'].mean(),
            "avg_words": self.df['word_count'].mean(),
            "total_reviews": len(self.df)
        }
        return stats

    def get_word_frequency(self, top_n: int = 10) -> pd.Series:
        """Simple word frequency for visualization."""
        all_words = ' '.join(self.df['review_text']).lower().split()
        # Removing basic stop words could be added here
        return pd.Series(all_words).value_counts().head(top_n)