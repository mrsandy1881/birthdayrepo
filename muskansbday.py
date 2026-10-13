
import streamlit as st
import time
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Muskan's Birthday Surprise 🎂",
    page_icon="🎁",
    layout="centered"
)

IST = ZoneInfo("Asia/Kolkata")
BIRTHDAY = datetime(2026, 10, 14, 0, 0, 0, tzinfo=IST)

# ---------------- BEAUTIFUL DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe0ec, #e8dfff, #c8e7ff);
}
h1, h2, h3, p {
    color: #873b76;
}
.hero {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #a52a72;
}
.card {
    background: rgba(255,255,255,0.85);
    padding: 25px;
    border-radius: 24px;
    text-align: center;
    color: #713b72;
    font-size: 19px;
    line-height: 1.8;
}
.countdown {
    text-align: center;
    background: rgba(255,255,255,0.8);
    padding: 25px;
    border-radius: 22px;
    font-size: 25px;
    font-weight: bold;
    color: #a52a72;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    '<div class="hero">🎁 A Special Surprise for Muskan 🎁</div>',
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center'>Made with ❤️ by Sandy</p>",
    unsafe_allow_html=True
)

photo = Path(__file__).parent / "muskan.jpg"

# ---------------- COUNTDOWN ----------------
countdown_box = st.empty()

while True:
    now = datetime.now(IST)
    remaining = int((BIRTHDAY - now).total_seconds())

    if remaining <= 0:
        countdown_box.empty()
        break

    days, remaining = divmod(remaining, 86400)
    hours, remaining = divmod(remaining, 3600)
    minutes, seconds = divmod(remaining, 60)

    countdown_box.markdown(f"""
    <div class="countdown">
        💖 Muskan's Birthday Countdown 💖
        <hr>
        🎂 {days} Days<br>
        ⏰ {hours:02d} Hours :
        {minutes:02d} Minutes :
        {seconds:02d} Seconds
        <p style="font-size:16px">
            The surprise will open at midnight! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1)

# ---------------- MIDNIGHT REVEAL ----------------
st.balloons()

st.markdown("""
<div class="hero">
    🎉 HAPPY BIRTHDAY, MUSKAN! 🎉
</div>
""", unsafe_allow_html=True)

if photo.exists():
    st.image(str(photo), use_container_width=True)
else:
    st.warning(
        "Photo not found. Add muskan.jpg beside app.py."
    )

st.markdown("""
<div class="card">
    💗 Dear Muskan 💗<br><br>

    Finally, the moment has arrived! 🎂✨<br><br>

    Wishing you a very Happy Birthday!
    May your life always be filled with happiness,
    success, love, laughter, and beautiful memories. 🌸<br><br>

    May every dream you have come true.
    Keep smiling, keep shining, and never stop being
    the wonderful person you are. 💫<br><br>

    I hope this new year of your life brings you
    countless reasons to smile and unforgettable moments.
    You deserve all the happiness in the world! 🎁<br><br>

    <b>Happy Birthday once again, Muskan! ❤️</b><br><br>

    With lots of best wishes,<br>
    <b>Your friend, Sandy 🫶</b>
</div>
""", unsafe_allow_html=True)

st.write("")
st.success("Your birthday surprise has been unlocked! 💖")
