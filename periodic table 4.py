import streamlit as st
import random

# --- Styling Aesthetic ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://cdn.pixabay.com/photo/2017/08/30/07/52/science-2694183_1280.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        color: #333;
    }

    .question-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(6px);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 0 25px rgba(0, 0, 0, 0.15);
        margin-bottom: 25px;
        color: #000;
    }

    .score-box {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(4px);
        padding: 15px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        color: #000;
        margin-top: 10px;
    }

    .stTextInput>div>div>input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc;
        border-radius: 10px;
    }

    .stButton>button {
        background: linear-gradient(to right, #64b5f6, #ba68c8);
        color: white;
        padding: 10px 24px;
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        filter: brightness(1.1);
        transform: scale(1.03);
    }

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("\U0001F3AE Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# Kuis Tabel Periodik
if selected_game == "Kuis Tabel Periodik":
    periodic_table = [
        {"name": "hidrogen", "symbol": "H", "number": 1, "group": 1, "period": 1},
        {"name": "helium", "symbol": "He", "number": 2, "group": 18, "period": 1},
        {"name": "litium", "symbol": "Li", "number": 3, "group": 1, "period": 2},
        {"name": "berilium", "symbol": "Be", "number": 4, "group": 2, "period": 2},
        {"name": "karbon", "symbol": "C", "number": 6, "group": 14, "period": 2},
    ]

    for key, default in {
        "score": 0,
        "question_num": 0,
        "current_question": None,
        "feedback": "",
        "answer_submitted": False
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    st.title("\U0001F389 Kuis Tabel Periodik Unsur")
    progress = st.progress(st.session_state.question_num / 5)

    def generate_question():
        element = random.choice(periodic_table)
        question_type = random.choice(["symbol", "number", "group", "period"])
        return {"element": element, "type": question_type}

    if st.session_state.question_num < 5:
        if st.session_state.current_question is None:
            st.session_state.current_question = generate_question()
            st.session_state.answer_submitted = False

        q = st.session_state.current_question
        e = q["element"]

        if q["type"] == "symbol":
            question_text = f"\U0001F9EA Apa simbol dari unsur *{e['name'].capitalize()}*?"
            correct_answer = e["symbol"]
        elif q["type"] == "number":
            question_text = f"\U0001F522 Berapa nomor atom dari *{e['name'].capitalize()}*?"
            correct_answer = str(e["number"])
        elif q["type"] == "group":
            question_text = f"\U0001F4DA Golongan berapa unsur *{e['name'].capitalize()}*?"
            correct_answer = str(e["group"])
        elif q["type"] == "period":
            question_text = f"\U0001F4CF Periode berapa unsur *{e['name'].capitalize()}*?"
            correct_answer = str(e["period"])

        with st.container():
            st.markdown('<div class="question-card">', unsafe_allow_html=True)
            st.subheader(f"Soal #{st.session_state.question_num + 1}")
            user_input = st.text_input(question_text, key=f"input_{st.session_state.question_num}")

            if st.button("Kirim Jawaban") and not st.session_state.answer_submitted:
                if user_input.strip().lower() == correct_answer.lower():
                    st.session_state.score += 1
                    st.session_state.feedback = "✅ Jawaban Benar!"
                    st.balloons()
                else:
                    st.session_state.feedback = f"❌ Salah. Jawaban yang benar: *{correct_answer}*"
                st.session_state.answer_submitted = True

            st.write(st.session_state.feedback)

            if st.session_state.answer_submitted:
                if st.button("➡️ Soal Berikutnya"):
                    st.session_state.question_num += 1
                    st.session_state.current_question = None
                    st.session_state.feedback = ""
                    st.session_state.answer_submitted = False

            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f"<div class='score-box'>\U0001F31F Skor: {st.session_state.score}/5</div>", unsafe_allow_html=True)
    else:
        st.success(f"\U0001F389 Kuis selesai! Skor akhir kamu: {st.session_state.score}/5")
        if st.button("🔁 Main Lagi"):
            for key in ["score", "question_num", "current_question", "feedback", "answer_submitted"]:
                del st.session_state[key]

# Kuis Kimia Organik
elif selected_game == "Kuis Kimia Organik":
    st.title("\U0001F9EA Kuis Kimia Organik")

    questions = [
        {"question": "Apa rumus molekul dari metana?", "answer": "CH4"},
        {"question": "Apa gugus fungsi dari alkohol?", "answer": "OH"},
        {"question": "Apa nama senyawa CH3COOH?", "answer": "Asam asetat"},
        {"question": "Apa nama senyawa dengan rumus C2H5OH?", "answer": "Etanol"},
        {"question": "Apa nama gugus fungsi -COOH?", "answer": "Asam karboksilat"},
    ]

    if "organic_score" not in st.session_state:
        st.session_state.organic_score = 0
        st.session_state.organic_index = 0
        st.session_state.organic_feedback = ""
        st.session_state.organic_submitted = False

    if st.session_state.organic_index < len(questions):
        q = questions[st.session_state.organic_index]
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        user_answer = st.text_input(f"\U0001F52C {q['question']}", key=f"organic_input_{st.session_state.organic_index}")

        if st.button("Kirim Jawaban", key=f"submit_{st.session_state.organic_index}") and not st.session_state.organic_submitted:
            if user_answer.strip().lower() == q["answer"].lower():
                st.session_state.organic_score += 1
                st.session_state.organic_feedback = "✅ Benar!"
                st.balloons()
            else:
                st.session_state.organic_feedback = f"❌ Salah. Jawaban yang benar: *{q['answer']}*"
            st.session_state.organic_submitted = True

        st.write(st.session_state.organic_feedback)

        if st.session_state.organic_submitted:
            if st.button("➡️ Soal Berikutnya", key=f"next_{st.session_state.organic_index}"):
                st.session_state.organic_index += 1
                st.session_state.organic_feedback = ""
                st.session_state.organic_submitted = False
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.success(f"Kuis selesai! Skor akhir kamu: {st.session_state.organic_score}/{len(questions)}")
        if st.button("🔁 Ulangi"):
            for key in ["organic_score", "organic_index", "organic_feedback", "organic_submitted"]:
                del st.session_state[key]










