
import streamlit as st
import streamlit.components.v1 as components
import os
import base64
import html

st.set_page_config(
    page_title="For Muskan 💗",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------
# LOAD MUSKAN'S PHOTO
# ---------------------------------
photo_path = "muskan.jpg"

if os.path.exists(photo_path):
    with open(photo_path, "rb") as f:
        photo_data = base64.b64encode(f.read()).decode("utf-8")

    extension = os.path.splitext(photo_path)[1].lower()
    mime = "image/png" if extension == ".png" else "image/jpeg"
    photo_src = f"data:{mime};base64,{photo_data}"
else:
    photo_src = ""

photo_section = (
    f'<img class="portrait" src="{photo_src}" alt="Muskan">'
    if photo_src
    else '<div class="photo-placeholder">📸<br>Add Muskan’s photo as muskan.jpg</div>'
)

# ---------------------------------
# WEBSITE
# ---------------------------------
page = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Arial, sans-serif;
    color: #713f68;
    background: transparent;
}

.page {
    overflow: hidden;
    position: relative;
    padding: 28px 16px 45px;
    text-align: center;
    border-radius: 28px;
    background:
      radial-gradient(circle at 10% 10%, #ffd5e8, transparent 35%),
      radial-gradient(circle at 90% 20%, #ded3ff, transparent 35%),
      linear-gradient(145deg, #fff7fb, #fff0f6, #f5efff);
}

.pill {
    display: inline-block;
    border: 1px solid #edc1dc;
    background: #ffffffb8;
    border-radius: 30px;
    padding: 9px 16px;
    font-size: 11px;
    letter-spacing: 2px;
    color: #a14e84;
}

h1 {
    font-family: Georgia, serif;
    font-size: clamp(38px, 8vw, 66px);
    margin: 20px 0 12px;
    line-height: 1.1;
    color: #a04d86;
}

.subtitle {
    max-width: 500px;
    margin: 0 auto 22px;
    line-height: 1.8;
    color: #936c90;
    font-size: 15px;
}

.decor {
    font-size: 24px;
    letter-spacing: 10px;
    animation: floaty 2.5s infinite alternate ease-in-out;
}

@keyframes floaty {
    to { transform: translateY(-8px); }
}

.photo-wrap {
    max-width: 340px;
    margin: 22px auto;
    padding: 8px;
    border-radius: 28px;
    background: linear-gradient(135deg, #ffb8da, #c9b9ff, #ffe2bc);
    box-shadow: 0 14px 35px #a56d9a30;
    animation: photoFloat 4s ease-in-out infinite;
}

.portrait {
    display: block;
    width: 100%;
    max-height: 430px;
    object-fit: cover;
    border-radius: 22px;
    animation: photoReveal 1.2s ease both;
}

@keyframes photoFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-7px); }
}

@keyframes photoReveal {
    from {
        opacity: 0;
        transform: scale(.95);
        filter: blur(4px);
    }
    to {
        opacity: 1;
        transform: scale(1);
        filter: blur(0);
    }
}

.photo-placeholder {
    padding: 75px 10px;
    border-radius: 22px;
    background: #fff7fb;
    line-height: 2;
}

.card {
    max-width: 590px;
    margin: 22px auto;
    padding: 26px 20px;
    border-radius: 26px;
    border: 1px solid #edcce5;
    background: #ffffffc9;
    box-shadow: 0 10px 32px #9c699515;
}

h2 {
    font-family: Georgia, serif;
    font-size: clamp(28px, 6vw, 40px);
    color: #a14e84;
    line-height: 1.3;
}

.message {
    color: #795b78;
    font-size: 15px;
    line-height: 2;
}

button {
    border: none;
    cursor: pointer;
    border-radius: 35px;
    padding: 13px 21px;
    margin: 7px 4px;
    font-size: 14px;
    font-weight: bold;
    color: white;
    background: linear-gradient(100deg, #df80b5, #a28ae5);
    box-shadow: 0 7px 17px #b576b62b;
    transition: transform .2s;
}

button:hover { transform: translateY(-3px) scale(1.02); }

.secondary {
    color: #98517f;
    background: white;
    border: 1px solid #edc5df;
}

#surprise {
    display: none;
    animation: appear .8s ease;
}

@keyframes appear {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.gift {
    font-size: 80px;
    cursor: pointer;
    display: inline-block;
    animation: bob 1.4s infinite alternate;
}

@keyframes bob {
    to { transform: translateY(-9px) rotate(4deg); }
}

/* ---------------------------------
   CHAPTER 21 BIRTHDAY SECTION
--------------------------------- */
.chapter-card {
    background: linear-gradient(145deg, #fffafd, #f8efff);
    border: 1px solid #e8c5dd;
    box-shadow: 0 15px 40px #9c69951c;
    position: relative;
    overflow: hidden;
}

.chapter-label {
    color: #b16b99;
    font-size: 10px;
    letter-spacing: 3px;
    margin-bottom: 4px;
}

.age-number {
    font-family: Georgia, serif;
    font-size: clamp(90px, 20vw, 145px);
    line-height: 1;
    font-weight: normal;
    background: linear-gradient(135deg, #e58ab8, #a28ae5);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 10px 30px #d7a4df30;
    animation: ageReveal 1.1s ease both;
}

.chapter-card h2 {
    margin-top: 8px;
}

.chapter-signature {
    margin-top: 18px;
    font-family: Georgia, serif;
    font-style: italic;
    font-size: 17px;
    color: #ad6795;
}

@keyframes ageReveal {
    from {
        opacity: 0;
        transform: translateY(12px) scale(.94);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

#reaction {
    min-height: 30px;
    color: #a14e84;
    font-weight: bold;
    line-height: 1.7;
}

.confetti {
    position: fixed;
    z-index: 99;
    top: -20px;
    pointer-events: none;
    animation: fall 3.5s linear forwards;
}

@keyframes fall {
    to {
        transform: translateY(110vh) rotate(760deg);
        opacity: .1;
    }
}

.footer {
    margin-top: 32px;
    color: #a783a4;
    font-size: 11px;
    letter-spacing: 2px;
    line-height: 2;
}

@media (max-width: 480px) {
    .page { padding: 24px 10px 35px; }
    .card { padding: 23px 15px; }
    button { padding: 12px 16px; }
    .age-number { font-size: 100px; }
}
</style>
</head>

<body>
<div class="page">

    <div class="decor">✧ ♡ ✧</div>
    <div class="pill">A LITTLE SURPRISE FOR YOU</div>

    <h1>Hey, Muskan! 💗</h1>
    <p class="subtitle">
        Someone has made a little corner of the internet
        just to celebrate YOU. 🌷
    </p>

    <div class="photo-wrap">PHOTO_SECTION</div>

    <div class="card" id="intro">
        <div style="font-size:48px">🎁</div>
        <h2>Ready for your surprise?</h2>
        <p class="message">
            There's a little birthday magic waiting for you.<br>
            This moment is all yours. 💌
        </p>
        <button onclick="openSurprise()">Open Your Surprise ✨</button>
    </div>

    <div id="surprise">

        <div class="decor">🎈 ✨ 🎈</div>

        <div class="card chapter-card">
            <div class="chapter-label">A NEW CHAPTER BEGINS</div>
            <div class="age-number">21</div>
            <h2>Chapter 21, Muskan.</h2>
            <p class="message">
                Twenty-one looks like a beautiful beginning. 💗<br><br>

                Here's to becoming more of yourself, choosing happiness,
                chasing the dreams that excite you, collecting unforgettable
                memories, and finding magic in the little things.<br><br>

                May this chapter be your most confident, happiest,
                and most beautiful one yet. You deserve a life that
                feels as wonderful as the dreams in your heart. ✨
            </p>
            <div class="chapter-signature">Your twenties, your story. ♡</div>
        </div>

        <div class="card">
            <h2>Happy Birthday,<br>Muskan! 🎂</h2>
            <p class="message">
                Today is about celebrating the wonderful person you are. 💕<br><br>

                May your life be filled with genuine smiles,
                beautiful memories, exciting opportunities,
                little unexpected joys and people who always
                remind you how special you are. 🌸<br><br>

                Keep dreaming big, laughing loudly and being
                your lovely self. You deserve so many beautiful
                things in this world. ✨<br><br>

                I'm really glad to have you as my friend.
                I hope this little surprise brings a big smile
                to your face today. 💗
            </p>

            <h2 style="font-size:29px">Lots of wishes,<br>Sandy 💖</h2>
        </div>

        <div class="card">
            <h2 style="font-size:30px">A little birthday magic ✨</h2>
            <p class="message">
                Make a wish, close your eyes for a moment,
                and imagine all the lovely things waiting for you. 🌙
            </p>

            <div class="gift" onclick="celebrate()">🎂</div>
            <p class="message">Tap the cake for more birthday magic!</p>

            <button onclick="celebrate()">More confetti! 🎉</button>
            <button class="secondary" onclick="hug()">Send a virtual hug 🤗</button>
            <button class="secondary" onclick="wish()">Make a wish 🌟</button>

            <p id="reaction" aria-live="polite"></p>
        </div>
    </div>

    <div class="footer">
        MADE WITH 💗 BY SANDY<br>
        A LITTLE BIRTHDAY MEMORY TO KEEP
    </div>
</div>

<script>
function confettiBurst() {
    const symbols = ["💗", "💕", "✨", "🌸", "🎉", "💖", "🎈"];

    for (let i = 0; i < 45; i++) {
        const item = document.createElement("span");
        item.className = "confetti";
        item.textContent =
            symbols[Math.floor(Math.random() * symbols.length)];

        item.style.left = Math.random() * 100 + "vw";
        item.style.animationDelay = Math.random() * 1.2 + "s";
        item.style.fontSize = (16 + Math.random() * 17) + "px";

        document.body.appendChild(item);
        setTimeout(() => item.remove(), 5000);
    }
}

function openSurprise() {
    document.getElementById("intro").style.display = "none";
    document.getElementById("surprise").style.display = "block";

    confettiBurst();

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

function celebrate() {
    confettiBurst();

    document.getElementById("reaction").textContent =
        "Yayyy, Muskan! 🎉 Sending you a sky full of happiness! 💗";
}

function hug() {
    document.getElementById("reaction").textContent =
        "Big virtual hug from Sandy! 🤗💗 Consider yourself hugged!";

    confettiBurst();
}

function wish() {
    document.getElementById("reaction").textContent =
        "✨ Wish made! May something beautiful find its way to you. 🌷💖";

    confettiBurst();
}
</script>
</body>
</html>
"""

page = page.replace("PHOTO_SECTION", photo_section)

components.html(page, height=2100, scrolling=True)
