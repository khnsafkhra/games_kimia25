import streamlit as st
import random

# Styling aesthetic background dengan gambar kimia dan teks input putih tulisannya hitam
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

    .stApp {
        background-image: url('https://images.unsplash.com/photo-1581090700227-1e8a0c40a2c8?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }
    .question-card {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 20px;
        box-shadow: 4px 4px 30px rgba(0,0,0,0.2);
        margin-bottom: 25px;
        animation: fadeIn 1s ease-in-out;
        color: #fff;
    }
    .score-box {
        background: rgba(0,0,0,0.35);
        backdrop-filter: blur(10px);
        padding: 15px; border-radius: 12px;
        font-size: 18px; font-weight: 600;
        text-align: center; color: white;
        margin-top: 10px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; padding: 10px 24px;
        border-radius: 10px; border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        filter: brightness(1.1); transform: scale(1.03);
    }
    .stTextInput>div>div>input {
        background-color: #fff !important;
        color: #000 !important;
        border: 1px solid #ccc; border-radius: 10px;
    }
    @keyframes fadeIn {
        from {opacity:0; transform:translateY(20px);}
        to {opacity:1; transform:translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("\U0001F3AE Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# Game 1: Kuis Tabel Periodik
if selected_game == "Kuis Tabel Periodik":
    st.title("\U0001F389 Kuis Tabel Periodik Unsur")
    periodic_table = [
        {"name": "hidrogen", "symbol": "H", "number": 1, "group": 1, "period": 1},
        {"name": "helium", "symbol": "He", "number": 2, "group": 18, "period": 1},
        {"name": "litium", "symbol": "Li", "number": 3, "group": 1, "period": 2},
        {"name": "berilium", "symbol": "Be", "number": 4, "group": 2, "period": 2},
        {"name": "karbon", "symbol": "C", "number": 6, "group": 14, "period": 2},
    ]

    for key, default in {
        "score": 0, "question_num": 0, "current_question": None, "feedback": "", "answer_submitted": False
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

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

        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.question_num + 1}")
        user_input = st.text_input(question_text, key=f"input_{st.session_state.question_num}")

        if st.button("Kirim Jawaban") and not st.session_state.answer_submitted:
            if user_input.strip().lower() == correct_answer.lower():
                st.session_state.score += 1
                st.session_state.feedback = random.choice([
                    "✅ Jawaban Benar! Hebat!",
                    "\U0001F389 Mantap! Kamu benar!",
                    "\U0001F525 Jawaban tepat! Good job!",
                    "\U0001F4A1 Cerdas sekali!",
                    "\U0001F44F Kamu jenius!"
                ])
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
        st.markdown(f"<div class='score-box'>\U0001F31F Skor Sementara: {st.session_state.score}/5</div>", unsafe_allow_html=True)
    else:
        st.success(f"\U0001F389 Kuis selesai! Skor akhir kamu: {st.session_state.score}/5")
        if st.button("🔁 Main Lagi"):
            for key in ["score", "question_num", "current_question", "feedback", "answer_submitted"]:
                del st.session_state[key]

# Game 2: Kuis Kimia Organik
elif selected_game == "Kuis Kimia Organik":
    st.title("\U0001F9EA Kuis Kimia Organik")
    questions = [
        {"question": "Apa rumus molekul dari metana?", "answer": "CH4"},
        {"question": "Apa gugus fungsi dari alkohol?", "answer": "OH"},
        {"question": "Apa nama senyawa CH3COOH?", "answer": "Asam asetat"},
        {"question": "Apa nama senyawa dengan rumus C2H5OH?", "answer": "Etanol"},
        {"question": "Apa rumus dari etena?", "answer": "C2H4"}
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







