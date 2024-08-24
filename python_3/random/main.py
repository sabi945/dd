import os
import google.generativeai as genai

def kirim_pesan_ke_gemini(pesan):
    """Mengirim pesan ke model Gemini dan mengembalikan respon."""

    # Konfigurasi model
    genai.configure(api_key=os.environ["GOOGLE_APPLICATION_CREDENTIALS"])  # Menggunakan env variable
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    # Memulai sesi chat
    chat_session = model.start_chat(history=[])  # History kosong untuk sesi baru

    # Mengirim pesan dan mendapatkan respon
    response = chat_session.send_message(pesan)
    return response.text