import streamlit as st
import random

# Pilih game
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# Tambahkan background image aesthetic
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1581090700227-1e8eedd41c08?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .stTextInput > div > div > input {
        background-color: white;
        color: black;
    }

    .question-card {
        background: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 15px;
        color: black;
        margin-bottom: 20px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.3);
    }

    .score-box {
        background: rgba(0,0,0,0.5);
        padding: 10px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-top: 15px;
    }

    .stButton>button {
        background-color: #0099cc;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
    }

    .stButton>button:hover {
        background-color: #0077aa;
    }
    </style>
""", unsafe_allow_html=True)

# Data soal
periodic_questions = [
    {"name": "hidrogen", "symbol": "H", "number": 1, "group": 1, "period": 1},
    {"name": "helium", "symbol": "He", "number": 2, "group": 18, "period": 1},
    {"name": "litium", "symbol": "Li", "number": 3, "group": 1, "period": 2},
    {"name": "berilium", "symbol": "Be", "number": 4, "group": 2, "period": 2},
    {"name": "oksigen", "symbol": "O", "number": 8, "group": 16, "period": 2},
]

organic_questions = [
    {"question": "Apa rumus molekul dari metana?", "answer": "CH4"},
    {"question": "Apa gugus fungsi dari alkohol?", "answer": "OH"},
    {"question": "Apa nama senyawa CH3COOH?", "answer": "Asam asetat"},
    {"question": "Apa rumus dari etena?", "answer": "C2H4"},
    {"question": "Apa nama senyawa CH3CH2CH2OH?", "answer": "Propanol"},
]

# ==== Kuis Tabel Periodik ====
if selected_game == "Kuis Tabel Periodik":
    for key in ["score", "question_num", "current_question", "feedback", "answer_submitted"]:
        if key not in st.session_state:
            st.session_state[key] = 0 if key in ["score", "question_num"] else None if key == "current_question" else ""

    st.title("🧪 Kuis Tabel Periodik")
    st.progress(st.session_state.question_num / 5)

    def generate_question():
        q = random.choice(periodic_questions)
        tipe = random.choice(["symbol", "number", "group", "period"])
        return {"element": q, "type": tipe}

    if st.session_state.question_num < 5:
        if st.session_state.current_question is None:
            st.session_state.current_question = generate_question()
            st.session_state.answer_submitted = False

        q = st.session_state.current_question
        e = q["element"]

        tanya, jawaban = {
            "symbol": (f"Apa simbol dari unsur {e['name'].capitalize()}?", e["symbol"]),
            "number": (f"Berapa nomor atom dari {e['name'].capitalize()}?", str(e["number"])),
            "group": (f"Golongan berapa unsur {e['name'].capitalize()}?", str(e["group"])),
            "period": (f"Periode berapa unsur {e['name'].capitalize()}?", str(e["period"]))
        }[q["type"]]

        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.question_num + 1}")
        user_input = st.text_input(tanya, key=f"input_{st.session_state.question_num}")

        if st.button("Kirim Jawaban") and not st.session_state.answer_submitted:
            if user_input.strip().lower() == jawaban.lower():
                st.session_state.score += 1
                st.session_state.feedback = "✅ Benar!"
                st.balloons()
            else:
                st.session_state.feedback = f"❌ Salah. Jawaban: *{jawaban}*"
            st.session_state.answer_submitted = True

        st.write(st.session_state.feedback)

        if st.session_state.answer_submitted:
            if st.button("➡️ Lanjut"):
                st.session_state.question_num += 1
                st.session_state.current_question = None
                st.session_state.feedback = ""

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="score-box">Skor: {st.session_state.score}/5</div>', unsafe_allow_html=True)

    else:
        st.success(f"🎉 Selesai! Skor akhir: {st.session_state.score}/5")
        if st.button("Ulangi"):
            for key in ["score", "question_num", "current_question", "feedback", "answer_submitted"]:
                del st.session_state[key]

# ==== Kuis Kimia Organik ====
else:
    st.title("🧬 Kuis Kimia Organik")

    for key in ["organic_index", "organic_score", "organic_feedback", "organic_submitted"]:
        if key not in st.session_state:
            st.session_state[key] = 0 if "index" in key or "score" in key else ""

    if st.session_state.organic_index < 5:
        q = organic_questions[st.session_state.organic_index]
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        user_answer = st.text_input(q["question"], key=f"org_input_{st.session_state.organic_index}")

        if st.button("Kirim Jawaban", key=f"submit_{st.session_state.organic_index}") and not st.session_state.organic_submitted:
            if user_answer.strip().lower() == q["answer"].lower():
                st.session_state.organic_score += 1
                st.session_state.organic_feedback = "✅ Benar!"
                st.balloons()
            else:
                st.session_state.organic_feedback = f"❌ Salah. Jawaban: *{q['answer']}*"
            st.session_state.organic_submitted = True

        st.write(st.session_state.organic_feedback)

        if st.session_state.organic_submitted:
            if st.button("➡️ Lanjut", key=f"next_{st.session_state.organic_index}"):
                st.session_state.organic_index += 1
                st.session_state.organic_feedback = ""
                st.session_state.organic_submitted = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="score-box">Skor: {st.session_state.organic_score}/5</div>', unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor: {st.session_state.organic_score}/5")
        if st.button("Ulangi"):
            for key in ["organic_index", "organic_score", "organic_feedback", "organic_submitted"]:
                del st.session_state[key]












