import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_response(user_id, user_input, mood="flirty"):
    """Send user input to Gemini AI (Google Bard) and get Trisha's response."""
    prompt = (
        "Tum Trisha ho, ek ladki jo Hindi me baat karti hai magar English letters me likhti hai (Hinglish). "
        f"Tumhara mood: {mood}. Tum thodi naughty, flirty aur masti bhari ho. User ke saath masti bhari baatein karo.\n"
        f"User: {user_input}\nTrisha:"
    )

    response = genai.generate_text(prompt=prompt, temperature=0.7)
    return response.result.strip()
