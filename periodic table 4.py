import streamlit as st
import random

# Sidebar untuk memilih game
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# Styling aesthetic & background merah
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: #ff4e4e;
        color: white;
    }

    .question-card {
        background: white;
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

# Game 1: Kuis Tabel Periodik
if selected_game == "Kuis Tabel Periodik":
    # Data unsur
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

    # Inisialisasi state
    for key, default in {
        "score": 0,
        "question_num": 0,
        "current_question": None,
        "feedback": "",
        "answer_submitted": False
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    st.title("🎉 Kuis Tabel Periodik Unsur")
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
        correct_answer = ""

        if q["type"] == "symbol":
            question_text = f"🧪 Apa simbol dari unsur *{e['name'].capitalize()}*?"
            correct_answer = e["symbol"]
        elif q["type"] == "number":
            question_text = f"🔢 Berapa nomor atom dari *{e['name'].capitalize()}*?"
            correct_answer = str(e["number"])
        elif q["type"] == "group":
            question_text = f"📚 Golongan berapa unsur *{e['name'].capitalize()}*?"
            correct_answer = str(e["group"])
        elif q["type"] == "period":
            question_text = f"📏 Periode berapa unsur *{e['name'].capitalize()}*?"
            correct_answer = str(e["period"])

        with st.container():
            st.markdown('<div class="question-card">', unsafe_allow_html=True)
            st.subheader(f"Soal #{st.session_state.question_num + 1}")
            user_input = st.text_input(question_text, key=f"input_{st.session_state.question_num}")

            if st.button("Kirim Jawaban") and not st.session_state.answer_submitted:
                if user_input.strip().lower() == correct_answer.lower():
                    st.session_state.score += 1
                    st.session_state.feedback = random.choice([
                        "✅ Jawaban Benar! Hebat!",
                        "🎉 Mantap! Kamu benar!",
                        "🔥 Jawaban tepat! Good job!",
                        "💡 Cerdas sekali!",
                        "👏 Kamu jenius!"
                    ])
                    st.balloons()
                    st.markdown("""
                        <audio autoplay>
                            <source src="https://www.soundjay.com/buttons/sounds/button-09.mp3" type="audio/mpeg">
                        </audio>
                    """, unsafe_allow_html=True)
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

        st.markdown(f"<div class='score-box'>🌟 Skor Sementara: {st.session_state.score}/5</div>", unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor akhir kamu: {st.session_state.score}/5")
        if st.button("🔁 Main Lagi"):
            for key in ["score", "question_num", "current_question", "feedback", "answer_submitted"]:
                del st.session_state[key]

# Game 2: Kuis Kimia Organik
elif selected_game == "Kuis Kimia Organik":
    st.title("🧪 Kuis Kimia Organik")

    questions = [
        {"question": "Apa rumus molekul dari metana?", "answer": "CH4"},
        {"question": "Apa gugus fungsi dari alkohol?", "answer": "OH"},
        {"question": "Apa nama senyawa CH3COOH?", "answer": "Asam asetat"},
    ]

    if "organic_score" not in st.session_state:
        st.session_state.organic_score = 0
        st.session_state.organic_index = 0
        st.session_state.organic_feedback = ""
        st.session_state.organic_done = False

    if st.session_state.organic_index < len(questions):
        q = questions[st.session_state.organic_index]
        user_answer = st.text_input(f"🔬 {q['question']}", key="organic_input")

        if st.button("Kirim Jawaban", key="organic_submit"):
            if user_answer.strip().lower() == q["answer"].lower():
                st.session_state.organic_score += 1
                st.session_state.organic_feedback = "✅ Benar!"
                st.balloons()
            else:
                st.session_state.organic_feedback = f"❌ Salah. Jawaban yang benar: *{q['answer']}*"
            st.session_state.organic_index += 1

        st.write(st.session_state.organic_feedback)
    else:
        st.success(f"Kuis selesai! Skor akhir kamu: {st.session_state.organic_score}/{len(questions)}")
        if st.button("🔁 Ulangi"):
            for key in ["organic_score", "organic_index", "organic_feedback"]:
                del st.session_state[key]

# Game 2: Kuis Kimia Organik
elif selected_game == "Kuis Kimia Organik":
    st.title("🧪 Kuis Kimia Organik")

    questions = [
        {"question": "Apa rumus molekul dari metana?", "answer": "CH4"},
        {"question": "Apa gugus fungsi dari alkohol?", "answer": "OH"},
        {"question": "Apa nama senyawa CH3COOH?", "answer": "Asam asetat"},
    ]

    if "organic_score" not in st.session_state:
        st.session_state.organic_score = 0
        st.session_state.organic_index = 0
        st.session_state.organic_feedback = ""
        st.session_state.organic_submitted = False

    if st.session_state.organic_index < len(questions):
        q = questions[st.session_state.organic_index]
        st.subheader(f"Soal #{st.session_state.organic_index + 1}")
        user_answer = st.text_input(f"🔬 {q['question']}", key=f"organic_input_{st.session_state.organic_index}")

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
            if st.button("➡️ Soal Berikutnya"):
                st.session_state.organic_index += 1
                st.session_state.organic_feedback = ""
                st.session_state.organic_submitted = False

        st.markdown(f"<div class='score-box'>🌟 Skor Sementara: {st.session_state.organic_score}/{len(questions)}</div>", unsafe_allow_html=True)
    else:
        st.success(f"Kuis selesai! Skor akhir kamu: {st.session_state.organic_score}/{len(questions)}")
        if st.button("🔁 Ulangi"):
            for key in ["organic_score", "organic_index", "organic_feedback", "organic_submitted"]:
                del st.session_state[key]
