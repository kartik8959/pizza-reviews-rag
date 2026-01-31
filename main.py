from langchain_ollama.llms import OllamaLLM
from vector import search_reviews

# Load LLM once
llm = OllamaLLM(model="llama3.2")

print("🍕 Pizza Review Assistant")
print("Ask questions based on real customer reviews.")
print("Type 'q' to quit.")
print("------------------------------------------------")

while True:
    question = input("❓ Your question: ")

    if question.lower() == "q":
        print("👋 Goodbye!")
        break

    # 1. Retrieve relevant reviews
    docs = search_reviews(question)

    reviews_text = "\n\n".join(doc.page_content for doc in docs)

    # 2️. Build prompt
    prompt = f"""
You are a helpful expert on a pizza restaurant.

Use ONLY the customer reviews below to answer.
If the reviews do not contain the answer, say:
"Not enough information based on reviews."

Customer Reviews:
{reviews_text}

Question:
{question}
"""

    # 3️. Ask the LLM
    answer = llm.invoke(prompt)

    print("\n🧠 Answer:")
    print(answer)
    print("------------------------------------------------")
