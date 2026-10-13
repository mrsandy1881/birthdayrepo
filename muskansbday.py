
import streamlit as st
import os

# ----------------------------------------
# PAGE SETTINGS
# ----------------------------------------
st.set_page_config(
    page_title="A Little Magic for Muskan 💗",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------
# AESTHETIC STYLING
# ----------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at top left, #ffe2ef 0%, transparent 45%),
        radial-gradient(ellipse at bottom right, #e6ddff 0%, transparent 45%),
        linear-gradient(145deg, #fff7fb, #f8f3ff 55%, #fff4f5);
    color: #593c58;
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 760px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    text-align: center;
    padding: 30px 16px 18px;
}

.eyebrow {
    display: inline-block;
    padding: 8px 15px;
    border: 1px solid #f1c6dc;
    background: rgba(255,255,255,0.65);
    border-radius: 40px;
    color: #a45682;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero h1 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(38px, 7vw, 62px);
    line-height: 1.15;
    color: #854d79;
    margin: 24px 0 12px;
}

.hero p {
    font-size: 16px;
    color: #8f6d8b;
    line-height: 1.8;
}

.photo-frame {
    padding: 10px;
    border-radius: 28px;
    background: linear-gradient(135deg, #f6c7df, #d7c7ff, #ffe4c9);
    box-shadow: 0 15px 45px rgba(155, 94, 145, 0.15);
    margin: 12px auto 24px;
}

.countdown-card, .letter-card {
    background: rgba(255,255,255,0.78);
    border: 1px solid rgba(227,190,219,0.8);
    border-radius: 26px;
    padding: 25px 22px;
    text-align: center;
    box-shadow: 0 12px 35px rgba(139,88,139,0.08);
    margin: 18px 0;
}

.letter-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 34px;
    line-height: 1.4;
    color: #934f7d;
}

.letter-text {
    font-size: 16px;
    line-height: 2;
    color: #765a75;
    text-align: center;
}

.sparkle {
    text-align: center;
    font-size: 27px;
    letter-spacing: 12px;
    animation: twinkle 2s ease-in-out infinite alternate;
}

@keyframes twinkle {
    from { opacity: .55; transform: translateY(0); }
    to { opacity: 1; transform: translateY(-4px); }
}

.heart {
    display: inline-block;
    animation: heartbeat 1.5s ease-in-out infinite;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.16); }
}

div.stButton > button {
    border: 0;
    border-radius: 40px;
    padding: 12px 25px;
    color: white;
    background: linear-gradient(100deg, #d77cae, #9c83d8);
    font-weight: 600;
    box-shadow: 0 8px 22px rgba(171,106,166,.22);
}

div.stButton > button:hover {
    color: white;
    border: 0;
    transform: translateY(-2px);
}

div[data-testid="stImage"] img {
    border-radius: 20px;
}

.footer-note {
    text-align: center;
    color: #a58ba4;
    font-size: 12px;
    letter-spacing: 1px;
    padding: 22px 0 8px;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .letter-card {
        padding: 22px 16px;
    }
    .letter-text {
        font-size: 15px;
    }
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# HERO SECTION
# ----------------------------------------
st.markdown("""
<div class="hero">
    <div class="sparkle">✧ ⋆ ✧</div>
    <span class="eyebrow">A little birthday magic</span>
    <h1>For Muskan <span class="heart">💗</span></h1>
    <p>
        Some people make ordinary days feel special.<br>
        Today, this little corner of the internet is all yours.
    </p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------
# MUSKAN'S PHOTO
# ----------------------------------------
if os.path.exists("muskan.jpg"):
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("muskan.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning(
        "Photo not found. Keep muskan.jpg in the same folder "
        "as muskansbday.py."
    )

# ----------------------------------------
# BIRTHDAY REVEAL - PREVIEW
# ----------------------------------------
st.balloons()

st.markdown("""
<div class="letter-card">
    <div class="sparkle">✧ 💗 ✧</div>

    <div class="letter-title">
        Happy Birthday,<br>Muskan! 🎂
    </div>

    <p class="letter-text">
        Today is all about you and the happiness you bring
        to the people around you. 💕<br><br>

        May your new year of life be filled with beautiful
        surprises, genuine smiles, exciting opportunities,
        peaceful days, and memories you'll always treasure. 🌷<br><br>

        Keep being your lovely, unique self.
        Never stop smiling, dreaming, or being the wonderful
        person you are. You deserve all the happiness
        life has to offer. ✨<br><br>

        Thank you for being such a wonderful friend.
        I hope this little surprise makes you smile today! 💌
    </p>

    <div class="letter-title" style="font-size:25px;">
        With lots of wishes,<br>
        Sandy <span class="heart">💖</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.snow()

# ----------------------------------------
# FOOTER
# ----------------------------------------
st.markdown("""
<div class="sparkle">♡ ✧ ♡</div>
<div class="footer-note">
    MADE WITH 💗 BY SANDY<br>
    A LITTLE MEMORY TO KEEP
</div>
""", unsafe_allow_html=True)
