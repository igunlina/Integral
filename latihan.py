import streamlit as st

def main():
    # Menu di sidebar
    menu = st.sidebar.radio("INTEGRAL", ["Indefinite Integral", "Review Turunan", "Definisi", "Rumus Dasar Integral", "Integral Trigonometri", "Sifat Kelinieran Integral", "Teknik Integrasi", "latihan"])
   
    if menu == "latihan":
        st.title('BISMILLAH')
        st.header('MARI BELAJAR INTEGRAL TAK TENTU (INDEFINITE INTEGRAL/PRIMITIVE\ANTIDERIVATIVE)')
        
        answer_1 = st.radio("Tentukan primitive dari fungsi $f(x)=2x$", ["$F(x)=x^2$", "$F(x)=2x^2$", "$F(x)=4$"]) 
        # Tombol Kuis
        if st.button("submit"):
            check_latihan_answers(answer_1)
            #run_latihan_quiz()

def run_latihan_quiz():
    # Pertanyaan 1
    answer_1 = st.radio("Tentukan primitive dari fungsi $f(x)=2x$", ["$F(x)=x^2$", "$F(x)=2x^2$", "$F(x)=4$"])
 
    # Tombol Submit
    submitted = st.button("Submit")
    if st.button("submit"):
        check_latihan_answers(answer_1)
        st.title('lewat sini')
    if submitted:
        st.title('lewat sini')
        check_latihan_answers(answer_1)

def check_latihan_answers(answer_1):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$F(x)=x^2$": "Benar"}

    if answer_1 in correct_answers :
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")
