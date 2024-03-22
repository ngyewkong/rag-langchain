# RAG Chatbot in Terminal CLI

## Letting ChatGPT has access to documentation (AWS EKS) & using it to answer queries and providing the sources as part of output (prevent hallucination)

- Python
- LangChain (RAG)
- Chroma (VectorDB)
- OpenAI API (ChatGPT)

### To run this project:

- Install required dependencies
  - pip install requirements.txt
- Run create_db.py to create vectordb of the vector embeddings of the markdown files
  - python3 create_db.py
- Optional: Execute compare_embeddings.py to check the cosine similarity scores of two words
  - python3 compare_embeddings.py "FIRST_WORD" "SECOND_WORD"
- Execute query.py with the question that you want to ask
  - python3 query.py "YOUR QUESTION RELATING TO WHAT DOCUMENTATION eg EKS"
