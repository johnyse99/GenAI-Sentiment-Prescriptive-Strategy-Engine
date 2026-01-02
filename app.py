import streamlit as st
import pandas as pd
from src.descriptive_analysis import SentimentDescriptive
from src.predictive_model import SentimentPredictor
from src.prescriptive_strategy import GenAIPrescriptiveEngine

def main():
    st.set_page_config(page_title="GenAI Sentiment Optimizer", layout="wide")
    st.title("🤖 GenAI Sentiment & Prescriptive Strategy")
    
    # Sidebar for Navigation
    menu = ["Data Exploration", "Sentiment Analysis", "AI Prescriptive Actions"]
    choice = st.sidebar.selectbox("Phase", menu)

    # Initialize Engines
    if 'data_manager' not in st.session_state:
        # Assuming we have a sample CSV in data/
        st.session_state.data_manager = SentimentDescriptive("data/customer_reviews.csv")
        st.session_state.predictor = SentimentPredictor()
        st.session_state.genai = GenAIPrescriptiveEngine()

    if choice == "Data Exploration":
        st.header("📊 Phase 1: Descriptive Insights")
        if st.session_state.data_manager.load_and_validate():
            stats = st.session_state.data_manager.get_text_stats()
            col1, col2 = st.columns(2)
            col1.metric("Total Reviews", stats['total_reviews'])
            col2.metric("Avg Word Count", round(stats['avg_words'], 2))
            
            st.subheader("Top Word Frequency")
            st.bar_chart(st.session_state.data_manager.get_word_frequency())

    elif choice == "Sentiment Analysis":
        st.header("🤖 Phase 2: Predictive NLP")
        if not st.session_state.data_manager.df.empty:
            results = st.session_state.predictor.analyze_sentiment(st.session_state.data_manager.df)
            st.dataframe(results[['review_text', 'sentiment', 'score']], use_container_width=True)
            st.session_state.processed_df = results
        else:
            st.warning("Please load data in Phase 1 first.")

    elif choice == "AI Prescriptive Actions":
        st.header("🎯 Phase 3: GenAI Business Prescriptions")
        if 'processed_df' in st.session_state:
            selected_review = st.selectbox("Select a review to process with GenAI:", 
                                           st.session_state.processed_df['review_text'])
            
            row = st.session_state.processed_df[st.session_state.processed_df['review_text'] == selected_review].iloc[0]
            
            if st.button("Generate AI Strategy"):
                prescription = st.session_state.genai.generate_prescription(row['review_text'], row['sentiment'])
                
                with st.expander("📝 AI Generated Executive Report", expanded=True):
                    st.write(f"**Sentiment Detected:** {row['sentiment']}")
                    st.info(f"**Suggested Response:** {prescription.suggested_response}")
                    st.success(f"**Incentive to Offer:** {prescription.compensation_offer}")
                    st.warning(f"**Action Priority:** {prescription.priority_level}")
        else:
            st.error("Model must classify sentiments before generating prescriptions.")

if __name__ == "__main__":
    main()