import streamlit as st
import random

# --- Pilih game di sidebar ---
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# --- CSS untuk background gambar dan transparansi konten ---
st.markdown("""
    <style>
    /* Background gambar pada seluruh aplikasi */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1592928832749-b90e32bc4fd9?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    /* Buat semua panel konten transparan agar background terlihat */
    [data-testid="stAppViewContainer"] .main {
        background-color: transparent !important;
    }
    [data-testid="stAppViewContainer"] .css-1d391kg, /* block-container */
    [data-testid="stAppViewContainer"] .css-18e3th9 { /* app view container inner */
        background-color: transparent !important;
    }

    /* Styling kartu soal */
    .question-card {
        background: rgba(255,255,255,0.85);
        padding: 20px;
        border-radius: 15px;
        color: #000;
        margin-bottom: 20px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.3);
    }
    /* Styling kotak skor */
    .score-box {
        background: rgba(0,0,0,0.6);
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-top: 15px;
    }
    /* Input putih dengan teks hitam */
    .stTextInput > div > div > input {
        background-color: white !important;
        color: black !important;
    }
    /* Tombol custom */
    .stButton>button {
        background: linear-gradient(to right, #00c6ff, #0072ff);
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        filter: brightness(1.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- Data soal ---
periodic_questions = [
    {"name":"hidrogen","symbol":"H","number":1,"group":1,"period":1},
    {"name":"helium","symbol":"He","number":2,"group":18,"period":1},
    {"name":"litium","symbol":"Li","number":3,"group":1,"period":2},
    {"name":"berilium","symbol":"Be","number":4,"group":2,"period":2},
    {"name":"oksigen","symbol":"O","number":8,"group":16,"period":2},
]
organic_questions = [
    {"question":"Apa rumus molekul dari metana?","answer":"CH4"},
    {"question":"Apa gugus fungsi dari alkohol?","answer":"OH"},
    {"question":"Apa nama senyawa CH3COOH?","answer":"Asam asetat"},
    {"question":"Apa rumus dari etena?","answer":"C2H4"},
    {"question":"Apa nama senyawa CH3CH2CH2OH?","answer":"Propanol"},
]

# ===== Kuis Tabel Periodik =====
if selected_game == "Kuis Tabel Periodik":
    # session state init
    for k,v in [("score",0),("question_num",0),("current",None),("feedback",""),("answered",False)]:
        if k not in st.session_state:
            st.session_state[k] = v

    st.title("🧪 Kuis Tabel Periodik")
    st.progress(st.session_state.question_num/5)

    def next_q():
        elm = random.choice(periodic_questions)
        typ = random.choice(["symbol","number","group","period"])
        return {"elm":elm,"type":typ}

    if st.session_state.question_num<5:
        if st.session_state.current is None:
            st.session_state.current = next_q()
            st.session_state.answered = False

        q = st.session_state.current
        e = q["elm"]
        mapping = {
            "symbol": (f"Apa simbol dari unsur {e['name'].capitalize()}?", e["symbol"]),
            "number": (f"Berapa nomor atom dari {e['name'].capitalize()}?", str(e["number"])),
            "group":  (f"Golongan berapa unsur {e['name'].capitalize()}?", str(e["group"])),
            "period": (f"Periode berapa unsur {e['name'].capitalize()}?", str(e["period"]))
        }
        text,ans = mapping[q["type"]]

        st.markdown('<div class="question-card">',unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.question_num+1}")
        user=st.text_input(text,key=f"in_{st.session_state.question_num}")
        if st.button("Kirim Jawaban") and not st.session_state.answered:
            if user.strip().lower()==ans.lower():
                st.session_state.score+=1
                st.session_state.feedback="✅ Benar!"
                st.balloons()
            else:
                st.session_state.feedback=f"❌ Salah. Jawaban: *{ans}*"
            st.session_state.answered=True
        st.write(st.session_state.feedback)
        if st.session_state.answered and st.button("➡️ Lanjut"):
            st.session_state.question_num+=1
            st.session_state.current=None
            st.session_state.feedback=""
            st.session_state.answered=False
        st.markdown('</div>',unsafe_allow_html=True)
        st.markdown(f'<div class="score-box">Skor: {st.session_state.score}/5</div>',unsafe_allow_html=True)
    else:
        st.success(f"🎉 Selesai! Skor akhir: {st.session_state.score}/5")
        if st.button("🔁 Ulangi"):
            for k in ["score","question_num","current","feedback","answered"]:
                del st.session_state[k]

# ===== Kuis Kimia Organik =====
else:
    st.title("🧬 Kuis Kimia Organik")
    # session state init
    for k,v in [("org_i",0),("org_score",0),("org_fb",""),("org_ans",False)]:
        if k not in st.session_state:
            st.session_state[k]=v

    if st.session_state.org_i < 5:
        q=organic_questions[st.session_state.org_i]
        st.markdown('<div class="question-card">',unsafe_allow_html=True)
        ua=st.text_input(q["question"],key=f"o_{st.session_state.org_i}")
        if st.button("Kirim Jawaban") and not st.session_state.org_ans:
            if ua.strip().lower()==q["answer"].lower():
                st.session_state.org_score+=1
                st.session_state.org_fb="✅ Benar!"
                st.balloons()
            else:
                st.session_state.org_fb=f"❌ Salah. Jawaban: *{q['answer']}*"
            st.session_state.org_ans=True
        st.write(st.session_state.org_fb)
        if st.session_state.org_ans and st.button("➡️ Lanjut"):
            st.session_state.org_i+=1
            st.session_state.org_fb=""
            st.session_state.org_ans=False
        st.markdown('</div>',unsafe_allow_html=True)
        st.markdown(f'<div class="score-box">Skor: {st.session_state.org_score}/5</div>',unsafe_allow_html=True)
    else:
        st.success(f"🎉 Selesai! Skor akhir: {st.session_state.org_score}/5")
        if st.button("🔁 Ulangi"):
            for k in ["org_i","org_score","org_fb","org_ans"]:
                del st.session_state[k]














