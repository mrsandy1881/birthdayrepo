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
# LOAD ASSETS (PHOTO, CAKE, MUSIC)
# ---------------------------------
def load_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        ext = os.path.splitext(path)[1].lower()
        mime = "image/png" if ext == ".png" else "image/jpeg"
        return f"data:{mime};base64,{data}"
    return ""

photo_src = load_image("muskan.jpg")
cake_src = load_image("muskan_cake.jpg")

music_path = "birthday_song.mp3"
if os.path.exists(music_path):
    with open(music_path, "rb") as f:
        music_data = base64.b64encode(f.read()).decode("utf-8")
    audio_src = f"data:audio/mpeg;base64,{music_data}"
else:
    audio_src = ""

photo_section = (
    f'<img class="portrait" src="{photo_src}" alt="Muskan">'
    if photo_src
    else '<div class="photo-placeholder">📸<br>Add Muskan’s photo as muskan.jpg</div>'
)

cake_section = (
    f'<img class="cake-portrait" src="{cake_src}" alt="Muskan’s Birthday Cake">'
    if cake_src
    else '<div class="photo-placeholder">🎂<br>Add AI cake image as muskan_cake.jpg</div>'
)

music_section = (
    f'<audio id="birthdaySong" loop src="{audio_src}"></audio>'
    if audio_src
    else '<audio id="birthdaySong"></audio>'
)

page = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Sacramento&family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: 'Quicksand', sans-serif;
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
    font-family: 'Sacramento', cursive;
    font-size: clamp(55px, 11vw, 95px);
    margin: 10px 0 12px;
    line-height: 1.1;
    color: #9c3f7c;
    font-weight: normal;
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
}

.portrait, .cake-portrait {
    display: block;
    width: 100%;
    max-height: 430px;
    object-fit: cover;
    border-radius: 22px;
}

.cake-wrap {
    max-width: 380px;
    margin: 20px auto;
    padding: 10px;
    border-radius: 28px;
    background: linear-gradient(135deg, #ffe2bc, #ffb8da, #c9b9ff);
    box-shadow: 0 14px 35px #a56d9a30;
    cursor: pointer;
    transition: transform .3s;
}

.cake-wrap:hover {
    transform: scale(1.02);
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
    font-family: 'Sacramento', cursive;
    font-size: clamp(40px, 8vw, 60px);
    color: #9c3f7c;
    line-height: 1.2;
    margin: 10px 0;
    font-weight: normal;
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
    font-family: 'Quicksand', sans-serif;
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

#reaction {
    min-height: 30px;
    color: #a14e84;
    font-weight: bold;
    line-height: 1.7;
    margin-top: 15px;
}

.confetti {
    position: fixed;
    z-index: 99;
    top: -20px;
    pointer-events: none;
    animation: fall 3.5s linear forwards;
}

@keyframes fall {
    to { transform: translateY(110vh) rotate(760deg); opacity: .1; }
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

        <div class="card">
            <h2>Happy Birthday, Muskan! 🎂</h2>
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

            <h2 style="font-size:45px">Lots of wishes, Sandy 💖</h2>
        </div>

        <div class="card">
            <h2>A little birthday magic ✨</h2>
            <p class="message">
                Make a wish, close your eyes for a moment,
                and imagine all the lovely things waiting for you. 🌙<br>
                <b>Tap your custom birthday cake below!</b>
            </p>

            <div class="cake-wrap" onclick="celebrate()">
                CAKE_SECTION
            </div>

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

function confettiBurst() {
    const symbols = ["💗", "💕", "✨", "🌸", "🎉", "💖", "🎈"];
    for (let i = 0; i < 45; i++) {
        const item = document.createElement("span");
        item.className = "confetti";
        item.textContent = symbols[Math.floor(Math.random() * symbols.length)];
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
    window.scrollTo({ top: 0, behavior: "smooth" });
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

async function toggleMusic() {
    const audio = document.getElementById("birthdaySong");
    const button = document.getElementById("musicButton");

    if (!audio.getAttribute("src")) {
        document.getElementById("reaction").textContent =
            "Add a music file named birthday_song.mp3 to the app folder to enable music. 🎵";
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

components.html(page, height=1850, scrolling=True)