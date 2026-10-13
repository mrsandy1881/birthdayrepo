
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

# ------------------------------------------
# LOAD EXISTING PHOTO
# ------------------------------------------
def load_image(path):
    if not os.path.exists(path):
        return ""

    with open(path, "rb") as file:
        data = base64.b64encode(file.read()).decode("utf-8")

    ext = os.path.splitext(path)[1].lower()
    mime_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp"
    }

    mime = mime_types.get(ext, "image/jpeg")
    return f"data:{mime};base64,{data}"


photo_src = load_image("muskan.jpg")
music_src = ""

if os.path.exists("birthday_song.mp3"):
    with open("birthday_song.mp3", "rb") as file:
        music_data = base64.b64encode(file.read()).decode("utf-8")
    music_src = f"data:audio/mpeg;base64,{music_data}"

if photo_src:
    photo_section = f"""
        <img class="portrait" src="{photo_src}" alt="Muskan">
    """
else:
    photo_section = """
        <div class="photo-placeholder">
            Add your existing photo as muskan.jpg
        </div>
    """

if music_src:
    music_section = f"""
        <audio id="birthdaySong" loop src="{music_src}"></audio>
    """
else:
    music_section = '<audio id="birthdaySong"></audio>'

# ------------------------------------------
# REAL CAKE PHOTO
# ------------------------------------------
cake_section = """
<div class="cake-image-wrap">
    <img
        class="cake-image"
        src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1200&q=90"
        alt="Birthday cake"
        onerror="this.style.display='none';document.getElementById('cakeError').style.display='block';"
    >
    <div id="cakeError" style="display:none;padding:25px">
        Cake photo unavailable. Check your internet connection.
    </div>
</div>

<div class="cake-label">
    <span>A LITTLE SWEETNESS, JUST FOR</span>
    <div class="cake-name">Muskan</div>
    <div class="cake-rule"></div>
</div>
"""

# ------------------------------------------
# WEBSITE
# ------------------------------------------
page = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: transparent;
    color: #30232b;
}

button {
    font: inherit;
}

.website {
    --ink: #30232b;
    --muted: #8d737f;
    --pink: #d66b98;
    --cream: #fff8f5;

    position: relative;
    overflow: hidden;
    isolation: isolate;
    padding: 24px 14px 35px;
    border-radius: 26px;
    background:
        radial-gradient(ellipse at 10% 5%, #f8d9e4 0%, transparent 35%),
        radial-gradient(ellipse at 95% 35%, #e8dff5 0%, transparent 32%),
        #fff8f5;
}

.content {
    max-width: 760px;
    margin: auto;
    position: relative;
    z-index: 2;
}

/* Tiny editorial header */
.nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    padding: 4px 3px 18px;
    border-bottom: 1px solid #e9d9dd;
}

.brand {
    font-family: Georgia, serif;
    font-size: 22px;
    letter-spacing: -.5px;
}

.brand span {
    color: #cf6795;
}

.nav-tag {
    font-size: 9px;
    letter-spacing: 2px;
    color: #977d88;
    text-align: right;
}

.hero {
    padding: 39px 4px 18px;
    text-align: center;
}

.eyebrow {
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #b16a89;
}

h1 {
    font-family: Georgia, "Times New Roman", serif;
    font-weight: normal;
    font-size: clamp(45px, 9vw, 77px);
    letter-spacing: -2.5px;
    line-height: 1.03;
    margin: 18px 0 14px;
    color: #452e3b;
}

h1 em {
    color: #d16e9b;
    font-weight: normal;
}

.intro {
    max-width: 440px;
    margin: auto;
    color: #907783;
    font-size: 13px;
    line-height: 1.9;
}

/* Editorial photograph */
.photo-stage {
    position: relative;
    max-width: 430px;
    margin: 28px auto 23px;
    padding: 0 13px 20px 0;
    animation: stageEnter 1s ease both;
}

.photo-backdrop {
    position: absolute;
    inset: 12px 0 0 14px;
    border-radius: 3px;
    background: #efd3df;
    transform: rotate(3deg);
}

.photo-frame {
    position: relative;
    z-index: 1;
    padding: 7px;
    background: #fffdfc;
    box-shadow: 0 17px 38px #6b3c4b1d;
    transform: rotate(-1.5deg);
    transition: transform .5s ease, box-shadow .5s ease;
}

.photo-frame:hover {
    transform: rotate(0deg) translateY(-4px);
    box-shadow: 0 24px 44px #6b3c4b2b;
}

.portrait {
    display: block;
    width: 100%;
    max-height: 480px;
    min-height: 240px;
    object-fit: cover;
    animation: portraitEnter 1.4s ease both;
}

.photo-placeholder {
    padding: 90px 12px;
    color: #8b6c7d;
    background: #f8e9ef;
    text-align: center;
}

.photo-caption {
    position: relative;
    z-index: 2;
    text-align: right;
    margin-top: 12px;
    padding-right: 7px;
    font-family: Georgia, serif;
    font-style: italic;
    color: #977a87;
    font-size: 13px;
}

.photo-sticker {
    position: absolute;
    z-index: 3;
    right: -1px;
    top: 18px;
    width: 65px;
    height: 65px;
    display: grid;
    place-items: center;
    border-radius: 50%;
    background: #d77a9f;
    color: white;
    font-family: Georgia, serif;
    font-size: 11px;
    text-align: center;
    line-height: 1.4;
    transform: rotate(9deg);
    box-shadow: 0 8px 20px #9c52722b;
    animation: stickerFloat 3s ease-in-out infinite;
}

@keyframes stageEnter {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes portraitEnter {
    from {
        opacity: .3;
        transform: scale(1.035);
        filter: blur(4px);
    }
    to {
        opacity: 1;
        transform: scale(1);
        filter: blur(0);
    }
}

@keyframes stickerFloat {
    0%, 100% { translate: 0 0; }
    50% { translate: 0 -5px; }
}

/* Cards */
.card {
    position: relative;
    margin: 24px auto;
    padding: 27px 23px;
    background: #fffdfc;
    border: 1px solid #eddee2;
    border-radius: 4px;
    box-shadow: 0 12px 30px #613c4b0a;
}

.card-tag {
    font-size: 9px;
    letter-spacing: 2.5px;
    color: #bb7894;
    text-transform: uppercase;
}

h2 {
    font-family: Georgia, "Times New Roman", serif;
    font-weight: normal;
    font-size: clamp(30px, 6vw, 44px);
    line-height: 1.2;
    color: #503544;
    margin: 15px 0;
}

.message {
    font-size: 14px;
    line-height: 2;
    color: #816b76;
}

.primary-btn,
.secondary-btn {
    border-radius: 3px;
    padding: 14px 19px;
    margin: 7px 3px;
    cursor: pointer;
    font-size: 11px;
    letter-spacing: .7px;
    transition: transform .25s, background .25s;
}

.primary-btn {
    color: white;
    border: 1px solid #c76c94;
    background: #c76c94;
}

.secondary-btn {
    color: #a3557c;
    border: 1px solid #e8cbd8;
    background: #fff8f9;
}

.primary-btn:hover,
.secondary-btn:hover {
    transform: translateY(-2px);
}

.primary-btn:hover {
    background: #ad527d;
}

#surprise {
    display: none;
    animation: reveal .8s ease both;
}

@keyframes reveal {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Cake photograph */
.cake-image-wrap {
    margin: 22px auto 15px;
    padding: 6px;
    background: white;
    border: 1px solid #ead8df;
    box-shadow: 0 15px 35px #68415118;
}

.cake-image {
    display: block;
    width: 100%;
    max-height: 400px;
    object-fit: cover;
}

.cake-label {
    margin: 15px auto 20px;
    padding: 14px 10px;
    text-align: center;
    border-top: 1px solid #e8cfd9;
    border-bottom: 1px solid #e8cfd9;
}

.cake-label span {
    color: #ad8194;
    font-size: 9px;
    letter-spacing: 2px;
}

.cake-name {
    font-family: Georgia, serif;
    font-size: 39px;
    color: #c76b95;
    margin: 5px 0;
}

.cake-rule {
    height: 2px;
    width: 36px;
    margin: auto;
    background: #dba5bc;
}

.candle-row {
    display: flex;
    justify-content: center;
    gap: 18px;
    height: 45px;
    margin: 12px 0 5px;
    align-items: flex-end;
}

.candle {
    position: relative;
    width: 7px;
    height: 25px;
    background: repeating-linear-gradient(
        135deg, #f0c4d7 0 5px, #bca8df 5px 9px
    );
    border-radius: 2px;
}

.flame {
    position: absolute;
    left: -2px;
    top: -15px;
    width: 11px;
    height: 16px;
    border-radius: 60% 40% 60% 40%;
    background: radial-gradient(ellipse at 50% 70%, #fff8ce, #ffb65c 55%, #ed7752);
    box-shadow: 0 0 12px #ffc16e;
    animation: flicker .2s infinite alternate;
}

.flame.off {
    opacity: 0;
    transform: scale(0);
}

@keyframes flicker {
    from { transform: rotate(-4deg) scale(1); }
    to { transform: rotate(4deg) scale(.86, 1.08); }
}

/* Realistic paper confetti */
.confetti {
    position: fixed;
    z-index: 999;
    top: -18px;
    pointer-events: none;
    animation: paperFall linear forwards;
}

@keyframes paperFall {
    0% {
        transform: translate3d(0, 0, 0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translate3d(var(--drift), 110vh, 0) rotate(760deg);
        opacity: .2;
    }
}

.flash {
    position: fixed;
    inset: 0;
    z-index: 998;
    pointer-events: none;
    background: white;
    animation: cameraFlash .65s ease-out forwards;
}

@keyframes cameraFlash {
    0% { opacity: .8; }
    100% { opacity: 0; }
}

#reaction {
    min-height: 27px;
    color: #b65f89;
    line-height: 1.8;
    font-size: 13px;
}

.footer {
    text-align: center;
    padding: 22px 0 4px;
    color: #a78b98;
    font-size: 9px;
    letter-spacing: 2px;
    line-height: 2;
}

@media (max-width: 480px) {
    .website { padding: 19px 10px 28px; }
    .hero { padding-top: 30px; }
    .card { padding: 23px 16px; }
    .photo-stage { max-width: 340px; }
    .photo-sticker { width: 54px; height: 54px; font-size: 10px; }
    .message { font-size: 13px; }
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
<div class="website">
<div class="content">

    <div class="nav">
        <div class="brand">little moments<span>.</span></div>
        <div class="nav-tag">A DAY FOR MUSKAN<br>OCTOBER 14</div>
    </div>

    <section class="hero">
        <div class="eyebrow">A page made just for you</div>
        <h1>Hey, <em>Muskan.</em></h1>
        <p class="intro">
            Someone has made a little corner of the internet
            just to celebrate YOU. 🌷
        </p>
    </section>

    <div class="photo-stage">
        <div class="photo-backdrop"></div>
        <div class="photo-frame">
            PHOTO_SECTION
        </div>
        <div class="photo-sticker">made<br>with love</div>
        <div class="photo-caption">A little moment, just for you.</div>
    </div>

    <div class="card" id="intro">
        <div class="card-tag">Your little surprise</div>
        <h2>Ready for a<br>little birthday magic?</h2>
        <p class="message">
            There's a little birthday magic waiting for you.<br>
            This moment is all yours. 💌
        </p>
        <button class="primary-btn" onclick="openSurprise()">
            OPEN YOUR SURPRISE &nbsp; ↗
        </button>
    </div>

    <div id="surprise">

        <div class="card">
            <div class="card-tag">Today is all about you</div>
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
            <div class="card-tag">Something sweet</div>
            <h2>A little birthday magic.</h2>

            <p class="message">
                Make a wish, close your eyes for a moment,
                and imagine all the lovely things waiting for you. 🌙
            </p>

            CAKE_SECTION

            <div class="candle-row" id="candles">
                <div class="candle"><div class="flame"></div></div>
                <div class="candle"><div class="flame"></div></div>
                <div class="candle"><div class="flame"></div></div>
                <div class="candle"><div class="flame"></div></div>
                <div class="candle"><div class="flame"></div></div>
            </div>

            <p class="message">Take a breath. Make a wish. This moment is yours.</p>

            <button class="primary-btn" onclick="blowCandles()">
                MAKE A WISH &nbsp; ✧
            </button>

            <div style="margin-top:17px">
                <button class="secondary-btn" onclick="celebrate()">A LITTLE MORE MAGIC</button>
                <button class="secondary-btn" onclick="hug()">A VIRTUAL HUG</button>
                <button class="secondary-btn" onclick="wish()">MAKE ANOTHER WISH</button>
                <button class="secondary-btn" onclick="toggleMusic()" id="musicButton">
                    ▶ PLAY BIRTHDAY MUSIC
                </button>
            </div>

            <p id="reaction" aria-live="polite"></p>
        </div>
    </div>

    <div class="footer">
        MADE WITH LOVE BY SANDY<br>
        A LITTLE BIRTHDAY MEMORY TO KEEP
    </div>
</div>
</div>

MUSIC_SECTION

<script>
let musicPlaying = false;
let candlesBlown = false;

function confettiBurst() {
    const colors = [
        "#d66b98", "#e8a9c2", "#b8a5df",
        "#f3d6a1", "#ffffff", "#d7b4ca"
    ];

    for (let i = 0; i < 100; i++) {
        const piece = document.createElement("span");
        piece.className = "confetti";

        piece.style.background =
            colors[Math.floor(Math.random() * colors.length)];

        piece.style.left = Math.random() * 100 + "vw";
        piece.style.width = (4 + Math.random() * 6) + "px";
        piece.style.height = (7 + Math.random() * 10) + "px";
        piece.style.borderRadius = Math.random() > .5 ? "50%" : "1px";
        piece.style.setProperty(
            "--drift", (Math.random() * 200 - 100) + "px"
        );
        piece.style.animationDuration = (3 + Math.random() * 2) + "s";
        piece.style.animationDelay = Math.random() * .8 + "s";

        document.body.appendChild(piece);
        setTimeout(() => piece.remove(), 6500);
    }
}

function cameraFlash() {
    const flash = document.createElement("div");
    flash.className = "flash";
    document.body.appendChild(flash);
    setTimeout(() => flash.remove(), 700);
}

function openSurprise() {
    document.getElementById("intro").style.display = "none";
    document.getElementById("surprise").style.display = "block";

    cameraFlash();
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
    cameraFlash();

    document.getElementById("reaction").textContent =
        "A little extra happiness, just for you, Muskan. 💗";
}

function hug() {
    document.getElementById("reaction").textContent =
        "Big virtual hug from Sandy! Consider yourself hugged. 🤗💗";
    confettiBurst();
}

function wish() {
    document.getElementById("reaction").textContent =
        "Wish made! May something beautiful find its way to you. 🌷💖";
    confettiBurst();
}

function blowCandles() {
    const flames = document.querySelectorAll(".flame");

    if (!candlesBlown) {
        flames.forEach(flame => flame.classList.add("off"));
        candlesBlown = true;

        document.getElementById("reaction").textContent =
            "Candles out! Keep your wish in your heart, Muskan. ✨";

        confettiBurst();
    } else {
        flames.forEach(flame => flame.classList.remove("off"));
        candlesBlown = false;

        document.getElementById("reaction").textContent =
            "One more chance to make a wish. 💗";
    }
}

async function toggleMusic() {
    const audio = document.getElementById("birthdaySong");
    const button = document.getElementById("musicButton");

    if (!audio.getAttribute("src")) {
        document.getElementById("reaction").textContent =
            "Add birthday_song.mp3 to the app folder to enable music.";
        return;
    }

    try {
        if (!musicPlaying) {
            await audio.play();
            musicPlaying = true;
            button.textContent = "❚❚ PAUSE BIRTHDAY MUSIC";
        } else {
            audio.pause();
            musicPlaying = false;
            button.textContent = "▶ PLAY BIRTHDAY MUSIC";
        }
    } catch (error) {
        document.getElementById("reaction").textContent =
            "Tap the music button again to start playback.";
    }
}
</script>
</body>
</html>
"""

page = page.replace("PHOTO_SECTION", photo_section)
page = page.replace("CAKE_SECTION", cake_section)
page = page.replace("MUSIC_SECTION", music_section)

components.html(page, height=2700, scrolling=True)
