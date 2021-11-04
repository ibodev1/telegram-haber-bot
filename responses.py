from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("sa", "Sa", "Sea"):
        return "Aleyküm selam"

    if user_message in ("merhaba", "Merhaba"):
        return "Merhaba"

    return "Yanlış veya bilinmeyen giriş yaptınız."
