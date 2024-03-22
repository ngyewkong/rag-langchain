from langchain_openai import OpenAIEmbeddings
from langchain.evaluation import load_evaluator
from dotenv import load_dotenv
import os
import sys

# load the .env file that contains the api key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def main(word1, word2):
    # Get embedding for a word.
    embedding_function = OpenAIEmbeddings()
    vector = embedding_function.embed_query("apple")
    print(f"Vector for 'apple': {vector}")
    print(f"Vector length: {len(vector)}")

    # Compare vector of two words
    evaluator = load_evaluator("pairwise_embedding_distance")
    # words = ("apple", "iphone")
    x = evaluator.evaluate_string_pairs(
        prediction=word1, prediction_b=word2)
    print(f"Comparing ({word1}, {word2}): {x}")


if __name__ == "__main__":
    # Check if the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: python3 compare_embeddings.py <word1> <word2>")
        sys.exit(1)

    # Pass the command line arguments to main
    main(sys.argv[1], sys.argv[2])
