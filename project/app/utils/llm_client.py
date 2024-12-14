# app/utils/llm_client.py

from huggingface_hub import InferenceClient
from app.config import HUGGING_FACE_API_KEY, HUGGING_FACE_MODEL

# Initialize the Hugging Face Inference Client
client = InferenceClient(api_key=HUGGING_FACE_API_KEY)


def query_llm(prompt: str) -> str:
    """
    Generate a response using Hugging Face's Inference Client.
    Args:
        prompt (str): The input prompt for the model.
    Returns:
        str: Generated response or an error message.
    """
    if not prompt.strip():
        raise ValueError("The prompt must not be empty.")

    try:
        messages = [{"role": "user", "content": prompt}]

        completion = client.chat.completions.create(
            model=HUGGING_FACE_MODEL,
            messages=messages,
            max_tokens=1000,  # Adjust as needed
        )

        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
