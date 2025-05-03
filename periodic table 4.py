import streamlit as st
import random

# Sidebar untuk memilih game
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# Styling aesthetic & background gradasi
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(to right, #ff9966, #ff5e62);
        color: white;
    }

    .question-card {
        background: white;
        color: black;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 4px 4px 20px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        animation: fadeIn 1s ease-in-out;
    }

    .score-box {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        padding: 15px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        color: white;
        margin-top: 10px;
    }

    .stButton>button {
        background-color: #6a11cb;
        background-image: linear-gradient(315deg, #6a11cb 0%, #2575fc 74%);
        color: white;
        padding: 10px 24px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        filter: brightness(1.1);
        transform: scale(1.03);
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# ========== GAME 1 ==========
if selected_game == "Kuis Tabel Periodik":
    st.title("🧪 Kuis Tabel Periodik Unsur")

    periodic_table = [
        {"name": "hidrogen", "symbol": "H", "number": 1, "group": 1, "period": 1},
        {"name": "helium", "symbol": "He", "number": 2, "group": 18, "period": 1},
        {"name": "litium", "symbol": "Li", "number": 3, "group": 1, "period": 2},
        {"name": "berilium", "symbol": "Be", "number": 4, "group": 2, "period": 2},
        {"name": "karbon", "symbol": "C", "number": 6, "group": 14, "period": 2},
        {"name": "oksigen", "symbol": "O", "number": 8, "group": 16, "period": 2},
        {"name": "natrium", "symbol": "Na", "number": 11, "group": 1, "period": 3},
        {"name": "kalsium", "symbol": "Ca", "number": 20, "group": 2, "period": 4},
    ]

    for key in ["pt_score", "pt_index", "pt_question", "pt_feedback", "pt_answered"]:
        if key not in st.session_state:
            st.session_state[key] = 0 if "score" in key or "index" in key else None

    def get_pt_question():
        element = random.choice(periodic_table)
        q_type = random.choice(["symbol", "number", "group", "period"])
        return {"element": element, "type": q_type}

    if st.session_state.pt_index < 5:
        if not st.session_state.pt_question:
            st.session_state.pt_question = get_pt_question()
            st.session_state.pt_answered = False

        q = st.session_state.pt_question
        e = q["element"]

        if q["type"] == "symbol":
            question_text = f"🧪 Apa simbol dari unsur *{e['name'].capitalize()}*?"
            correct = e["symbol"]
        elif q["type"] == "number":
            question_text = f"🔢 Berapa nomor atom dari *{e['name'].capitalize()}*?"
            correct = str(e["number"])
        elif q["type"] == "group":
            question_text = f"📚 Golongan berapa unsur *{e['name'].capitalize()}*?"
            correct = str(e["group"])
        else:
            question_text = f"📏 Periode berapa unsur *{e['name'].capitalize()}*?"
            correct = str(e["period"])

        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.pt_index + 1}")
        answer = st.text_input(question_text, key=f"pt_input_{st.session_state.pt_index}")

        if st.button("Kirim Jawaban", key=f"pt_submit_{st.session_state.pt_index}") and not st.session_state.pt_answered:
            if answer.strip().lower() == correct.lower():
                st.session_state.pt_score += 1
                st.session_state.pt_feedback = "✅ Benar!"
                st.balloons()
            else:
                st.session_state.pt_feedback = f"❌ Salah. Jawaban benar:




