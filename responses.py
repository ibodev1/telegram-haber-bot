from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("deneme", "sa"):
        return "As"

    return "Yanlış veya bilinmeyen giriş yaptınız."
