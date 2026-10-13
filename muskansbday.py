```python
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
# WEBSITE
# ---------------------------------
page = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Stylish fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Dancing+Script:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: 'DM Sans', sans-serif;
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
    font-family: 'Dancing Script', cursive;
    font-size: clamp(48px, 9vw, 78px);
    font-weight: 700;
    margin: 20px 0 12px;
    line-height: 1.15;
    color: #a04d86;
    text-shadow: 0 5px 20px #eab3d450;
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
    background: #ffffffd9;
    box-shadow: 0 10px 32px #9c699515;
}

h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(32px, 6vw, 44px);
    font-weight: 600;
    color: #a14e84;
    line-height: 1.2;
}

.message {
    font-family: 'DM Sans', sans-serif;
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
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 600;
    color: white;
    background: linear-gradient(100deg, #df80b5, #a28ae5);
    box-shadow: 0 7px 17px #b576b62b;
    transition: transform .2s, box-shadow .2s;
}

button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 10px 23px #b576b650;
}

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
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(90px, 20vw, 145px);
    line-height: 1;
    font-weight: 600;
    background: linear-gradient(135deg, #e58ab8, #a28ae5);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 10px 30px #d7a4df30;
    animation: ageReveal 1.1s ease both;
}

.chapter-card h2 {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(34px, 7vw, 48px);
    margin-top: 8px;
}

.chapter-signature {
    margin-top: 18px;
    font-family: 'Dancing Script', cursive;
    font-size: 25px;
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

/* ---------------------------------
   CSS BIRTHDAY CAKE
   No external image required
--------------------------------- */
.cake-scene {
    position: relative;
    width: min(100%, 350px);
    height: 290px;
    margin: 22px auto 10px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 26px;
    animation: cakeFloat 3s ease-in-out infinite;
}

@keyframes cakeFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
}

.cake-shadow {
    position: absolute;
    bottom: 17px;
    width: 270px;
    height: 24px;
    background: #a76a9c25;
    border-radius: 50%;
    filter: blur(7px);
}

.cake-plate {
    position: absolute;
    bottom: 18px;
    width: 290px;
    height: 22px;
    border-radius: 50%;
    background: linear-gradient(180deg, #fff, #e7d7ed 65%, #cdb8d8);
    border: 2px solid #ead8ed;
    box-shadow: 0 6px 8px #91618d20;
}

.cake-base {
    position: absolute;
    bottom: 38px;
    width: 240px;
    height: 91px;
    border-radius: 15px 15px 22px 22px;
    background: linear-gradient(90deg, #d96fa7, #f5b8d5 28%, #ffe1ed 52%, #e99bc6 82%, #c9619c);
    box-shadow: inset 0 -10px 0 #c65c95, inset 0 8px 0 #fff0f7;
    border-bottom: 5px solid #c65c95;
}

.cake-base::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 19px;
    border-radius: 50%;
    background: linear-gradient(90deg, #fff0f8, #fffafd, #f5c7e1);
}

.cake-top {
    position: absolute;
    bottom: 121px;
    width: 240px;
    height: 43px;
    border-radius: 50%;
    background: linear-gradient(160deg, #fff9fd, #f9d8eb 75%, #eaa8ce);
    border: 2px solid #f7cde4;
    box-shadow: 0 5px 8px #a95d9130;
}

.cake-top::after {
    content: "";
    position: absolute;
    left: 12px;
    right: 12px;
    top: 8px;
    height: 10px;
    border-radius: 50%;
    border-top: 3px dotted #dfa0c5;
}

.cake-drip {
    position: absolute;
    z-index: 2;
    bottom: 100px;
    width: 240px;
    height: 30px;
    background: #f9d8eb;
    border-radius: 0 0 15px 15px;
    clip-path: polygon(0 0,100% 0,100% 45%,94% 45%,92% 100%,86% 100%,83% 45%,72% 45%,69% 78%,63% 78%,60% 45%,45% 45%,42% 100%,36% 100%,33% 45%,20% 45%,17% 75%,11% 75%,9% 45%,0 45%);
}

.cake-ribbon {
    position: absolute;
    z-index: 3;
    bottom: 64px;
    width: 240px;
    height: 8px;
    background: linear-gradient(90deg, #b94d8a, #f3a7d0, #b94d8a);
    box-shadow: 0 2px 3px #9c3c7d25;
}

.cake-name {
    position: absolute;
    z-index: 5;
    bottom: 72px;
    left: 50%;
    transform: translateX(-50%);
    width: 178px;
    padding: 5px 3px 7px;
    border-radius: 12px;
    background: linear-gradient(145deg, #fff9fc, #ffe8f4);
    border: 1px solid #e9b2d2;
    color: #a3447f;
    font-family: 'Dancing Script', cursive;
    font-size: 28px;
    font-weight: 700;
    text-shadow: 0 1px #fff;
    box-shadow: 0 3px 8px #9c467a22;
}

.candle {
    position: absolute;
    z-index: 6;
    bottom: 158px;
    width: 10px;
    height: 43px;
    border-radius: 4px 4px 2px 2px;
    background: repeating-linear-gradient(
        135deg, #fff9ff 0px, #fff9ff 5px,
        #dca5ed 5px, #dca5ed 9px
    );
    box-shadow: 0 2px 4px #a55a9c20;
}

.candle.one { left: calc(50% - 28px); }
.candle.two { left: calc(50% + 18px); }

.flame {
    position: absolute;
    left: 1px;
    top: -19px;
    width: 8px;
    height: 16px;
    border-radius: 70% 30% 65% 35%;
    transform: rotate(45deg);
    background: linear-gradient(135deg, #fff6a3, #ff9b45 75%);
    box-shadow: 0 0 12px #ffc46b, 0 0 22px #ffb3d8;
    transform-origin: bottom center;
    animation: flicker .65s infinite alternate;
}

@keyframes flicker {
    from { transform: rotate(40deg) scale(.9); }
    to { transform: rotate(52deg) scale(1.08); }
}

.cake-pearl {
    position: absolute;
    z-index: 4;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #fff9fd;
    box-shadow: 0 0 3px #d98eb8;
}

.pearl1 { left: 66px; bottom: 49px; }
.pearl2 { left: 91px; bottom: 49px; }
.pearl3 { right: 91px; bottom: 49px; }
.pearl4 { right: 66px; bottom: 49px; }

.cake-sparkle {
    position: absolute;
    color: #c78bb5;
    font-size: 21px;
    animation: sparkle 1.8s infinite alternate;
}

.sparkle1 { top: 25px; left: 23px; }
.sparkle2 { top: 55px; right: 22px; animation-delay: .5s; }
.sparkle3 { top: 105px; left: 42px; animation-delay: .8s; }
.sparkle4 { top: 110px; right: 40px; animation-delay: .3s; }

@keyframes sparkle {
    from { opacity: .45; transform: scale(.8) rotate(0); }
    to { opacity: 1; transform: scale(1.2) rotate(18deg); }
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
    .cake-scene { transform: scale(.94); transform-origin: bottom center; }
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
            <h2>Happy Birthday,<br>Muskan! 💗</h2>
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

            <h2 style="font-size:36px">Lots of wishes,<br><span style="font-family:'Dancing Script',cursive">Sandy 💖</span></h2>
        </div>

        <div class="card">
            <h2 style="font-size:36px">A little birthday magic ✨</h2>
            <p class="message">
                Make a wish, close your eyes for a moment,
                and imagine all the lovely things waiting for you. 🌙
            </p>

            <!-- Decorative CSS cake with Muskan's name -->
            <div class="cake-scene" onclick="celebrate()" role="button" tabindex="0" aria-label="Tap Muskan's birthday cake">
                <span class="cake-sparkle sparkle1">✧</span>
                <span class="cake-sparkle sparkle2">✦</span>
                <span class="cake-sparkle sparkle3">✧</span>
                <span class="cake-sparkle sparkle4">✦</span>

                <div class="cake-shadow"></div>
                <div class="cake-plate"></div>
                <div class="cake-base"></div>
                <div class="cake-top"></div>
                <div class="cake-drip"></div>
                <div class="cake-ribbon"></div>

                <div class="cake-name">Muskan</div>

                <div class="candle one"><span class="flame"></span></div>
                <div class="candle two"><span class="flame"></span></div>

                <span class="cake-pearl pearl1"></span>
                <span class="cake-pearl pearl2"></span>
                <span class="cake-pearl pearl3"></span>
                <span class="cake-pearl pearl4"></span>
            </div>

            <p class="message">A special cake for a special girl. ♡<br>Tap the cake for more birthday magic!</p>

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

components.html(page, height=2600, scrolling=True)
```
