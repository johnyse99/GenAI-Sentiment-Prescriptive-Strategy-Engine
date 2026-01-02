"""
Utility Script: Seed Data Generator
Description: Creates a synthetic dataset of customer reviews for Project 2.
Standards: Senior Data Engineering (Automated environment setup).
"""

import pandas as pd
import os
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_reviews_dataset():
    """Generates a CSV file with sample customer reviews."""
    data = {
        "review_id": [1, 2, 3, 4, 5],
        "customer_name": ["Alice Smith", "Bob Johnson", "Charlie Davis", "Diana Prince", "Edward Norton"],
        "review_text": [
            "The product quality is absolutely amazing! I am very happy with my purchase and the fast shipping.",
            "I am extremely disappointed. The item arrived broken and the customer service was very rude.",
            "The product is okay, it does the job but the packaging was a bit damaged during delivery.",
            "Worst experience ever. I requested a refund two weeks ago and nobody has contacted me yet.",
            "Very satisfied with the performance. It exceeded my expectations for the price point."
        ],
        "rating": [5, 1, 3, 1, 5]
    }

    df = pd.DataFrame(data)

    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    
    file_path = 'data/customer_reviews.csv'
    df.to_csv(file_path, index=False)
    
    logger.info(f"Successfully generated {file_path} with {len(df)} sample reviews.")

if __name__ == "__main__":
    generate_reviews_dataset()