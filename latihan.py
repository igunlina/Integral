import streamlit as st

def main():
    # Menu di sidebar
    menu = st.sidebar.radio("INTEGRAL", ["Indefinite Integral", "Review Turunan", "Definisi", "Rumus Dasar Integral", "Integral Trigonometri", "Sifat Kelinieran Integral", "Teknik Integrasi", "latihan"])
   
    if menu == "latihan":
        st.title('BISMILLAH')
        st.header('MARI BELAJAR INTEGRAL TAK TENTU (INDEFINITE INTEGRAL/PRIMITIVE\ANTIDERIVATIVE)')
        
        # Pertanyaan 1
        answer_1 = st.radio("Tentukan primitive dari fungsi $f(x)=2x$", ["$F(x)=x^2$", "$F(x)=2x^2$", "$F(x)=4$"]) 
        # Pertanyaan 2
        answer_2 = st.radio("Tentukan primitive dari fungsi $f(x)=x^2$", ["$F(x)= \\frac{1}{3} x^3$", "$F(x)=2x$", "$F(x)=\\frac{1}{2} x^2$"])

        # Pertanyaan 3
        answer_3 = st.radio("Tentukan primitive dari fungsi $f(x)=0$", ["$F(x)=0$", "$F(x)=C \in \mathbb{R}$", "$F(x)=3x^2$"])
        # Tombol Kuis
        if st.button("submit"):
            check_definisi_answers(answer_1, answer_2, answer_3)
            
def check_definisi_answers(answer_1, answer_2, answer_3):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$F(x)=x^2$": "Benar", "$F(x)= \\frac{1}{3} x^3$": "Benar", "$F(x)=0$": "Benar"}

    if answer_1 in correct_answers and answer_2 in correct_answers and answer_3 in correct_answers:
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")









if __name__ == '__main__':
    main()
