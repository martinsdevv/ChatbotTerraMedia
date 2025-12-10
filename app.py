import json
import os
import time

import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from PIL import Image

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("ERRO: Configure a GROQ_API_KEY no arquivo .env")
    st.stop()

client = Groq(api_key=api_key)

st.set_page_config(page_title="Terra Média Chat", page_icon="💍", layout="centered")


def load_characters():
    chars = {}
    chars_dir = "characters"
    if not os.path.exists(chars_dir):
        os.makedirs(chars_dir)
        return {}
    for filename in os.listdir(chars_dir):
        if filename.endswith(".json"):
            path = os.path.join(chars_dir, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    char_id = filename.replace(".json", "")
                    chars[char_id] = data
            except Exception as e:
                st.error(f"Erro ao ler {filename}: {e}")
    return chars


personagens = load_characters()
if not personagens:
    st.error("Nenhum personagem encontrado na pasta 'characters/'.")
    st.stop()

st.sidebar.title("Escolha o Personagem")
char_id = st.sidebar.selectbox("Quem você quer invocar?", list(personagens.keys()))
current_char = personagens[char_id]


def get_assistant_avatar(char_data):
    avatar_config = char_data.get("avatar", "🤖")
    if avatar_config.endswith((".png", ".jpg", ".jpeg", ".webp")):
        try:
            image_path = os.path.join("characters", avatar_config)
            return Image.open(image_path)
        except Exception:
            return "🤖"
    return avatar_config


assistant_avatar_final = get_assistant_avatar(current_char)

st.title(f"{current_char['name']}")
st.markdown(current_char.get("description", ""))

if "last_char" not in st.session_state or st.session_state.last_char != char_id:
    st.session_state.messages = []
    st.session_state.last_char = char_id
    if "first_message" in current_char:
        st.session_state.messages.append(
            {"role": "assistant", "content": current_char["first_message"]}
        )

for message in st.session_state.messages:
    avatar_to_use = assistant_avatar_final if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar_to_use):
        st.markdown(message["content"])

if prompt := st.chat_input("Diga algo..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    groq_messages = [{"role": "system", "content": current_char["system_instruction"]}]

    for msg in st.session_state.messages:
        groq_messages.append({"role": msg["role"], "content": msg["content"]})

    with st.chat_message("assistant", avatar=assistant_avatar_final):
        placeholder = st.empty()
        full_response = ""

        with st.spinner(f"*{current_char['name']} está conspirando...*"):
            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=groq_messages,
                    temperature=current_char.get("temperature", 1.0),
                    max_tokens=1024,
                    top_p=1,
                    stream=True,
                    stop=None,
                )

                for chunk in completion:
                    content = chunk.choices[0].delta.content
                    if content:
                        full_response += content
                        placeholder.markdown(full_response + "▌")

                placeholder.markdown(full_response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )

            except Exception as e:
                st.error(f"Erro na API do Groq: {e}")
