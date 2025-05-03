import streamlit as st
import random

# Sidebar untuk memilih game
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# Styling aesthetic & background dengan gambar kimia
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: white;
    }

    .stApp {
        background-image: url('https://cdn.pixabay.com/photo/2020/03/14/08/52/chemistry-4928952_1280.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .question-card {
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(8px);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
    }

    .score-box {
        background: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(6px);
        padding: 15px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        color: white;
        margin-top: 10px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
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

    .stTextInput>div>div>input {
        background-color: white;
        color: black;
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Data untuk kuis tabel periodik (5 soal)
periodic_questions = [
    {"name": "hidrogen", "symbol": "H", "number": 1, "group": 1, "period": 1},
    {"name": "helium", "symbol": "He", "number": 2, "group": 18, "period": 1},
    {"name": "litium", "symbol": "Li", "number": 3, "group": 1, "period": 2},
    {"name": "berilium", "symbol": "Be", "number": 4, "group": 2, "period": 2},
    {"name": "oksigen", "symbol": "O", "number": 8, "group": 16, "period": 2},
]

# Data untuk kuis kimia organik (5 soal)
organic_questions = [
    {"question": "Apa rumus molekul dari metana?", "answer": "CH4"},
    {"question": "Apa gugus fungsi dari alkohol?", "answer": "OH"},
    {"question": "Apa nama senyawa CH3COOH?", "answer": "Asam asetat"},
    {"question": "Apa rumus dari etena?", "answer": "C2H4"},
    {"question": "Apa nama senyawa CH3CH2CH2OH?", "answer": "Propanol"},
]

# ========== KUIS TABEL PERIODIK ==========
if selected_game == "Kuis Tabel Periodik":
    for key, default in {
        "score": 0,
        "question_num": 0,
        "current_question": None,
        "feedback": "",
        "answer_submitted": False
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    st.title("🧪 Kuis Tabel Periodik Unsur")
    st.progress(st.session_state.question_num / 5)

    def generate_periodic_question():
        element = random.choice(periodic_questions)
        qtype = random.choice(["symbol", "number", "group", "period"])
        return {"element": element, "type": qtype}

    if st.session_state.question_num < 5:
        if st.session_state.current_question is None:
            st.session_state.current_question = generate_periodic_question()
            st.session_state.answer_submitted = False

        q = st.session_state.current_question
        e = q["element"]

        question_text, correct_answer = {
            "symbol": (f"Apa simbol dari unsur *{e['name'].capitalize()}*?", e["symbol"]),
            "number": (f"Berapa nomor atom dari *{e['name'].capitalize()}*?", str(e["number"])),
            "group": (f"Golongan berapa unsur *{e['name'].capitalize()}*?", str(e["group"])),
            "period": (f"Periode berapa unsur *{e['name'].capitalize()}*?", str(e["period"]))
        }[q["type"]]

        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.question_num + 1}")
        user_input = st.text_input(question_text, key=f"input_{st.session_state.question_num}")

        if st.button("Kirim Jawaban") and not st.session_state.answer_submitted:
            if user_input.strip().lower() == correct_answer.lower():
                st.session_state.score += 1
                st.session_state.feedback = "✅ Benar!"
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
        st.markdown(f"<div class='score-box'>⭐ Skor: {st.session_state.score}/5</div>", unsafe_allow_html=True)
    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.score}/5")
        if st.button("🔁 Main Lagi"):
            for key in ["score", "question_num", "current_question", "feedback", "answer_submitted"]:
                del st.session_state[key]

# ========== KUIS KIMIA ORGANIK ==========
elif selected_game == "Kuis Kimia Organik":
    st.title("🧬 Kuis Kimia Organik")

    if "organic_score" not in st.session_state:
        st.session_state.organic_score = 0
        st.session_state.organic_index = 0
        st.session_state.organic_feedback = ""
        st.session_state.organic_submitted = False

    if st.session_state.organic_index < len(organic_questions):
        q = organic_questions[st.session_state.organic_index]
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
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
            if st.button("➡️ Soal Berikutnya", key=f"next_{st.session_state.organic_index}"):
                st.session_state.organic_index += 1
                st.session_state.organic_feedback = ""
                st.session_state.organic_submitted = False
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'>⭐ Skor: {st.session_state.organic_score}/5</div>", unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.organic_score}/5")
        if st.button("🔁 Ulangi"):
            for key in ["organic_score", "organic_index", "organic_feedback", "organic_submitted"]:
                del st.session_state[key]












