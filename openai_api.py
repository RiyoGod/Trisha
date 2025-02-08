import together
from config import TOGETHER_API_KEY

together.api_key = TOGETHER_API_KEY

def generate_response(user_id, user_input, mood="flirty"):
    """Send user input to Together AI model and get Trisha's response."""
    prompt = (
        "Tum Trisha ho, ek ladki jo Hindi me baat karti hai magar English letters me likhti hai (Hinglish). "
        f"Tumhara mood: {mood}. Tum thodi naughty, flirty aur masti bhari ho. User ke saath masti bhari baatein karo.\n"
        f"User: {user_input}\nTrisha:"
    )

    response = together.Completion.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",  # Updated model
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    
    # ✅ Fix: Properly access the text from the response
    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return "Sorry, mujhe samajh nahi aaya. Kya tum dobara keh sakte ho? 😊"
