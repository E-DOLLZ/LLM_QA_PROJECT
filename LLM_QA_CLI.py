

# LLM_QA_CLI.py
import string
from cohere import ClientV2

API_KEY = "utIG5RamCvCm7TbdYbdoFm3vynjp2ZlrNMVhf7Ek"
client = ClientV2(API_KEY)
MODEL = "command-xlarge-nightly"

def preprocess(question):
    question = question.lower()
    question = question.translate(str.maketrans("", "", string.punctuation))
    return question

def ask_cohere(question):
    try:
        response = client.chat(
            model=MODEL,
            messages=[{"role": "user", "content": question}],
        )
        # Extract the text from the first item in the content list
        return response.message.content[0].text
    except Exception as e:
        raise RuntimeError(f"API Error: {e}")


def main():
    print("=== Cohere V2 Chat CLI ===")
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ").strip()
        if question.lower() == "exit":
            print("Exiting CLI. Goodbye!")
            break
        processed = preprocess(question)
        print(f"\nProcessed question: {processed}")
        try:
            answer = ask_cohere(processed)
            print(f"\nAnswer:\n{answer}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
