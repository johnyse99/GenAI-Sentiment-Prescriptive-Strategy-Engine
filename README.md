# GenAI Sentiment Analyzer & Prescriptive Strategy Engine

This project demonstrates an advanced implementation of **Generative AI** for business automation. It moves beyond simple sentiment classification by utilizing AI to prescribe specific customer recovery actions and personalized responses, aligning with the **IBM Applied Data Science** curriculum (Course 11: Generative AI).

## 🏗️ Technical Architecture
The system is built on a modular three-phase pipeline to ensure high cohesion and low coupling:

1.  **Descriptive Phase**: Textual EDA using word frequency analysis and token distribution to understand the customer voice.
2.  **Predictive Phase**: Sentiment classification using NLP (Polarity & Subjectivity) to categorize reviews into Positive, Negative, or Neutral.
3.  **Prescriptive Phase (GenAI)**: A strategic engine that acts as an LLM orchestrator, generating automated business responses and compensation plans based on the detected sentiment.

## 🛠️ Tech Stack & Standards
* **Core**: Python 3.12, Pandas.
* **NLP & AI**: TextBlob / Hugging Face for sentiment; GenAI Prompt Engineering for strategies.
* **Data Integrity**: **Pydantic** models for strict input validation and schema enforcement.
* **UI/UX**: **Streamlit** for the interactive executive dashboard.
* **Software Engineering**: Specific `try-except` blocks, `logging` modules, and **Dependency Injection**.

## 🚀 Installation & Usage
1.  Ensure you have a `data/customer_reviews.csv` file with a `review_text` column.
2.  Install requirements: `pip install -r requirements.txt`.
3.  Run the application: `streamlit run app.py`.

---

## ❓ Interview FAQ (NLP & GenAI)

**Q: What is the difference between Predictive Sentiment and Prescriptive GenAI in this project?**
A: Predictive Sentiment answers "What is the customer feeling?" using NLP models. Prescriptive GenAI answers "What should the business do about it?" by generating context-aware solutions through structured prompts.

**Q: How do you handle bias or hallucinations in the GenAI responses?**
A: This senior implementation uses **Pydantic** to validate the structured output of the AI (ActionPlan). By enforcing a schema (category, response, compensation), we limit the "creativity" of the LLM to predefined business guardrails.

**Q: Why use Streamlit's `session_state` for this pipeline?**
A: In an industrial dashboard, re-calculating NLP scores or calling GenAI APIs on every user click is expensive and slow. `session_state` persists the processed data between fragments, optimizing performance and reducing API costs.

---

📄 **License**
This project is distributed under the MIT license. Its purpose is strictly educational and research-based, developed as an Applied Data Science solution.

**Note for recruiters:**
This project highlights the transition from traditional Machine Learning to **Generative AI Applications**. It showcases the ability to design an end-to-end automated workflow where AI makes autonomous business decisions based on textual data, a key requirement for modern AI Architect roles.
