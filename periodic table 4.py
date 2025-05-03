import streamlit as st
import random

# Daftar contoh unsur (bisa diperluas)
periodic_table = [
    {"name": "hidrogen", "symbol": "H", "number": 1, "group": 1, "period": 1},
    {"name": "helium", "symbol": "He", "number": 2, "group": 18, "period": 1},
    {"name": "litium", "symbol": "Li", "number": 3, "group": 1, "period": 2},
    {"name": "berilium", "symbol": "Be", "number": 4, "group": 2, "period": 2},
    {"name": "boron", "symbol": "B", "number": 5, "group": 13, "period": 2},
    {"name": "karbon", "symbol": "C", "number": 6, "group": 14, "period": 2},
    {"name": "nitrogen", "symbol": "N", "number": 7, "group": 15, "period": 2},
    {"name": "oksigen", "symbol": "O", "number": 8, "group": 16, "period": 2},
    {"name": "fluorin", "symbol": "F", "number": 9, "group": 17, "period": 2},
    {"name": "neon", "symbol": "Ne", "number": 10, "group": 18, "period": 2},
    {"name": "natrium", "symbol": "Na", "number": 11, "group": 1, "period": 3},
    {"name": "magnesium", "symbol": "Mg", "number": 12, "group": 2, "period": 3},
    {"name": "aluminium", "symbol": "Al", "number": 13, "group": 13, "period": 3},
    {"name": "silikon", "symbol": "Si", "number": 14, "group": 14, "period": 3},
    {"name": "fosfor", "symbol": "P", "number": 15, "group": 15, "period": 3},
    {"name": "belerang", "symbol": "S", "number": 16, "group": 16, "period": 3},
    {"name": "klorin", "symbol": "Cl", "number": 17, "group": 17, "period": 3},
    {"name": "argon", "symbol": "Ar", "number": 18, "group": 18, "period": 3},
    {"name": "kalium", "symbol": "K", "number": 19, "group": 1, "period": 4},
    {"name": "kalsium", "symbol": "Ca", "number": 20, "group": 2, "period": 4},
    {"name": "skandium", "symbol": "Sc", "number": 21, "group": 3, "period": 4},
    {"name": "titanium", "symbol": "Ti", "number": 22, "group": 4, "period": 4},
    {"name": "vanadium", "symbol": "V", "number": 23, "group": 5, "period": 4},
    {"name": "chromium", "symbol": "Cr", "number": 24, "group": 6, "period": 4},
    {"name": "mangan", "symbol": "Mn", "number": 25, "group": 7, "period": 4},
    {"name": "besi", "symbol": "Fe", "number": 26, "group": 8, "period": 4},
    {"name": "kobalt", "symbol": "Co", "number": 27, "group": 9, "period": 4},
    {"name": "nikel", "symbol": "Ni", "number": 28, "group": 10, "period": 4},
    {"name": "tembaga", "symbol": "Cu", "number": 29, "group": 11, "period": 4},
    {"name": "zinc", "symbol": "Zn", "number": 30, "group": 12, "period": 4},
    {"name": "gallium", "symbol": "Ga", "number": 31, "group": 13, "period": 4},
    {"name": "germanium", "symbol": "Ge", "number": 32, "group": 14, "period": 4},
    {"name": "arsen", "symbol": "As", "number": 33, "group": 15, "period": 4},
    {"name": "selenium", "symbol": "Se", "number": 34, "group": 16, "period": 4},
    {"name": "bromine", "symbol": "Br", "number": 35, "group": 17, "period": 4},
    {"name": "krypton", "symbol": "Kr", "number": 36, "group": 18, "period": 4},
    {"name": "rubidium", "symbol": "Rb", "number": 37, "group": 1, "period": 5},
    {"name": "strontium", "symbol": "Sr", "number": 38, "group": 2, "period": 5},
    {"name": "yttrium", "symbol": "Y", "number": 39, "group": 3, "period": 5},
    {"name": "zirconium", "symbol": "Zr", "number": 40, "group": 4, "period": 5}
]

# Inisialisasi session state jika belum ada
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_num' not in st.session_state:
    st.session_state.question_num = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

def generate_question():
    element = random.choice(periodic_table)
    question_type = random.choice(["symbol", "number", "group", "period"])
    return {"element": element, "type": question_type}

st.title("🔬 Kuis Tabel Periodik")

if st.session_state.question_num < 5:
    # Generate a new question if needed
    if st.session_state.current_question is None:
        st.session_state.current_question = generate_question()

    # Ensure the current question exists before trying to access it
    if st.session_state.current_question:
        q = st.session_state.current_question
        e = q["element"]
        q_text = ""
        correct_answer = ""

        # Check the type of question and set the appropriate question text and correct answer
        if q["type"] == "symbol":
            q_text = f"Apa simbol dari unsur '{e['name'].capitalize()}'?"
            correct_answer = e["symbol"]
        elif q["type"] == "number":
            q_text = f"Berapa nomor atom dari '{e['name'].capitalize()}'?"
            correct_answer = str(e["number"])
        elif q["type"] == "group":
            q_text = f"Golongan berapa unsur '{e['name'].capitalize()}'?"
            correct_answer = str(e["group"])
        elif q["type"] == "period":
            q_text = f"Periode berapa unsur '{e['name'].capitalize()}'?"
            correct_answer = str(e["period"])

        user_input = st.text_input(q_text, key=f"question_{st.session_state.question_num}")

        if st.button("Kirim Jawaban"):
            if user_input.strip().lower() == correct_answer.lower():
                st.session_state.score += 1
                st.session_state.feedback = "✅ Benar!"
            else:
                st.session_state.feedback = f"❌ Salah. Jawaban yang benar: {correct_answer}"

            # Proceed to next question and generate a new one
            st.session_state.question_num += 1
            st.session_state.current_question = None  # Reset the current question for the next one

# Display the score and feedback
st.markdown(f"### Skor: {st.session_state.score}/5")
st.write(st.session_state.feedback)

# End of quiz
if st.session_state.question_num >= 5:
    st.success(f"🎉 Kuis selesai! Skor akhir kamu: {st.session_state.score}/5")
    if st.button("Main Lagi"):
        # Reset session state variables
        for key in ["score", "question_num", "current_question", "feedback"]:
            if key == "score" or key == "question_num":
                st.session_state[key] = 0
            else:
                st.session_state[key] = None

import streamlit as st
import random

# Data unsur (dipangkas untuk contoh)
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

# Styling aesthetic & ramai
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(to right, #a1c4fd, #c2e9fb);
        color: #333;
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

st.title("🎉 Kuis Tabel Periodik Unsur")

# Progress bar
progress = st.progress(st.session_state.question_num / 5)

# Soal generator
def generate_question():
    element = random.choice(periodic_table)
    question_type = random.choice(["symbol", "number", "group", "period"])
    return {"element": element, "type": question_type}

# Tampilan pertanyaan
if st.session_state.question_num < 5:
    if st.session_state.current_question is None:
        st.session_state.current_question = generate_question()
        st.session_state.answer_submitted = False

    q = st.session_state.current_question
    e = q["element"]
    correct_answer = ""

    # Soal
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
                st.balloons()  # 🎈 Kejutan animasi
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

# Selesai kuis
else:
    st.success(f"🎉 Kuis selesai! Skor akhir kamu: {st.session_state.score}/5")
    if st.button("🔁 Main Lagi"):
        for key in ["score", "question_num", "current_question", "feedback", "answer_submitted"]:
            del st.session_state[key]
