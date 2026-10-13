
import streamlit as st
import streamlit.components.v1 as components
import os
import base64

st.set_page_config(
    page_title="Muskan's Birthday ✨",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------
# YOUR EXISTING PHOTO
# ------------------------------------------
photo_src = ""

if os.path.exists("muskan.jpg"):
    with open("muskan.jpg", "rb") as f:
        photo_src = (
            "data:image/jpeg;base64,"
            + base64.b64encode(f.read()).decode()
        )

if not photo_src:
    photo_src = "https://placehold.co/600x750/24172d/ffffff?text=Muskan"

# ------------------------------------------
# CAKE PHOTO
# ------------------------------------------
# Realistic cake photograph from Unsplash.
# Internet access is needed to load this image.
cake_src = (
    "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    "?auto=format&fit=crop&w=1000&q=85"
)

# ------------------------------------------
# HTML PAGE
# ------------------------------------------
page = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
    margin: 0;
    background: transparent;
    font-family: Inter, Arial, sans-serif;
    color: #fff1fa;
}

.site {
    overflow: hidden;
    position: relative;
    border-radius: 25px;
    padding: 30px 18px 35px;
    background:
      radial-gradient(ellipse at 15% 5%, #773b76 0%, transparent 38%),
      radial-gradient(ellipse at 90% 25%, #3c317c 0%, transparent 40%),
      linear-gradient(150deg, #100d20, #20112c 52%, #120e25);
}

.glow {
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    filter: blur(85px);
    opacity: .28;
    pointer-events: none;
    animation: drift 8s ease-in-out infinite alternate;
}

.glow.one { background: #ff58b4; top: 10%; left: -100px; }
.glow.two { background: #8870ff; top: 48%; right: -100px; }

@keyframes drift {
    from { transform: translateY(-20px); }
    to { transform: translateY(50px); }
}

.content {
    position: relative;
    z-index: 1;
    max-width: 850px;
    margin: auto;
    text-align: center;
}

.topline {
    display: inline-block;
    padding: 9px 16px;
    border: 1px solid #ffffff30;
    border-radius: 30px;
    background: #ffffff0b;
    color: #ffc5e9;
    font-size: 10px;
    letter-spacing: 3px;
}

h1 {
    font-family: Georgia, serif;
    font-size: clamp(42px, 8vw, 78px);
    line-height: 1.08;
    letter-spacing: -2px;
    margin: 24px 0 14px;
    background: linear-gradient(100deg, #fff4fc, #ff9dd5, #d6c4ff);
    color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
}

.subtitle {
    color: #d9c1df;
    font-size: 15px;
    line-height: 1.9;
    max-width: 520px;
    margin: 0 auto 24px;
}

.portrait-wrap {
    position: relative;
    width: min(100%, 380px);
    margin: 28px auto;
    padding: 5px;
    border-radius: 25px;
    background: linear-gradient(135deg, #ff90d0, #9b7dff, #ffe2b2);
    box-shadow: 0 0 35px #ff62c12a;
    animation: photoFloat 4s ease-in-out infinite;
}

.portrait {
    display: block;
    width: 100%;
    max-height: 470px;
    object-fit: cover;
    border-radius: 21px;
    animation: photoReveal 1.5s ease both;
}

@keyframes photoFloat {
    0%, 100% { transform: translateY(0) rotate(-.5deg); }
    50% { transform: translateY(-9px) rotate(.5deg); }
}

@keyframes photoReveal {
    from { opacity: 0; transform: scale(.93); filter: blur(5px); }
    to { opacity: 1; transform: scale(1); filter: blur(0); }
}

.photo-caption {
    margin-top: 13px;
    color: #f5c4e6;
    font-size: 12px;
    letter-spacing: 2px;
}

.card {
    margin: 28px auto;
    padding: 25px 20px;
    max-width: 670px;
    border: 1px solid #ffffff20;
    border-radius: 25px;
    background: linear-gradient(145deg, #ffffff12, #ffffff05);
    box-shadow: 0 18px 50px #00000020;
    backdrop-filter: blur(12px);
}

h2 {
    font-family: Georgia, serif;
    font-size: clamp(28px, 5vw, 43px);
    line-height: 1.25;
    color: #ffd4ed;
    margin: 12px 0;
}

.wish {
    color: #eee0f2;
    font-size: 15px;
    line-height: 2;
}

button {
    cursor: pointer;
    border: 1px solid #ffffff20;
    border-radius: 40px;
    padding: 13px 20px;
    margin: 7px 4px;
    color: white;
    font-size: 13px;
    font-weight: 600;
    background: linear-gradient(105deg, #e85da8, #8d71ec);
    box-shadow: 0 7px 25px #bc5da333;
    transition: transform .2s, box-shadow .2s;
}

button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 28px #bc5da355;
}

.secondary {
    background: #ffffff0c;
    border: 1px solid #ffffff30;
}

#surprise { display: none; animation: reveal .9s ease both; }

@keyframes reveal {
    from { opacity: 0; transform: translateY(22px); }
    to { opacity: 1; transform: translateY(0); }
}

.gift {
    font-size: 65px;
    margin: 12px;
    animation: giftBounce 1.5s infinite alternate;
}

@keyframes giftBounce {
    to { transform: translateY(-7px) rotate(5deg); }
}

.cake-frame {
    max-width: 570px;
    margin: 24px auto;
    padding: 8px;
    border-radius: 23px;
    background: linear-gradient(130deg, #ff9bce, #c4a7ff, #ffe5b6);
    box-shadow: 0 0 45px #ef80cb24;
    overflow: hidden;
}

.cake {
    display: block;
    width: 100%;
    max-height: 390px;
    object-fit: cover;
    border-radius: 17px;
    animation: cakeAppear 1.2s ease both;
}

@keyframes cakeAppear {
    from { transform: scale(1.08); opacity: .4; }
    to { transform: scale(1); opacity: 1; }
}

.cake-name {
    margin-top: 15px;
    font-family: Georgia, serif;
    font-size: 28px;
    color: #ffb8e2;
    text-shadow: 0 0 22px #ff67c7;
}

.cake-note {
    font-size: 12px;
    line-height: 1.7;
    color: #d7c4e3;
}

#response {
    min-height: 28px;
    color: #ffbce4;
    line-height: 1.8;
    margin-top: 12px;
}

.footer {
    margin-top: 36px;
    color: #c1a7cb;
    font-size: 10px;
    letter-spacing: 2px;
    line-height: 2.1;
}

.confetti {
    position: fixed;
    z-index: 100;
    top: -25px;
    pointer-events: none;
    animation: confettiFall 4s linear forwards;
}

@keyframes confettiFall {
    to {
        transform: translateY(110vh) rotate(720deg);
        opacity: .15;
    }
}

.twinkle {
    animation: twinkle 1.6s ease-in-out infinite alternate;
}

@keyframes twinkle {
    from { opacity: .5; }
    to { opacity: 1; }
}

@media(max-width: 480px) {
    .site { padding: 25px 11px; }
    .card { padding: 22px 15px; }
    .wish { font-size: 14px; }
    button { padding: 12px 15px; }
}
</style>
</head>

<body>
<div class="site">
<div class="glow one"></div>
<div class="glow two"></div>

<div class="content">

    <div class="topline">A SPECIAL LITTLE SURPRISE</div>
    <h1>It's your moment,<br>Muskan.</h1>

    <p class="subtitle">
        One little page, a thousand good wishes,
        and a whole lot of love for your special day. ✨
    </p>

    <div class="portrait-wrap">
        <img class="portrait" src="PHOTO_SOURCE" alt="Muskan">
    </div>
    <div class="photo-caption">THE WORLD IS A LITTLE BRIGHTER WITH YOU IN IT</div>

    <div class="card" id="intro">
        <div class="gift">🎁</div>
        <h2>Something special awaits...</h2>
        <p class="wish">
            I made this little surprise just for you.<br>
            Ready to open it? 💌
        </p>
        <button onclick="openSurprise()">Open your surprise ✨</button>
    </div>

    <div id="surprise">

        <div class="card">
            <div class="twinkle">✦ ✧ ✦</div>
            <h2>Happy Birthday,<br>Muskan! 🎂</h2>

            <p class="wish">
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

            <h2 style="font-size:30px">
                Lots of wishes,<br>Sandy 💖
            </h2>
        </div>

        <div class="card">
            <h2>A cake made for your day 🎂</h2>
            <p class="wish">
                Every birthday deserves a little sweetness.
            </p>

            <div class="cake-frame">
                <img class="cake" src="CAKE_SOURCE" alt="Birthday cake"
                     onerror="this.style.display='none';document.getElementById('cakeFallback').style.display='block';">
            </div>
            <div id="cakeFallback" style="display:none;color:#ffd4ed;padding:20px">
                The cake photo couldn't load. Please check your internet connection.
            </div>

            <div class="cake-name">Made for Muskan ✨</div>
            <p class="cake-note">
                Imagine the candles glowing, your favourite people cheering,
                and one beautiful wish coming true. 💗
            </p>

            <button onclick="blowCandles()">Make a wish & blow the candles 🕯️</button>
            <p id="candleMessage" class="wish"></p>
        </div>

        <div class="card">
            <h2>Let's celebrate you ✨</h2>
            <p class="wish">
                A little happiness, a virtual hug, and a sky full of wishes.
            </p>

            <button onclick="celebrate()">More confetti! 🎉</button>
            <button class="secondary" onclick="hug()">Send a virtual hug 🤗</button>
            <button class="secondary" onclick="wish()">Make a wish 🌟</button>
            <button class="secondary" onclick="toggleMusic()" id="musicButton">
                ▶ Play birthday music 🎵
            </button>

            <p id="response" aria-live="polite"></p>
        </div>

    </div>

    <div class="footer">
        MADE WITH 💗 BY SANDY<br>
        A LITTLE BIRTHDAY MEMORY TO KEEP
    </div>
</div>
</div>

<script>
let musicPlaying = false;

function burst() {
    const symbols = ["💗", "✨", "🌸", "🎉", "💖", "🎊", "🎈", "✦"];
    for (let i = 0; i < 65; i++) {
        const el = document.createElement("span");
        el.className = "confetti";
        el.textContent = symbols[Math.floor(Math.random() * symbols.length)];
        el.style.left = Math.random() * 100 + "vw";
        el.style.animationDelay = Math.random() * 1.5 + "s";
        el.style.fontSize = (14 + Math.random() * 20) + "px";
        document.body.appendChild(el);
        setTimeout(() => el.remove(), 5000);
    }
}

function openSurprise() {
    document.getElementById("intro").style.display = "none";
    document.getElementById("surprise").style.display = "block";
    burst();
    setTimeout(() => {
        document.getElementById("surprise").scrollIntoView({
            behavior: "smooth", block: "start"
        });
    }, 100);
}

function celebrate() {
    burst();
    document.getElementById("response").textContent =
        "A whole sky of happiness, just for you, Muskan! 🎉💗";
}

function hug() {
    document.getElementById("response").textContent =
        "Sending you the biggest virtual hug from Sandy! 🤗💖";
    burst();
}

function wish() {
    document.getElementById("response").textContent =
        "Wish made! May your heart's sweetest wish come true. 🌟";
    burst();
}

function blowCandles() {
    document.getElementById("candleMessage").textContent =
        "✨ Candles blown! Keep your wish in your heart, Muskan. May it come true! 💗";
    burst();
}

function toggleMusic() {
    document.getElementById("response").textContent =
        "To enable music, add your chosen song file to the page and connect the audio player. 🎵";
}
</script>
</body>
</html>
"""

page = page.replace("PHOTO_SOURCE", photo_src)
page = page.replace("CAKE_SOURCE", cake_src)

components.html(page, height=2600, scrolling=True)
