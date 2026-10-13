import streamlit as st
import streamlit.components.v1 as components
import os
import base64
from datetime import datetime

st.set_page_config(
    page_title="A Special Surprise 💗",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------------
# SET MUSKAN'S BIRTHDAY DATE & TIME (12:00 AM Midnight)
# Format: datetime(YYYY, MM, DD, HH, MM, SS)
# -------------------------------------------------------------
BIRTHDAY_TARGET = datetime(2026, 10, 15, 0, 0, 0)  # Update as needed

# Check server-side if midnight has passed
now = datetime.now()
is_unlocked = now >= BIRTHDAY_TARGET

# ---------------------------------
# LOAD ASSETS (PHOTO, CAKE)
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

photo_section = (
    f'<img class="portrait" src="{photo_src}" alt="Muskan">'
    if photo_src
    else '<div class="photo-placeholder">📸<br>Add Muskan’s photo as muskan.jpg</div>'
)

cake_section = (
    f'<img class="cake-portrait" src="{cake_src}" alt="Muskan’s Birthday Cake">'
    if cake_src
    else '<div class="photo-placeholder">🎂<br>Add cake image as muskan_cake.jpg</div>'
)

# ---------------------------------
# HTML & CSS PAGE TEMPLATE
# ---------------------------------
page = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Sacramento&display=swap" rel="stylesheet">
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
    font-weight: 600;
    color: #a14e84;
}

h1 {
    font-family: 'Sacramento', cursive;
    font-weight: normal;
    font-size: clamp(55px, 11vw, 95px);
    margin: 10px 0 12px;
    line-height: 1.1;
    color: #9c3f7c;
}

.subtitle {
    max-width: 500px;
    margin: 0 auto 22px;
    line-height: 1.8;
    color: #936c90;
    font-size: 15px;
    font-weight: 500;
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
    padding: 10px;
    border-radius: 32px;
    background: linear-gradient(60deg, #ffb8da, #c9b9ff, #ffe2bc, #ff9ebb, #b19eff);
    background-size: 300% 300%;
    box-shadow: 0 0 25px rgba(223, 128, 181, 0.6), 0 0 50px rgba(162, 138, 229, 0.4);
    animation: instaFrameGlow 6s ease infinite, floatPhoto 3s ease-in-out infinite alternate;
}

@keyframes instaFrameGlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes floatPhoto {
    0% { transform: translateY(0px); }
    100% { transform: translateY(-6px); }
}

.portrait, .cake-portrait {
    display: block;
    width: 100%;
    max-height: 430px;
    object-fit: cover;
    border-radius: 24px;
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
    font-weight: normal;
    font-size: clamp(38px, 8vw, 60px);
    color: #9c3f7c;
    line-height: 1.2;
    margin: 10px 0;
}

.message {
    color: #795b78;
    font-size: 15px;
    line-height: 2;
    font-weight: 500;
}

button {
    border: none;
    cursor: pointer;
    border-radius: 35px;
    padding: 13px 21px;
    margin: 7px 4px;
    font-size: 14px;
    font-weight: 600;
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

.countdown-grid {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin: 20px 0;
}

.time-box {
    background: #fff0f6;
    border: 1px solid #edc1dc;
    padding: 12px 15px;
    border-radius: 16px;
    min-width: 70px;
    box-shadow: 0 4px 15px rgba(156, 63, 124, 0.08);
}

.time-number {
    font-size: 24px;
    font-weight: 700;
    color: #9c3f7c;
}

.time-label {
    font-size: 10px;
    letter-spacing: 1px;
    color: #a783a4;
    font-weight: 600;
    margin-top: 4px;
}

#lock-card, #open-card, #surprise, #top-decor {
    display: none;
}

@keyframes appear {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

#surprise {
    animation: appear .8s ease;
}

#reaction {
    min-height: 30px;
    color: #a14e84;
    font-weight: 600;
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
    font-weight: 600;
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

    <!-- TOP DECOR (Revealed after opening) -->
    <div class="decor" id="top-decor">✧ 21 ✧</div>
    <div class="pill" id="top-pill">A SPECIAL MOMENT</div>

    <!-- DYNAMIC HEADER -->
    <h1 id="main-title">Counting Down... ✨</h1>
    <p class="subtitle" id="main-subtitle">
        Something wonderful and exciting is on its way. Stay tuned! 🌷
    </p>

    <!-- HIDDEN PHOTO WRAP (Revealed only when surprise opens) -->
    <div class="photo-wrap" id="photo-container">
        PHOTO_SECTION
    </div>

    <!-- 1. LOCKED COUNTDOWN CARD (Shown before 12 AM) -->
    <div class="card" id="lock-card">
        <div style="font-size:48px">⏳</div>
        <h2>Waiting for Midnight...</h2>
        <p class="message">
            Shhh! A special surprise is locked inside.<br>
            The countdown is on. Come back when the clock strikes 12! 🌙
        </p>
        
        <div class="countdown-grid">
            <div class="time-box">
                <div class="time-number" id="days">00</div>
                <div class="time-label">DAYS</div>
            </div>
            <div class="time-box">
                <div class="time-number" id="hours">00</div>
                <div class="time-label">HOURS</div>
            </div>
            <div class="time-box">
                <div class="time-number" id="minutes">00</div>
                <div class="time-label">MINS</div>
            </div>
            <div class="time-box">
                <div class="time-number" id="seconds">00</div>
                <div class="time-label">SECS</div>
            </div>
        </div>
    </div>

    <!-- 2. OPEN SURPRISE CARD (Shown after 12 AM before clicking) -->
    <div class="card" id="open-card">
        <div style="font-size:48px">🎁</div>
        <h2>The time has arrived!</h2>
        <p class="message">
            The clock has struck midnight! Your special surprise is finally ready.<br>
            Click below to open it up! 💌
        </p>
        <button onclick="openSurprise()">Open Your Surprise ✨</button>
    </div>

    <!-- 3. FULL UNLOCKED SURPRISE CONTENT (Shown after clicking open) -->
    <div id="surprise">
        <div class="decor">🎈 ✨ 🎈</div>

        <div class="card">
            <h2>Cheers to 21 Years, Muskan! 🎂</h2>
            <p class="message">
                Happy 21st Birthday! Turning 21 is a huge milestone, and today is all about celebrating the incredible person you've become. 💕<br><br>

                May your 21st year be filled with unforgettable adventures, genuine smiles, beautiful memories, exciting opportunities, and people who remind you how truly special you are. 🌸<br><br>

                Keep dreaming big, laughing out loud, and shining your bright light everywhere you go. You deserve all the happiness in the world! ✨<br><br>

                I'm so lucky to have you as my friend. I hope this little surprise brings the biggest smile to your face today. 💗
            </p>

            <h2 style="font-size:28px">Lots of love, Sandy 💖</h2>
        </div>

        <div class="card">
            <h2>A little 21st birthday magic ✨</h2>
            <p class="message">
                Make a wish for your 21st year, close your eyes for a moment,
                and imagine all the wonderful things coming your way. 🌙<br>
                <b>Tap your custom birthday cake below!</b>
            </p>

            <div class="cake-wrap" onclick="celebrate()">
                CAKE_SECTION
            </div>

            <button onclick="celebrate()">More confetti! 🎉</button>
            <button class="secondary" onclick="hug()">Send a virtual hug 🤗</button>
            <button class="secondary" onclick="wish()">Make a wish 🌟</button>

            <p id="reaction" aria-live="polite"></p>
        </div>
    </div>

    <div class="footer">
        MADE WITH 💗 BY SANDY<br>
        CELEBRATING MUSKAN'S 21ST BIRTHDAY
    </div>
</div>

<script>
const targetDate = new Date("TARGET_DATE_STR").getTime();
let isUnlocked = IS_UNLOCKED_BOOL;

function checkState() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    if (distance <= 0 || isUnlocked) {
        // Past midnight: Show the "Open Surprise" button card, hide countdown
        document.getElementById("lock-card").style.display = "none";
        document.getElementById("open-card").style.display = "block";
    } else {
        // Before midnight: Show countdown card, hide open button
        document.getElementById("lock-card").style.display = "block";
        document.getElementById("open-card").style.display = "none";
    }
}

function confettiBurst() {
    const symbols = ["💗", "💕", "✨", "🌸", "🎉", "💖", "🎈", "🥂"];
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
    // Hide the open button card
    document.getElementById("open-card").style.display = "none";
    
    // REVEAL ALL 21ST BIRTHDAY DETAILS & PHOTO
    document.getElementById("top-decor").style.display = "block";
    document.getElementById("top-pill").textContent = "ENTERING A FABULOUS NEW CHAPTER";
    document.getElementById("main-title").textContent = "Happy 21st, Muskan! 💗";
    document.getElementById("main-subtitle").innerHTML = "Stepping into 21 with grace, beauty, and magic. ✨<br>Here is a little corner of the internet made just to celebrate YOU. 🌷";
    
    document.getElementById("photo-container").style.display = "block";
    document.getElementById("surprise").style.display = "block";
    
    confettiBurst();
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function updateCountdown() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    if (distance <= 0) {
        isUnlocked = true;
        checkState();
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    const daysElem = document.getElementById("days");
    if (daysElem) {
        daysElem.textContent = String(days).padStart(2, '0');
        document.getElementById("hours").textContent = String(hours).padStart(2, '0');
        document.getElementById("minutes").textContent = String(minutes).padStart(2, '0');
        document.getElementById("seconds").textContent = String(seconds).padStart(2, '0');
    }
}

// Initial state check
checkState();
setInterval(updateCountdown, 1000);

function celebrate() {
    confettiBurst();
    document.getElementById("reaction").textContent =
        "Yayyy, Happy 21st Muskan! 🎉 Wishing you the best year yet! 💗";
}

function hug() {
    document.getElementById("reaction").textContent =
        "Big warm 21st birthday hug from Sandy! 🤗💗";
    confettiBurst();
}

function wish() {
    document.getElementById("reaction").textContent =
        "✨ 21st wish made! May all your dreams turn into reality. 🌷💖";
    confettiBurst();
}
</script>
</body>
</html>
"""

# Format Target Date string for JS
target_str = BIRTHDAY_TARGET.strftime("%Y-%m-%dT%H:%M:%S")

# Inject placeholders safely
page = page.replace("PHOTO_SECTION", photo_section)
page = page.replace("CAKE_SECTION", cake_section)
page = page.replace("TARGET_DATE_STR", target_str)
page = page.replace("IS_UNLOCKED_BOOL", "true" if is_unlocked else "false")

components.html(page, height=1750, scrolling=True)