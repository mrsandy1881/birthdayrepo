
import streamlit as st
import streamlit.components.v1 as components
import os
import base64

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
# LOAD BIRTHDAY MUSIC
# ---------------------------------
music_path = "birthday_song.mp3"

if os.path.exists(music_path):
    with open(music_path, "rb") as f:
        music_data = base64.b64encode(f.read()).decode("utf-8")
    audio_src = f"data:audio/mpeg;base64,{music_data}"
else:
    audio_src = ""

music_section = (
    f'<audio id="birthdaySong" loop src="{audio_src}"></audio>'
    if audio_src
    else '<audio id="birthdaySong"></audio>'
)

# ---------------------------------
# REAL CAKE PHOTO
# ---------------------------------
cake_section = """
<div class="cake-frame">
    <img
        class="cake-photo"
        src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1200&q=90"
        alt="Beautiful birthday cake"
        onerror="this.style.display='none';document.getElementById('cakeFallback').style.display='block';"
    >
    <div id="cakeFallback" style="display:none;padding:40px 10px;color:#fff0fa">
        The cake photo couldn't load. Please check your internet connection.
    </div>
</div>

<div class="cake-nameplate">
    <span class="nameplate-small">A LITTLE SOMETHING SWEET FOR</span>
    <div class="nameplate-name">Muskan</div>
    <div class="nameplate-heart">♡</div>
</div>
"""

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

html { scroll-behavior: smooth; }

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    color: #fff4fb;
    background: transparent;
}

.page {
    position: relative;
    overflow: hidden;
    isolation: isolate;
    padding: 32px 16px 42px;
    text-align: center;
    border-radius: 28px;
    background:
        radial-gradient(ellipse at 8% 5%, #713d72 0%, transparent 35%),
        radial-gradient(ellipse at 95% 22%, #49377f 0%, transparent 36%),
        radial-gradient(ellipse at 50% 95%, #55274f 0%, transparent 40%),
        linear-gradient(145deg, #130f23, #25132e 55%, #151025);
}

/* Soft ambient lighting */
.ambient {
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    filter: blur(85px);
    opacity: .3;
    z-index: -1;
    pointer-events: none;
    animation: ambientMove 8s ease-in-out infinite alternate;
}

.ambient.one {
    background: #ff6ebd;
    left: -100px;
    top: 12%;
}

.ambient.two {
    background: #8f78ff;
    right: -100px;
    top: 48%;
    animation-delay: -3s;
}

@keyframes ambientMove {
    from { transform: translateY(-20px); }
    to { transform: translateY(65px); }
}

.pill {
    display: inline-block;
    padding: 10px 16px;
    border: 1px solid #ffffff30;
    border-radius: 30px;
    background: #ffffff0b;
    color: #ffc5e7;
    font-size: 10px;
    letter-spacing: 3px;
}

h1 {
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(43px, 8vw, 76px);
    line-height: 1.08;
    letter-spacing: -2px;
    margin: 25px 0 14px;
    color: #ffd9f0;
    background: linear-gradient(105deg, #fff4fc, #ff9fd5, #d4c3ff);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    max-width: 510px;
    margin: 0 auto 25px;
    color: #d9c2e1;
    font-size: 15px;
    line-height: 1.9;
}

.decor {
    color: #ffb9e1;
    font-size: 20px;
    letter-spacing: 12px;
    margin-bottom: 18px;
    animation: twinkle 2s ease-in-out infinite alternate;
}

@keyframes twinkle {
    from { opacity: .55; }
    to { opacity: 1; }
}

/* Animated photo */
.photo-wrap {
    position: relative;
    max-width: 350px;
    margin: 30px auto 16px;
    padding: 5px;
    border-radius: 26px;
    background: linear-gradient(135deg, #ffacd8, #9f85ff, #ffe5ba);
    box-shadow: 0 0 35px #f16ab52b, 0 20px 45px #00000035;
    animation: photoFloat 4.5s ease-in-out infinite;
}

.photo-wrap::before {
    content: "";
    position: absolute;
    inset: -3px;
    border-radius: 29px;
    border: 1px solid #ffb6df50;
    pointer-events: none;
}

.portrait {
    display: block;
    width: 100%;
    max-height: 450px;
    object-fit: cover;
    border-radius: 22px;
    animation: photoEnter 1.2s ease both;
}

@keyframes photoFloat {
    0%, 100% { transform: translateY(0) rotate(-.4deg); }
    50% { transform: translateY(-8px) rotate(.4deg); }
}

@keyframes photoEnter {
    from {
        opacity: 0;
        transform: scale(.94);
        filter: blur(6px);
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
    background: #291b37;
    line-height: 2;
    color: #f7c6e5;
}

.photo-caption {
    color: #d9b2d8;
    font-size: 10px;
    letter-spacing: 2px;
    line-height: 2;
    margin-bottom: 30px;
}

/* Glass-style cards */
.card {
    max-width: 640px;
    margin: 25px auto;
    padding: 28px 22px;
    border-radius: 25px;
    border: 1px solid #ffffff22;
    background: linear-gradient(145deg, #ffffff12, #ffffff06);
    box-shadow: 0 18px 45px #0000001b;
    backdrop-filter: blur(12px);
}

h2 {
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(29px, 6vw, 43px);
    color: #ffd1eb;
    line-height: 1.3;
    margin: 14px 0;
}

.message {
    color: #ead9ec;
    font-size: 15px;
    line-height: 2;
}

button {
    border: 1px solid #ffffff22;
    cursor: pointer;
    border-radius: 35px;
    padding: 13px 21px;
    margin: 7px 4px;
    font-size: 13px;
    font-weight: bold;
    color: white;
    background: linear-gradient(105deg, #e35ca9, #9275e9);
    box-shadow: 0 7px 24px #b576b62b;
    transition: transform .25s, box-shadow .25s;
}

button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px #e86ab455;
}

button:active { transform: scale(.98); }

.secondary {
    color: #f5d9ee;
    background: #ffffff0b;
    border: 1px solid #ffffff35;
}

#surprise {
    display: none;
    animation: reveal .9s ease both;
}

@keyframes reveal {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.gift {
    font-size: 65px;
    cursor: pointer;
    display: inline-block;
    filter: drop-shadow(0 0 18px #ff91d65c);
    animation: giftBob 1.8s ease-in-out infinite alternate;
}

@keyframes giftBob {
    to { transform: translateY(-8px) rotate(4deg); }
}

/* Real cake image section */
.cake-frame {
    position: relative;
    max-width: 560px;
    margin: 24px auto 18px;
    padding: 5px;
    overflow: hidden;
    border-radius: 23px;
    background: linear-gradient(135deg, #ffb3dd, #bba7ff, #ffe4bb);
    box-shadow: 0 0 35px #f16ab526, 0 18px 38px #00000025;
}

.cake-photo {
    display: block;
    width: 100%;
    max-height: 400px;
    object-fit: cover;
    border-radius: 19px;
    animation: cakeReveal 1.2s ease both;
}

@keyframes cakeReveal {
    from { opacity: .4; transform: scale(1.06); }
    to { opacity: 1; transform: scale(1); }
}

.cake-nameplate {
    display: inline-block;
    min-width: 230px;
    padding: 17px 35px 12px;
    margin: 0 auto 12px;
    border: 1px solid #ffc2e74f;
    border-radius: 16px;
    background: linear-gradient(145deg, #ffffff12, #ffffff05);
    box-shadow: 0 0 24px #ff83cb14;
}

.nameplate-small {
    font-size: 9px;
    letter-spacing: 2px;
    color: #e8b5da;
}

.nameplate-name {
    margin-top: 6px;
    font-family: Georgia, serif;
    font-size: 38px;
    color: #ffc5e5;
    text-shadow: 0 0 20px #ff72c76b;
}

.nameplate-heart {
    color: #ff9cd5;
    font-size: 18px;
    animation: twinkle 1.4s infinite alternate;
}

/* Candle-style decoration */
.candles {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    gap: 13px;
    height: 55px;
    margin: 15px auto 5px;
}

.candle {
    position: relative;
    width: 8px;
    height: 30px;
    border-radius: 3px;
    background: repeating-linear-gradient(
        135deg, #ffd3ec 0 5px, #d9b8ff 5px 9px
    );
}

.flame {
    position: absolute;
    width: 10px;
    height: 17px;
    left: -1px;
    top: -17px;
    border-radius: 60% 40% 55% 45%;
    background: radial-gradient(ellipse at 50% 65%, #fffbd0 0 15%, #ffca67 40%, #ff7e52 75%);
    box-shadow: 0 0 13px #ffb45d, 0 0 25px #ffb45d75;
    transform-origin: bottom center;
    animation: flicker .18s infinite alternate;
}

@keyframes flicker {
    from { transform: rotate(-5deg) scale(1); }
    to { transform: rotate(5deg) scale(.88, 1.08); }
}

.flame.off {
    opacity: 0;
    transform: scale(0);
}

#reaction {
    min-height: 30px;
    color: #ffbde4;
    font-weight: bold;
    line-height: 1.8;
    margin-top: 12px;
}

/* Confetti particles */
.confetti {
    position: fixed;
    z-index: 999;
    top: -25px;
    pointer-events: none;
    animation: confettiFall 4s linear forwards;
}

@keyframes confettiFall {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(110vh) rotate(760deg); opacity: .15; }
}

.spark {
    position: fixed;
    z-index: 998;
    pointer-events: none;
    color: #ffd7f0;
    text-shadow: 0 0 12px #ff8ed6;
    animation: sparkRise 2.5s ease-out forwards;
}

@keyframes sparkRise {
    from { transform: translateY(0) scale(.5); opacity: 0; }
    20% { opacity: 1; }
    to { transform: translateY(-130px) scale(1.3); opacity: 0; }
}

.footer {
    margin-top: 34px;
    color: #c6a6cd;
    font-size: 10px;
    letter-spacing: 2px;
    line-height: 2;
}

@media (max-width: 480px) {
    .page { padding: 25px 10px 35px; }
    .card { padding: 23px 15px; }
    .message { font-size: 14px; }
    button { padding: 12px 16px; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
        scroll-behavior: auto !important;
    }
}
</style>
</head>

<body>
<div class="page">

    <div class="ambient one"></div>
    <div class="ambient two"></div>

    <div class="decor">✧ ♡ ✧</div>
    <div class="pill">A LITTLE SURPRISE FOR YOU</div>

    <h1>Hey, Muskan! 💗</h1>
    <p class="subtitle">
        Someone has made a little corner of the internet
        just to celebrate YOU. 🌷
    </p>

    <div class="photo-wrap">PHOTO_SECTION</div>
    <div class="photo-caption">A LITTLE MOMENT, MADE A LITTLE MORE SPECIAL</div>

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
        <div class="decor">✧ 🎈 ✧</div>

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

            CAKE_SECTION

            <div class="candles" id="candles">
                <div class="candle"><div class="flame"></div></div>
                <div class="candle"><div class="flame"></div></div>
                <div class="candle"><div class="flame"></div></div>
                <div class="candle"><div class="flame"></div></div>
                <div class="candle"><div class="flame"></div></div>
            </div>

            <p class="message">Make a wish, Muskan. It's your moment. ✨</p>

            <button onclick="blowCandles()">Make a wish & blow the candles 🕯️</button>
            <br>
            <button onclick="celebrate()">More confetti! 🎉</button>
            <button class="secondary" onclick="hug()">Send a virtual hug 🤗</button>
            <button class="secondary" onclick="wish()">Make a wish 🌟</button>
            <button class="secondary" onclick="toggleMusic()" id="musicButton">
                ▶ Play birthday music 🎵
            </button>

            <p id="reaction" aria-live="polite"></p>
        </div>
    </div>

    <div class="footer">
        MADE WITH 💗 BY SANDY<br>
        A LITTLE BIRTHDAY MEMORY TO KEEP
    </div>
</div>

MUSIC_SECTION

<script>
let musicPlaying = false;
let candlesBlown = false;

function confettiBurst() {
    const colors = ["#ff8fcf", "#c3a7ff", "#ffe3a3", "#ffffff", "#ffb8de"];

    for (let i = 0; i < 85; i++) {
        const item = document.createElement("span");
        item.className = "confetti";

        // Use realistic confetti shapes rather than emoji rain.
        item.style.background = colors[Math.floor(Math.random() * colors.length)];
        item.style.left = Math.random() * 100 + "vw";
        item.style.animationDelay = Math.random() * 1.4 + "s";
        item.style.animationDuration = (3 + Math.random() * 2) + "s";
        item.style.width = (4 + Math.random() * 6) + "px";
        item.style.height = (7 + Math.random() * 10) + "px";
        item.style.borderRadius = Math.random() > .5 ? "50%" : "2px";

        document.body.appendChild(item);
        setTimeout(() => item.remove(), 6000);
    }

    // A few soft glowing sparkles
    for (let i = 0; i < 18; i++) {
        const spark = document.createElement("span");
        spark.className = "spark";
        spark.textContent = "✦";
        spark.style.left = Math.random() * 100 + "vw";
        spark.style.top = (35 + Math.random() * 55) + "vh";
        spark.style.fontSize = (10 + Math.random() * 17) + "px";
        spark.style.animationDelay = Math.random() * .8 + "s";

        document.body.appendChild(spark);
        setTimeout(() => spark.remove(), 3500);
    }
}

function openSurprise() {
    document.getElementById("intro").style.display = "none";
    document.getElementById("surprise").style.display = "block";
    confettiBurst();

    setTimeout(() => {
        document.getElementById("surprise").scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }, 100);
}

function celebrate() {
    confettiBurst();
    document.getElementById("reaction").textContent =
        "Yayyy, Muskan! Sending you a sky full of happiness! 💗";
}

function hug() {
    document.getElementById("reaction").textContent =
        "Big virtual hug from Sandy! Consider yourself hugged! 🤗💗";
    confettiBurst();
}

function wish() {
    document.getElementById("reaction").textContent =
        "Wish made! May something beautiful find its way to you. 🌷💖";
    confettiBurst();
}

function blowCandles() {
    if (!candlesBlown) {
        document.querySelectorAll(".flame").forEach(flame => {
            flame.classList.add("off");
        });

        candlesBlown = true;
        document.getElementById("reaction").textContent =
            "Candles blown! ✨ Keep your wish in your heart, Muskan. May it come true! 💗";

        confettiBurst();
    } else {
        document.querySelectorAll(".flame").forEach(flame => {
            flame.classList.remove("off");
        });

        candlesBlown = false;
        document.getElementById("reaction").textContent =
            "The candles are glowing again. Make another wish! 🕯️";
    }
}

async function toggleMusic() {
    const audio = document.getElementById("birthdaySong");
    const button = document.getElementById("musicButton");

    if (!audio.getAttribute("src")) {
        document.getElementById("reaction").textContent =
            "Add birthday_song.mp3 to the app folder to enable music. 🎵";
        return;
    }

    try {
        if (!musicPlaying) {
            await audio.play();
            musicPlaying = true;
            button.textContent = "❚❚ Pause birthday music 🎵";
        } else {
            audio.pause();
            musicPlaying = false;
            button.textContent = "▶ Play birthday music 🎵";
        }
    } catch (error) {
        document.getElementById("reaction").textContent =
            "Tap Play again to start the music. 🎵";
    }
}
</script>
</body>
</html>
"""

page = page.replace("PHOTO_SECTION", photo_section)
page = page.replace("CAKE_SECTION", cake_section)
page = page.replace("MUSIC_SECTION", music_section)

components.html(page, height=2500, scrolling=True)
