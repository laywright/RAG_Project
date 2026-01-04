from google import genai
from hybrid_function import hybrid_search
from prompt import generate_answer  # your fixed generate_answer function
import embedded
import loading_files
import hybrid_function
import prompt


if __name__ == "__main__":
    test_query = "Can an employee be terminated without notice in India?"
    result = generate_answer(test_query)
    print("\n💬 Gemini's Answer:\n")
    print(result)
