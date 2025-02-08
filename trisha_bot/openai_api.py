import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(user_id, user_input, mood="flirty"):
    """Send user input to OpenAI and get Trisha's response in Hinglish."""
    prompt = (
        "Tum Trisha ho, ek ladki jo Hindi me baat karti hai magar English letters me likhti hai (Hinglish). "
        f"Tumhara mood: {mood}. Tum thodi naughty, flirty aur masti bhari ho. User ke saath masti bhari baatein karo.\n"
        f"User: {user_input}\nTrisha:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=100
    )

    return response["choices"][0]["message"]["content"].strip()
