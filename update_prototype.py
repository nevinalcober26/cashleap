import os

with open('new_avatar_b64.txt') as f:
    avatar_b64 = f.read().strip()
with open('card2_b64.txt') as f:
    card2_b64 = f.read().strip()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CASHLEAP - Mobile Prototype Previewer</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}

    body {{
      font-family: var(--font-main);
      background: #08061a;
      min-height: 100vh;
      min-height: 100dvh;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      overflow: hidden;
      user-select: none;
      -webkit-user-select: none;
    }}

    /* Clean Frameless Mobile Viewport */
    .phone-frame {{
      width: 376px;
      height: 812px;
      max-height: 100dvh;
      border-radius: 0px;
      position: relative;
      overflow: hidden;
      clip-path: inset(0);
      isolation: isolate;
      transform: translateZ(0);
      box-shadow: none;
      background: #0d0c2b;
    }}

    .scrollbar-none::-webkit-scrollbar {{
      display: none;
      width: 0;
      height: 0;
    }}
    .scrollbar-none {{
      -ms-overflow-style: none;
      scrollbar-width: none;
    }}

    @media (max-width: 480px) {{
      .phone-frame {{
        width: 100vw;
        height: 100dvh;
        max-height: 100dvh;
      }}
    }}

    /* Screen Backgrounds */
    .splash-bg {{
      background-color: #2f288a;
      background-image: 
        radial-gradient(circle at 12% 6%, rgba(133, 86, 134, 0.85) 0%, rgba(133, 86, 134, 0) 45%),
        radial-gradient(circle at 92% 8%, rgba(89, 21, 138, 0.95) 0%, rgba(89, 21, 138, 0) 50%),
        radial-gradient(circle at 96% 42%, rgba(131, 68, 128, 0.85) 0%, rgba(131, 68, 128, 0) 52%),
        radial-gradient(circle at 15% 88%, rgba(23, 27, 138, 0.95) 0%, rgba(23, 27, 138, 0) 60%),
        radial-gradient(circle at 90% 92%, rgba(92, 57, 125, 0.8) 0%, rgba(92, 57, 125, 0) 55%),
        linear-gradient(155deg, #5d3b75 0%, #372588 38%, #212085 75%, #463078 100%);
    }}

    .login-bg {{
      background-color: #0b0b26;
      background-image:
        radial-gradient(circle at 6% 6%, rgba(189, 108, 125, 0.78) 0%, rgba(130, 68, 128, 0.38) 26%, rgba(11, 11, 38, 0) 54%),
        radial-gradient(circle at 62% 8%, rgba(58, 22, 138, 0.85) 0%, rgba(11, 11, 38, 0) 48%),
        radial-gradient(circle at 92% 28%, rgba(82, 41, 140, 0.55) 0%, rgba(11, 11, 38, 0) 45%),
        radial-gradient(circle at 96% 84%, rgba(73, 23, 165, 0.78) 0%, rgba(11, 11, 38, 0) 55%),
        linear-gradient(180deg, #191345 0%, #0d0c29 42%, #0a0a24 72%, #190e4f 100%);
    }}

    .auth-bg {{
      background-color: #0c0b29;
      background-image:
        radial-gradient(circle at 8% 10%, rgba(142, 68, 173, 0.45) 0%, rgba(12, 11, 41, 0) 55%),
        radial-gradient(circle at 85% 15%, rgba(68, 45, 142, 0.6) 0%, rgba(12, 11, 41, 0) 50%),
        radial-gradient(circle at 92% 82%, rgba(45, 130, 255, 0.3) 0%, rgba(12, 11, 41, 0) 55%),
        radial-gradient(circle at 10% 90%, rgba(120, 24, 154, 0.35) 0%, rgba(12, 11, 41, 0) 50%),
        linear-gradient(180deg, #171243 0%, #0c0b29 48%, #090822 75%, #140d3f 100%);
    }}

    .welcome-bg {{
      background-color: #382c7a;
      background-image: 
        radial-gradient(circle at 95% 42%, rgba(135, 70, 130, 0.75) 0%, rgba(135, 70, 130, 0) 55%),
        radial-gradient(circle at 8% 88%, rgba(44, 62, 160, 0.88) 0%, rgba(44, 62, 160, 0) 58%),
        radial-gradient(circle at 88% 8%, rgba(105, 41, 140, 0.68) 0%, rgba(105, 41, 140, 0) 45%),
        linear-gradient(160deg, #654480 0%, #52357a 32%, #3d3480 65%, #2c3e9b 100%);
    }}

    /* Screen 6: Home Screen Background */
    .home-bg {{
      background-color: #0b0922;
      background-image: 
        radial-gradient(circle at 20% 10%, rgba(138, 75, 175, 0.32) 0%, rgba(11, 9, 34, 0) 48%),
        radial-gradient(circle at 85% 14%, rgba(68, 45, 150, 0.45) 0%, rgba(11, 9, 34, 0) 50%),
        radial-gradient(circle at 50% 48%, rgba(55, 30, 110, 0.22) 0%, rgba(11, 9, 34, 0) 55%),
        linear-gradient(180deg, #1f1455 0%, #15103a 28%, #0f0c2f 55%, #08061a 100%);
    }}

    /* Splash Logo Animations */
    .logo-petal {{
      opacity: 0;
      transform-box: fill-box;
      transform-origin: center;
    }}
    .animate-splash .petal-1 {{ animation: petalPop1 0.85s cubic-bezier(0.34, 1.56, 0.64, 1) 0.15s forwards; }}
    .animate-splash .petal-2 {{ animation: petalPop2 0.85s cubic-bezier(0.34, 1.56, 0.64, 1) 0.28s forwards; }}
    .animate-splash .petal-3 {{ animation: petalPop3 0.85s cubic-bezier(0.34, 1.56, 0.64, 1) 0.41s forwards; }}
    .animate-splash .petal-4 {{ animation: petalPop4 0.85s cubic-bezier(0.34, 1.56, 0.64, 1) 0.54s forwards; }}
    .animate-splash .petal-5 {{ animation: petalPop5 0.85s cubic-bezier(0.34, 1.56, 0.64, 1) 0.67s forwards; }}

    .logo-letter {{
      opacity: 0;
      transform: translateX(-14px) scale(0.94);
      transform-box: fill-box;
      transform-origin: left center;
    }}
    .animate-splash .letter-1 {{ animation: letterSlide 0.6s cubic-bezier(0.22, 1, 0.36, 1) 0.72s forwards; }}
    .animate-splash .letter-2 {{ animation: letterSlide 0.6s cubic-bezier(0.22, 1, 0.36, 1) 0.79s forwards; }}
    .animate-splash .letter-3 {{ animation: letterSlide 0.6s cubic-bezier(0.22, 1, 0.36, 1) 0.86s forwards; }}
    .animate-splash .letter-4 {{ animation: letterSlide 0.6s cubic-bezier(0.22, 1, 0.36, 1) 0.93s forwards; }}
    .animate-splash .letter-5 {{ animation: letterSlide 0.6s cubic-bezier(0.22, 1, 0.36, 1) 1.00s forwards; }}
    .animate-splash .letter-6 {{ animation: letterSlide 0.6s cubic-bezier(0.22, 1, 0.36, 1) 1.07s forwards; }}
    .animate-splash .letter-7 {{ animation: letterSlide 0.6s cubic-bezier(0.22, 1, 0.36, 1) 1.14s forwards; }}
    .animate-splash .letter-8 {{ animation: letterSlide 0.6s cubic-bezier(0.22, 1, 0.36, 1) 1.21s forwards; }}

    .animate-splash .logo-wrapper {{
      animation: logoBreath 2.6s ease-in-out 0.1s forwards;
    }}

    @keyframes petalPop1 {{
      0% {{ opacity: 0; transform: translate(-22px, -22px) scale(0.2) rotate(-45deg); }}
      70% {{ opacity: 1; transform: translate(2px, 2px) scale(1.06) rotate(4deg); }}
      100% {{ opacity: 1; transform: translate(0, 0) scale(1) rotate(0deg); }}
    }}
    @keyframes petalPop2 {{
      0% {{ opacity: 0; transform: translate(22px, -22px) scale(0.2) rotate(45deg); }}
      70% {{ opacity: 1; transform: translate(-2px, 2px) scale(1.06) rotate(-4deg); }}
      100% {{ opacity: 1; transform: translate(0, 0) scale(1) rotate(0deg); }}
    }}
    @keyframes petalPop3 {{
      0% {{ opacity: 0; transform: translate(-25px, 0px) scale(0.2) rotate(-60deg); }}
      70% {{ opacity: 1; transform: translate(2px, 0px) scale(1.06) rotate(5deg); }}
      100% {{ opacity: 1; transform: translate(0, 0) scale(1) rotate(0deg); }}
    }}
    @keyframes petalPop4 {{
      0% {{ opacity: 0; transform: translate(-22px, 22px) scale(0.2) rotate(-45deg); }}
      70% {{ opacity: 1; transform: translate(2px, -2px) scale(1.06) rotate(4deg); }}
      100% {{ opacity: 1; transform: translate(0, 0) scale(1) rotate(0deg); }}
    }}
    @keyframes petalPop5 {{
      0% {{ opacity: 0; transform: translate(22px, 22px) scale(0.2) rotate(60deg); }}
      70% {{ opacity: 1; transform: translate(-2px, -2px) scale(1.06) rotate(-4deg); }}
      100% {{ opacity: 1; transform: translate(0, 0) scale(1) rotate(0deg); }}
    }}
    @keyframes letterSlide {{
      0% {{ opacity: 0; transform: translateX(-14px) scale(0.92); filter: blur(4px); }}
      100% {{ opacity: 1; transform: translateX(0) scale(1); filter: blur(0px); }}
    }}
    @keyframes logoBreath {{
      0% {{ transform: scale(0.92); }}
      65% {{ transform: scale(1.02); filter: drop-shadow(0 8px 28px rgba(220, 214, 232, 0.28)); }}
      100% {{ transform: scale(1); filter: drop-shadow(0 4px 16px rgba(220, 214, 232, 0.14)); }}
    }}

    /* Screen Transitions */
    .screen-layer {{
      position: absolute !important;
      inset: 0;
      width: 100%;
      height: 100%;
      transition: opacity 0.65s cubic-bezier(0.22, 1, 0.36, 1), transform 0.65s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .screen-hidden-left {{
      opacity: 0;
      transform: translateX(-28px) scale(0.96);
      pointer-events: none;
    }}
    .screen-hidden-right {{
      opacity: 0;
      transform: translateX(28px) scale(0.96);
      pointer-events: none;
    }}
    .screen-active {{
      opacity: 1;
      transform: translate(0, 0) scale(1);
      pointer-events: auto;
    }}

    /* Option Pill Cards */
    .option-card {{
      height: 68px;
      border-radius: 36px;
      transition: all 0.32s cubic-bezier(0.22, 1, 0.36, 1);
      border: 1px solid transparent;
      background: transparent;
    }}
    .option-card.selected {{
      background: rgba(255, 255, 255, 0.085);
      border-color: rgba(255, 255, 255, 0.11);
      box-shadow: none;
      backdrop-filter: blur(12px);
    }}
    .option-card:not(.selected):hover {{
      background: rgba(255, 255, 255, 0.035);
    }}

    /* Pink Checkmark Badge */
    .check-badge {{
      width: 28px;
      height: 28px;
      border-radius: 9999px;
      background: #ff2a6d;
      box-shadow: none;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    /* Chevron Wave Animation */
    @keyframes chevronPulse {{
      0%, 100% {{ opacity: 0.18; }}
      50% {{ opacity: 0.85; }}
    }}
    .chevron-1 {{ animation: chevronPulse 1.6s infinite 0.0s; }}
    .chevron-2 {{ animation: chevronPulse 1.6s infinite 0.22s; }}
    .chevron-3 {{ animation: chevronPulse 1.6s infinite 0.44s; }}

    /* Bottom Slider Track */
    .slider-track {{
      height: 82px;
      border-radius: 42px;
      background: rgba(15, 13, 41, 0.76);
      border: 1px solid rgba(255, 255, 255, 0.05);
      box-shadow: none;
      backdrop-filter: blur(16px);
    }}
    .slider-thumb {{
      width: 72px;
      height: 72px;
      border-radius: 9999px;
      background: linear-gradient(145deg, #2d82ff 0%, #1c6ef2 100%);
      box-shadow: none;
      touch-action: none;
      transition: transform 0.25s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.25s ease;
    }}
    .slider-thumb.dragging {{
      transition: none;
      box-shadow: none;
    }}

    /* Animated Slide to Send Shimmer & Thumb Pulse */
    @keyframes slideSendShimmer {{
      0% {{ background-position: 200% center; }}
      100% {{ background-position: -200% center; }}
    }}
    @keyframes slideSendThumbNudge {{
      0%, 100% {{ transform: translateX(0px) scale(1); box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.45); }}
      50% {{ transform: translateX(5px) scale(1.03); box-shadow: 0 0 18px 2px rgba(59, 130, 246, 0.45); }}
    }}
    .slide-send-label {{
      background: linear-gradient(90deg, rgba(255,255,255,0.65) 0%, #ffffff 45%, #93c5fd 50%, #ffffff 55%, rgba(255,255,255,0.65) 100%);
      background-size: 220% auto;
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: slideSendShimmer 2.6s linear infinite;
    }}
    .slide-send-thumb-idle {{
      animation: slideSendThumbNudge 2.1s ease-in-out infinite;
    }}

    /* Face ID Scanner Visuals */
    .faceid-frame {{
      width: 176px;
      height: 176px;
      border-radius: 36px;
      position: relative;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(16px);
      box-shadow: none;
    }}

    .corner-bracket {{
      position: absolute;
      width: 28px;
      height: 28px;
      border-color: #2d82ff;
      transition: border-color 0.3s ease;
    }}
    .corner-tl {{ top: 12px; left: 12px; border-top: 3.5px solid #2d82ff; border-left: 3.5px solid #2d82ff; border-top-left-radius: 12px; }}
    .corner-tr {{ top: 12px; right: 12px; border-top: 3.5px solid #2d82ff; border-right: 3.5px solid #2d82ff; border-top-right-radius: 12px; }}
    .corner-bl {{ bottom: 12px; left: 12px; border-bottom: 3.5px solid #2d82ff; border-left: 3.5px solid #2d82ff; border-bottom-left-radius: 12px; }}
    .corner-br {{ bottom: 12px; right: 12px; border-bottom: 3.5px solid #2d82ff; border-right: 3.5px solid #2d82ff; border-bottom-right-radius: 12px; }}

    .scanning-laser {{
      position: absolute;
      left: 18px;
      right: 18px;
      height: 3px;
      background: linear-gradient(90deg, transparent, #38bdf8 25%, #60a5fa 50%, #c084fc 75%, transparent);
      box-shadow: 0 0 16px 2px #38bdf8, 0 0 30px #818cf8;
      border-radius: 9999px;
      top: 24px;
      opacity: 0;
    }}
    .is-scanning .scanning-laser {{
      opacity: 1;
      animation: scanLaser 1.8s ease-in-out infinite alternate;
    }}

    @keyframes scanLaser {{
      0% {{ top: 22px; }}
      100% {{ top: 148px; }}
    }}

    .faceid-radar {{
      position: absolute;
      inset: -22px;
      border-radius: 50px;
      border: 1px solid rgba(45, 130, 255, 0.25);
      animation: radarPulse 2.4s ease-out infinite;
      pointer-events: none;
    }}
    .faceid-radar-2 {{
      position: absolute;
      inset: -44px;
      border-radius: 64px;
      border: 1px solid rgba(192, 132, 252, 0.15);
      animation: radarPulse 2.4s ease-out infinite 0.7s;
      pointer-events: none;
    }}
    @keyframes radarPulse {{
      0% {{ transform: scale(0.92); opacity: 0.8; }}
      100% {{ transform: scale(1.18); opacity: 0; }}
    }}

    /* Keypad Button */
    .keypad-btn {{
      width: 66px;
      height: 66px;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.055);
      border: 1px solid rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(14px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
      cursor: pointer;
    }}
    .keypad-btn:active {{
      background: rgba(255, 255, 255, 0.18);
      border-color: rgba(255, 255, 255, 0.25);
      transform: scale(0.92);
      box-shadow: 0 0 16px rgba(255, 255, 255, 0.15);
    }}

    /* Secret Key Passcode Dots */
    .passcode-dot {{
      width: 14px;
      height: 14px;
      border-radius: 9999px;
      border: 1.5px solid rgba(255, 255, 255, 0.35);
      background: rgba(255, 255, 255, 0.06);
      transition: all 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .passcode-dot.filled {{
      background: linear-gradient(135deg, #2d82ff 0%, #1c6ef2 100%);
      border-color: #38bdf8;
      box-shadow: 0 0 14px rgba(45, 130, 255, 0.85);
      transform: scale(1.18);
    }}

    /* Welcome Screen Animated Concentric Rings */
    @keyframes welcomeRingWave {{
      0%, 100% {{
        transform: scale(0.92);
        opacity: 0.25;
        border-color: rgba(210, 195, 245, 0.14);
      }}
      50% {{
        transform: scale(1.10);
        opacity: 0.95;
        border-color: rgba(236, 224, 255, 0.52);
        box-shadow: 0 0 28px rgba(192, 132, 252, 0.28);
      }}
    }}

    @keyframes welcomeRippleExpand {{
      0% {{
        transform: scale(0.52);
        opacity: 0.75;
        border-color: rgba(216, 180, 254, 0.55);
      }}
      75% {{
        opacity: 0.22;
      }}
      100% {{
        transform: scale(1.22);
        opacity: 0;
        border-color: rgba(216, 180, 254, 0);
      }}
    }}

    @keyframes welcomeAvatarGlow {{
      0%, 100% {{
        transform: scale(1);
        box-shadow: 0 0 0 6px rgba(196, 170, 240, 0.16), 0 0 28px rgba(168, 85, 247, 0.35);
      }}
      50% {{
        transform: scale(1.045);
        box-shadow: 0 0 0 10px rgba(216, 180, 254, 0.28), 0 0 42px rgba(192, 132, 252, 0.55);
      }}
    }}

    .concentric-ring-1 {{
      width: 136px;
      height: 136px;
      border-radius: 9999px;
      border: 1.5px solid rgba(220, 205, 255, 0.35);
      box-shadow: 0 0 25px rgba(180, 150, 230, 0.18);
      animation: welcomeRingWave 2.1s cubic-bezier(0.4, 0, 0.2, 1) infinite 0s;
      will-change: transform, opacity;
    }}
    .concentric-ring-2 {{
      width: 170px;
      height: 170px;
      border-radius: 9999px;
      border: 1.25px solid rgba(215, 198, 250, 0.26);
      animation: welcomeRingWave 2.1s cubic-bezier(0.4, 0, 0.2, 1) infinite 0.24s;
      will-change: transform, opacity;
    }}
    .concentric-ring-3 {{
      width: 208px;
      height: 208px;
      border-radius: 9999px;
      border: 1.15px solid rgba(210, 195, 245, 0.18);
      animation: welcomeRingWave 2.1s cubic-bezier(0.4, 0, 0.2, 1) infinite 0.48s;
      will-change: transform, opacity;
    }}
    .concentric-ring-4 {{
      width: 250px;
      height: 250px;
      border-radius: 9999px;
      border: 1px solid rgba(210, 195, 245, 0.12);
      animation: welcomeRingWave 2.1s cubic-bezier(0.4, 0, 0.2, 1) infinite 0.72s;
      will-change: transform, opacity;
    }}
    .concentric-ripple-1 {{
      width: 244px;
      height: 244px;
      border-radius: 9999px;
      border: 1.5px solid rgba(216, 180, 254, 0.42);
      animation: welcomeRippleExpand 2.4s cubic-bezier(0.16, 1, 0.3, 1) infinite 0s;
      pointer-events: none;
      will-change: transform, opacity;
    }}
    .concentric-ripple-2 {{
      width: 244px;
      height: 244px;
      border-radius: 9999px;
      border: 1.5px solid rgba(192, 132, 252, 0.35);
      animation: welcomeRippleExpand 2.4s cubic-bezier(0.16, 1, 0.3, 1) infinite 1.2s;
      pointer-events: none;
      will-change: transform, opacity;
    }}
    .welcome-avatar-shell {{
      animation: welcomeAvatarGlow 2.1s ease-in-out infinite;
      will-change: transform, box-shadow;
    }}

    /* Native iOS Alert Modal */
    .ios-modal-card {{
      background: rgba(30, 28, 54, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.14);
      backdrop-filter: blur(28px);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
      border-radius: 20px;
    }}

    /* Screen 6: Vibrant Credit Card Styling matching Image 2 */
    .debit-card-gradient {{
      background: linear-gradient(108deg, #f7aa11 0%, #f14f52 46%, #4947d5 82%, #3a47d8 100%);
      background-origin: border-box;
      background-clip: border-box;
      background-repeat: no-repeat;
      box-shadow: none;
    }}

    /* Ultra-realistic Glass Container Circle matching uploaded image media_1792692834975_611fbfd2.png */
    .action-btn, .glass-circle-btn {{
      width: 58px;
      height: 58px;
      border-radius: 9999px;
      position: relative;
      background: rgba(255, 255, 255, 0.025);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #c6c0e8;
      cursor: pointer;
      box-shadow: none;
      transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}

    .action-btn::before, .glass-circle-btn::before {{
      content: '';
      position: absolute;
      inset: 0px;
      border-radius: 9999px;
      padding: 1px;
      background: linear-gradient(135deg, 
        rgba(255, 255, 255, 0.25) 0%, 
        rgba(255, 255, 255, 0.06) 40%, 
        rgba(198, 192, 232, 0.45) 70%, 
        rgba(255, 255, 255, 0.95) 100%
      );
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      pointer-events-none;
    }}

    .action-btn:hover, .glass-circle-btn:hover {{
      background: rgba(255, 255, 255, 0.08);
      color: #ffffff;
      transform: translateY(-2px);
      box-shadow: none;
    }}

    .action-btn:active, .glass-circle-btn:active {{
      transform: scale(0.93);
      background: rgba(255, 255, 255, 0.14);
    }}

    .card2-gradient {{
      background: radial-gradient(circle at 10% 15%, #ed13d3 0%, transparent 55%),
                  radial-gradient(circle at 50% 12%, #49d6ae 0%, transparent 60%),
                  radial-gradient(circle at 90% 20%, #1b52f1 0%, transparent 60%),
                  radial-gradient(circle at 15% 90%, #d8b4fe 0%, transparent 50%),
                  radial-gradient(circle at 60% 85%, #7c3aed 0%, transparent 60%),
                  #1b52f1;
      box-shadow: none;
    }}

        /* Apple Spring Press & Micro-interactions */
    .apple-press {{
      transition: transform 0.16s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.16s ease;
      user-select: none;
      -webkit-user-select: none;
    }}
    .apple-press:active {{
      transform: scale(0.93) !important;
    }}

    /* Apple Icon Pop Bounce */
    @keyframes appleIconBounce {{
      0% {{ transform: scale(1); }}
      35% {{ transform: scale(0.82); }}
      70% {{ transform: scale(1.18); }}
      100% {{ transform: scale(1); }}
    }}
    .apple-icon-pop {{
      animation: appleIconBounce 0.38s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    /* Apple Card Holographic Shimmer */
    .card-holographic-glint {{
      background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.35) 0%, rgba(255, 255, 255, 0.05) 50%, transparent 80%);
      mix-blend-mode: overlay;
      transition: opacity 0.3s ease;
      will-change: transform, opacity;
    }}

    /* Dynamic Island States */
    .dynamic-island-container {{
      transition: width 0.38s cubic-bezier(0.34, 1.56, 0.64, 1),
                  height 0.38s cubic-bezier(0.34, 1.56, 0.64, 1),
                  border-radius 0.38s cubic-bezier(0.34, 1.56, 0.64, 1),
                  padding 0.38s ease,
                  box-shadow 0.38s ease,
                  border-color 0.38s ease;
    }}
    .dynamic-island-expanded {{
      width: 324px !important;
      height: 52px !important;
      border-radius: 26px !important;
      padding: 0 16px !important;
      background: #000000 !important;
      border-color: rgba(255, 255, 255, 0.25) !important;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.85) !important;
    }}

    /* Number counter roll animation */
    @keyframes balancePulse {{
      0% {{ transform: scale(1); }}
      50% {{ transform: scale(1.08); color: #34d399; }}
      100% {{ transform: scale(1); }}
    }}
    .balance-pop {{
      animation: balancePulse 0.45s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    /* Modal Backdrop Blur */
    /* Apple iOS 18 Translucent Liquid Glass Bottom Sheet */
    .liquid-glass-sheet {{
      background: linear-gradient(180deg, rgba(25, 20, 58, 0.96) 0%, rgba(12, 10, 32, 0.99) 100%) !important;
      backdrop-filter: blur(40px) saturate(140%) !important;
      -webkit-backdrop-filter: blur(40px) saturate(140%) !important;
      border-top: 1px solid rgba(255, 255, 255, 0.24) !important;
      border-left: none !important;
      border-right: none !important;
      border-bottom: none !important;
      box-shadow: none !important;
    }}

    /* Prevent nested backdrop-filter edge bleed on modal sheets */
    .apple-sheet-backdrop .liquid-glass-sheet {{
      background: linear-gradient(180deg, #1a153b 0%, #0e0c26 100%) !important;
      backdrop-filter: none !important;
      -webkit-backdrop-filter: none !important;
      border-left: none !important;
      border-right: none !important;
      border-bottom: none !important;
      box-shadow: none !important;
    }}

    /* Scanner Laser Animation */
    @keyframes scannerSweep {{
      0% {{ top: 12px; opacity: 0.2; }}
      20% {{ opacity: 1; }}
      80% {{ opacity: 1; }}
      100% {{ top: calc(100% - 16px); opacity: 0.2; }}
    }}
    .scanner-laser-line {{
      animation: scannerSweep 2.2s ease-in-out infinite alternate;
    }}

    .apple-sheet-backdrop {{
      top: -2px !important;
      left: -2px !important;
      right: -2px !important;
      bottom: -2px !important;
      background: rgba(7, 6, 22, 0.86) !important;
      backdrop-filter: blur(18px) !important;
      -webkit-backdrop-filter: blur(18px) !important;
    }}

    /* Floating Pill Bottom Navigation matching Uploaded Image media_1792691438984_d3dc6eed.png */
    
    /* Gradient Skeleton Loading Shimmer Effect (Borderless & Silky Smooth) */
    @keyframes skeletonGradientSweep {{
      0% {{ background-position: 200% 0; }}
      100% {{ background-position: -200% 0; }}
    }}
    #tabSkeletonOverlay {{
      transition: opacity 0.42s cubic-bezier(0.16, 1, 0.3, 1), transform 0.42s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
      border: none !important;
    }}
    #tabSkeletonOverlay, #tabSkeletonOverlay * {{
      border: none !important;
      box-shadow: none !important;
      outline: none !important;
    }}
    .skeleton-shimmer {{
      background: linear-gradient(
        90deg,
        rgba(255, 255, 255, 0.04) 0%,
        rgba(255, 255, 255, 0.04) 22%,
        rgba(139, 92, 246, 0.14) 40%,
        rgba(56, 189, 248, 0.18) 50%,
        rgba(236, 72, 153, 0.13) 60%,
        rgba(255, 255, 255, 0.04) 78%,
        rgba(255, 255, 255, 0.04) 100%
      );
      background-size: 200% 100%;
      animation: skeletonGradientSweep 1.65s linear infinite;
      border: none !important;
    }}
    .skeleton-card-shimmer {{
      background: linear-gradient(
        108deg,
        rgba(28, 22, 64, 0.72) 0%,
        rgba(28, 22, 64, 0.72) 20%,
        rgba(99, 102, 241, 0.22) 38%,
        rgba(56, 189, 248, 0.24) 50%,
        rgba(217, 70, 239, 0.18) 62%,
        rgba(28, 22, 64, 0.72) 80%,
        rgba(28, 22, 64, 0.72) 100%
      );
      background-size: 200% 100%;
      animation: skeletonGradientSweep 1.65s linear infinite;
      border: none !important;
    }}

    .pill-bottom-nav {{
      width: 359px;
      height: 76px;
      border-radius: 9999px;
      background: linear-gradient(90deg, #1f3a82 0%, #1a3178 35%, #132469 70%, #0e195c 100%);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.14), 0 12px 36px rgba(0, 0, 0, 0.55);
      position: absolute;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%) translateY(0);
      overflow: hidden;
      z-index: 45;
      pointer-events: auto;
      transition: opacity 0.32s cubic-bezier(0.22, 1, 0.36, 1), transform 0.32s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .pill-bottom-nav.nav-visible {{
      opacity: 1;
      pointer-events: auto;
      transform: translateX(-50%) translateY(0);
    }}
    .pill-bottom-nav.nav-hidden {{
      opacity: 0;
      pointer-events: none;
      transform: translateX(-50%) translateY(40px);
    }}

    .dock-tab {{
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      cursor: pointer;
      position: relative;
      transition: all 0.2s ease;
      color: #8c98bb;
      user-select: none;
      -webkit-user-select: none;
      pointer-events: auto;
    }}
    .dock-tab.active {{
      color: #ffffff;
    }}
    .dock-tab:active {{
      transform: scale(0.94);
    }}

    .dock-active-bar {{
      position: absolute;
      bottom: 0;
      width: 44px;
      height: 4px;
      background: #008eff;
      border-top-left-radius: 9999px;
      border-top-right-radius: 9999px;
      box-shadow: 0 0 12px #008eff;
      transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1);
    }}

  </style>
</head>
<body class="p-0 m-0">

  <!-- Mobile Device Viewport (Frameless Mobile View) -->
  <div class="phone-frame" id="phoneFrame">

    <!-- Floating Notification Capsule (Hidden when idle; Time & Signal Bar Removed) -->
    <div class="absolute top-0 inset-x-0 h-11 px-6 flex items-center justify-center z-40 pointer-events-none text-white select-none">
      <div 
        id="dynamicIsland" 
        onclick="onDynamicIslandTap()"
        class="dynamic-island-container absolute top-2 left-1/2 -translate-x-1/2 bg-black border border-white/10 rounded-full h-[28px] w-[98px] flex items-center justify-between px-2.5 pointer-events-none opacity-0 cursor-pointer shadow-sm z-50 overflow-hidden transition-opacity duration-300"
        title="Notification"
      >
        <div id="islandContentLeft" class="flex items-center gap-2 overflow-hidden">
          <div id="islandIconDot" class="w-2.5 h-2.5 rounded-full bg-emerald-400 flex-shrink-0 animate-pulse"></div>
          <span id="islandTitle" class="text-[11px] font-semibold tracking-tight text-white hidden whitespace-nowrap">Cashleap</span>
        </div>
        <div id="islandContentRight" class="flex items-center gap-1.5 flex-shrink-0">
          <span id="islandSub" class="text-[9.5px] font-mono font-medium text-emerald-400">AED</span>
          <div class="w-2.5 h-2.5 rounded-full bg-[#18181b] border border-white/15 flex items-center justify-center">
            <div class="w-1 h-1 rounded-full bg-blue-400/80"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SCREEN 1: SPLASH SCREEN                    -->
    <!-- ========================================== -->
    <div id="splashScreen" onclick="showScreen('login')" class="screen-layer splash-bg screen-active animate-splash flex flex-col items-center justify-center cursor-pointer" title="Tap to continue to Login">
      <div class="w-56 h-56 rounded-full bg-purple-300/10 blur-3xl absolute pointer-events-none"></div>
      <div class="logo-wrapper relative z-10 px-6 flex items-center justify-center">
        <svg width="224" height="76" viewBox="0 0 342 98" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="CASHLEAP Logo">
          <g id="logoIcon" fill="#DCD6E8">
            <path class="logo-petal petal-1" d="M 0 0 H 32 A 32 32 0 0 1 0 32 Z" />
            <path class="logo-petal petal-2" d="M 32 0 H 64 A 32 32 0 0 1 32 32 Z" />
            <path class="logo-petal petal-3" d="M 32 32 H 0 A 32 32 0 0 0 32 64 Z" />
            <path class="logo-petal petal-4" d="M 0 64 H 32 A 32 32 0 0 1 0 96 Z" />
            <path class="logo-petal petal-5" d="M 32 96 V 64 A 32 32 0 0 1 64 96 Z" />
          </g>
          <g id="logoWordmark" fill="#DCD6E8">
            <path class="logo-letter letter-1" d="M 88 49 C 88 37.8 96.2 30 107.2 30 C 116.8 30 124.2 36.1 125.4 45.4 H 115.6 C 114.6 41.2 111.5 38.8 107.2 38.8 C 101.4 38.8 97.6 42.9 97.6 49 C 97.6 55.1 101.4 59.2 107.2 59.2 C 111.6 59.2 114.7 56.8 115.7 52.4 H 125.5 C 124.2 61.9 116.8 68 107.2 68 C 96.2 68 88 60.2 88 49 Z" />
            <path class="logo-letter letter-2" fill-rule="evenodd" clip-rule="evenodd" d="M 137.5 30.8 H 148.2 L 160.2 67.2 H 150.2 L 148.1 60.1 H 136.9 L 134.8 67.2 H 125.1 L 137.5 30.8 Z M 139.2 52.4 H 145.8 L 142.5 41.2 L 139.2 52.4 Z" />
            <path class="logo-letter letter-3" d="M 161.0 55.4 H 170.4 C 170.7 58.6 173.1 60.2 176.8 60.2 C 180.3 60.2 182.5 58.7 182.5 56.6 C 182.5 54.6 180.8 53.6 176.4 52.7 L 172.1 51.8 C 165.4 50.4 161.9 47.0 161.9 41.3 C 161.9 34.7 167.5 30.0 176.2 30.0 C 184.8 30.0 190.5 34.7 190.8 41.6 H 181.6 C 181.2 38.8 179.2 37.4 176.0 37.4 C 172.8 37.4 170.9 38.8 170.9 40.8 C 170.9 42.6 172.4 43.6 176.7 44.5 L 180.9 45.4 C 188.1 46.9 191.8 50.1 191.8 56.0 C 191.8 63.3 185.9 68.0 176.6 68.0 C 167.0 68.0 161.3 63.0 161.0 55.4 Z" />
            <path class="logo-letter letter-4" d="M 195.2 30.8 H 204.5 V 44.6 H 215.6 V 30.8 H 224.9 V 67.2 H 215.6 V 52.8 H 204.5 V 67.2 H 195.2 V 30.8 Z" />
            <path class="logo-letter letter-5" d="M 229.0 30.8 H 238.3 V 58.9 H 250.5 V 67.2 H 229.0 V 30.8 Z" />
            <path class="logo-letter letter-6" d="M 253.0 30.8 H 274.8 V 38.6 H 262.2 V 44.9 H 273.5 V 52.3 H 262.2 V 59.3 H 275.0 V 67.2 H 253.0 V 30.8 Z" />
            <path class="logo-letter letter-7" fill-rule="evenodd" clip-rule="evenodd" d="M 287.0 30.8 H 297.7 L 309.7 67.2 H 299.7 L 297.6 60.1 H 286.4 L 284.3 67.2 H 274.6 L 287.0 30.8 Z M 288.7 52.4 H 295.3 L 292.0 41.2 L 288.7 52.4 Z" />
            <path class="logo-letter letter-8" d="M 312.5 30.8 H 321.5 V 67.2 H 312.5 V 30.8 Z M 324.2 30.8 H 326.8 C 334.2 30.8 339.2 35.2 339.2 42.1 H 324.2 V 30.8 Z M 321.5 45.2 H 339.2 C 338.6 51.8 333.7 55.8 326.5 55.8 H 321.5 V 47.8 H 326.0 C 328.8 47.8 330.4 46.8 330.8 45.2 H 321.5 Z" />
          </g>
        </svg>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SCREEN 2: CHOOSE LOGIN TYPE                -->
    <!-- ========================================== -->
    <div id="loginScreen" class="screen-layer login-bg screen-hidden-right flex flex-col justify-between pt-12 pb-7 px-6">
      <div>
        <div class="px-1">
          <h1 class="text-[28px] font-bold tracking-[-0.02em] text-white leading-tight">
            Choose login type
          </h1>
          <p class="mt-3.5 text-[15px] text-[#8d8ca8] font-normal leading-[1.45] max-w-[260px]">
            You can choose one of 3 ways to protect your data
          </p>
        </div>

        <div class="mt-10 space-y-3" role="radiogroup" aria-label="Login Type">
          <div 
            id="option-faceid"
            onclick="selectOption('faceid')"
            role="radio"
            aria-checked="true"
            tabindex="0"
            class="option-card selected flex items-center justify-between px-6 cursor-pointer"
          >
            <div class="flex items-center gap-5">
              <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg" class="text-[#a5a3bd]">
                <path d="M8.5 3.5H6C4.61929 3.5 3.5 4.61929 3.5 6V8.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M19.5 3.5H22C23.3807 3.5 24.5 4.61929 24.5 6V8.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M8.5 24.5H6C4.61929 24.5 3.5 23.3807 3.5 22V19.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M19.5 24.5H22C23.3807 24.5 24.5 23.3807 24.5 22V19.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <circle cx="10.2" cy="11.2" r="1.2" fill="currentColor"/>
                <circle cx="17.8" cy="11.2" r="1.2" fill="currentColor"/>
                <path d="M10.5 16.8C11.5 18.1 12.7 18.7 14 18.7C15.3 18.7 16.5 18.1 17.5 16.8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
              </svg>
              <span class="text-[16px] font-bold text-white tracking-tight">Face ID</span>
            </div>
            <div id="badge-faceid" class="check-badge flex items-center justify-center scale-100 opacity-100">
              <svg width="13" height="10" viewBox="0 0 13 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.5 5.2L4.8 8.5L11.5 1.5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>

          <div 
            id="option-secretkey"
            onclick="selectOption('secretkey')"
            role="radio"
            aria-checked="false"
            tabindex="0"
            class="option-card flex items-center justify-between px-6 cursor-pointer"
          >
            <div class="flex items-center gap-5">
              <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg" class="text-[#a5a3bd]">
                <path d="M8.5 3.5H6C4.61929 3.5 3.5 4.61929 3.5 6V8.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M19.5 3.5H22C23.3807 3.5 24.5 4.61929 24.5 6V8.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M8.5 24.5H6C4.61929 24.5 3.5 23.3807 3.5 22V19.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M19.5 24.5H22C23.3807 24.5 24.5 23.3807 24.5 22V19.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <circle cx="11.2" cy="14" r="2.3" stroke="currentColor" stroke-width="1.7"/>
                <path d="M13.5 14H18.8M16.6 14V15.8M18.5 14V15.8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span class="text-[16px] font-bold text-white tracking-tight">Secret Key</span>
            </div>
            <div id="badge-secretkey" class="check-badge flex items-center justify-center scale-0 opacity-0">
              <svg width="13" height="10" viewBox="0 0 13 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.5 5.2L4.8 8.5L11.5 1.5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Slider Action -->
      <div class="relative w-full select-none">
        <div id="sliderTrack" class="slider-track w-full flex items-center justify-between px-1.5 relative overflow-hidden select-none cursor-pointer" style="touch-action: none; -webkit-user-select: none;">
          <button 
            id="sliderThumb"
            type="button"
            aria-label="Next"
            class="slider-thumb flex items-center justify-center text-white z-20 cursor-grab active:cursor-grabbing focus:outline-none select-none"
            style="touch-action: none; -webkit-user-select: none;"
          >
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="pointer-events-none">
              <path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
          <span id="sliderLabel" class="absolute left-1/2 -translate-x-1/2 text-[16px] font-medium text-white/95 tracking-wide pointer-events-none transition-opacity duration-200">
            Next
          </span>
          <div id="sliderChevrons" class="flex items-center pr-6 pointer-events-none transition-opacity duration-200">
            <svg width="28" height="18" viewBox="0 0 28 18" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path class="chevron-1" d="M2 2L9 9L2 16" stroke="white" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
              <path class="chevron-2" d="M10 2L17 9L10 16" stroke="white" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
              <path class="chevron-3" d="M18 2L25 9L18 16" stroke="white" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SCREEN 3: FACE ID SCREEN                   -->
    <!-- ========================================== -->
    <div id="faceidScreen" class="screen-layer auth-bg screen-hidden-right flex flex-col justify-between pt-6 pb-8 px-6">
      <div class="flex items-center justify-between">
        <button 
          onclick="showScreen('login')" 
          class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/15 active:scale-95 flex items-center justify-center text-white border border-white/10 transition cursor-pointer"
          title="Back to Login Type"
        >
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
        <span class="text-xs font-semibold uppercase tracking-widest text-slate-400">Biometric Login</span>
        <button 
          onclick="showScreen('secretkey')"
          class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/15 active:scale-95 flex items-center justify-center text-purple-300 border border-white/10 transition cursor-pointer"
          title="Switch to Secret Key"
        >
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />
          </svg>
        </button>
      </div>

      <div class="flex flex-col items-center justify-center my-auto">
        <div id="faceidVisualBox" class="faceid-frame flex items-center justify-center is-scanning relative">
          <div class="faceid-radar"></div>
          <div class="faceid-radar-2"></div>

          <div class="corner-bracket corner-tl"></div>
          <div class="corner-bracket corner-tr"></div>
          <div class="corner-bracket corner-bl"></div>
          <div class="corner-bracket corner-br"></div>

          <div class="scanning-laser"></div>

          <div id="faceidGlyphContainer" class="relative z-10 text-white/90 transition-transform duration-300">
            <svg id="faceidDefaultSvg" width="86" height="86" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg" class="drop-shadow-[0_0_16px_rgba(56,189,248,0.5)]">
              <path d="M8.5 3.5H6C4.61929 3.5 3.5 4.61929 3.5 6V8.5" stroke="#60a5fa" stroke-width="1.8" stroke-linecap="round"/>
              <path d="M19.5 3.5H22C23.3807 3.5 24.5 4.61929 24.5 6V8.5" stroke="#60a5fa" stroke-width="1.8" stroke-linecap="round"/>
              <path d="M8.5 24.5H6C4.61929 24.5 3.5 23.3807 3.5 22V19.5" stroke="#60a5fa" stroke-width="1.8" stroke-linecap="round"/>
              <path d="M19.5 24.5H22C23.3807 24.5 24.5 23.3807 24.5 22V19.5" stroke="#60a5fa" stroke-width="1.8" stroke-linecap="round"/>
              <circle cx="10.2" cy="11.2" r="1.4" fill="#ffffff"/>
              <circle cx="17.8" cy="11.2" r="1.4" fill="#ffffff"/>
              <path d="M14 13.8V15.5" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>
              <path d="M10.2 18.2C11.3 19.4 12.6 20 14 20C15.4 20 16.7 19.4 17.8 18.2" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>
            </svg>

            <div id="faceidSuccessBadge" class="hidden flex items-center justify-center w-20 h-20 rounded-full bg-emerald-500/20 border-2 border-emerald-400 shadow-[0_0_30px_rgba(52,211,153,0.6)] animate-bounce">
              <svg class="w-10 h-10 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
              </svg>
            </div>
          </div>
        </div>

        <div class="mt-8 text-center px-4">
          <h2 id="faceidStatusHeading" class="text-[22px] font-bold text-white tracking-tight">
            Scanning Face ID...
          </h2>
          <p id="faceidStatusDesc" class="mt-1.5 text-sm text-[#8d8ca8] font-normal max-w-[240px] mx-auto leading-relaxed">
            Position your face in front of the camera to unlock Cashleap
          </p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="space-y-3">
        <button 
          id="btnTriggerFaceId"
          onclick="triggerFaceIdScan()"
          class="w-full h-14 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 active:scale-[0.98] text-white font-semibold text-[15px] tracking-wide flex items-center justify-center gap-2 transition cursor-pointer"
        >
          <svg class="w-5 h-5 text-blue-200" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
          </svg>
          <span>Verify Face ID</span>
        </button>

        <div class="flex items-center justify-between px-2 pt-1">
          <button 
            onclick="showFaceIdFailureModal()"
            class="text-xs text-slate-400 hover:text-slate-300 font-medium underline underline-offset-4 cursor-pointer transition"
          >
            Simulate Failure
          </button>
          <button 
            onclick="showScreen('secretkey')"
            class="text-xs text-indigo-400 hover:text-indigo-300 font-semibold cursor-pointer flex items-center gap-1 transition"
          >
            <span>Use Secret Key</span>
            <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SCREEN 4: SECRET KEY SCREEN                -->
    <!-- ========================================== -->
    <div id="secretkeyScreen" class="screen-layer auth-bg screen-hidden-right flex flex-col justify-between pt-6 pb-6 px-6">
      <div class="flex items-center justify-between">
        <button 
          onclick="showScreen('login')" 
          class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/15 active:scale-95 flex items-center justify-center text-white border border-white/10 transition cursor-pointer"
          title="Back to Login Type"
        >
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
        <span class="text-xs font-semibold uppercase tracking-widest text-slate-400">Passcode</span>
        <button 
          onclick="showScreen('faceid')"
          class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/15 active:scale-95 flex items-center justify-center text-blue-300 border border-white/10 transition cursor-pointer"
          title="Switch to Face ID"
        >
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
      </div>

      <div class="flex flex-col items-center text-center mt-2">
        <div class="w-14 h-14 rounded-2xl bg-white/[0.08] border border-white/15 backdrop-blur-md flex items-center justify-center mb-3 text-purple-300">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>

        <h2 class="text-[22px] font-bold text-white tracking-tight">
          Enter Secret Key
        </h2>
        <p class="mt-1 text-xs text-[#8d8ca8] font-normal">
          Enter your 6-digit key to authenticate
        </p>

        <div id="passcodeDotsGroup" class="flex items-center justify-center gap-3.5 mt-5">
          <div class="passcode-dot" id="pdot-0"></div>
          <div class="passcode-dot" id="pdot-1"></div>
          <div class="passcode-dot" id="pdot-2"></div>
          <div class="passcode-dot" id="pdot-3"></div>
          <div class="passcode-dot" id="pdot-4"></div>
          <div class="passcode-dot" id="pdot-5"></div>
        </div>

        <button 
          onclick="quickFillPin()"
          class="mt-2.5 px-3 py-0.5 rounded-full bg-white/5 hover:bg-white/10 text-[11px] text-indigo-300 border border-white/5 transition cursor-pointer"
        >
          Quick Fill: 123456
        </button>
      </div>

      <div class="grid grid-cols-3 gap-x-5 gap-y-3.5 mx-auto max-w-[260px] pb-1">
        <button onclick="pressPinKey('1')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">1</span>
          <span class="text-[8px] font-semibold text-transparent leading-none mt-1">-</span>
        </button>
        <button onclick="pressPinKey('2')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">2</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">ABC</span>
        </button>
        <button onclick="pressPinKey('3')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">3</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">DEF</span>
        </button>
        <button onclick="pressPinKey('4')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">4</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">GHI</span>
        </button>
        <button onclick="pressPinKey('5')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">5</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">JKL</span>
        </button>
        <button onclick="pressPinKey('6')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">6</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">MNO</span>
        </button>
        <button onclick="pressPinKey('7')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">7</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">PQRS</span>
        </button>
        <button onclick="pressPinKey('8')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">8</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">TUV</span>
        </button>
        <button onclick="pressPinKey('9')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">9</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">WXYZ</span>
        </button>
        <button onclick="showScreen('faceid')" class="keypad-btn text-blue-400 hover:text-white" title="Use Face ID">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
        <button onclick="pressPinKey('0')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">0</span>
          <span class="text-[8px] font-semibold text-transparent leading-none mt-1">-</span>
        </button>
        <button onclick="pressBackspace()" class="keypad-btn text-slate-300 hover:text-white" title="Delete">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2M3 12l6.414 6.414a2 2 0 001.414.586H19a2 2 0 002-2V7a2 2 0 00-2-2h-8.172a2 2 0 00-1.414.586L3 12z" />
          </svg>
        </button>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SCREEN 5: WELCOME SCREEN (Clean & Auto)   -->
    <!-- ========================================== -->
    <div id="welcomeScreen" onclick="showScreen('home')" class="screen-layer welcome-bg screen-hidden-right flex flex-col justify-between pt-12 pb-8 px-6 cursor-pointer">
      <div class="flex flex-col items-center justify-center my-auto relative">
        <div id="welcomeRingsContainer" class="relative flex items-center justify-center mb-6">
          <div class="absolute concentric-ripple-1"></div>
          <div class="absolute concentric-ripple-2"></div>
          <div class="absolute concentric-ring-4"></div>
          <div class="absolute concentric-ring-3"></div>
          <div class="absolute concentric-ring-2"></div>
          <div class="absolute concentric-ring-1"></div>

          <div class="welcome-avatar-shell relative z-10 w-[112px] h-[112px] rounded-full overflow-hidden border-2 border-white/35 bg-white/10">
            <img 
              id="mariceAvatarImg"
              src="{avatar_b64}" 
              alt="Marice" 
              class="w-full h-full object-cover"
            />
          </div>
        </div>

        <div class="text-center mt-2">
          <p class="text-[#beb8d1] text-[16px] font-normal tracking-wide">
            Welcome back,
          </p>
          <h1 class="text-white text-[34px] font-bold tracking-tight mt-1 leading-tight">
            Marice!
          </h1>
        </div>
      </div>

      <div class="flex flex-col items-center space-y-3 pb-2">
        <span class="text-[11px] text-white/50 tracking-wider uppercase font-medium animate-pulse">
          Opening Cashleap...
        </span>
        <div class="w-32 h-1 bg-white/30 rounded-full pointer-events-none"></div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SCREEN 6: HOME SCREEN                      -->
    <!-- ========================================== -->
    <div id="homeScreen" class="screen-layer home-bg screen-hidden-right flex flex-col justify-between pt-4 pb-0 px-0 overflow-hidden">
      
      <!-- Upper Section: Header, Draggable Card Carousel, Quick Actions -->
      <div id="homeTopSection" class="w-full px-0 pt-1 pb-2 select-none">
        
        <!-- Home Header (padded px-5) -->
        <div class="flex items-center justify-between px-5 mt-1 mb-4">
          <!-- Left: User Avatar & Greeting (Clickable for Account & Profile) -->
          <div onclick="openUserProfileModal()" class="flex items-center gap-3 cursor-pointer hover:opacity-90 active:scale-95 transition apple-press" title="View Account & Profile">
            <div class="relative flex-shrink-0">
              <div class="w-[42px] h-[42px] rounded-full overflow-hidden border-2 border-white/25 bg-white/10">
                <img src="{avatar_b64}" alt="Marice" class="w-full h-full rounded-full object-cover" />
              </div>
              <div class="absolute -bottom-0.5 -right-0.5 z-20 w-3 h-3 rounded-full bg-emerald-400 border-2 border-[#120d2d] shadow-sm"></div>
            </div>
            <div class="flex flex-col">
              <span class="text-xs text-[#9d93b8] font-normal leading-tight">Hello,</span>
              <span class="text-[15px] font-bold text-white tracking-tight leading-tight mt-0.5 flex items-center gap-1">
                Marice Cervantes
                <svg class="w-3 h-3 text-blue-400" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </span>
            </div>
          </div>

          <!-- Scan & Notification Buttons matching Uploaded Image media_1793709351754_9a85a48c.png -->
          <div class="flex items-center gap-2.5">
            <!-- 1. Scan Icon Button -->
            <button 
              id="headerScanBtn"
              onclick="openScannerModal()" 
              class="w-10 h-10 rounded-full bg-white/[0.08] hover:bg-white/[0.14] border border-white/15 backdrop-blur-md flex items-center justify-center text-white apple-press transition cursor-pointer shadow-sm" 
              title="Scan QR / Barcode"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 8V6a2 2 0 0 1 2-2h2"/>
                <path d="M16 4h2a2 2 0 0 1 2 2v2"/>
                <path d="M20 16v2a2 2 0 0 1-2 2h-2"/>
                <path d="M8 20H6a2 2 0 0 1-2-2v-2"/>
                <line x1="9" y1="12" x2="15" y2="12" stroke-width="2.4"/>
              </svg>
            </button>

            <!-- 2. Notification Bell Button with Pink Badge -->
            <button 
              id="headerNotifBtn"
              onclick="openNotificationsModal()" 
              class="w-10 h-10 rounded-full bg-white/[0.08] hover:bg-white/[0.14] border border-white/15 backdrop-blur-md flex items-center justify-center text-white relative apple-press transition cursor-pointer shadow-sm" 
              title="Notifications"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
              <!-- Authentic Coral Pink Unread Dot Badge -->
              <span id="headerNotificationBadge" class="absolute top-1.5 right-1.5 w-2.5 h-2.5 rounded-full bg-[#ff2a6d] border border-[#1a1638] transition-transform"></span>
            </button>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- DRAGGABLE CARD CAROUSEL (ZERO PADDING - FULL BLEED)     -->
        <!-- ======================================================== -->
        <div class="relative w-full overflow-hidden my-1 pt-1 pb-2 px-0 select-none">
          <div class="relative w-full h-[184px] overflow-hidden cursor-grab active:cursor-grabbing" id="cardCarouselContainer">
            <!-- Carousel Track holding cards side by side -->
            <div id="cardCarouselTrack" class="flex items-center gap-3 absolute left-0 top-0 transition-transform duration-500 ease-out" style="transform: translateX(-11.5px);">
              
              <!-- Card 0 / Add Button Pill on Left (Opens Add New Card Modal) -->
              <div id="addCardPillBtn" onclick="openAddCardModal()" class="w-8 h-[178px] rounded-r-[22px] bg-white/[0.045] hover:bg-white/[0.1] active:scale-95 border-y border-r border-white/15 backdrop-blur-md flex items-center justify-center cursor-pointer flex-shrink-0 transition-all apple-press group" title="Add New Card to Wallet">
                <span class="text-xl font-light text-white/60 group-hover:text-white group-hover:scale-125 transition-all -translate-x-0.5">+</span>
              </div>

              <!-- Card 1: Balance Card (Sunrise Amber/Pink/Blue) -->
              <div id="card-item-1" onclick="handleCardClick(1)" class="w-[310px] h-[178px] rounded-[28px] debit-card-gradient p-5 flex flex-col justify-between text-white relative flex-shrink-0 cursor-pointer transition-all duration-300 hover:scale-[1.01] overflow-hidden apple-press">
                <!-- Dynamic Holographic Specular Glint -->
                <div class="card-holographic-glint absolute inset-0 pointer-events-none rounded-[28px] opacity-0 transition-opacity duration-300"></div>

                <!-- Active badge (tappable for card details) -->
                <div id="card1-active-badge" onclick="event.stopPropagation(); openCardDetailsScreen(1);" class="absolute top-3.5 right-4 bg-black/35 hover:bg-black/55 backdrop-blur-md px-2.5 py-0.5 rounded-full border border-white/20 text-[10px] font-semibold text-white flex items-center gap-1 transition-all cursor-pointer">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  Active
                </div>

                <div>
                  <span class="text-[11px] font-medium text-white/80 tracking-wide">Card Balance</span>
                  <div class="flex items-baseline gap-1 mt-0.5">
                    <span id="cardBalanceNum" class="text-[29px] font-bold tracking-tight text-white leading-none transition-transform">3,350.60</span>
                    <span class="text-[13px] font-bold text-white/90">AED</span>
                  </div>
                </div>

                <div class="text-[13.5px] font-mono tracking-[0.2em] text-white/90 font-medium">
                  **** **** **** 0329
                </div>

                <div class="flex items-center justify-between pt-1">
                  <div class="flex items-center gap-2">
                    <div class="flex flex-col text-[7px] font-bold uppercase tracking-wider text-white/70 leading-tight">
                      <span>VALID</span>
                      <span>THRU</span>
                    </div>
                    <span class="text-[13px] font-bold text-white tracking-wide">03/24</span>
                  </div>

                  <!-- Mastercard Brand Mark -->
                  <div class="flex items-center" title="Mastercard">
                    <svg class="w-9 h-5.5" viewBox="0 0 38 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <circle cx="13" cy="12" r="10.5" fill="#EB001B"/>
                      <circle cx="25" cy="12" r="10.5" fill="#F79E1B" fill-opacity="0.95"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Card 2: Debit Card (Exact design from uploaded PDF with Mastercard) -->
              <div id="card-item-2" onclick="handleCardClick(2)" class="w-[310px] h-[178px] rounded-[28px] overflow-hidden relative flex-shrink-0 cursor-pointer transition-all duration-300 hover:scale-[1.01] bg-[#1a183d] apple-press">
                <div class="card-holographic-glint absolute inset-0 pointer-events-none rounded-[28px] opacity-0 transition-opacity duration-300"></div>
                <img src="{card2_b64}" alt="Debit Card" class="w-full h-full object-cover rounded-[28px] select-none pointer-events-none" />
                
                <!-- Active badge for Card 2 -->
                <div id="card2-active-badge" onclick="event.stopPropagation(); openCardDetailsScreen(2);" class="absolute top-3.5 right-4 bg-black/40 hover:bg-black/55 backdrop-blur-md px-2.5 py-0.5 rounded-full border border-white/20 text-[10px] font-semibold text-white flex items-center gap-1 opacity-0 transition-all cursor-pointer">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                  Active
                </div>
              </div>

              <!-- Card 3 / Add Button Pill on Right (Touches Right Edge) -->
              <div onclick="openCardSelectionModal()" class="w-8 h-[178px] rounded-l-[22px] bg-white/[0.045] border-y border-l border-white/15 backdrop-blur-md flex items-center justify-center cursor-pointer flex-shrink-0 hover:bg-white/[0.08] transition apple-press" title="Select or Add Debit Card">
                <span class="text-lg font-light text-white/50">+</span>
              </div>

            </div>
          </div>

          <!-- Carousel Indicators: 1 Active Pill + 3 Inactive Dots -->
          <div class="flex items-center justify-center gap-1.5 mt-2.5">
            <span id="card-dot-1" onclick="selectCardIndex(1)" class="w-6 h-1 rounded-full bg-white cursor-pointer transition-all" title="Card 1"></span>
            <span id="card-dot-2" onclick="selectCardIndex(2)" class="w-3.5 h-1 rounded-full bg-white/20 hover:bg-white/40 cursor-pointer transition-all" title="Debit Card (0319)"></span>
            <span id="card-dot-3" onclick="selectCardIndex(3)" class="w-3.5 h-1 rounded-full bg-white/20 hover:bg-white/40 cursor-pointer transition-all" title="Card 3"></span>
            <span id="card-dot-4" onclick="selectCardIndex(4)" class="w-3.5 h-1 rounded-full bg-white/20 hover:bg-white/40 cursor-pointer transition-all" title="Card 4"></span>
          </div>
        </div>

        <!-- 4 Quick Action Buttons (Glass Container Circles matching uploaded image) -->
        <div class="grid grid-cols-4 gap-2 mt-3 mb-2 px-5">
          <!-- 1. Add -->
          <div class="flex flex-col items-center">
            <button onclick="triggerQuickAction('add')" class="action-btn apple-press" title="Add Funds">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Add</span>
          </div>

          <!-- 2. Withdraw -->
          <div class="flex flex-col items-center">
            <button onclick="triggerQuickAction('withdraw')" class="action-btn apple-press" title="Withdraw">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 11V7.5A2.5 2.5 0 0 1 6.5 5h11A2.5 2.5 0 0 1 20 7.5V11" />
                <path d="M7.5 7h9a1.5 1.5 0 0 1 1.5 1.5v7a3.5 3.5 0 0 1-3.5 3.5h-5A3.5 3.5 0 0 1 6 15.5v-7A1.5 1.5 0 0 1 7.5 7z" />
                <path d="M11 9.5v5M10 10h2.5a1.25 1.25 0 0 1 0 2.5H10m0 0h2.8a1.35 1.35 0 0 1 0 2.7H10" stroke-width="1.5" />
                <line x1="11.5" y1="8.5" x2="11.5" y2="9.5" stroke-width="1.5" />
                <line x1="11.5" y1="15.2" x2="11.5" y2="16.2" stroke-width="1.5" />
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Withdraw</span>
          </div>

          <!-- 3. Send -->
          <div class="flex flex-col items-center">
            <button onclick="triggerQuickAction('send')" class="action-btn apple-press" title="Send Money & Beneficiaries">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 4v11M7.5 8.5L12 4l4.5 4.5" />
                <path d="M5 14.5v2.5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-2.5" />
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Send</span>
          </div>

          <!-- 4. Schedule -->
          <div class="flex flex-col items-center">
            <button onclick="triggerQuickAction('schedule')" class="action-btn apple-press" title="Schedule Payment">
              <svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M7 3v2M17 3v2" />
                <path d="M4 9h3M10 9h10" />
                <path d="M4 7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v9.5a3.5 3.5 0 0 1-3.5 3.5H7.5A3.5 3.5 0 0 1 4 16.5V7z" />
                <circle cx="8" cy="13" r="0.9" fill="currentColor" />
                <circle cx="12" cy="13" r="0.9" fill="currentColor" />
                <circle cx="16" cy="13" r="0.9" fill="currentColor" />
                <circle cx="8" cy="16.5" r="0.9" fill="currentColor" />
                <circle cx="12" cy="16.5" r="0.9" fill="currentColor" />
                <circle cx="16" cy="16.5" r="0.9" fill="currentColor" />
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Schedule</span>
          </div>
        </div>

      </div>

      <!-- ======================================================== -->
      <!-- EXPANDABLE & DRAGGABLE RECENT TRANSACTIONS BOTTOM SHEET  -->
      <!-- ======================================================== -->
      <div 
        id="recentTransactionsSheet" 
        class="liquid-glass-sheet absolute left-0 right-0 bottom-0 rounded-t-[34px] z-20 flex flex-col transition-transform duration-400 ease-out overflow-hidden" 
        style="top: 38px; transform: translateY(356px);"
      >
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>
        <!-- Sheet Handle & Drag Area -->
        <div id="sheetDragHandleArea" class="px-5 pt-3 pb-2 cursor-grab active:cursor-grabbing select-none flex-shrink-0" style="touch-action: none;" title="Drag up to expand transactions">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mx-auto mb-3 transition-colors"></div>
          
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <h3 class="text-[17px] font-bold text-white tracking-tight">Recent Transaction</h3>
              <span id="sheetCountBadge" class="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-white/10 text-slate-300">8 Items</span>
            </div>
            
            <button 
              id="sheetToggleBtn" 
              onclick="toggleTransactionsSheet()" 
              class="text-xs text-blue-400 hover:text-blue-300 flex items-center gap-1 font-semibold transition cursor-pointer"
            >
              <span id="sheetToggleLabel">See All</span>
              <svg id="sheetToggleChevron" class="w-3.5 h-3.5 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M5 15l7-7 7 7"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Scrollable Transaction List -->
        <div id="sheetScrollArea" class="flex-1 overflow-y-auto px-5 pt-1 pb-[420px] space-y-0.5 scrollbar-none">
          
          <!-- 1. Amazon Prime Video (Cyan Glow) -->
          <div onclick="openTxDetail('amazonPrime')" class="flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] active:bg-white/[0.08] active:scale-[0.985] transition-all duration-150 cursor-pointer rounded-xl px-2 -mx-2 select-none">
            <div class="flex items-center gap-3.5">
              <div class="w-11 h-11 rounded-full bg-[#00a8e1] flex flex-col items-center justify-center text-white flex-shrink-0" style="box-shadow: 0 0 14px rgba(0, 168, 225, 0.45);">
                <span class="text-[9px] font-black leading-tight tracking-tighter">prime</span>
                <span class="text-[8px] font-bold leading-none tracking-tighter opacity-90">video</span>
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white leading-tight">Amazon Prime</h4>
                <p class="text-xs text-[#8e8ca6] mt-0.5">Today 20:00 • Subscription</p>
              </div>
            </div>
            <span class="text-sm font-semibold text-white tracking-tight">-16.00 AED</span>
          </div>

          <!-- 2. Spotify (Green Glow) -->
          <div class="flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] transition cursor-pointer">
            <div class="flex items-center gap-3.5">
              <div class="w-11 h-11 rounded-full bg-[#1db954] flex items-center justify-center text-black flex-shrink-0" style="box-shadow: 0 0 14px rgba(29, 185, 84, 0.45);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
                </svg>
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white leading-tight">Spotify</h4>
                <p class="text-xs text-[#8e8ca6] mt-0.5">Today 20:00 • Music Streaming</p>
              </div>
            </div>
            <span class="text-sm font-semibold text-white tracking-tight">-5.00 AED</span>
          </div>

          <!-- 3. Amazon Store (Warm Orange Glow) -->
          <div class="flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] transition cursor-pointer">
            <div class="flex items-center gap-3.5">
              <div class="w-11 h-11 rounded-full bg-[#ff9900] flex items-center justify-center text-white flex-shrink-0" style="box-shadow: 0 0 14px rgba(255, 153, 0, 0.45);">
                <span class="font-bold text-lg leading-none -translate-y-0.5">a</span>
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white leading-tight">Amazon Store</h4>
                <p class="text-xs text-[#8e8ca6] mt-0.5">Today 20:00 • E-Commerce</p>
              </div>
            </div>
            <span class="text-sm font-semibold text-white tracking-tight">-5.00 AED</span>
          </div>

          <!-- 4. eBay (Colorful eBay Logo + Coral Glow) -->
          <div class="flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] transition cursor-pointer">
            <div class="flex items-center gap-3.5">
              <div class="w-11 h-11 rounded-full bg-white flex items-center justify-center flex-shrink-0" style="box-shadow: 0 0 14px rgba(229, 50, 56, 0.35);">
                <span class="text-[15px] font-black tracking-tight leading-none" style="font-family: sans-serif;"><span style="color:#e53238;">e</span><span style="color:#0064d2;">b</span><span style="color:#f5af02;">a</span><span style="color:#86b817;">y</span></span>
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white leading-tight">eBay</h4>
                <p class="text-xs text-[#8e8ca6] mt-0.5">Yesterday 14:20 • Marketplace</p>
              </div>
            </div>
            <span class="text-sm font-semibold text-white tracking-tight">-84.50 AED</span>
          </div>

          <!-- 5. Walmart (Electric Blue + Yellow Spark Glow) -->
          <div class="flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] transition cursor-pointer">
            <div class="flex items-center gap-3.5">
              <div class="w-11 h-11 rounded-full bg-[#0071ce] flex items-center justify-center flex-shrink-0" style="box-shadow: 0 0 14px rgba(0, 113, 206, 0.45);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="#ffc220">
                  <rect x="10.5" y="1.5" width="3" height="5.5" rx="1.5"/>
                  <rect x="10.5" y="17" width="3" height="5.5" rx="1.5"/>
                  <rect x="10.5" y="1.5" width="3" height="5.5" rx="1.5" transform="rotate(60 12 12)"/>
                  <rect x="10.5" y="17" width="3" height="5.5" rx="1.5" transform="rotate(60 12 12)"/>
                  <rect x="10.5" y="1.5" width="3" height="5.5" rx="1.5" transform="rotate(120 12 12)"/>
                  <rect x="10.5" y="17" width="3" height="5.5" rx="1.5" transform="rotate(120 12 12)"/>
                </svg>
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white leading-tight">Walmart</h4>
                <p class="text-xs text-[#8e8ca6] mt-0.5">20 Oct, 11:15 • Groceries</p>
              </div>
            </div>
            <span class="text-sm font-semibold text-white tracking-tight">-142.30 AED</span>
          </div>

          <!-- 6. Apple Services (Frosted Glow) -->
          <div class="flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] transition cursor-pointer">
            <div class="flex items-center gap-3.5">
              <div class="w-11 h-11 rounded-full bg-[#1c1c1e] flex items-center justify-center flex-shrink-0 border border-white/10" style="box-shadow: 0 0 12px rgba(255, 255, 255, 0.2);">
                <svg width="20" height="20" viewBox="0 0 170 170" fill="currentColor" class="text-white -translate-y-0.5">
                  <path d="M150.37 130.25c-2.45 5.66-5.35 10.87-8.71 15.66-4.58 6.53-8.33 11.05-11.22 13.56-4.48 4.12-9.28 6.23-14.42 6.35-3.69 0-8.14-1.05-13.32-3.18-5.19-2.12-9.97-3.17-14.34-3.17-4.58 0-9.49 1.05-14.75 3.17-5.26 2.13-9.5 3.24-12.74 3.35-4.35.13-9.16-1.9-14.42-6.08-3.7-3.04-7.59-7.71-11.66-14.01-6.1-9.45-10.9-19.8-14.42-31.06-3.51-11.25-5.27-22.18-5.27-32.78 0-14.34 3.48-26.06 10.44-35.15 6.96-9.1 15.82-13.78 26.58-14.03 4.58 0 9.87 1.25 15.88 3.75 6 2.5 10.02 3.79 12.06 3.86 1.63 0 5.66-1.3 12.08-3.89 6.43-2.59 11.43-3.83 15.01-3.72 11.45.65 20.35 4.67 26.71 12.05-10.02 6.13-14.93 14.74-14.73 25.82.2 8.78 3.53 16.03 10.01 21.75 6.48 5.72 14.15 8.95 23.01 9.69-2.22 6.74-4.83 13.36-7.83 19.87zM119.22 33.15c0-6.73 2.45-13.06 7.34-19 4.9-5.94 10.94-9.75 18.12-11.43.34 2.18.52 4.14.52 5.88 0 6.64-2.58 13.11-7.75 19.41-5.17 6.31-11.25 9.94-18.23 10.89v-5.75z"/>
                </svg>
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white leading-tight">Apple Services</h4>
                <p class="text-xs text-[#8e8ca6] mt-0.5">19 Oct, 09:45 • Cloud & Apps</p>
              </div>
            </div>
            <span class="text-sm font-semibold text-white tracking-tight">-19.99 AED</span>
          </div>

          <!-- 7. Starbucks (Emerald Green Glow) -->
          <div class="flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] transition cursor-pointer">
            <div class="flex items-center gap-3.5">
              <div class="w-11 h-11 rounded-full bg-[#00704a] flex items-center justify-center flex-shrink-0" style="box-shadow: 0 0 14px rgba(0, 112, 74, 0.45);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" class="text-white">
                  <path d="M18 8h1a4 4 0 0 1 0 8h-1" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z" stroke-linecap="round" stroke-linejoin="round"/>
                  <line x1="6" y1="1" x2="6" y2="4" stroke-linecap="round"/>
                  <line x1="10" y1="1" x2="10" y2="4" stroke-linecap="round"/>
                  <line x1="14" y1="1" x2="14" y2="4" stroke-linecap="round"/>
                </svg>
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white leading-tight">Starbucks Coffee</h4>
                <p class="text-xs text-[#8e8ca6] mt-0.5">18 Oct, 08:30 • Dining</p>
              </div>
            </div>
            <span class="text-sm font-semibold text-white tracking-tight">-28.00 AED</span>
          </div>

          <!-- 8. Netflix (Crimson Red Glow) -->
          <div class="flex items-center justify-between py-3 hover:bg-white/[0.04] transition cursor-pointer">
            <div class="flex items-center gap-3.5">
              <div class="w-11 h-11 rounded-full bg-[#141414] flex items-center justify-center flex-shrink-0 border border-red-900/30" style="box-shadow: 0 0 14px rgba(229, 9, 20, 0.45);">
                <span class="text-xl font-black text-[#e50914] leading-none" style="font-family: sans-serif;">N</span>
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white leading-tight">Netflix</h4>
                <p class="text-xs text-[#8e8ca6] mt-0.5">16 Oct, 21:00 • Entertainment</p>
              </div>
            </div>
            <span class="text-sm font-semibold text-white tracking-tight">-45.00 AED</span>
          </div>

        </div>
      </div>

    </div>

    <!-- ======================================================== -->
    <!-- SCREEN 7: CARD DETAILS (MATCHING UPLOADED IMAGE)         -->
    <!-- ======================================================== -->
    <div id="cardDetailScreen" class="screen-layer home-bg screen-hidden-right flex flex-col justify-between pt-5 pb-0 px-0 overflow-hidden select-none text-white">
      
      <div class="flex-1 overflow-y-auto px-5 pb-28 scrollbar-none">
      <!-- Top Bar: Circular Glass Back Button & Circular Glass Settings Gear -->
      <div class="flex items-center justify-between w-full mb-4 pt-1">
        <!-- Back Button (<) -->
        <button 
          onclick="showScreen('home')" 
          class="w-11 h-11 rounded-full bg-white/[0.08] hover:bg-white/[0.14] active:scale-95 border border-white/15 backdrop-blur-md flex items-center justify-center text-white/90 transition cursor-pointer apple-press shadow-sm"
          title="Back to Home Dashboard"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
        </button>

        <!-- Settings Gear Button (⚙) -->
        <button 
          onclick="openCardSettingsAction()" 
          class="w-11 h-11 rounded-full bg-white/[0.08] hover:bg-white/[0.14] active:scale-95 border border-white/15 backdrop-blur-md flex items-center justify-center text-white/90 transition cursor-pointer apple-press shadow-sm"
          title="Card Settings & Controls"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="3"></circle>
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
          </svg>
        </button>
      </div>

      <!-- Current Balance Hero Section -->
      <div class="flex flex-col items-center justify-center text-center mt-1 mb-2">
        <span class="text-[13px] font-medium text-[#9e94b8] tracking-tight mb-1">Current Balance</span>
        <div class="flex items-baseline justify-center">
          <span id="cdCurrentBalance" class="text-[42px] font-extrabold text-white tracking-tight leading-none">3,350.60</span>
          <span class="text-xs font-bold text-white/85 ml-1.5 self-end mb-1">AED</span>
        </div>
      </div>

      <!-- Key-Value Info Rows (Credit, Minimum Due, Last Payment) -->
      <div class="w-full px-2 mt-6 mb-6 space-y-3.5">
        <div class="flex items-center justify-between">
          <span class="text-[13.5px] font-medium text-[#9e94b8]">Credit</span>
          <span id="cdCreditLimit" class="text-[14px] font-semibold text-white tracking-tight">35,000.00 AED</span>
        </div>
        <div class="flex items-center justify-between">
          <span class="text-[13.5px] font-medium text-[#9e94b8]">Minimum Amount due</span>
          <span id="cdMinDue" class="text-[14px] font-semibold text-white tracking-tight">960.00 AED</span>
        </div>
        <div class="flex items-center justify-between">
          <span class="text-[13.5px] font-medium text-[#9e94b8]">Last Payment</span>
          <span id="cdLastPayment" class="text-[14px] font-semibold text-white tracking-tight">May 25, 2024</span>
        </div>
      </div>

      <!-- Grouped Card 1: Cashback, Statements, Customize Card, Freeze Account -->
      <div class="w-full rounded-[24px] bg-[#1a1738]/85 border border-white/[0.12] backdrop-blur-2xl overflow-hidden divide-y divide-white/[0.08] shadow-lg">
        
        <!-- Row 1: Cashback (with 200.00 AED in coral red) -->
        <div onclick="handleCashbackClick()" class="flex items-center justify-between px-4 py-3.5 hover:bg-white/[0.06] active:bg-white/[0.1] transition cursor-pointer apple-press select-none">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 text-slate-300 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="23 4 23 10 17 10"></polyline>
              <polyline points="1 20 1 14 7 14"></polyline>
              <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
            </svg>
            <span class="text-[14px] font-medium text-white">Cashback</span>
          </div>
          <div class="flex items-center gap-2">
            <span id="cdCashback" class="text-[14px] font-bold text-[#ff2a6d] tracking-tight">200.00 AED</span>
            <svg class="w-4 h-4 text-white/40 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Row 2: Statements -->
        <div onclick="handleStatementsClick()" class="flex items-center justify-between px-4 py-3.5 hover:bg-white/[0.06] active:bg-white/[0.1] transition cursor-pointer apple-press select-none">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 text-slate-300 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
              <line x1="16" y1="13" x2="8" y2="13"></line>
              <line x1="16" y1="17" x2="8" y2="17"></line>
              <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
            <span class="text-[14px] font-medium text-white">Statements</span>
          </div>
          <svg class="w-4 h-4 text-white/40 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </div>

        <!-- Row 3: Customize Card -->
        <div onclick="handleCustomizeCardClick()" class="flex items-center justify-between px-4 py-3.5 hover:bg-white/[0.06] active:bg-white/[0.1] transition cursor-pointer apple-press select-none">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 text-slate-300 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
              <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
            </svg>
            <span class="text-[14px] font-medium text-white">Customize Card</span>
          </div>
          <svg class="w-4 h-4 text-white/40 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </div>

        <!-- Row 4: Freeze my Account -->
        <div onclick="handleFreezeAccountClick()" class="flex items-center justify-between px-4 py-3.5 hover:bg-white/[0.06] active:bg-white/[0.1] transition cursor-pointer apple-press select-none">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 text-slate-300 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="2" x2="12" y2="22"></line>
              <line x1="12" y1="2" x2="9" y2="5"></line>
              <line x1="12" y1="2" x2="15" y2="5"></line>
              <line x1="12" y1="22" x2="9" y2="19"></line>
              <line x1="12" y1="22" x2="15" y2="19"></line>
              <line x1="3.5" y1="7" x2="20.5" y2="17"></line>
              <line x1="3.5" y1="7" x2="7" y2="6.5"></line>
              <line x1="3.5" y1="7" x2="5" y2="10"></line>
              <line x1="20.5" y1="17" x2="17" y2="17.5"></line>
              <line x1="20.5" y1="17" x2="19" y2="14"></line>
              <line x1="3.5" y1="17" x2="20.5" y2="7"></line>
              <line x1="3.5" y1="17" x2="5" y2="14"></line>
              <line x1="3.5" y1="17" x2="7" y2="17.5"></line>
              <line x1="20.5" y1="7" x2="19" y2="10"></line>
              <line x1="20.5" y1="7" x2="17" y2="6.5"></line>
            </svg>
            <span id="cdFreezeLabel" class="text-[14px] font-medium text-white">Freeze my Account</span>
          </div>
          <svg class="w-4 h-4 text-white/40 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </div>

      </div>

      <!-- Grouped Card 2: Apple Wallet & Transactions -->
      <div class="w-full rounded-[24px] bg-[#1a1738]/85 border border-white/[0.12] backdrop-blur-2xl overflow-hidden divide-y divide-white/[0.08] shadow-lg mt-3.5">
        
        <!-- Row 1: Add Apple Wallet -->
        <div onclick="handleAddAppleWalletClick()" class="flex items-center justify-between px-4 py-3.5 hover:bg-white/[0.06] active:bg-white/[0.1] transition cursor-pointer apple-press select-none">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 text-slate-300 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="5" width="20" height="14" rx="2"></rect>
              <line x1="2" y1="10" x2="22" y2="10"></line>
              <circle cx="17.5" cy="14.5" r="1" fill="currentColor"></circle>
            </svg>
            <span class="text-[14px] font-medium text-white">Add Apple Wallet</span>
          </div>
          <svg class="w-4 h-4 text-white/40 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </div>

        <!-- Row 2: Transactions -->
        <div onclick="handleCardTransactionsClick()" class="flex items-center justify-between px-4 py-3.5 hover:bg-white/[0.06] active:bg-white/[0.1] transition cursor-pointer apple-press select-none">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 text-slate-300 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
              <line x1="8" y1="6" x2="21" y2="6"></line>
              <line x1="8" y1="12" x2="21" y2="12"></line>
              <line x1="8" y1="18" x2="21" y2="18"></line>
              <polyline points="3 6 4 7 3 8"></polyline>
              <polyline points="3 12 4 13 3 14"></polyline>
              <polyline points="3 18 4 19 3 20"></polyline>
            </svg>
            <span class="text-[14px] font-medium text-white">Transactions</span>
          </div>
          <svg class="w-4 h-4 text-white/40 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </div>

        <!-- Row 3: Language Change / Switcher (Arabic <-> English) -->
        <div id="cardLangRow" class="flex items-center justify-between px-4 py-3.5 hover:bg-white/[0.04] transition select-none">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 text-slate-300 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="2" y1="12" x2="22" y2="12"></line>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
            </svg>
            <div class="flex flex-col">
              <span id="cdLangLabel" class="text-[14px] font-medium text-white leading-tight">Language</span>
              <span id="cdLangSub" class="text-[11px] text-[#9e94b8] mt-0.5">English • العربية</span>
            </div>
          </div>
          <!-- Segmented Arabic / English Switcher Pill -->
          <div class="flex items-center p-0.5 rounded-full bg-white/[0.08] border border-white/10 backdrop-blur-md">
            <button 
              type="button" 
              id="langBtnEn" 
              onclick="setAppLanguage('en')" 
              class="px-2.5 py-1 rounded-full text-[11px] font-bold transition-all cursor-pointer bg-blue-600 text-white shadow-sm"
            >
              English
            </button>
            <button 
              type="button" 
              id="langBtnAr" 
              onclick="setAppLanguage('ar')" 
              class="px-2.5 py-1 rounded-full text-[11px] font-medium text-[#9e94b8] hover:text-white transition-all cursor-pointer"
            >
              العربية
            </button>
          </div>
        </div>

      </div>
      </div>

    </div>

    <!-- ========================================== -->
    <!-- SCANNER QR / BARCODE MODAL                 -->
        <!-- ======================================================== -->
        <!-- ======================================================== -->
    <!-- ======================================================== -->
    <!-- ======================================================== -->
    <!-- ======================================================== -->
    <!-- SCREEN 8: STATISTICS / MY EXPENSES (APPLE BOTTOMSHEET)     -->
    <!-- ======================================================== -->
    <div id="statisticsScreen" class="screen-layer home-bg screen-hidden-right flex flex-col justify-between pt-4 pb-0 px-0 overflow-hidden select-none text-white">
      
      <!-- Upper Section: Header Capsule, Headline, Chart Card (padded px-4) -->
      <div id="statsTopSection" class="w-full px-4 pt-1 select-none flex-shrink-0">
        
        <!-- Top Bar: Translucent Capsule Header Bar matching Uploaded Screenshot -->
        <div class="w-full rounded-full bg-white/[0.05] border border-white/[0.08] backdrop-blur-xl px-3 py-1.5 flex items-center justify-between mb-2 shadow-sm">
          <!-- Left: Avatar & Greeting (Clickable for Account & Profile) -->
          <div onclick="openUserProfileModal()" class="flex items-center gap-2.5 cursor-pointer hover:opacity-90 active:scale-95 transition apple-press" title="View Account & Profile">
            <div class="w-8 h-8 rounded-full p-[1px] bg-gradient-to-tr from-pink-500/50 via-purple-500/30 to-cyan-400/40 shadow-sm flex-shrink-0 relative">
              <img 
                src="{avatar_b64}" 
                alt="Marice Cervantes" 
                class="w-full h-full rounded-full object-cover" 
              />
              <div class="absolute -bottom-0.5 -right-0.5 z-20 w-2.5 h-2.5 rounded-full bg-emerald-400 border-2 border-[#120d2d] shadow-sm"></div>
            </div>
            <div class="flex flex-col">
              <span class="text-[10.5px] font-medium text-[#9e94b8] tracking-tight leading-none mb-0.5">Hello,</span>
              <span class="text-[13.5px] font-bold text-white tracking-tight leading-none flex items-center gap-1">
                Marice Cervantes
                <svg class="w-2.5 h-2.5 text-blue-400 opacity-80" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </span>
            </div>
          </div>

          <!-- Right: Circular Glass Buttons (Scan QR & Notification Bell) -->
          <div class="flex items-center gap-1.5">
            <button 
              onclick="openScannerModal()" 
              class="w-7 h-7 rounded-full bg-white/[0.06] hover:bg-white/[0.12] active:scale-95 border border-white/10 backdrop-blur-md flex items-center justify-center text-white/90 transition cursor-pointer apple-press shadow-sm"
              title="Scan QR Code"
            >
              <svg class="w-3.5 h-3.5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 8V5a1 1 0 0 1 1-1h3"></path>
                <path d="M4 16v3a1 1 0 0 0 1 1h3"></path>
                <path d="M16 4h3a1 1 0 0 1 1 1v3"></path>
                <path d="M16 20h3a1 1 0 0 0 1-1v-3"></path>
                <line x1="8" y1="12" x2="16" y2="12"></line>
              </svg>
            </button>

            <button 
              onclick="openNotificationsModal()" 
              class="w-7 h-7 rounded-full bg-white/[0.06] hover:bg-white/[0.12] active:scale-95 border border-white/10 backdrop-blur-md relative flex items-center justify-center text-white/90 transition cursor-pointer apple-press shadow-sm"
              title="Notifications"
            >
              <svg class="w-3.5 h-3.5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              <span class="absolute top-1 right-1 w-1.5 h-1.5 rounded-full bg-[#ff2a6d] shadow-[0_0_6px_#ff2a6d]"></span>
            </button>
          </div>
        </div>

        <!-- Title: My Expenses (with Proper Padding & Margins) -->
        <div class="pt-3.5 pb-4 px-0.5 my-1">
          <h1 class="text-[27px] font-extrabold text-white tracking-tight leading-none">My Expenses</h1>
        </div>

        <!-- Chart Container Card -->
        <div class="w-full rounded-[22px] bg-[#141033]/80 border border-white/[0.08] p-3.5 backdrop-blur-xl relative shadow-lg mb-1">
          <!-- Top: Balance & Period Filters (D, W, M, Y) -->
          <div class="flex items-start justify-between w-full mb-1">
            <div>
              <span class="text-[10.5px] font-medium text-[#9e94b8] tracking-tight block mb-0.5">Current Balance</span>
              <div class="flex items-baseline">
                <span id="statsBalanceAmount" class="text-[23px] font-extrabold text-white tracking-tight leading-none">3,350.60</span>
                <span class="text-[11px] font-bold text-white/70 ml-1 leading-none">AED</span>
              </div>
            </div>

            <!-- D, W, M, Y Period Filters -->
            <div class="flex items-center gap-3 pt-0.5">
              <button onclick="setStatsPeriod('D', true)" id="btn-period-D" class="text-[12px] font-semibold text-[#8c82ab] hover:text-white transition cursor-pointer px-0.5">D</button>
              <button onclick="setStatsPeriod('W', true)" id="btn-period-W" class="text-[12px] font-bold text-[#ff2a6d] relative flex flex-col items-center cursor-pointer px-0.5">
                W
                <span id="dot-period-W" class="w-1.5 h-1.5 rounded-full bg-[#ff2a6d] mt-0.5 shadow-[0_0_6px_#ff2a6d]"></span>
              </button>
              <button onclick="setStatsPeriod('M', true)" id="btn-period-M" class="text-[12px] font-semibold text-[#8c82ab] hover:text-white transition cursor-pointer px-0.5">M</button>
              <button onclick="setStatsPeriod('Y', true)" id="btn-period-Y" class="text-[12px] font-semibold text-[#8c82ab] hover:text-white transition cursor-pointer px-0.5">Y</button>
            </div>
          </div>

          <!-- The Spline Area SVG Chart -->
          <div class="relative w-full h-[120px] select-none">
            <!-- Floating Tooltip Badge on Chart -->
            <div id="statsChartBadge" class="absolute z-10 transition-all duration-300 pointer-events-none transform -translate-x-1/2 -translate-y-full" style="left: 208px; top: 24px;">
              <span id="statsBadgeText" class="text-[12px] font-bold text-white tracking-tight drop-shadow-md">3,350.60 AED</span>
            </div>

            <svg id="statsChartSvg" viewBox="0 0 310 120" class="w-full h-full overflow-visible">
              <defs>
                <linearGradient id="statsAreaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="#ff2a6d" stop-opacity="0.55" />
                  <stop offset="50%" stop-color="#be185d" stop-opacity="0.2" />
                  <stop offset="100%" stop-color="#141033" stop-opacity="0.0" />
                </linearGradient>
                <filter id="statsLineGlow" x="-20%" y="-20%" width="140%" height="140%">
                  <feDropShadow dx="0" dy="0" stdDeviation="3" flood-color="#ff2a6d" flood-opacity="0.8" />
                </filter>
              </defs>

              <!-- Horizontal Dashed Gridlines -->
              <line x1="0" y1="24" x2="310" y2="24" stroke="rgba(255,255,255,0.05)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="0" y1="52" x2="310" y2="52" stroke="rgba(255,255,255,0.05)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="0" y1="80" x2="310" y2="80" stroke="rgba(255,255,255,0.05)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="0" y1="108" x2="310" y2="108" stroke="rgba(255,255,255,0.05)" stroke-dasharray="2 3" stroke-width="1" />

              <!-- Vertical Dashed Gridlines -->
              <line x1="18" y1="12" x2="18" y2="114" stroke="rgba(255,255,255,0.03)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="64" y1="12" x2="64" y2="114" stroke="rgba(255,255,255,0.03)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="112" y1="12" x2="112" y2="114" stroke="rgba(255,255,255,0.03)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="160" y1="12" x2="160" y2="114" stroke="rgba(255,255,255,0.03)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="208" y1="12" x2="208" y2="114" stroke="rgba(255,255,255,0.03)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="256" y1="12" x2="256" y2="114" stroke="rgba(255,255,255,0.03)" stroke-dasharray="2 3" stroke-width="1" />
              <line x1="296" y1="12" x2="296" y2="114" stroke="rgba(255,255,255,0.03)" stroke-dasharray="2 3" stroke-width="1" />

              <!-- Area Gradient Fill -->
              <path id="statsAreaPath" 
                    d="M 0,72 C 9,72 12,74 18,74 C 36,74 46,68 64,68 C 82,68 94,82 112,82 C 130,82 142,60 160,58 C 178,56 192,30 208,30 C 224,30 240,50 256,50 C 272,50 282,36 296,36 L 310,44 L 310,120 L 0,120 Z" 
                    fill="url(#statsAreaGrad)" 
                    class="transition-all duration-500 ease-out" />

              <!-- Glowing Line Curve -->
              <path id="statsLinePath" 
                    d="M 0,72 C 9,72 12,74 18,74 C 36,74 46,68 64,68 C 82,68 94,82 112,82 C 130,82 142,60 160,58 C 178,56 192,30 208,30 C 224,30 240,50 256,50 C 272,50 282,36 296,36 L 310,44" 
                    fill="none" 
                    stroke="#ff2a6d" 
                    stroke-width="2.5" 
                    stroke-linecap="round" 
                    stroke-linejoin="round"
                    filter="url(#statsLineGlow)"
                    class="transition-all duration-500 ease-out" />

              <!-- Vertical Guideline at Selected Day (Thu) -->
              <line id="statsActiveGuideline" x1="208" y1="30" x2="208" y2="114" stroke="rgba(255,255,255,0.38)" stroke-width="1.3" stroke-dasharray="2 2" class="transition-all duration-300" />

              <!-- Active Point Halo & Emerald Dot -->
              <circle id="statsActiveHalo" cx="208" cy="30" r="7" fill="rgba(16, 185, 129, 0.28)" class="transition-all duration-300" />
              <circle id="statsActiveDot" cx="208" cy="30" r="4" fill="#10b981" stroke="#ffffff" stroke-width="1.8" class="transition-all duration-300 shadow-[0_0_8px_#10b981]" />
            </svg>
          </div>

          <!-- X-Axis Days of Week -->
          <div id="statsDaysRow" class="flex items-center justify-between w-full mt-1 px-0.5 select-none">
            <button onclick="selectStatsDay(0)" id="stats-day-0" class="text-[11px] font-medium text-[#8c82ab] hover:text-white transition py-0.5 px-1 cursor-pointer">Sun</button>
            <button onclick="selectStatsDay(1)" id="stats-day-1" class="text-[11px] font-medium text-[#8c82ab] hover:text-white transition py-0.5 px-1 cursor-pointer">Mon</button>
            <button onclick="selectStatsDay(2)" id="stats-day-2" class="text-[11px] font-medium text-[#8c82ab] hover:text-white transition py-0.5 px-1 cursor-pointer">Tue</button>
            <button onclick="selectStatsDay(3)" id="stats-day-3" class="text-[11px] font-medium text-[#8c82ab] hover:text-white transition py-0.5 px-1 cursor-pointer">Wed</button>
            <button onclick="selectStatsDay(4)" id="stats-day-4" class="text-[11px] font-bold text-white bg-[#251f47] border border-white/10 rounded-full px-2.5 py-0.5 cursor-pointer transition">Thu</button>
            <button onclick="selectStatsDay(5)" id="stats-day-5" class="text-[11px] font-medium text-[#8c82ab] hover:text-white transition py-0.5 px-1 cursor-pointer">Fri</button>
            <button onclick="selectStatsDay(6)" id="stats-day-6" class="text-[11px] font-medium text-[#8c82ab] hover:text-white transition py-0.5 px-1 cursor-pointer">Sat</button>
          </div>
        </div>

      </div>

      <!-- ======================================================== -->
      <!-- TRUE DRAGGABLE & EXPANDABLE LIQUID GLASS BOTTOM SHEET     -->
      <!-- ======================================================== -->
      <div 
        id="statsCategoriesSheet" 
        class="liquid-glass-sheet absolute left-0 right-0 bottom-0 rounded-t-[34px] z-20 flex flex-col transition-transform duration-400 ease-out overflow-hidden" 
        style="top: 38px; transform: translateY(338px);"
      >
        <!-- Liquid Glass Specular Top Highlight Line -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <!-- Ambient Top Sheen -->
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Draggable Handle Area (Matches Apple iOS Bottom Sheet) -->
        <div id="statsSheetDragHandleArea" class="px-5 pt-3 pb-2 cursor-grab active:cursor-grabbing select-none flex-shrink-0" style="touch-action: none;" title="Drag up to expand categories">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mx-auto mb-3 transition-colors"></div>

          <!-- Section Title Row -->
          <div class="flex items-center justify-between">
            <h2 class="text-[17px] font-bold text-white tracking-tight">Categories</h2>
            <button 
              id="statsSheetToggleBtn" 
              onclick="toggleStatsCategoriesSheet()" 
              class="text-xs text-blue-400 hover:text-blue-300 flex items-center gap-1 font-semibold transition cursor-pointer"
            >
              <span id="statsSheetToggleLabel">See All</span>
              <svg id="statsSheetToggleChevron" class="w-3.5 h-3.5 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M5 15l7-7 7 7"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Scrollable Clean Categories List -->
        <div id="statsCategoriesList" class="flex-1 overflow-y-auto px-5 pb-[420px] divide-y divide-white/[0.08] relative z-10 scrollbar-none">
          
          <!-- Item 1: Groceries -->
          <div onclick="handleCategoryClick('Groceries', '400.00 AED', '40%')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06Z"></path>
                  <path d="M10 2c1 .5 2 2 2 5"></path>
                </svg>
              </div>
              <span class="text-[14.5px] font-semibold text-white tracking-tight">Groceries</span>
            </div>
            <div class="flex items-center gap-4">
              <span class="text-[12.5px] font-medium text-[#9e94b8]">40%</span>
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">400.00 AED</span>
            </div>
          </div>

          <!-- Item 2: Entertainment -->
          <div onclick="handleCategoryClick('Entertainment', '800.500 AED', '20%')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="6" y1="12" x2="10" y2="12"></line>
                  <line x1="8" y1="10" x2="8" y2="14"></line>
                  <line x1="15" y1="13" x2="15.01" y2="13"></line>
                  <line x1="18" y1="11" x2="18.01" y2="11"></line>
                  <rect x="2" y="6" width="20" height="12" rx="6"></rect>
                </svg>
              </div>
              <span class="text-[14.5px] font-semibold text-white tracking-tight">Entertainment</span>
            </div>
            <div class="flex items-center gap-4">
              <span class="text-[12.5px] font-medium text-[#9e94b8]">20%</span>
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">800.500 AED</span>
            </div>
          </div>

          <!-- Item 3: Shopping -->
          <div onclick="handleCategoryClick('Shopping', '550.00 AED', '25%')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
                  <line x1="3" y1="6" x2="21" y2="6"></line>
                  <path d="M16 10a4 4 0 0 1-8 0"></path>
                </svg>
              </div>
              <span class="text-[14.5px] font-semibold text-white tracking-tight">Shopping</span>
            </div>
            <div class="flex items-center gap-4">
              <span class="text-[12.5px] font-medium text-[#9e94b8]">25%</span>
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">550.00 AED</span>
            </div>
          </div>

          <!-- Item 4: Dining & Cafe -->
          <div onclick="handleCategoryClick('Dining & Cafe', '320.00 AED', '15%')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>
                  <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>
                  <line x1="6" y1="1" x2="6" y2="4"></line>
                  <line x1="10" y1="1" x2="10" y2="4"></line>
                  <line x1="14" y1="1" x2="14" y2="4"></line>
                </svg>
              </div>
              <span class="text-[14.5px] font-semibold text-white tracking-tight">Dining & Cafe</span>
            </div>
            <div class="flex items-center gap-4">
              <span class="text-[12.5px] font-medium text-[#9e94b8]">15%</span>
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">320.00 AED</span>
            </div>
          </div>

          <!-- Item 5: Subscriptions & Digital Services (Visible when expanded) -->
          <div onclick="handleCategoryClick('Subscriptions', '185.00 AED', '8%')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
              </div>
              <span class="text-[14.5px] font-semibold text-white tracking-tight">Subscriptions</span>
            </div>
            <div class="flex items-center gap-4">
              <span class="text-[12.5px] font-medium text-[#9e94b8]">8%</span>
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">185.00 AED</span>
            </div>
          </div>

          <!-- Item 6: Travel & Transit (Visible when expanded) -->
          <div onclick="handleCategoryClick('Travel & Transit', '450.00 AED', '12%')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.3c.4-.2.6-.6.5-1.1z"></path>
                </svg>
              </div>
              <span class="text-[14.5px] font-semibold text-white tracking-tight">Travel & Transit</span>
            </div>
            <div class="flex items-center gap-4">
              <span class="text-[12.5px] font-medium text-[#9e94b8]">12%</span>
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">450.00 AED</span>
            </div>
          </div>

        </div>
      </div>



    </div>

    <!-- ======================================================== -->
    <!-- SCREEN 9: FINANCE HUB (CONSISTENT HOMESCREEN & STATS THEME)-->
    <!-- ======================================================== -->
    <div id="financeScreen" class="screen-layer home-bg screen-hidden-right flex flex-col justify-between pt-4 pb-0 px-0 overflow-hidden select-none text-white">
      
      <!-- Upper Section: Capsule Header, Portfolio Card, Quick Actions -->
      <div id="financeTopSection" class="w-full px-4 pt-1 select-none flex-shrink-0">
        
        <!-- Top Bar: Translucent Capsule Header Bar matching Home & Statistics -->
        <div class="w-full rounded-full bg-white/[0.05] border border-white/[0.08] backdrop-blur-xl px-3 py-1.5 flex items-center justify-between mb-2 shadow-sm">
          <!-- Left: Avatar & Greeting (Clickable for Account & Profile) -->
          <div onclick="openUserProfileModal()" class="flex items-center gap-2.5 cursor-pointer hover:opacity-90 active:scale-95 transition apple-press" title="View Account & Profile">
            <div class="w-8 h-8 rounded-full p-[1px] bg-gradient-to-tr from-pink-500/50 via-purple-500/30 to-cyan-400/40 shadow-sm flex-shrink-0 relative">
              <img 
                src="{avatar_b64}" 
                alt="Marice Cervantes" 
                class="w-full h-full rounded-full object-cover" 
              />
              <div class="absolute -bottom-0.5 -right-0.5 z-20 w-2.5 h-2.5 rounded-full bg-emerald-400 border-2 border-[#120d2d] shadow-sm"></div>
            </div>
            <div class="flex flex-col">
              <span class="text-[10.5px] font-medium text-[#9e94b8] tracking-tight leading-none mb-0.5">Hello,</span>
              <span class="text-[13.5px] font-bold text-white tracking-tight leading-none flex items-center gap-1">
                Marice Cervantes
                <svg class="w-2.5 h-2.5 text-blue-400 opacity-80" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </span>
            </div>
          </div>

          <!-- Right: Circular Glass Buttons (Scan QR & Notification Bell) -->
          <div class="flex items-center gap-1.5">
            <button 
              onclick="openScannerModal()" 
              class="w-7 h-7 rounded-full bg-white/[0.06] hover:bg-white/[0.12] active:scale-95 border border-white/10 backdrop-blur-md flex items-center justify-center text-white/90 transition cursor-pointer apple-press shadow-sm"
              title="Scan QR Code"
            >
              <svg class="w-3.5 h-3.5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 8V5a1 1 0 0 1 1-1h3"></path>
                <path d="M4 16v3a1 1 0 0 0 1 1h3"></path>
                <path d="M16 4h3a1 1 0 0 1 1 1v3"></path>
                <path d="M16 20h3a1 1 0 0 0 1-1v-3"></path>
                <line x1="8" y1="12" x2="16" y2="12"></line>
              </svg>
            </button>

            <button 
              onclick="openNotificationsModal()" 
              class="w-7 h-7 rounded-full bg-white/[0.06] hover:bg-white/[0.12] active:scale-95 border border-white/10 backdrop-blur-md relative flex items-center justify-center text-white/90 transition cursor-pointer apple-press shadow-sm"
              title="Notifications"
            >
              <svg class="w-3.5 h-3.5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              <span class="absolute top-1 right-1 w-1.5 h-1.5 rounded-full bg-[#ff2a6d] shadow-[0_0_6px_#ff2a6d]"></span>
            </button>
          </div>
        </div>

        <!-- Title: Finance with Proper Padding & Margins (Matches Statistics My Expenses) -->
        <div class="pt-2.5 pb-3.5 px-0.5 flex items-center justify-between">
          <div>
            <h1 class="text-[27px] font-extrabold text-white tracking-tight leading-none">Finance</h1>
          </div>
          <button 
            onclick="toggleStealthMode()" 
            class="px-2.5 py-1 rounded-full bg-white/[0.06] hover:bg-white/[0.12] border border-white/10 text-[11px] font-medium text-white/80 transition flex items-center gap-1.5 cursor-pointer apple-press"
            title="Mask or unmask balances"
          >
            <svg class="w-3.5 h-3.5 text-white/70" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
              <circle cx="12" cy="12" r="3"></circle>
            </svg>
            <span id="financeStealthLabel">Visible</span>
          </button>
        </div>

        <!-- Total Assets Hero Card (Matches Statistics Chart Card Design & Glass Style) -->
        <div class="w-full rounded-[22px] bg-[#141033]/80 border border-white/[0.08] p-4 backdrop-blur-xl relative shadow-lg mb-2">
          <span class="text-[10.5px] font-medium text-[#9e94b8] tracking-tight block mb-0.5">Total Portfolio & Net Worth</span>
          <div class="flex items-baseline">
            <span id="financeTotalNetWorth" class="text-[26px] font-extrabold text-white tracking-tight">23,901.20</span>
            <span class="text-[12px] font-bold text-white/80 ml-1">AED</span>
          </div>

          <div class="w-full h-[1px] bg-white/[0.07] my-3"></div>

          <div class="grid grid-cols-2 gap-3">
            <div>
              <span class="text-[10.5px] text-[#9e94b8] font-medium block">Available Balance</span>
              <span id="financeAvailableBal" class="text-[14.5px] font-bold text-white tracking-tight block mt-0.5">5,501.20 AED</span>
            </div>
            <div onclick="showScreen('vault')" class="cursor-pointer group rounded-xl p-1 -m-1 hover:bg-white/[0.04] transition" title="Open Savings Vaults">
              <span class="text-[10.5px] text-[#9e94b8] group-hover:text-white font-medium flex items-center gap-1 transition">
                Locked Vaults
                <svg class="w-3 h-3 text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M9 18l6-6-6-6"/></svg>
              </span>
              <span id="financeVaultsBal" class="text-[14.5px] font-bold text-white tracking-tight block mt-0.5">18,400.00 AED</span>
            </div>
          </div>
        </div>

        <!-- 4 Quick Action Buttons (Matching Homescreen action-btn Circular Glass Style) -->
        <div class="grid grid-cols-4 gap-2 mt-2 mb-2 px-1">
          <!-- 1. Transfer -->
          <div class="flex flex-col items-center">
            <button onclick="openTransferModal()" class="action-btn apple-press" title="Transfer Funds">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 4v11M7.5 8.5L12 4l4.5 4.5" />
                <path d="M5 14.5v2.5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-2.5" />
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Transfer</span>
          </div>

          <!-- 2. Exchange -->
          <div class="flex flex-col items-center">
            <button onclick="openExchangeModal()" class="action-btn apple-press" title="Exchange Currency">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
                <line x1="12" y1="22.08" x2="12" y2="12"></line>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Exchange</span>
          </div>

          <!-- 3. Top Up -->
          <div class="flex flex-col items-center">
            <button onclick="triggerQuickAction('add')" class="action-btn apple-press" title="Deposit / Top Up">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Top Up</span>
          </div>

          <!-- 4. Vault -->
          <div class="flex flex-col items-center">
            <button onclick="showScreen('vault')" class="action-btn apple-press" title="Savings Vaults">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Vault</span>
          </div>
        </div>

      </div>

      <!-- ======================================================== -->
      <!-- EXPANDABLE & DRAGGABLE ACCOUNTS & VAULTS BOTTOM SHEET    -->
      <!-- ======================================================== -->
      <div 
        id="financeBottomSheet" 
        class="liquid-glass-sheet absolute left-0 right-0 bottom-0 rounded-t-[34px] z-20 flex flex-col transition-transform duration-400 ease-out overflow-hidden" 
        style="top: 38px; transform: translateY(325px);"
      >
        <!-- Liquid Glass Specular Top Highlight Line -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <!-- Ambient Top Sheen -->
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Draggable Handle Area (Matches Statistics Bottom Sheet Exactly) -->
        <div id="financeSheetDragHandleArea" class="px-5 pt-3 pb-2 cursor-grab active:cursor-grabbing select-none flex-shrink-0" style="touch-action: none;" title="Drag up to expand accounts">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mx-auto mb-3 transition-colors"></div>

          <!-- Section Title Row -->
          <div class="flex items-center justify-between">
            <h2 class="text-[17px] font-bold text-white tracking-tight">Accounts & Vaults</h2>
            <button 
              id="financeSheetToggleBtn" 
              onclick="toggleFinanceBottomSheet()" 
              class="text-xs text-blue-400 hover:text-blue-300 flex items-center gap-1 font-semibold transition cursor-pointer"
            >
              <span id="financeSheetToggleLabel">See All</span>
              <svg id="financeSheetToggleChevron" class="w-3.5 h-3.5 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M5 15l7-7 7 7"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Scrollable Clean Accounts & Vaults List (Consistent with Statistics Categories) -->
        <div id="financeAccountsList" class="flex-1 overflow-y-auto px-5 pb-[420px] divide-y divide-white/[0.08] relative z-10 scrollbar-none">
          
          <!-- Item 1: Checking Account -->
          <div onclick="handleAccountClick('Checking Account', '14,250.00 AED', '•••• 8920')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="2" y="5" width="20" height="14" rx="2"></rect>
                  <line x1="2" y1="10" x2="22" y2="10"></line>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Primary Checking</span>
                <span class="text-[11.5px] text-[#9e94b8]">•••• 8920 • Direct Sync</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">14,250.00 AED</span>
              <span class="text-[10px] text-emerald-400 font-medium">Active</span>
            </div>
          </div>

          <!-- Item 2: Salary Account -->
          <div onclick="handleAccountClick('Salary Account', '6,800.00 AED', '•••• 4129')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Salary Account</span>
                <span class="text-[11.5px] text-[#9e94b8]">•••• 4129 • Monthly Payroll</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">6,800.00 AED</span>
              <span class="text-[10px] text-emerald-400 font-medium">Active</span>
            </div>
          </div>

          <!-- Item 3: Emergency Reserve Vault -->
          <div onclick="handleAccountClick('Emergency Reserve Vault', '12,000.00 AED', '3.75% APY')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Emergency Reserve</span>
                <span class="text-[11.5px] text-[#9e94b8]">3.75% APY • Auto-Save Vault</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">12,000.00 AED</span>
              <span class="text-[10px] text-[#9e94b8]">Locked</span>
            </div>
          </div>

          <!-- Item 4: Tokyo Vacation 2025 -->
          <div onclick="handleAccountClick('Tokyo Vacation 2025', '6,400.00 AED', 'Goal Target 15,000 AED')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Tokyo Vacation 2025</span>
                <span class="text-[11.5px] text-[#9e94b8]">Goal Target 15,000 AED</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">6,400.00 AED</span>
              <span class="text-[10px] text-[#9e94b8]">42%</span>
            </div>
          </div>

          <!-- Item 5: Multi-Currency Travel Pocket -->
          <div onclick="handleAccountClick('Travel Currency Pocket', '2,450.00 AED', 'USD, EUR, GBP')" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="2" y1="12" x2="22" y2="12"></line>
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Global Currency Pocket</span>
                <span class="text-[11.5px] text-[#9e94b8]">USD, EUR, GBP Pockets</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">2,450.00 AED</span>
              <span class="text-[10px] text-emerald-400 font-medium">Ready</span>
            </div>
          </div>

        </div>
      </div>



    </div>

    <!-- ======================================================== -->
    <!-- SCREEN 10: WALLET FEATURES & SERVICES (MOBILE WALLET HUB)  -->
    <!-- ======================================================== -->
    <div id="othersScreen" class="screen-layer home-bg screen-hidden-right flex flex-col justify-between pt-4 pb-0 px-0 overflow-hidden select-none text-white">
      
      <!-- Upper Section: Capsule Header, Apple Wallet Pass Hero, Quick Actions -->
      <div id="othersTopSection" class="w-full px-4 pt-1 select-none flex-shrink-0">
        
        <!-- Top Bar: Translucent Capsule Header Bar matching Home & Statistics -->
        <div class="w-full rounded-full bg-white/[0.05] border border-white/[0.08] backdrop-blur-xl px-3 py-1.5 flex items-center justify-between mb-2 shadow-sm">
          <!-- Left: Avatar & Greeting (Clickable for Account & Profile) -->
          <div onclick="openUserProfileModal()" class="flex items-center gap-2.5 cursor-pointer hover:opacity-90 active:scale-95 transition apple-press" title="View Account & Profile">
            <div class="w-8 h-8 rounded-full p-[1px] bg-gradient-to-tr from-pink-500/50 via-purple-500/30 to-cyan-400/40 shadow-sm flex-shrink-0 relative">
              <img 
                src="{avatar_b64}" 
                alt="Marice Cervantes" 
                class="w-full h-full rounded-full object-cover" 
              />
              <div class="absolute -bottom-0.5 -right-0.5 z-20 w-2.5 h-2.5 rounded-full bg-emerald-400 border-2 border-[#120d2d] shadow-sm"></div>
            </div>
            <div class="flex flex-col">
              <span class="text-[10.5px] font-medium text-[#9e94b8] tracking-tight leading-none mb-0.5">Hello,</span>
              <span class="text-[13.5px] font-bold text-white tracking-tight leading-none flex items-center gap-1">
                Marice Cervantes
                <svg class="w-2.5 h-2.5 text-blue-400 opacity-80" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </span>
            </div>
          </div>

          <!-- Right: Circular Glass Buttons (Scan QR & Notification Bell) -->
          <div class="flex items-center gap-1.5">
            <button 
              onclick="openScannerModal()" 
              class="w-7 h-7 rounded-full bg-white/[0.06] hover:bg-white/[0.12] active:scale-95 border border-white/10 backdrop-blur-md flex items-center justify-center text-white/90 transition cursor-pointer apple-press shadow-sm"
              title="Scan QR Code"
            >
              <svg class="w-3.5 h-3.5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 8V5a1 1 0 0 1 1-1h3"></path>
                <path d="M4 16v3a1 1 0 0 0 1 1h3"></path>
                <path d="M16 4h3a1 1 0 0 1 1 1v3"></path>
                <path d="M16 20h3a1 1 0 0 0 1-1v-3"></path>
                <line x1="8" y1="12" x2="16" y2="12"></line>
              </svg>
            </button>

            <button 
              onclick="openNotificationsModal()" 
              class="w-7 h-7 rounded-full bg-white/[0.06] hover:bg-white/[0.12] active:scale-95 border border-white/10 backdrop-blur-md relative flex items-center justify-center text-white/90 transition cursor-pointer apple-press shadow-sm"
              title="Notifications"
            >
              <svg class="w-3.5 h-3.5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              <span class="absolute top-1 right-1 w-1.5 h-1.5 rounded-full bg-[#ff2a6d] shadow-[0_0_6px_#ff2a6d]"></span>
            </button>
          </div>
        </div>

        <!-- Title: Wallet Features -->
        <div class="pt-2.5 pb-3.5 px-0.5 flex items-center justify-between">
          <div>
            <h1 class="text-[27px] font-extrabold text-white tracking-tight leading-none">Wallet Features</h1>
          </div>
        </div>

        <!-- Apple Wallet Pass & Contactless Hero Card (Colorful Gradient Matching Home Card) -->
        <div class="w-full rounded-[28px] debit-card-gradient p-5 relative overflow-hidden mb-2">
          <div class="relative z-10 flex items-start justify-between mb-3.5">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-2xl bg-black/25 backdrop-blur-md border border-white/25 flex items-center justify-center text-white flex-shrink-0">
                <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="2" y="5" width="20" height="14" rx="3"></rect>
                  <path d="M2 10h20"></path>
                </svg>
              </div>
              <div>
                <span class="text-[15px] font-bold text-white block tracking-tight">Apple Wallet & NFC Pass</span>
                <span class="text-[11px] text-white/85 font-medium">Contactless Tap to Pay provisioned</span>
              </div>
            </div>
          </div>

          <!-- Add / View Pass in Apple Wallet Button -->
          <button 
            onclick="handleAddToAppleWalletClick()" 
            class="relative z-10 w-full py-2.5 px-3 rounded-[16px] bg-black/35 hover:bg-black/50 active:scale-[0.98] backdrop-blur-md border border-white/25 text-white text-[12.5px] font-semibold flex items-center justify-center gap-2 transition cursor-pointer apple-press"
          >
            <svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.37c.63-.78 1.06-1.85.95-2.93-.93.04-2.02.63-2.67 1.39-.58.67-.99 1.77-.85 2.82 1.05.08 2.08-.55 2.57-1.28z"/>
            </svg>
            <span>View Pass in Apple Wallet</span>
          </button>
        </div>

        <!-- 4 Quick Action Buttons (Matching Homescreen action-btn Circular Glass Style) -->
        <div class="grid grid-cols-4 gap-2 mt-2 mb-2 px-1">
          <!-- 1. Bill Pay -->
          <div class="flex flex-col items-center">
            <button onclick="openBillPayModal()" class="action-btn apple-press" title="Pay Bills & Utilities">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Bill Pay</span>
          </div>

          <!-- 2. Split Bill -->
          <div class="flex flex-col items-center">
            <button onclick="openSplitBillModal()" class="action-btn apple-press" title="Split Bill with Friends">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Split Bill</span>
          </div>

          <!-- 3. Vouchers -->
          <div class="flex flex-col items-center">
            <button onclick="openGiftCardsModal()" class="action-btn apple-press" title="Digital Gift Vouchers">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 12 20 22 4 22 4 12"></polyline>
                <rect x="2" y="7" width="20" height="5"></rect>
                <line x1="12" y1="22" x2="12" y2="7"></line>
                <path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path>
                <path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Vouchers</span>
          </div>

          <!-- 4. Rewards -->
          <div class="flex flex-col items-center">
            <button onclick="openRewardsModal()" class="action-btn apple-press" title="LeapPoints & Rewards">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Rewards</span>
          </div>
        </div>

      </div>

      <!-- ======================================================== -->
      <!-- EXPANDABLE & DRAGGABLE WALLET SERVICES BOTTOM SHEET      -->
      <!-- ======================================================== -->
      <div 
        id="othersBottomSheet" 
        class="liquid-glass-sheet absolute left-0 right-0 bottom-0 rounded-t-[34px] z-20 flex flex-col transition-transform duration-400 ease-out overflow-hidden" 
        style="top: 38px; transform: translateY(325px);"
      >
        <!-- Liquid Glass Specular Top Highlight Line -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <!-- Ambient Top Sheen -->
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Draggable Handle Area (Matches Statistics Bottom Sheet Exactly) -->
        <div id="othersSheetDragHandleArea" class="px-5 pt-3 pb-2 cursor-grab active:cursor-grabbing select-none flex-shrink-0" style="touch-action: none;" title="Drag up to expand features">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mx-auto mb-3 transition-colors"></div>

          <!-- Section Title Row -->
          <div class="flex items-center justify-between">
            <h2 class="text-[17px] font-bold text-white tracking-tight">All Features</h2>
            <button 
              id="othersSheetToggleBtn" 
              onclick="toggleOthersBottomSheet()" 
              class="text-xs text-blue-400 hover:text-blue-300 flex items-center gap-1 font-semibold transition cursor-pointer"
            >
              <span id="othersSheetToggleLabel">See All</span>
              <svg id="othersSheetToggleChevron" class="w-3.5 h-3.5 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M5 15l7-7 7 7"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Scrollable Clean Features List (Consistent with Statistics Categories) -->
        <div id="othersFeaturesList" class="flex-1 overflow-y-auto px-5 pb-[420px] divide-y divide-white/[0.08] relative z-10 scrollbar-none">
          
          <!-- Item 1: Utilities & Bills -->
          <div onclick="openBillPayModal()" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Utility & Telecom Bills</span>
                <span class="text-[11.5px] text-[#9e94b8]">DEWA, SEWA, Salik, Du, Etisalat</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[13px] font-semibold text-blue-400">Pay Now</span>
            </div>
          </div>

          <!-- Item 2: Split Bill with Friends -->
          <div onclick="openSplitBillModal()" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Split Bill / Group Leap</span>
                <span class="text-[11.5px] text-[#9e94b8]">Split dining, groceries or rent</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[13px] font-semibold text-blue-400">Share Link</span>
            </div>
          </div>

          <!-- Item 3: Digital Gift Vouchers -->
          <div onclick="openGiftCardsModal()" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20 12 20 22 4 22 4 12"></polyline>
                  <rect x="2" y="7" width="20" height="5"></rect>
                  <line x1="12" y1="22" x2="12" y2="7"></line>
                  <path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path>
                  <path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Digital Brand Vouchers</span>
                <span class="text-[11.5px] text-[#9e94b8]">Amazon, Apple, Noon, PlayStation</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[13px] font-semibold text-blue-400">Shop 40+</span>
            </div>
          </div>

          <!-- Item 4: Leap Loyalty Club -->
          <div onclick="openRewardsModal()" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">LeapPoints Rewards</span>
                <span class="text-[11.5px] text-[#9e94b8]">1,420 Pts • 2% Unlimited Cashback</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[13px] font-semibold text-emerald-400">Redeem</span>
            </div>
          </div>

          <!-- Item 5: Multi-Currency FX Pockets -->
          <div onclick="openExchangeModal()" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="2" y1="12" x2="22" y2="12"></line>
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Global Travel Currency</span>
                <span class="text-[11.5px] text-[#9e94b8]">0% FX Markup on USD, EUR, GBP</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[13px] font-semibold text-blue-400">Convert</span>
            </div>
          </div>

          <!-- Item 6: International Remittance -->
          <div onclick="openTransferModal()" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="22" y1="2" x2="11" y2="13"></line>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">Worldwide Money Wire</span>
                <span class="text-[11.5px] text-[#9e94b8]">Send money to 60+ countries</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[13px] font-semibold text-blue-400">Send Wire</span>
            </div>
          </div>

          <!-- Item 7: 24/7 Priority Concierge -->
          <div onclick="openSupportChat()" class="flex items-center justify-between py-3 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
              </div>
              <div class="flex flex-col">
                <span class="text-[14.5px] font-semibold text-white tracking-tight">24/7 Live Support Chat</span>
                <span class="text-[11.5px] text-[#9e94b8]">Cashleap Client Concierge</span>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-[13px] font-semibold text-emerald-400">Live 24/7</span>
            </div>
          </div>

        </div>
      </div>



    </div>


    <!-- ======================================================== -->
    <!-- SCREEN 11: SAVINGS VAULTS SCREEN FLOW                    -->
    <!-- ======================================================== -->
    <div id="vaultScreen" class="screen-layer home-bg screen-hidden-right flex flex-col justify-between pt-4 pb-0 px-0 overflow-hidden select-none text-white">
      
      <!-- Upper Section: Capsule Header, Title, Total Vault Hero Card & Quick Actions -->
      <div id="vaultTopSection" class="w-full px-4 pt-1 select-none flex-shrink-0">
        
        <!-- Top Bar: Translucent Capsule Header Bar matching Home, Finance & Statistics -->
        <div class="w-full rounded-full bg-white/[0.05] border border-white/[0.08] backdrop-blur-xl px-3 py-1.5 flex items-center justify-between mb-2 shadow-sm">
          <!-- Left: Back to Finance & Subtitle -->
          <div class="flex items-center gap-2.5">
            <button 
              onclick="showScreen('finance')" 
              class="w-8 h-8 rounded-full bg-white/[0.07] hover:bg-white/[0.14] active:scale-95 border border-white/10 flex items-center justify-center text-white transition cursor-pointer apple-press"
              title="Back to Finance"
            >
              <svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 18l-6-6 6-6"/>
              </svg>
            </button>
            <div class="flex flex-col">
              <span class="text-[10.5px] font-medium text-[#9e94b8] tracking-tight leading-none mb-0.5">Finance Portfolio</span>
              <span class="text-[13.5px] font-bold text-white tracking-tight leading-none flex items-center gap-1">
                Savings Vaults
                <svg class="w-2.5 h-2.5 text-emerald-400 opacity-90" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </span>
            </div>
          </div>

          <!-- Right: Add Vault & Notifications -->
          <div class="flex items-center gap-1.5">
            <button 
              onclick="openCreateVaultModal()" 
              class="h-7 px-2.5 rounded-full bg-blue-600/25 hover:bg-blue-600/35 active:scale-95 border border-blue-400/40 backdrop-blur-md flex items-center gap-1 text-[10.5px] font-semibold text-white transition cursor-pointer apple-press shadow-sm"
              title="Create New Savings Vault"
            >
              <svg class="w-3 h-3 text-blue-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
              <span>New Vault</span>
            </button>
          </div>
        </div>

        <!-- Title Row matching Statistics & Finance -->
        <div class="pt-2 pb-3 px-0.5 flex items-center justify-between">
          <div>
            <h1 class="text-[26px] font-extrabold text-white tracking-tight leading-none">My Vaults</h1>
          </div>
          <div class="px-2.5 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/30 flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="text-[10.5px] font-bold text-emerald-300 tracking-wide">Up to 5.10% APY</span>
          </div>
        </div>

        <!-- Total Vault Balance Hero Card (Matches Statistics & Finance Glass Card Style) -->
        <div class="w-full rounded-[22px] bg-[#141033]/85 border border-white/[0.08] p-4 backdrop-blur-xl relative shadow-lg mb-2">
          <div class="flex items-start justify-between">
            <div>
              <span class="text-[10.5px] font-medium text-[#9e94b8] tracking-tight block mb-0.5">Total Vault Balance</span>
              <div class="flex items-baseline">
                <span id="vaultTotalBalance" class="text-[26px] font-extrabold text-white tracking-tight">18,400.00</span>
                <span class="text-[12px] font-bold text-white/80 ml-1">AED</span>
              </div>
            </div>
            <div class="text-right">
              <span class="text-[10px] text-[#9e94b8] font-medium block">Yield Earned YTD</span>
              <span id="vaultTotalYield" class="text-[13px] font-bold text-emerald-400 tracking-tight">+742.50 AED</span>
            </div>
          </div>

          <!-- Overall Goal Progress Bar -->
          <div class="mt-3 mb-1">
            <div class="flex items-center justify-between text-[10.5px] mb-1.5">
              <span class="text-[#9e94b8] font-medium">Combined Goal Progress</span>
              <span id="vaultOverallProgressLabel" class="text-white font-semibold">71% of 26,000 AED</span>
            </div>
            <div class="w-full h-2 rounded-full bg-white/[0.07] overflow-hidden p-[1px]">
              <div id="vaultOverallProgressBar" class="h-full rounded-full bg-gradient-to-r from-blue-500 via-indigo-500 to-emerald-400 transition-all duration-500" style="width: 71%;"></div>
            </div>
          </div>
        </div>

        <!-- 4 Quick Action Buttons (Matching Homescreen action-btn Circular Glass Style) -->
        <div class="grid grid-cols-4 gap-2 mt-2 mb-2 px-1">
          <!-- 1. Deposit -->
          <div class="flex flex-col items-center">
            <button onclick="openVaultActionModal('deposit')" class="action-btn apple-press" title="Deposit into Vault">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 3v12M7.5 10.5L12 15l4.5-4.5" />
                <path d="M5 15.5v2.5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-2.5" />
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Deposit</span>
          </div>

          <!-- 2. Withdraw -->
          <div class="flex flex-col items-center">
            <button onclick="openVaultActionModal('withdraw')" class="action-btn apple-press" title="Withdraw to Card">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 15V3M7.5 7.5L12 3l4.5 4.5" />
                <path d="M5 15.5v2.5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-2.5" />
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">Withdraw</span>
          </div>

          <!-- 3. New Vault -->
          <div class="flex flex-col items-center">
            <button onclick="openCreateVaultModal()" class="action-btn apple-press" title="Create New Vault">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                <line x1="12" y1="14" x2="12" y2="19"></line>
                <line x1="9.5" y1="16.5" x2="14.5" y2="16.5"></line>
              </svg>
            </button>
            <span class="text-xs text-[#a09bb8] font-medium mt-1.5">New Goal</span>
          </div>

          <!-- 4. Auto Round-Up -->
          <div class="flex flex-col items-center">
            <button onclick="toggleVaultAutoSave()" class="action-btn apple-press" title="Toggle Spare Change Auto-Save">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="23 4 23 10 17 10"></polyline>
                <polyline points="1 20 1 14 7 14"></polyline>
                <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
              </svg>
            </button>
            <span id="vaultAutoSaveQuickLabel" class="text-xs text-emerald-400 font-medium mt-1.5">Auto-Save</span>
          </div>
        </div>

      </div>

      <!-- ======================================================== -->
      <!-- EXPANDABLE & DRAGGABLE ACTIVE VAULTS BOTTOM SHEET        -->
      <!-- ======================================================== -->
      <div 
        id="vaultGoalsSheet" 
        class="liquid-glass-sheet absolute left-0 right-0 bottom-0 rounded-t-[34px] z-20 flex flex-col transition-transform duration-400 ease-out overflow-hidden" 
        style="top: 38px; transform: translateY(338px);"
      >
        <!-- Liquid Glass Specular Top Highlight Line -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <!-- Ambient Top Sheen -->
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Draggable Handle Area -->
        <div id="vaultSheetDragHandleArea" class="px-5 pt-3 pb-2 cursor-grab active:cursor-grabbing select-none flex-shrink-0" style="touch-action: none;" title="Drag up to expand savings vaults">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mx-auto mb-3 transition-colors"></div>

          <!-- Section Title Row -->
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <h2 class="text-[17px] font-bold text-white tracking-tight">Active Vaults</h2>
              <span id="vaultActiveCountBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-white/[0.08] border border-white/10 text-[#9e94b8]">3 Goals</span>
            </div>
            <button 
              id="vaultSheetToggleBtn" 
              onclick="toggleVaultBottomSheet()" 
              class="text-xs text-blue-400 hover:text-blue-300 flex items-center gap-1 font-semibold transition cursor-pointer"
            >
              <span id="vaultSheetToggleLabel">See All</span>
              <svg id="vaultSheetToggleChevron" class="w-3.5 h-3.5 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M5 15l7-7 7 7"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Scrollable Active Vaults List -->
        <div id="vaultGoalsList" class="flex-1 overflow-y-auto px-5 pb-[420px] divide-y divide-white/[0.08] relative z-10 scrollbar-none">
          
          <!-- Vault 1: Emergency Reserve Vault -->
          <div onclick="openVaultActionModal('deposit', 'emergency')" class="py-3.5 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center justify-between mb-2">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                  <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                  </svg>
                </div>
                <div class="flex flex-col">
                  <span class="text-[14.5px] font-semibold text-white tracking-tight">Emergency Reserve</span>
                  <span class="text-[11px] text-[#9e94b8]">4.85% APY • Auto-Save Active</span>
                </div>
              </div>
              <div class="flex flex-col items-end">
                <span id="vault-bal-emergency" class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">12,000.00 AED</span>
                <span id="vault-pct-emergency" class="text-[10.5px] text-emerald-400 font-semibold">80% of 15,000</span>
              </div>
            </div>
            <div class="w-full h-1.5 rounded-full bg-white/[0.07] overflow-hidden">
              <div id="vault-bar-emergency" class="h-full rounded-full bg-gradient-to-r from-blue-500 to-emerald-400 transition-all duration-500" style="width: 80%;"></div>
            </div>
          </div>

          <!-- Vault 2: Tokyo Vacation 2025 -->
          <div onclick="openVaultActionModal('deposit', 'tokyo')" class="py-3.5 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center justify-between mb-2">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                  <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"></path>
                  </svg>
                </div>
                <div class="flex flex-col">
                  <span class="text-[14.5px] font-semibold text-white tracking-tight">Tokyo Vacation 2025</span>
                  <span class="text-[11px] text-[#9e94b8]">4.50% APY • 2x Spare Change</span>
                </div>
              </div>
              <div class="flex flex-col items-end">
                <span id="vault-bal-tokyo" class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">4,200.00 AED</span>
                <span id="vault-pct-tokyo" class="text-[10.5px] text-blue-400 font-semibold">70% of 6,000</span>
              </div>
            </div>
            <div class="w-full h-1.5 rounded-full bg-white/[0.07] overflow-hidden">
              <div id="vault-bar-tokyo" class="h-full rounded-full bg-gradient-to-r from-indigo-500 to-cyan-400 transition-all duration-500" style="width: 70%;"></div>
            </div>
          </div>

          <!-- Vault 3: Investment & Gold Reserve -->
          <div onclick="openVaultActionModal('deposit', 'gold')" class="py-3.5 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center justify-between mb-2">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">
                  <svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                    <polyline points="2 17 12 22 22 17"></polyline>
                    <polyline points="2 12 12 17 22 12"></polyline>
                  </svg>
                </div>
                <div class="flex flex-col">
                  <span class="text-[14.5px] font-semibold text-white tracking-tight">Gold & Yield Reserve</span>
                  <span class="text-[11px] text-[#9e94b8]">5.10% APY • 90-Day Fixed Term</span>
                </div>
              </div>
              <div class="flex flex-col items-end">
                <span id="vault-bal-gold" class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">2,200.00 AED</span>
                <span id="vault-pct-gold" class="text-[10.5px] text-purple-300 font-semibold">44% of 5,000</span>
              </div>
            </div>
            <div class="w-full h-1.5 rounded-full bg-white/[0.07] overflow-hidden">
              <div id="vault-bar-gold" class="h-full rounded-full bg-gradient-to-r from-purple-500 to-pink-500 transition-all duration-500" style="width: 44%;"></div>
            </div>
          </div>

        </div>
      </div>

    </div>



    <!-- ======================================================== -->
    <!-- SCREEN 12: SEND MONEY & BENEFICIARIES SCREEN FLOW        -->
    <!-- ======================================================== -->
    <div id="sendMoneyScreen" class="screen-layer home-bg screen-hidden-right flex flex-col justify-between pt-4 pb-0 px-0 overflow-hidden select-none text-white">
      
      <!-- Upper Section: Capsule Header, Title, Cashleap User Lookup Card & Quick Actions -->
      <div id="sendMoneyTopSection" class="w-full px-4 pt-1 select-none flex-shrink-0">
        
        <!-- Top Bar: Translucent Capsule Header Bar matching Home, Statistics & Vault -->
        <div class="w-full rounded-full bg-white/[0.05] border border-white/[0.08] backdrop-blur-xl px-3 py-1.5 flex items-center justify-between mb-2 shadow-sm">
          <!-- Left: Back to Home & Title -->
          <div class="flex items-center gap-2.5">
            <button 
              onclick="showScreen('home')" 
              class="w-8 h-8 rounded-full bg-white/[0.07] hover:bg-white/[0.14] active:scale-95 border border-white/10 flex items-center justify-center text-white transition cursor-pointer apple-press"
              title="Back to Home"
            >
              <svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 18l-6-6 6-6"/>
              </svg>
            </button>
            <div class="flex flex-col">
              <span class="text-[10.5px] font-medium text-[#9e94b8] tracking-tight leading-none mb-0.5">Instant P2P & Bank</span>
              <span class="text-[13.5px] font-bold text-white tracking-tight leading-none flex items-center gap-1">
                Send Money
                <svg class="w-2.5 h-2.5 text-blue-400 opacity-90" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </span>
            </div>
          </div>

          <!-- Right: + Add Beneficiary Button -->
          <div class="flex items-center gap-1.5">
            <button 
              onclick="openAddBeneficiaryModal('cashleap')" 
              class="h-7 px-2.5 rounded-full bg-blue-600/25 hover:bg-blue-600/35 active:scale-95 border border-blue-400/40 backdrop-blur-md flex items-center gap-1 text-[10.5px] font-semibold text-white transition cursor-pointer apple-press shadow-sm"
              title="Add New Beneficiary"
            >
              <svg class="w-3 h-3 text-blue-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
              <span>Add Beneficiary</span>
            </button>
          </div>
        </div>

        <!-- Title Row matching Statistics & Finance -->
        <div class="pt-1.5 pb-2.5 px-0.5 flex items-center justify-between">
          <div>
            <h1 class="text-[26px] font-extrabold text-white tracking-tight leading-none">Recipients</h1>
          </div>
          <div class="px-2.5 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/30 flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="text-[10.5px] font-bold text-emerald-300 tracking-wide">0.00 AED Fee</span>
          </div>
        </div>

        <!-- Cashleap User Search & Quick Contacts Hero Card (Matches Statistics & Finance Glass Card) -->
        <div class="w-full rounded-[22px] bg-[#141033]/85 border border-white/[0.08] p-3.5 backdrop-blur-xl relative shadow-lg mb-2">
          <!-- Search Bar for @leaptag, Mobile or IBAN -->
          <div class="relative flex items-center mb-3">
            <svg class="w-4 h-4 text-[#9e94b8] absolute left-3.5 pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input 
              type="text" 
              id="sendBeneficiarySearchInput" 
              oninput="filterSendBeneficiaries(this.value)" 
              placeholder="Search @leaptag, name, phone or IBAN..." 
              class="w-full bg-white/[0.05] border border-white/10 rounded-xl pl-9 pr-3 py-2 text-xs text-white placeholder-[#8e8ca8] focus:outline-none focus:border-blue-500 transition"
            />
          </div>

          <!-- Horizontal Cashleap Users Avatar Strip -->
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-semibold uppercase tracking-wider text-[#9e94b8]">Cashleap Network Users</span>
            <span id="quickUsersCountLabel" class="text-[10px] font-semibold text-blue-400">Instant • @leaptag</span>
          </div>
          <div id="sendQuickAvatarsRow" class="flex items-center gap-3 overflow-x-auto pb-1 pt-0.5 scrollbar-none">
            <!-- + Add New Button -->
            <div onclick="openAddBeneficiaryModal('cashleap')" class="flex flex-col items-center gap-1 cursor-pointer apple-press flex-shrink-0">
              <div class="w-11 h-11 rounded-full bg-white/[0.05] hover:bg-white/[0.1] border border-dashed border-blue-400/60 flex items-center justify-center text-blue-400 transition">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
                  <line x1="12" y1="5" x2="12" y2="19"></line>
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                </svg>
              </div>
              <span class="text-[10px] font-semibold text-blue-300">Add New</span>
            </div>

            <!-- User 1: Sarah Jenkins -->
            <div onclick="openSendToBeneficiary('sarah')" class="flex flex-col items-center gap-1 cursor-pointer apple-press flex-shrink-0">
              <div class="relative">
                <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-indigo-600 to-blue-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs shadow-sm">SJ</div>
                <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </span>
              </div>
              <span class="text-[10px] text-white/90 font-medium truncate w-12 text-center">Sarah</span>
            </div>

            <!-- User 2: Alex Rivera -->
            <div onclick="openSendToBeneficiary('alex')" class="flex flex-col items-center gap-1 cursor-pointer apple-press flex-shrink-0">
              <div class="relative">
                <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs shadow-sm">AR</div>
                <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </span>
              </div>
              <span class="text-[10px] text-white/90 font-medium truncate w-12 text-center">Alex</span>
            </div>

            <!-- User 3: David Chen -->
            <div onclick="openSendToBeneficiary('david')" class="flex flex-col items-center gap-1 cursor-pointer apple-press flex-shrink-0">
              <div class="relative">
                <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-purple-600 to-indigo-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs shadow-sm">DC</div>
                <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </span>
              </div>
              <span class="text-[10px] text-white/90 font-medium truncate w-12 text-center">David</span>
            </div>

            <!-- User 4: Omar Al Maktoum -->
            <div onclick="openSendToBeneficiary('omar')" class="flex flex-col items-center gap-1 cursor-pointer apple-press flex-shrink-0">
              <div class="relative">
                <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-emerald-600 to-teal-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs shadow-sm">OM</div>
                <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </span>
              </div>
              <span class="text-[10px] text-white/90 font-medium truncate w-12 text-center">Omar</span>
            </div>

            <!-- User 5: Elena Rostova -->
            <div onclick="openSendToBeneficiary('elena')" class="flex flex-col items-center gap-1 cursor-pointer apple-press flex-shrink-0">
              <div class="relative">
                <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-slate-700 to-indigo-800 border border-white/25 flex items-center justify-center text-white font-bold text-xs shadow-sm">ER</div>
              </div>
              <span class="text-[10px] text-white/90 font-medium truncate w-12 text-center">Elena</span>
            </div>
          </div>
        </div>

        <!-- 4 Quick Action Buttons (Matching Homescreen action-btn Circular Glass Style) -->
        <div class="grid grid-cols-4 gap-2 mt-1.5 mb-2 px-1">
          <!-- 1. Add Cashleap User -->
          <div class="flex flex-col items-center">
            <button onclick="openAddBeneficiaryModal('cashleap')" class="action-btn apple-press" title="Add Cashleap User (@leaptag)">
              <svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="8.5" cy="7" r="4"></circle>
                <line x1="20" y1="8" x2="20" y2="14"></line>
                <line x1="23" y1="11" x2="17" y2="11"></line>
              </svg>
            </button>
            <span class="text-[11px] text-[#a09bb8] font-medium mt-1">Cashleap User</span>
          </div>

          <!-- 2. Add Bank IBAN -->
          <div class="flex flex-col items-center">
            <button onclick="openAddBeneficiaryModal('iban')" class="action-btn apple-press" title="Add Bank IBAN Beneficiary">
              <svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="3" y1="22" x2="21" y2="22"></line>
                <line x1="6" y1="18" x2="6" y2="11"></line>
                <line x1="10" y1="18" x2="10" y2="11"></line>
                <line x1="14" y1="18" x2="14" y2="11"></line>
                <line x1="18" y1="18" x2="18" y2="11"></line>
                <polygon points="12 2 20 7 4 7"></polygon>
              </svg>
            </button>
            <span class="text-[11px] text-[#a09bb8] font-medium mt-1">Bank IBAN</span>
          </div>

          <!-- 3. QR Pay -->
          <div class="flex flex-col items-center">
            <button onclick="openScannerModal()" class="action-btn apple-press" title="Scan Cashleap QR">
              <svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 8V5a1 1 0 0 1 1-1h3"></path>
                <path d="M4 16v3a1 1 0 0 0 1 1h3"></path>
                <path d="M16 4h3a1 1 0 0 1 1 1v3"></path>
                <path d="M16 20h3a1 1 0 0 0 1-1v-3"></path>
                <line x1="8" y1="12" x2="16" y2="12"></line>
              </svg>
            </button>
            <span class="text-[11px] text-[#a09bb8] font-medium mt-1">Scan QR</span>
          </div>

          <!-- 4. Direct Send -->
          <div class="flex flex-col items-center">
            <button onclick="openSendToBeneficiary('sarah')" class="action-btn apple-press" title="Send Money Immediately">
              <svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
              </svg>
            </button>
            <span class="text-[11px] text-[#a09bb8] font-medium mt-1">Quick Send</span>
          </div>
        </div>

      </div>

      <!-- ======================================================== -->
      <!-- EXPANDABLE & DRAGGABLE SAVED BENEFICIARIES BOTTOM SHEET  -->
      <!-- ======================================================== -->
      <div 
        id="sendBeneficiariesSheet" 
        class="liquid-glass-sheet absolute left-0 right-0 bottom-0 rounded-t-[34px] z-20 flex flex-col transition-transform duration-400 ease-out overflow-hidden" 
        style="top: 38px; transform: translateY(338px);"
      >
        <!-- Liquid Glass Specular Top Highlight Line -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <!-- Ambient Top Sheen -->
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Draggable Handle Area -->
        <div id="sendSheetDragHandleArea" class="px-5 pt-3 pb-2 cursor-grab active:cursor-grabbing select-none flex-shrink-0" style="touch-action: none;" title="Drag up to expand beneficiaries">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mx-auto mb-2.5 transition-colors"></div>

          <!-- Section Title Row -->
          <div class="flex items-center justify-between mb-2">
            <div class="flex items-center gap-2">
              <h2 class="text-[17px] font-bold text-white tracking-tight">Saved Beneficiaries</h2>
              <span id="sendBeneficiariesCountBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-white/[0.08] border border-white/10 text-[#9e94b8]">5 Saved</span>
            </div>
            <button 
              id="sendSheetToggleBtn" 
              onclick="toggleSendBottomSheet()" 
              class="text-xs text-blue-400 hover:text-blue-300 flex items-center gap-1 font-semibold transition cursor-pointer"
            >
              <span id="sendSheetToggleLabel">See All</span>
              <svg id="sendSheetToggleChevron" class="w-3.5 h-3.5 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M5 15l7-7 7 7"/>
              </svg>
            </button>
          </div>

          <!-- Filter Pills (All / Cashleap Users / Bank IBAN) -->
          <div class="flex items-center gap-1.5">
            <button type="button" id="ben-filter-all" onclick="setBeneficiaryFilter('all')" class="px-3 py-1 rounded-full bg-blue-600/30 border border-blue-500/60 text-[10.5px] font-semibold text-white transition cursor-pointer">All Recipients</button>
            <button type="button" id="ben-filter-cashleap" onclick="setBeneficiaryFilter('cashleap')" class="px-3 py-1 rounded-full bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] hover:text-white transition cursor-pointer">Cashleap Users</button>
            <button type="button" id="ben-filter-iban" onclick="setBeneficiaryFilter('iban')" class="px-3 py-1 rounded-full bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] hover:text-white transition cursor-pointer">Bank IBAN</button>
          </div>
        </div>

        <!-- Scrollable Beneficiaries List -->
        <div id="sendBeneficiariesList" class="flex-1 overflow-y-auto px-5 pb-[420px] divide-y divide-white/[0.08] relative z-10 scrollbar-none">
          
          <!-- Beneficiary 1: Sarah Jenkins (Cashleap User) -->
          <div data-ben-type="cashleap" data-ben-search="sarah jenkins @sarah.j +971 50 842 1920" onclick="openSendToBeneficiary('sarah')" class="beneficiary-row py-3 flex items-center justify-between hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="relative flex-shrink-0">
                <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-indigo-600 to-blue-500 border border-white/20 flex items-center justify-center text-white font-bold text-xs">SJ</div>
                <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </span>
              </div>
              <div class="flex flex-col">
                <div class="flex items-center gap-1.5">
                  <span class="text-[14px] font-semibold text-white tracking-tight">Sarah Jenkins</span>
                  <span class="text-[9px] font-bold uppercase px-1.5 py-0.2 rounded bg-blue-500/20 border border-blue-400/30 text-blue-300">Cashleap</span>
                </div>
                <span class="text-[11px] text-[#9e94b8]">@sarah.j • +971 50 842 1920</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[11.5px] font-semibold text-blue-400">Send</span>
              <svg class="w-4 h-4 text-white/40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
            </div>
          </div>

          <!-- Beneficiary 2: Alex Rivera (Cashleap User) -->
          <div data-ben-type="cashleap" data-ben-search="alex rivera @alex.r +971 52 391 0488" onclick="openSendToBeneficiary('alex')" class="beneficiary-row py-3 flex items-center justify-between hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="relative flex-shrink-0">
                <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-500 border border-white/20 flex items-center justify-center text-white font-bold text-xs">AR</div>
                <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </span>
              </div>
              <div class="flex flex-col">
                <div class="flex items-center gap-1.5">
                  <span class="text-[14px] font-semibold text-white tracking-tight">Alex Rivera</span>
                  <span class="text-[9px] font-bold uppercase px-1.5 py-0.2 rounded bg-blue-500/20 border border-blue-400/30 text-blue-300">Cashleap</span>
                </div>
                <span class="text-[11px] text-[#9e94b8]">@alex.r • +971 52 391 0488</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[11.5px] font-semibold text-blue-400">Send</span>
              <svg class="w-4 h-4 text-white/40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
            </div>
          </div>

          <!-- Beneficiary 3: David Chen (Cashleap User) -->
          <div data-ben-type="cashleap" data-ben-search="david chen @david.c +971 55 901 2341" onclick="openSendToBeneficiary('david')" class="beneficiary-row py-3 flex items-center justify-between hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="relative flex-shrink-0">
                <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-purple-600 to-indigo-500 border border-white/20 flex items-center justify-center text-white font-bold text-xs">DC</div>
                <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </span>
              </div>
              <div class="flex flex-col">
                <div class="flex items-center gap-1.5">
                  <span class="text-[14px] font-semibold text-white tracking-tight">David Chen</span>
                  <span class="text-[9px] font-bold uppercase px-1.5 py-0.2 rounded bg-blue-500/20 border border-blue-400/30 text-blue-300">Cashleap</span>
                </div>
                <span class="text-[11px] text-[#9e94b8]">@david.c • +971 55 901 2341</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[11.5px] font-semibold text-blue-400">Send</span>
              <svg class="w-4 h-4 text-white/40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
            </div>
          </div>

          <!-- Beneficiary 4: Omar Al Maktoum (Cashleap User) -->
          <div data-ben-type="cashleap" data-ben-search="omar al maktoum @omar.m +971 50 112 7789" onclick="openSendToBeneficiary('omar')" class="beneficiary-row py-3 flex items-center justify-between hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="relative flex-shrink-0">
                <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-emerald-600 to-teal-500 border border-white/20 flex items-center justify-center text-white font-bold text-xs">OM</div>
                <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </span>
              </div>
              <div class="flex flex-col">
                <div class="flex items-center gap-1.5">
                  <span class="text-[14px] font-semibold text-white tracking-tight">Omar Al Maktoum</span>
                  <span class="text-[9px] font-bold uppercase px-1.5 py-0.2 rounded bg-blue-500/20 border border-blue-400/30 text-blue-300">Cashleap</span>
                </div>
                <span class="text-[11px] text-[#9e94b8]">@omar.m • +971 50 112 7789</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[11.5px] font-semibold text-blue-400">Send</span>
              <svg class="w-4 h-4 text-white/40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
            </div>
          </div>

          <!-- Beneficiary 5: Elena Rostova (Bank IBAN) -->
          <div data-ben-type="iban" data-ben-search="elena rostova emirates nbd ae4202600010158492019" onclick="openSendToBeneficiary('elena')" class="beneficiary-row py-3 flex items-center justify-between hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press">
            <div class="flex items-center gap-3.5">
              <div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white font-bold text-xs flex-shrink-0">ER</div>
              <div class="flex flex-col">
                <div class="flex items-center gap-1.5">
                  <span class="text-[14px] font-semibold text-white tracking-tight">Elena Rostova</span>
                  <span class="text-[9px] font-bold uppercase px-1.5 py-0.2 rounded bg-white/10 border border-white/15 text-[#9e94b8]">IBAN</span>
                </div>
                <span class="text-[11px] text-[#9e94b8]">Emirates NBD • AE42 •••• 2019</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[11.5px] font-semibold text-blue-400">Send</span>
              <svg class="w-4 h-4 text-white/40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
            </div>
          </div>

        </div>
      </div>

    </div>

    <!-- ======================================================== -->
    <!-- MODAL: ADD NEW BENEFICIARY / CASHLEAP USER               -->
    <!-- ======================================================== -->
    <div id="addBeneficiaryModal" onclick="if(event.target === this) closeAddBeneficiaryModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="addBeneficiarySheet" class="liquid-glass-sheet relative overflow-hidden w-full max-h-[88%] rounded-t-[34px] px-5 pt-3.5 pb-6 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col">
        <!-- Specular top highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Drag Handle & Header -->
        <div class="flex flex-col items-center mb-2.5 flex-shrink-0">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeAddBeneficiaryModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold tracking-tight text-white">Add Beneficiary</h3>
              <p class="text-[11px] text-[#9e94b8] mt-0.5">Add a Cashleap user (@leaptag) or bank IBAN</p>
            </div>
            <button onclick="closeAddBeneficiaryModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
        </div>

        <!-- Type Switcher: Cashleap User vs Bank IBAN -->
        <div class="grid grid-cols-2 gap-1.5 p-1 rounded-xl bg-white/[0.05] border border-white/10 mb-3 flex-shrink-0">
          <button type="button" id="ben-mode-cashleap" onclick="setAddBeneficiaryMode('cashleap')" class="py-2 rounded-lg bg-blue-600 text-white text-xs font-bold transition cursor-pointer flex items-center justify-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="4"/><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-3.92 7.94"/></svg>
            <span>Cashleap User</span>
          </button>
          <button type="button" id="ben-mode-iban" onclick="setAddBeneficiaryMode('iban')" class="py-2 rounded-lg text-[#9e94b8] hover:text-white text-xs font-semibold transition cursor-pointer flex items-center justify-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="22" x2="21" y2="22"/><polygon points="12 2 20 7 4 7"/><line x1="6" y1="18" x2="6" y2="11"/><line x1="10" y1="18" x2="10" y2="11"/><line x1="14" y1="18" x2="14" y2="11"/><line x1="18" y1="18" x2="18" y2="11"/></svg>
            <span>Bank IBAN</span>
          </button>
        </div>

        <!-- Scrollable Form -->
        <div class="overflow-y-auto flex-1 pr-0.5 space-y-3 scrollbar-none my-0.5">
          
          <!-- Cashleap User Lookup Field -->
          <div id="benCashleapFields" class="space-y-3">
            <div>
              <div class="flex items-center justify-between mb-1">
                <label class="text-[11px] font-semibold text-[#9e94b8]">Cashleap @leaptag or Mobile Number</label>
                <span id="benVerifyBadge" class="text-[10px] font-semibold text-emerald-400 flex items-center gap-1">
                  <svg class="w-3 h-3" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                  Verified User
                </span>
              </div>
              <div class="relative flex items-center">
                <span class="absolute left-3.5 text-xs font-bold text-blue-400">@</span>
                <input 
                  type="text" 
                  id="newBenLeapTagInput" 
                  value="khalid.mansoor" 
                  oninput="onBenLeapTagInput(this.value)"
                  class="w-full bg-white/[0.05] border border-white/15 rounded-xl pl-8 pr-20 py-2.5 text-xs font-mono text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 transition" 
                  placeholder="username or +971 50..." 
                />
                <button type="button" onclick="lookupCashleapUserTag()" class="absolute right-2 px-2.5 py-1 rounded-lg bg-blue-600/30 hover:bg-blue-600/45 border border-blue-400/40 text-[10px] font-semibold text-blue-200 transition cursor-pointer">
                  Lookup
                </button>
              </div>
            </div>

            <!-- Live Discovered Cashleap User Preview Card -->
            <div class="rounded-2xl bg-white/[0.04] border border-white/10 p-3 flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div id="newBenPreviewAvatar" class="w-10 h-10 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs">KM</div>
                <div>
                  <div class="flex items-center gap-1.5">
                    <span id="newBenPreviewName" class="text-xs font-bold text-white">Khalid Al Mansoor</span>
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                  </div>
                  <span id="newBenPreviewSub" class="text-[10.5px] text-[#9e94b8] block">@khalid.mansoor • Instant P2P</span>
                </div>
              </div>
              <span class="text-[9.5px] font-bold uppercase px-2 py-0.5 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-300">Zero Fee</span>
            </div>
          </div>

          <!-- Bank IBAN Fields (Hidden by default) -->
          <div id="benIbanFields" class="space-y-3 hidden">
            <div>
              <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1">UAE / International IBAN</label>
              <input 
                type="text" 
                id="newBenIbanInput" 
                value="AE07 0331 2345 6789 0123 456" 
                class="w-full bg-white/[0.05] border border-white/15 rounded-xl px-3.5 py-2.5 text-xs font-mono text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 tracking-wider transition" 
                placeholder="AE00 0000 0000 0000 0000 000" 
              />
            </div>
            <div>
              <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1.5">Select Receiving Bank</label>
              <div class="grid grid-cols-4 gap-1.5">
                <button type="button" onclick="selectBenBank(this, 'Emirates NBD')" class="ben-bank-pill py-1.5 px-2 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[10px] font-semibold text-white truncate cursor-pointer">ENBD</button>
                <button type="button" onclick="selectBenBank(this, 'ADCB Bank')" class="ben-bank-pill py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 text-[10px] font-medium text-[#9e94b8] truncate cursor-pointer">ADCB</button>
                <button type="button" onclick="selectBenBank(this, 'First Abu Dhabi')" class="ben-bank-pill py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 text-[10px] font-medium text-[#9e94b8] truncate cursor-pointer">FAB</button>
                <button type="button" onclick="selectBenBank(this, 'Mashreq Neo')" class="ben-bank-pill py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 text-[10px] font-medium text-[#9e94b8] truncate cursor-pointer">Mashreq</button>
              </div>
            </div>
          </div>

          <!-- Beneficiary Full Name Input -->
          <div>
            <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1">Recipient Full Name</label>
            <input 
              type="text" 
              id="newBenFullNameInput" 
              value="Khalid Al Mansoor" 
              oninput="onBenFullNameInput(this.value)"
              class="w-full bg-white/[0.05] border border-white/15 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-semibold transition" 
              placeholder="Enter recipient full name" 
            />
          </div>

          <!-- Relationship / Tag Preset Pills -->
          <div>
            <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1.5">Relationship Category</label>
            <div class="grid grid-cols-4 gap-2">
              <button type="button" onclick="selectBenRelation(this)" class="ben-rel-pill py-1.5 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[10.5px] font-semibold text-white transition cursor-pointer">Friend</button>
              <button type="button" onclick="selectBenRelation(this)" class="ben-rel-pill py-1.5 rounded-lg bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer">Family</button>
              <button type="button" onclick="selectBenRelation(this)" class="ben-rel-pill py-1.5 rounded-lg bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer">Business</button>
              <button type="button" onclick="selectBenRelation(this)" class="ben-rel-pill py-1.5 rounded-lg bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer">Rent / Services</button>
            </div>
          </div>

          <!-- Save & Add Beneficiary Submit Button -->
          <div class="grid grid-cols-2 gap-2.5 pt-1">
            <button type="button" onclick="confirmAddBeneficiary(false)" class="py-3 rounded-2xl bg-white/[0.08] hover:bg-white/[0.14] border border-white/15 text-white font-semibold text-xs transition cursor-pointer apple-press">
              Save Beneficiary
            </button>
            <button type="button" onclick="confirmAddBeneficiary(true)" class="py-3 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 text-white font-semibold text-xs transition cursor-pointer apple-press shadow-lg flex items-center justify-center gap-1.5">
              <span>Save & Send Now</span>
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
          </div>

        </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- MODAL: CREATE NEW SAVINGS VAULT (#createVaultModal)      -->
    <!-- ======================================================== -->
    <div id="createVaultModal" onclick="if(event.target === this) closeCreateVaultModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="createVaultSheet" class="liquid-glass-sheet relative overflow-hidden w-full max-h-[88%] rounded-t-[34px] px-5 pt-3.5 pb-6 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col">
        <!-- Specular top highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Drag Handle & Header -->
        <div class="flex flex-col items-center mb-2.5 flex-shrink-0">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeCreateVaultModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold tracking-tight text-white">Create Savings Vault</h3>
              <p class="text-[11px] text-[#9e94b8] mt-0.5">Earn daily compound yield up to 5.10% APY</p>
            </div>
            <button onclick="closeCreateVaultModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
        </div>

        <!-- Scrollable Form -->
        <div class="overflow-y-auto flex-1 pr-0.5 space-y-3.5 scrollbar-none my-0.5">
          
          <!-- Category Preset Selector -->
          <div>
            <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1.5">Vault Category</label>
            <div class="grid grid-cols-4 gap-2">
              <button type="button" id="vault-cat-travel" onclick="selectVaultCategory('Travel', 'Europe Summer Trip', '8000')" class="vault-cat-pill py-2 px-1.5 rounded-xl bg-blue-600/25 border border-blue-500/60 text-white text-[10.5px] font-semibold flex flex-col items-center gap-1 transition cursor-pointer">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/></svg>
                <span>Travel</span>
              </button>
              <button type="button" id="vault-cat-reserve" onclick="selectVaultCategory('Reserve', 'Rainy Day Fund', '10000')" class="vault-cat-pill py-2 px-1.5 rounded-xl bg-white/[0.04] border border-white/10 text-[#9e94b8] hover:text-white text-[10.5px] font-medium flex flex-col items-center gap-1 transition cursor-pointer">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                <span>Reserve</span>
              </button>
              <button type="button" id="vault-cat-tech" onclick="selectVaultCategory('Purchase', 'MacBook Pro M4', '9500')" class="vault-cat-pill py-2 px-1.5 rounded-xl bg-white/[0.04] border border-white/10 text-[#9e94b8] hover:text-white text-[10.5px] font-medium flex flex-col items-center gap-1 transition cursor-pointer">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                <span>Purchase</span>
              </button>
              <button type="button" id="vault-cat-wealth" onclick="selectVaultCategory('Wealth', 'Real Estate Deposit', '25000')" class="vault-cat-pill py-2 px-1.5 rounded-xl bg-white/[0.04] border border-white/10 text-[#9e94b8] hover:text-white text-[10.5px] font-medium flex flex-col items-center gap-1 transition cursor-pointer">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                <span>Wealth</span>
              </button>
            </div>
          </div>

          <!-- Vault Name Input -->
          <div>
            <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1">Vault Name</label>
            <input 
              type="text" 
              id="newVaultNameInput" 
              value="Europe Summer Trip" 
              class="w-full bg-white/[0.05] border border-white/15 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-semibold tracking-wide transition" 
              placeholder="e.g. Dream Car Deposit" 
            />
          </div>

          <!-- Target Goal & Initial Deposit in 2-Column Grid -->
          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1">Target Goal (AED)</label>
              <div class="relative flex items-center">
                <input 
                  type="number" 
                  id="newVaultTargetInput" 
                  value="8000" 
                  class="w-full bg-white/[0.05] border border-white/15 rounded-xl pl-3.5 pr-11 py-2.5 text-xs font-mono font-bold text-white focus:outline-none focus:border-blue-500 transition" 
                />
                <span class="absolute right-3 text-[10px] font-bold text-[#9e94b8]">AED</span>
              </div>
            </div>

            <div>
              <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1">Initial Deposit</label>
              <div class="relative flex items-center">
                <input 
                  type="number" 
                  id="newVaultInitialInput" 
                  value="1000" 
                  class="w-full bg-white/[0.05] border border-white/15 rounded-xl pl-3.5 pr-11 py-2.5 text-xs font-mono font-bold text-emerald-400 focus:outline-none focus:border-blue-500 transition" 
                />
                <span class="absolute right-3 text-[10px] font-bold text-[#9e94b8]">AED</span>
              </div>
            </div>
          </div>

          <!-- Yield Plan Selector -->
          <div>
            <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1.5">Yield Term & APY</label>
            <div class="grid grid-cols-2 gap-2.5">
              <button type="button" id="vault-term-flex" onclick="selectVaultTerm('flex')" class="p-2.5 rounded-xl bg-blue-600/20 border border-blue-500/60 text-left transition cursor-pointer">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-white">4.50% APY</span>
                  <span class="text-[9px] font-bold uppercase px-1.5 py-0.5 rounded bg-blue-500/30 text-blue-200">Flexible</span>
                </div>
                <span class="text-[10px] text-[#9e94b8] block mt-0.5">Withdraw anytime instantly</span>
              </button>
              <button type="button" id="vault-term-fixed" onclick="selectVaultTerm('fixed')" class="p-2.5 rounded-xl bg-white/[0.04] border border-white/10 text-left transition cursor-pointer">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-emerald-400">5.10% APY</span>
                  <span class="text-[9px] font-bold uppercase px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300">90-Day Lock</span>
                </div>
                <span class="text-[10px] text-[#9e94b8] block mt-0.5">Boosted fixed rate</span>
              </button>
            </div>
          </div>

          <!-- Funding Source Info Card -->
          <div class="rounded-2xl bg-white/[0.04] border border-white/10 p-3 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-6 rounded-md debit-card-gradient border border-white/20 flex items-center justify-center text-[8px] font-mono font-bold text-white">0329</div>
              <div>
                <span class="text-xs font-semibold text-white block leading-tight">Cashleap Mastercard</span>
                <span class="text-[10px] text-[#9e94b8]">Available: 3,350.60 AED</span>
              </div>
            </div>
            <span class="text-[10px] font-semibold text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded-full">Instant</span>
          </div>

          <!-- Submit Button -->
          <button onclick="confirmCreateVault()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 active:scale-98 text-white font-semibold text-xs transition cursor-pointer apple-press shadow-lg flex items-center justify-center gap-2">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            <span>Create & Fund Vault</span>
          </button>

        </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- MODAL: VAULT DEPOSIT & WITHDRAW (#vaultActionModal)      -->
    <!-- ======================================================== -->
    <div id="vaultActionModal" onclick="if(event.target === this) closeVaultActionModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="vaultActionSheet" class="liquid-glass-sheet relative overflow-hidden w-full max-h-[86%] rounded-t-[34px] px-5 pt-3.5 pb-6 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col">
        <!-- Specular top highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Drag Handle & Header -->
        <div class="flex flex-col items-center mb-2.5 flex-shrink-0">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeVaultActionModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 id="vaultActionModalTitle" class="text-[17px] font-bold tracking-tight text-white">Deposit to Vault</h3>
              <p id="vaultActionModalSub" class="text-[11px] text-[#9e94b8] mt-0.5">Instant transfer from Cashleap Mastercard (•••• 0329)</p>
            </div>
            <button onclick="closeVaultActionModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
        </div>

        <!-- Mode Switcher (Deposit vs Withdraw) -->
        <div class="grid grid-cols-2 gap-1.5 p-1 rounded-xl bg-white/[0.05] border border-white/10 mb-3">
          <button type="button" id="vault-mode-deposit" onclick="setVaultActionMode('deposit')" class="py-2 rounded-lg bg-blue-600 text-white text-xs font-bold transition cursor-pointer">
            Deposit Funds
          </button>
          <button type="button" id="vault-mode-withdraw" onclick="setVaultActionMode('withdraw')" class="py-2 rounded-lg text-[#9e94b8] hover:text-white text-xs font-semibold transition cursor-pointer">
            Withdraw to Card
          </button>
        </div>

        <!-- Select Target Vault Pills -->
        <div class="mb-3">
          <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1.5">Select Savings Vault</label>
          <div class="grid grid-cols-3 gap-1.5">
            <button type="button" id="vault-sel-emergency" onclick="selectTargetVault('emergency')" class="py-2 px-2 rounded-xl bg-blue-600/25 border border-blue-500/60 text-[10.5px] font-semibold text-white truncate transition cursor-pointer">
              Emergency Reserve
            </button>
            <button type="button" id="vault-sel-tokyo" onclick="selectTargetVault('tokyo')" class="py-2 px-2 rounded-xl bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] truncate transition cursor-pointer">
              Tokyo Vacation
            </button>
            <button type="button" id="vault-sel-gold" onclick="selectTargetVault('gold')" class="py-2 px-2 rounded-xl bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] truncate transition cursor-pointer">
              Gold Reserve
            </button>
          </div>
        </div>

        <!-- Selected Vault Balance Summary Box -->
        <div class="rounded-2xl bg-white/[0.04] border border-white/10 p-3 mb-3 flex items-center justify-between">
          <div>
            <span id="vaultSelectedNameLabel" class="text-xs font-bold text-white block">Emergency Reserve Vault</span>
            <span id="vaultSelectedApyLabel" class="text-[10.5px] text-emerald-400 font-medium">4.85% APY • Goal: 15,000 AED</span>
          </div>
          <div class="text-right">
            <span class="text-[10px] text-[#9e94b8] block">Current Balance</span>
            <span id="vaultSelectedBalLabel" class="text-sm font-extrabold text-white font-mono">12,000.00 AED</span>
          </div>
        </div>

        <!-- Amount Input & Preset Chips -->
        <div class="mb-4">
          <div class="flex items-center justify-between mb-1">
            <label class="text-[11px] font-semibold text-[#9e94b8]">Amount (AED)</label>
            <span class="text-[10.5px] text-blue-400 font-medium">Card Avail: 3,350.60 AED</span>
          </div>
          <div class="relative flex items-center mb-2">
            <input 
              type="number" 
              id="vaultActionAmountInput" 
              value="500.00" 
              class="w-full bg-white/[0.05] border border-white/15 rounded-2xl px-4 py-3 text-xl font-extrabold font-mono text-white focus:outline-none focus:border-blue-500 transition" 
            />
            <span class="absolute right-4 text-xs font-bold text-[#9e94b8]">AED</span>
          </div>
          <div class="grid grid-cols-4 gap-2">
            <button type="button" onclick="setVaultPresetAmount('100.00')" class="py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 text-[11px] font-semibold text-slate-300 transition cursor-pointer">+100</button>
            <button type="button" onclick="setVaultPresetAmount('250.00')" class="py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 text-[11px] font-semibold text-slate-300 transition cursor-pointer">+250</button>
            <button type="button" onclick="setVaultPresetAmount('500.00')" class="py-1.5 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[11px] font-semibold text-white transition cursor-pointer">+500</button>
            <button type="button" onclick="setVaultPresetAmount('1000.00')" class="py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 text-[11px] font-semibold text-slate-300 transition cursor-pointer">+1,000</button>
          </div>
        </div>

        <!-- Execute Button -->
        <button id="vaultActionSubmitBtn" onclick="executeVaultAction()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 active:scale-98 text-white font-semibold text-xs transition cursor-pointer apple-press shadow-lg flex items-center justify-center gap-2">
          <span>Confirm Instant Deposit</span>
        </button>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- MODAL: BILL PAY & UTILITIES (INTERACTIVE WALLET FEATURE) -->
    <!-- ======================================================== -->
    <div id="billPayModal" class="absolute inset-0 bg-black/85 backdrop-blur-xl z-50 opacity-0 pointer-events-none transition-opacity duration-300 flex flex-col justify-end">
      <div id="billPaySheet" class="w-full bg-[#141033] border-t border-white/20 rounded-t-[32px] p-6 text-white transform translate-y-full transition-transform duration-300 max-h-[85vh] overflow-y-auto">
        <div class="w-12 h-1 rounded-full bg-white/20 mx-auto mb-4 cursor-pointer" onclick="closeBillPayModal()"></div>
        <div class="flex items-center justify-between mb-4">
          <div>
            <h3 class="text-xl font-bold tracking-tight">Pay Bills & Utilities</h3>
            <span class="text-xs text-[#9d93b8]">Zero processing fees with Cashleap</span>
          </div>
          <button onclick="closeBillPayModal()" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-white cursor-pointer apple-press">✕</button>
        </div>

        <!-- Provider Selection Pills -->
        <div class="mb-4">
          <label class="text-xs text-[#9d93b8] font-medium block mb-2">Select Provider</label>
          <div class="grid grid-cols-3 gap-2">
            <button id="provider-dewa" onclick="selectBillProvider('DEWA Electricity & Water')" class="bill-provider-pill active py-2.5 px-2 rounded-xl bg-white/[0.08] border border-blue-400 text-center text-xs font-bold text-white transition apple-press">
              DEWA
            </button>
            <button id="provider-salik" onclick="selectBillProvider('Salik Toll Recharge')" class="bill-provider-pill py-2.5 px-2 rounded-xl bg-white/[0.04] border border-white/10 text-center text-xs font-semibold text-[#9d93b8] hover:text-white transition apple-press">
              Salik
            </button>
            <button id="provider-telecom" onclick="selectBillProvider('Du / Etisalat Mobile')" class="bill-provider-pill py-2.5 px-2 rounded-xl bg-white/[0.04] border border-white/10 text-center text-xs font-semibold text-[#9d93b8] hover:text-white transition apple-press">
              Telecom
            </button>
          </div>
        </div>

        <div class="space-y-3 mb-5">
          <div>
            <label id="billAccountLabel" class="text-xs text-[#9d93b8] font-medium block mb-1">DEWA Premise Number</label>
            <input id="billAccountInput" type="text" value="209-482-198" class="w-full bg-white/[0.06] border border-white/15 rounded-xl px-4 py-3 text-white text-sm font-mono focus:outline-none focus:border-blue-400" />
          </div>

          <div>
            <label class="text-xs text-[#9d93b8] font-medium block mb-1">Amount Due</label>
            <div class="relative">
              <input id="billAmountInput" type="number" value="285.50" class="w-full bg-white/[0.06] border border-white/15 rounded-xl px-4 py-3 text-white text-lg font-bold font-mono focus:outline-none focus:border-blue-400" />
              <span class="absolute right-4 top-3.5 text-xs font-bold text-[#9d93b8]">AED</span>
            </div>
          </div>
        </div>

        <button onclick="executeBillPayment()" class="w-full py-3.5 rounded-2xl bg-blue-600 hover:bg-blue-500 active:scale-[0.98] font-bold text-white text-[15px] shadow-lg shadow-blue-600/30 transition cursor-pointer apple-press">
          Confirm & Pay Bill
        </button>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- MODAL: SPLIT BILL / GROUP LEAP (INTERACTIVE WALLET)      -->
    <!-- ======================================================== -->
    <div id="splitBillModal" class="absolute inset-0 bg-black/85 backdrop-blur-xl z-50 opacity-0 pointer-events-none transition-opacity duration-300 flex flex-col justify-end">
      <div id="splitBillSheet" class="w-full bg-[#141033] border-t border-white/20 rounded-t-[32px] p-6 text-white transform translate-y-full transition-transform duration-300 max-h-[85vh] overflow-y-auto">
        <div class="w-12 h-1 rounded-full bg-white/20 mx-auto mb-4 cursor-pointer" onclick="closeSplitBillModal()"></div>
        <div class="flex items-center justify-between mb-4">
          <div>
            <h3 class="text-xl font-bold tracking-tight">Split Bill with Friends</h3>
            <span class="text-xs text-[#9d93b8]">Instant shareable payment link</span>
          </div>
          <button onclick="closeSplitBillModal()" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-white cursor-pointer apple-press">✕</button>
        </div>

        <div class="space-y-4 mb-5">
          <div>
            <label class="text-xs text-[#9d93b8] font-medium block mb-1">Total Bill Amount</label>
            <div class="relative">
              <input id="splitTotalInput" oninput="updateSplitCalculation()" type="number" value="340.00" class="w-full bg-white/[0.06] border border-white/15 rounded-xl px-4 py-3 text-white text-xl font-bold font-mono focus:outline-none focus:border-blue-400" />
              <span class="absolute right-4 top-3.5 text-xs font-bold text-[#9d93b8]">AED</span>
            </div>
          </div>

          <div>
            <label class="text-xs text-[#9d93b8] font-medium block mb-2">Split Between</label>
            <div class="grid grid-cols-4 gap-2">
              <button id="split-2" onclick="setSplitCount(2)" class="split-btn py-2 rounded-xl bg-white/[0.04] border border-white/10 text-center text-sm font-semibold text-[#9d93b8] hover:text-white transition apple-press">2 People</button>
              <button id="split-3" onclick="setSplitCount(3)" class="split-btn py-2 rounded-xl bg-white/[0.04] border border-white/10 text-center text-sm font-semibold text-[#9d93b8] hover:text-white transition apple-press">3 People</button>
              <button id="split-4" onclick="setSplitCount(4)" class="split-btn active py-2 rounded-xl bg-white/[0.08] border border-blue-400 text-center text-sm font-bold text-white transition apple-press">4 People</button>
              <button id="split-5" onclick="setSplitCount(5)" class="split-btn py-2 rounded-xl bg-white/[0.04] border border-white/10 text-center text-sm font-semibold text-[#9d93b8] hover:text-white transition apple-press">5 People</button>
            </div>
          </div>

          <!-- Per-person summary card -->
          <div class="rounded-2xl bg-white/[0.05] border border-white/10 p-4 flex items-center justify-between">
            <span class="text-xs text-[#9d93b8] font-medium">Each Person Pays</span>
            <div class="flex items-baseline">
              <span id="splitEachAmount" class="text-2xl font-black text-white font-mono tracking-tight">85.00</span>
              <span class="text-xs font-bold text-[#9d93b8] ml-1">AED</span>
            </div>
          </div>
        </div>

        <button onclick="generateSplitBillLink()" class="w-full py-3.5 rounded-2xl bg-blue-600 hover:bg-blue-500 active:scale-[0.98] font-bold text-white text-[15px] shadow-lg shadow-blue-600/30 transition cursor-pointer apple-press">
          Copy Split Leap Link
        </button>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- MODAL: DIGITAL GIFT VOUCHERS (INTERACTIVE WALLET)        -->
    <!-- ======================================================== -->
    <div id="giftCardsModal" onclick="if(event.target === this) closeGiftCardsModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none text-white select-none">
      <div id="giftCardsSheet" class="liquid-glass-sheet relative overflow-hidden w-full max-h-[92%] rounded-t-[34px] px-5 pt-3.5 pb-6 flex flex-col transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)]">
        
        <!-- Specular top highlight line -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Sheet Drag Handle & Header -->
        <div class="flex flex-col items-center mb-3 flex-shrink-0">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeGiftCardsModal()"></div>
          
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[19px] font-extrabold tracking-tight text-white leading-tight">Digital Brand Vouchers</h3>
              <p class="text-[11.5px] text-[#9e94b8] mt-0.5">Instant activation • 0.00 AED processing fee</p>
            </div>
            <button onclick="closeGiftCardsModal()" class="w-8 h-8 rounded-full bg-white/[0.08] hover:bg-white/[0.14] border border-white/10 flex items-center justify-center text-white/80 hover:text-white transition cursor-pointer apple-press" title="Close">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
        </div>

        <!-- Category Pills Filter Bar -->
        <div class="flex items-center gap-1.5 pb-3 overflow-x-auto scrollbar-none flex-shrink-0">
          <button type="button" onclick="filterVouchers('all')" data-voucher-cat="all" class="voucher-cat-pill px-3 py-1.5 rounded-full bg-blue-600/30 border border-blue-400/50 text-[11px] font-semibold text-white transition cursor-pointer flex-shrink-0">
            All (6)
          </button>
          <button type="button" onclick="filterVouchers('shopping')" data-voucher-cat="shopping" class="voucher-cat-pill px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/10 text-[11px] font-medium text-[#9e94b8] hover:text-white transition cursor-pointer flex-shrink-0">
            Shopping
          </button>
          <button type="button" onclick="filterVouchers('tech')" data-voucher-cat="tech" class="voucher-cat-pill px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/10 text-[11px] font-medium text-[#9e94b8] hover:text-white transition cursor-pointer flex-shrink-0">
            Tech & Apps
          </button>
          <button type="button" onclick="filterVouchers('gaming')" data-voucher-cat="gaming" class="voucher-cat-pill px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/10 text-[11px] font-medium text-[#9e94b8] hover:text-white transition cursor-pointer flex-shrink-0">
            Gaming
          </button>
          <button type="button" onclick="filterVouchers('entertainment')" data-voucher-cat="entertainment" class="voucher-cat-pill px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/10 text-[11px] font-medium text-[#9e94b8] hover:text-white transition cursor-pointer flex-shrink-0">
            Entertainment
          </button>
        </div>

        <!-- Scrollable Vouchers Grid (Premium Cards with Vector Logos & Glass Depth) -->
        <div id="voucherCardsGrid" class="flex-1 overflow-y-auto pr-0.5 space-y-2.5 pb-3 scrollbar-none">
          <div class="grid grid-cols-2 gap-2.5">
            
            <!-- 1. Apple Store -->
            <div onclick="purchaseGiftCard('Apple Store', 200)" data-voucher-cat="tech" class="voucher-card rounded-[22px] bg-gradient-to-b from-white/[0.07] to-white/[0.02] hover:from-white/[0.12] hover:to-white/[0.05] border border-white/15 p-3.5 flex flex-col justify-between cursor-pointer apple-press transition shadow-sm group">
              <div>
                <div class="flex items-start justify-between mb-3">
                  <div class="w-10 h-10 rounded-2xl bg-white/[0.10] border border-white/20 flex items-center justify-center text-white flex-shrink-0 shadow-inner group-hover:scale-105 transition-transform">
                    <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.37c.63-.78 1.06-1.85.95-2.93-.93.04-2.02.63-2.67 1.39-.58.67-.99 1.77-.85 2.82 1.05.08 2.08-.55 2.57-1.28z"/>
                    </svg>
                  </div>
                  <span class="text-[9.5px] font-bold text-blue-300 bg-blue-500/15 border border-blue-400/30 px-2 py-0.5 rounded-full flex-shrink-0">
                    Official
                  </span>
                </div>
                <h4 class="text-[14px] font-bold text-white tracking-tight leading-tight">Apple Store</h4>
                <p class="text-[11px] text-[#9e94b8] mt-0.5">Hardware & iCloud</p>
              </div>
              <div class="pt-3 border-t border-white/[0.08] mt-3 flex items-baseline justify-between">
                <span class="text-[15px] font-extrabold text-white font-mono">200.00 <span class="text-[10px] font-bold text-[#9e94b8]">AED</span></span>
                <span class="text-[10px] font-semibold text-emerald-400">+3% Pts</span>
              </div>
            </div>

            <!-- 2. Amazon UAE -->
            <div onclick="purchaseGiftCard('Amazon UAE', 100)" data-voucher-cat="shopping" class="voucher-card rounded-[22px] bg-gradient-to-b from-white/[0.07] to-white/[0.02] hover:from-white/[0.12] hover:to-white/[0.05] border border-white/15 p-3.5 flex flex-col justify-between cursor-pointer apple-press transition shadow-sm group">
              <div>
                <div class="flex items-start justify-between mb-3">
                  <div class="w-10 h-10 rounded-2xl bg-amber-500/15 border border-amber-400/30 flex items-center justify-center text-amber-300 flex-shrink-0 shadow-inner group-hover:scale-105 transition-transform">
                    <svg class="w-5 h-5 text-amber-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="9" cy="21" r="1"></circle>
                      <circle cx="20" cy="21" r="1"></circle>
                      <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                    </svg>
                  </div>
                  <span class="text-[9.5px] font-bold text-emerald-300 bg-emerald-500/15 border border-emerald-400/30 px-2 py-0.5 rounded-full flex-shrink-0">
                    5% Back
                  </span>
                </div>
                <h4 class="text-[14px] font-bold text-white tracking-tight leading-tight">Amazon UAE</h4>
                <p class="text-[11px] text-[#9e94b8] mt-0.5">Prime & Retail</p>
              </div>
              <div class="pt-3 border-t border-white/[0.08] mt-3 flex items-baseline justify-between">
                <span class="text-[15px] font-extrabold text-white font-mono">100.00 <span class="text-[10px] font-bold text-[#9e94b8]">AED</span></span>
                <span class="text-[10px] font-semibold text-amber-300">Prime</span>
              </div>
            </div>

            <!-- 3. PlayStation Store -->
            <div onclick="purchaseGiftCard('PlayStation Store', 120)" data-voucher-cat="gaming" class="voucher-card rounded-[22px] bg-gradient-to-b from-white/[0.07] to-white/[0.02] hover:from-white/[0.12] hover:to-white/[0.05] border border-white/15 p-3.5 flex flex-col justify-between cursor-pointer apple-press transition shadow-sm group">
              <div>
                <div class="flex items-start justify-between mb-3">
                  <div class="w-10 h-10 rounded-2xl bg-indigo-500/15 border border-indigo-400/30 flex items-center justify-center text-indigo-300 flex-shrink-0 shadow-inner group-hover:scale-105 transition-transform">
                    <svg class="w-5 h-5 text-indigo-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="6" width="20" height="12" rx="4"></rect>
                      <path d="M6 12h4m-2-2v4"></path>
                      <circle cx="15.5" cy="10.5" r="1" fill="currentColor"></circle>
                      <circle cx="17.5" cy="13.5" r="1" fill="currentColor"></circle>
                    </svg>
                  </div>
                  <span class="text-[9.5px] font-bold text-purple-300 bg-purple-500/15 border border-purple-400/30 px-2 py-0.5 rounded-full flex-shrink-0">
                    Gaming
                  </span>
                </div>
                <h4 class="text-[14px] font-bold text-white tracking-tight leading-tight">PlayStation</h4>
                <p class="text-[11px] text-[#9e94b8] mt-0.5">PS5, PSN & Plus</p>
              </div>
              <div class="pt-3 border-t border-white/[0.08] mt-3 flex items-baseline justify-between">
                <span class="text-[15px] font-extrabold text-white font-mono">120.00 <span class="text-[10px] font-bold text-[#9e94b8]">AED</span></span>
                <span class="text-[10px] font-semibold text-purple-300">PSN Code</span>
              </div>
            </div>

            <!-- 4. Noon Shopping -->
            <div onclick="purchaseGiftCard('Noon Shopping', 150)" data-voucher-cat="shopping" class="voucher-card rounded-[22px] bg-gradient-to-b from-white/[0.07] to-white/[0.02] hover:from-white/[0.12] hover:to-white/[0.05] border border-white/15 p-3.5 flex flex-col justify-between cursor-pointer apple-press transition shadow-sm group">
              <div>
                <div class="flex items-start justify-between mb-3">
                  <div class="w-10 h-10 rounded-2xl bg-yellow-500/15 border border-yellow-400/30 flex items-center justify-center text-yellow-300 flex-shrink-0 shadow-inner group-hover:scale-105 transition-transform">
                    <svg class="w-5 h-5 text-yellow-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
                      <line x1="3" y1="6" x2="21" y2="6"></line>
                      <path d="M16 10a4 4 0 0 1-8 0"></path>
                    </svg>
                  </div>
                  <span class="text-[9.5px] font-bold text-amber-300 bg-amber-500/15 border border-amber-400/30 px-2 py-0.5 rounded-full flex-shrink-0">
                    Express
                  </span>
                </div>
                <h4 class="text-[14px] font-bold text-white tracking-tight leading-tight">Noon Shopping</h4>
                <p class="text-[11px] text-[#9e94b8] mt-0.5">Electronics & Trends</p>
              </div>
              <div class="pt-3 border-t border-white/[0.08] mt-3 flex items-baseline justify-between">
                <span class="text-[15px] font-extrabold text-white font-mono">150.00 <span class="text-[10px] font-bold text-[#9e94b8]">AED</span></span>
                <span class="text-[10px] font-semibold text-emerald-400">Instant</span>
              </div>
            </div>

            <!-- 5. Spotify Premium -->
            <div onclick="purchaseGiftCard('Spotify Premium', 60)" data-voucher-cat="entertainment" class="voucher-card rounded-[22px] bg-gradient-to-b from-white/[0.07] to-white/[0.02] hover:from-white/[0.12] hover:to-white/[0.05] border border-white/15 p-3.5 flex flex-col justify-between cursor-pointer apple-press transition shadow-sm group">
              <div>
                <div class="flex items-start justify-between mb-3">
                  <div class="w-10 h-10 rounded-2xl bg-emerald-500/15 border border-emerald-400/30 flex items-center justify-center text-emerald-300 flex-shrink-0 shadow-inner group-hover:scale-105 transition-transform">
                    <svg class="w-5 h-5 text-emerald-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="12" cy="12" r="10"></circle>
                      <path d="M8 11.5c3-1 6-1 8 0"></path>
                      <path d="M7 14.5c3.5-1 7.5-1 10 0"></path>
                      <path d="M9 8.5c2.5-.8 5-.8 7 0"></path>
                    </svg>
                  </div>
                  <span class="text-[9.5px] font-bold text-emerald-300 bg-emerald-500/15 border border-emerald-400/30 px-2 py-0.5 rounded-full flex-shrink-0">
                    Audio
                  </span>
                </div>
                <h4 class="text-[14px] font-bold text-white tracking-tight leading-tight">Spotify Premium</h4>
                <p class="text-[11px] text-[#9e94b8] mt-0.5">3-Month Music Pass</p>
              </div>
              <div class="pt-3 border-t border-white/[0.08] mt-3 flex items-baseline justify-between">
                <span class="text-[15px] font-extrabold text-white font-mono">60.00 <span class="text-[10px] font-bold text-[#9e94b8]">AED</span></span>
                <span class="text-[10px] font-semibold text-emerald-400">Zero Fee</span>
              </div>
            </div>

            <!-- 6. Netflix Code -->
            <div onclick="purchaseGiftCard('Netflix', 75)" data-voucher-cat="entertainment" class="voucher-card rounded-[22px] bg-gradient-to-b from-white/[0.07] to-white/[0.02] hover:from-white/[0.12] hover:to-white/[0.05] border border-white/15 p-3.5 flex flex-col justify-between cursor-pointer apple-press transition shadow-sm group">
              <div>
                <div class="flex items-start justify-between mb-3">
                  <div class="w-10 h-10 rounded-2xl bg-rose-500/15 border border-rose-400/30 flex items-center justify-center text-rose-300 flex-shrink-0 shadow-inner group-hover:scale-105 transition-transform">
                    <svg class="w-5 h-5 text-rose-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="3" width="20" height="14" rx="2"></rect>
                      <line x1="8" y1="21" x2="16" y2="21"></line>
                      <line x1="12" y1="17" x2="12" y2="21"></line>
                    </svg>
                  </div>
                  <span class="text-[9.5px] font-bold text-rose-300 bg-rose-500/15 border border-rose-400/30 px-2 py-0.5 rounded-full flex-shrink-0">
                    Cinema
                  </span>
                </div>
                <h4 class="text-[14px] font-bold text-white tracking-tight leading-tight">Netflix Code</h4>
                <p class="text-[11px] text-[#9e94b8] mt-0.5">4K Ultra HD Movies</p>
              </div>
              <div class="pt-3 border-t border-white/[0.08] mt-3 flex items-baseline justify-between">
                <span class="text-[15px] font-extrabold text-white font-mono">75.00 <span class="text-[10px] font-bold text-[#9e94b8]">AED</span></span>
                <span class="text-[10px] font-semibold text-rose-300">Direct</span>
              </div>
            </div>

          </div>
        </div>

        <!-- Sleek Bottom Action Footer with Balance & Dismiss -->
        <div class="pt-3 flex-shrink-0">
          <div class="rounded-2xl bg-white/[0.04] border border-white/10 px-4 py-2.5 flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
              <span class="text-[11.5px] text-[#9e94b8]">Wallet Balance:</span>
              <span class="text-xs font-bold text-white font-mono">3,350.60 AED</span>
            </div>
            <span class="text-[11px] font-semibold text-blue-400">Instant Delivery</span>
          </div>
        </div>

      </div>
    </div>

    <!-- ======================================================== -->
    <!-- MODAL: LEAP REWARDS & CASHBACK (INTERACTIVE WALLET)      -->
    <!-- ======================================================== -->
    <div id="rewardsModal" class="absolute inset-0 bg-black/85 backdrop-blur-xl z-50 opacity-0 pointer-events-none transition-opacity duration-300 flex flex-col justify-end">
      <div id="rewardsSheet" class="w-full bg-[#141033] border-t border-white/20 rounded-t-[32px] p-6 text-white transform translate-y-full transition-transform duration-300 max-h-[85vh] overflow-y-auto">
        <div class="w-12 h-1 rounded-full bg-white/20 mx-auto mb-4 cursor-pointer" onclick="closeRewardsModal()"></div>
        <div class="flex items-center justify-between mb-4">
          <div>
            <h3 class="text-xl font-bold tracking-tight">LeapPoints Rewards</h3>
            <span class="text-xs text-[#9d93b8]">Your cashback tier and earned points</span>
          </div>
          <button onclick="closeRewardsModal()" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-white cursor-pointer apple-press">✕</button>
        </div>

        <div class="rounded-2xl bg-gradient-to-r from-purple-900/40 via-pink-900/30 to-blue-900/40 border border-white/15 p-4 mb-4">
          <div class="flex items-center justify-between mb-1">
            <span class="text-xs font-semibold text-[#9d93b8]">Available Rewards Points</span>
            <span class="text-[10px] font-bold text-[#ff2a6d] bg-[#ff2a6d]/15 px-2 py-0.5 rounded-full border border-[#ff2a6d]/30">Tier 2</span>
          </div>
          <div class="flex items-baseline">
            <span id="rewardsPointsBalance" class="text-3xl font-extrabold text-white tracking-tight">1,420</span>
            <span class="text-xs font-bold text-[#9d93b8] ml-1.5">PTS (= 142.00 AED)</span>
          </div>
        </div>

        <div class="space-y-2 mb-5 text-xs text-[#9d93b8]">
          <div class="flex items-center justify-between py-1.5 border-b border-white/[0.06]">
            <span>Card Cashback Rate</span>
            <span class="text-white font-bold">2.0% on All Swipes</span>
          </div>
          <div class="flex items-center justify-between py-1.5 border-b border-white/[0.06]">
            <span>Points Expiry</span>
            <span class="text-white font-bold">Never Expires</span>
          </div>
          <div class="flex items-center justify-between py-1.5">
            <span>Redemption Method</span>
            <span class="text-white font-bold">Instant Statement Credit</span>
          </div>
        </div>

        <button onclick="redeemRewardsPoints()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-[#ff2a6d] to-pink-600 hover:from-pink-500 hover:to-rose-600 active:scale-[0.98] font-bold text-white text-[15px] shadow-lg shadow-pink-600/30 transition cursor-pointer apple-press">
          Redeem 142.00 AED into Card
        </button>
      </div>
    </div>
    <div id="scannerModal" class="absolute inset-0 bg-black/92 backdrop-blur-2xl z-50 flex flex-col justify-between py-6 px-5 transition-opacity duration-300 opacity-0 pointer-events-none text-white select-none">
      
      <!-- Top Scanner Controls -->
      <div class="flex items-center justify-between pt-6 px-1">
        <button onclick="closeScannerModal()" class="w-10 h-10 rounded-full bg-white/15 hover:bg-white/25 flex items-center justify-center text-white transition apple-press">
          ✕
        </button>
        <span class="text-sm font-semibold tracking-tight text-white/90">Scan QR or Barcode</span>
        <button id="scannerTorchBtn" onclick="toggleScannerTorch()" class="w-10 h-10 rounded-full bg-white/15 hover:bg-white/25 flex items-center justify-center text-white transition apple-press" title="Toggle Flashlight">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
          </svg>
        </button>
      </div>

      <!-- Viewfinder Frame -->
      <div class="flex flex-col items-center my-auto">
        <div id="scannerFrame" class="relative w-[240px] h-[240px] rounded-3xl border border-white/20 flex items-center justify-center overflow-hidden bg-white/[0.02]">
          
          <!-- Corner Target Brackets -->
          <div class="absolute top-2 left-2 w-7 h-7 border-t-3 border-l-3 border-cyan-400 rounded-tl-xl transition-colors"></div>
          <div class="absolute top-2 right-2 w-7 h-7 border-t-3 border-r-3 border-cyan-400 rounded-tr-xl transition-colors"></div>
          <div class="absolute bottom-2 left-2 w-7 h-7 border-b-3 border-l-3 border-cyan-400 rounded-bl-xl transition-colors"></div>
          <div class="absolute bottom-2 right-2 w-7 h-7 border-b-3 border-r-3 border-cyan-400 rounded-br-xl transition-colors"></div>

          <!-- Animated Laser Scanning Line -->
          <div class="scanner-laser-line absolute left-3 right-3 h-[2.5px] bg-gradient-to-r from-cyan-400 via-blue-400 to-indigo-400 rounded-full shadow-[0_0_12px_#38bdf8]"></div>

          <!-- Subtle QR Silhouette Mock -->
          <div class="opacity-25 pointer-events-none">
            <svg width="110" height="110" viewBox="0 0 24 24" fill="currentColor">
              <path d="M3 3h8v8H3zm2 2v4h4V5zm8-2h8v8h-8zm2 2v4h4V5zM3 13h8v8H3zm2 2v4h4v-4zm13-2h3v3h-3zm-5 0h3v3h-3zm2 5h3v3h-3zm3 0h3v3h-3zm-5-3h3v3h-3zm5-5h3v3h-3z"/>
            </svg>
          </div>
        </div>

        <p class="text-xs text-white/70 font-medium mt-4 text-center max-w-[220px]">
          Align Cashleap or merchant QR code within the frame
        </p>
      </div>

      <!-- Bottom Actions -->
      <div class="flex flex-col gap-2.5 pb-2">
        <button onclick="simulateScanSuccess()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 text-white font-semibold text-xs tracking-wide transition apple-press flex items-center justify-center gap-2 shadow-lg">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
          Simulate Scan Detection
        </button>
        <button onclick="simulatePhotoScan()" class="w-full py-2.5 rounded-2xl bg-white/[0.08] hover:bg-white/[0.14] text-white/90 text-xs font-medium transition apple-press flex items-center justify-center gap-2">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>
          Upload from Photo Library
        </button>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- NOTIFICATIONS CENTER UI (APPLE STYLE)      -->
    <!-- ========================================== -->
    <div id="notificationsModal" onclick="if(event.target === this) closeNotificationsModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none text-white select-none">
      <div id="notificationsSheet" class="liquid-glass-sheet relative overflow-hidden w-full rounded-t-[34px] px-6 pt-5 pb-8 transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col gap-3.5 max-h-[82%]">
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Header & Unread Count -->
        <div class="flex flex-col items-center">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeNotificationsModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div class="flex items-center gap-2">
              <h3 class="text-[17px] font-bold tracking-tight text-white">Notifications</h3>
              <span id="notifCountBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-[#ff2a6d]/20 text-[#ff2a6d] border border-[#ff2a6d]/30">3 New</span>
            </div>
            <div class="flex items-center gap-2">
              <button onclick="markAllNotificationsRead()" class="text-xs text-blue-400 hover:text-blue-300 font-semibold transition cursor-pointer apple-press">
                Clear All
              </button>
              <button onclick="closeNotificationsModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">
                ✕
              </button>
            </div>
          </div>
        </div>

        <!-- Notifications Scroll List -->
        <div id="notifListContainer" class="space-y-2.5 overflow-y-auto max-h-[420px] scrollbar-none py-1">
          
          <!-- Item 1: Cashback -->
          <div onclick="dismissNotification(this, 'Starbucks Cashback')" class="notif-item p-3.5 rounded-2xl bg-white/[0.045] hover:bg-white/[0.08] active:bg-white/[0.1] border border-white/10 flex items-start gap-3 transition cursor-pointer apple-press relative">
            <div class="w-10 h-10 rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 font-bold text-sm flex-shrink-0">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/></svg>
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between">
                <span class="text-xs font-semibold text-white truncate">Cashback Credited (+15.50 AED)</span>
                <span class="text-[10px] text-slate-400">2m ago</span>
              </div>
              <p class="text-[11px] text-slate-300/90 leading-snug mt-0.5">
                Your reward from Starbucks Oat Flat White has been added to your Cashleap balance.
              </p>
            </div>
            <span class="notif-unread-dot w-2 h-2 rounded-full bg-[#ff2a6d] flex-shrink-0 mt-1"></span>
          </div>

          <!-- Item 2: Amazon Prime -->
          <div onclick="dismissNotification(this, 'Amazon Prime')" class="notif-item p-3.5 rounded-2xl bg-white/[0.045] hover:bg-white/[0.08] active:bg-white/[0.1] border border-white/10 flex items-start gap-3 transition cursor-pointer apple-press relative">
            <div class="w-10 h-10 rounded-full bg-[#00a8e1]/20 border border-[#00a8e1]/40 flex items-center justify-center text-[#00a8e1] font-bold text-xs flex-shrink-0">
              prime
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between">
                <span class="text-xs font-semibold text-white truncate">Payment Approved (-16.00 AED)</span>
                <span class="text-[10px] text-slate-400">1h ago</span>
              </div>
              <p class="text-[11px] text-slate-300/90 leading-snug mt-0.5">
                Amazon Prime Video monthly subscription renewed via Mastercard •••• 0329.
              </p>
            </div>
            <span class="notif-unread-dot w-2 h-2 rounded-full bg-[#ff2a6d] flex-shrink-0 mt-1"></span>
          </div>

          <!-- Item 3: Face ID Security -->
          <div onclick="dismissNotification(this, 'Face ID Verified')" class="notif-item p-3.5 rounded-2xl bg-white/[0.045] hover:bg-white/[0.08] active:bg-white/[0.1] border border-white/10 flex items-start gap-3 transition cursor-pointer apple-press relative">
            <div class="w-10 h-10 rounded-full bg-blue-500/20 border border-blue-500/40 flex items-center justify-center text-blue-400 font-bold text-sm flex-shrink-0">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between">
                <span class="text-xs font-semibold text-white truncate">Face ID Sign-in Successful</span>
                <span class="text-[10px] text-slate-400">3h ago</span>
              </div>
              <p class="text-[11px] text-slate-300/90 leading-snug mt-0.5">
                New login authenticated on iPhone 16 Pro (iOS 18.1).
              </p>
            </div>
            <span class="notif-unread-dot w-2 h-2 rounded-full bg-[#ff2a6d] flex-shrink-0 mt-1"></span>
          </div>

          <!-- Item 4: October Statement -->
          <div onclick="dismissNotification(this, 'Statement Ready')" class="notif-item p-3.5 rounded-2xl bg-white/[0.045] hover:bg-white/[0.08] active:bg-white/[0.1] border border-white/10 flex items-start gap-3 transition cursor-pointer apple-press relative opacity-75">
            <div class="w-10 h-10 rounded-full bg-purple-500/20 border border-purple-500/40 flex items-center justify-center text-purple-400 font-bold text-sm flex-shrink-0">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between">
                <span class="text-xs font-semibold text-white truncate">October Statement Ready</span>
                <span class="text-[10px] text-slate-400">Yesterday</span>
              </div>
              <p class="text-[11px] text-slate-300/90 leading-snug mt-0.5">
                Your monthly spending report is ready to review. Total 3,350.60 AED balance.
              </p>
            </div>
          </div>

        </div>

        <button onclick="closeNotificationsModal()" class="w-full py-3 rounded-2xl bg-white/[0.08] hover:bg-white/[0.14] text-white font-semibold text-xs transition apple-press">
          Done
        </button>
      </div>
    </div>

    <!-- Backdrop Dimmer for Recent Transactions Expansion -->
    <div id="sheetBackdrop" onclick="setSheetExpanded(false)" class="absolute inset-0 bg-black/60 backdrop-blur-[6px] z-15 opacity-0 pointer-events-none transition-opacity duration-300 ease-out"></div>

    <!-- ========================================== -->
    <!-- APPLE PAY TRANSACTION RECEIPT MODAL        -->
    <!-- ========================================== -->
    <div id="txDetailModal" onclick="if(event.target === this) closeTxDetail()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="txDetailSheet" class="liquid-glass-sheet relative overflow-hidden w-full rounded-t-[34px] px-6 pt-5 pb-8 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col gap-4">
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Sheet Handle & Close -->
        <div class="flex flex-col items-center">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeTxDetail()"></div>
          <div class="flex items-center justify-between w-full">
            <span class="text-xs uppercase tracking-wider font-semibold text-[#8c84aa]">Apple Pay Receipt</span>
            <button onclick="closeTxDetail()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">✕</button>
          </div>
        </div>

        <!-- Receipt Header -->
        <div class="flex flex-col items-center text-center mt-1">
          <div id="txDetailLogo" class="w-14 h-14 rounded-full flex items-center justify-center text-white mb-2.5 shadow-md">
            <!-- Dynamic Logo -->
          </div>
          <h3 id="txDetailName" class="text-[19px] font-bold tracking-tight text-white leading-tight">Merchant</h3>
          <p id="txDetailCategory" class="text-xs text-[#9d93b8] mt-0.5">Category</p>
          <div id="txDetailAmount" class="text-[32px] font-extrabold tracking-tight text-white mt-2 mb-1">-16.00 AED</div>
          <span class="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 text-[11px] font-semibold">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Completed
          </span>
        </div>

        <!-- Transaction Details Card -->
        <div class="bg-white/[0.045] border border-white/10 rounded-2xl p-3.5 space-y-2 text-xs">
          <div class="flex justify-between items-center text-[#9d93b8]">
            <span>Payment Method</span>
            <span id="txDetailCard" class="font-medium text-white">Cashleap Mastercard (•••• 0329)</span>
          </div>
          <div class="flex justify-between items-center text-[#9d93b8]">
            <span>Date & Time</span>
            <span id="txDetailTime" class="font-medium text-white">Today at 20:00</span>
          </div>
          <div class="flex justify-between items-center text-[#9d93b8]">
            <span>Reference ID</span>
            <span id="txDetailRef" class="font-mono text-white/90">TX-84920194</span>
          </div>
        </div>

        <!-- Actions -->
        <div class="flex flex-col gap-2 pt-1">
          <button onclick="repeatPaymentAction()" class="w-full py-3 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 active:scale-98 text-white font-semibold text-xs transition cursor-pointer apple-press">
            Repeat Transaction
          </button>
          <button onclick="downloadReceiptAction()" class="w-full py-2.5 rounded-2xl bg-white/[0.07] hover:bg-white/[0.12] active:scale-98 text-white/90 font-medium text-xs transition cursor-pointer apple-press flex items-center justify-center gap-1.5">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Download Apple Wallet PDF
          </button>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL: ADD FUNDS (APPLE PAY STYLE)         -->
    <!-- ========================================== -->
    <div id="addFundsModal" onclick="if(event.target === this) closeQuickActionModal('add')" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="addFundsSheet" class="liquid-glass-sheet relative overflow-hidden w-full rounded-t-[34px] px-6 pt-5 pb-8 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col gap-4">
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <div class="flex flex-col items-center">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeQuickActionModal('add')"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold tracking-tight text-white">Add to Cashleap</h3>
              <p class="text-xs text-[#9d93b8]">Instant Apple Pay deposit</p>
            </div>
            <button onclick="closeQuickActionModal('add')" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">✕</button>
          </div>
        </div>

        <!-- Deposit Amount Display -->
        <div class="flex flex-col items-center py-2 bg-white/[0.035] border border-white/10 rounded-2xl">
          <span class="text-xs text-[#8c84aa]">Deposit Amount</span>
          <div class="flex items-baseline gap-1 mt-1">
            <span class="text-[18px] font-bold text-white/70">+</span>
            <span id="addFundsValue" class="text-[34px] font-extrabold tracking-tight text-white">250.00</span>
            <span class="text-xs font-bold text-white/80">AED</span>
          </div>
        </div>

        <!-- Preset Chips -->
        <div class="grid grid-cols-4 gap-2">
          <button onclick="setAddAmount(50)" class="py-2 rounded-xl bg-white/[0.06] hover:bg-white/[0.12] active:bg-blue-600 font-semibold text-xs text-white border border-white/10 transition apple-press">+50</button>
          <button onclick="setAddAmount(100)" class="py-2 rounded-xl bg-white/[0.06] hover:bg-white/[0.12] active:bg-blue-600 font-semibold text-xs text-white border border-white/10 transition apple-press">+100</button>
          <button onclick="setAddAmount(250)" class="py-2 rounded-xl bg-blue-600/30 border border-blue-500/50 font-semibold text-xs text-blue-300 transition apple-press">+250</button>
          <button onclick="setAddAmount(500)" class="py-2 rounded-xl bg-white/[0.06] hover:bg-white/[0.12] active:bg-blue-600 font-semibold text-xs text-white border border-white/10 transition apple-press">+500</button>
        </div>

        <!-- Source Selector -->
        <div class="flex items-center justify-between p-3 rounded-xl bg-white/[0.04] border border-white/10">
          <div class="flex items-center gap-2.5">
            <div class="w-7 h-7 rounded-lg bg-black border border-white/20 flex items-center justify-center text-white text-[11px] font-bold">
              Pay
            </div>
            <div class="flex flex-col">
              <span class="text-xs font-semibold text-white">Apple Pay</span>
              <span class="text-[10px] text-slate-400">Default Payment Card</span>
            </div>
          </div>
          <span class="text-xs text-blue-400 font-medium cursor-pointer">Change</span>
        </div>

        <button onclick="confirmAddFunds()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 active:scale-98 text-white font-semibold text-xs transition cursor-pointer apple-press flex items-center justify-center gap-2 shadow-sm">
          <span>Deposit with Apple Pay</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
        </button>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL: SEND MONEY & BENEFICIARIES SHEET    -->
    <!-- ========================================== -->
    <div id="sendMoneyModal" onclick="if(event.target === this) closeQuickActionModal('send')" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="sendMoneySheet" class="liquid-glass-sheet relative overflow-hidden w-full max-h-[92%] rounded-t-[34px] px-6 pt-4 pb-7 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col">
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Sheet Drag Handle & Clean Header -->
        <div class="flex flex-col items-center mb-4 flex-shrink-0">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3.5 cursor-pointer transition-colors" onclick="closeQuickActionModal('send')"></div>
          <div class="w-full">
            <h3 class="text-[19px] font-bold tracking-tight text-white leading-tight">Send Money</h3>
            <p class="text-[12px] text-[#9d93b8] mt-1">Send to Cashleap users (@leaptag) or bank IBAN</p>
          </div>
        </div>

        <!-- Scrollable Sheet Body with Generous Premium Spacing -->
        <div class="overflow-y-auto flex-1 space-y-4 scrollbar-none pr-0.5">

          <!-- Cashleap Users & Beneficiaries Quick Strip + Search -->
          <div class="rounded-[22px] bg-white/[0.035] border border-white/10 p-4">
            <!-- Search Input -->
            <div class="relative flex items-center mb-3.5">
              <svg class="w-4 h-4 text-[#9e94b8] absolute left-3.5 pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
              <input 
                type="text" 
                id="sendSheetSearchInput" 
                oninput="filterSendSheetBeneficiaries(this.value)" 
                placeholder="Search @leaptag, Cashleap user, or IBAN..." 
                class="w-full bg-white/[0.05] border border-white/10 rounded-xl pl-9 pr-3.5 py-2.5 text-xs text-white placeholder-[#8e8ca8] focus:outline-none focus:border-blue-500 transition"
              />
            </div>

            <!-- Horizontal Cashleap Users Avatar Strip -->
            <div class="flex items-center justify-between mb-2.5">
              <span class="text-[10.5px] font-semibold uppercase tracking-wider text-[#9e94b8]">Cashleap Users & Saved (<span id="sendSheetCountBadge">5</span>)</span>
            </div>

            <div id="sendSheetAvatarsRow" class="flex items-center gap-3.5 overflow-x-auto pb-1 pt-0.5 scrollbar-none">
              <!-- + Add New Beneficiary -->
              <div onclick="openAddBeneficiaryModal('cashleap')" class="flex flex-col items-center gap-1.5 cursor-pointer apple-press flex-shrink-0">
                <div class="w-11 h-11 rounded-full bg-white/[0.05] hover:bg-white/[0.1] border border-dashed border-blue-400/60 flex items-center justify-center text-blue-400 transition">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
                    <line x1="12" y1="5" x2="12" y2="19"></line>
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                  </svg>
                </div>
                <span class="text-[10px] font-semibold text-blue-300">Add New</span>
              </div>

              <!-- User 1: Sarah -->
              <div onclick="selectSheetBeneficiary('sarah')" class="flex flex-col items-center gap-1.5 cursor-pointer apple-press flex-shrink-0">
                <div class="relative">
                  <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-indigo-600 to-blue-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs">SJ</div>
                  <span class="absolute -bottom-0.5 -right-0.5 z-20 w-3 h-3 rounded-full bg-emerald-400 border-2 border-[#161233]"></span>
                </div>
                <span class="text-[10px] text-white/90 font-medium truncate w-11 text-center">Sarah</span>
              </div>

              <!-- User 2: Alex -->
              <div onclick="selectSheetBeneficiary('alex')" class="flex flex-col items-center gap-1.5 cursor-pointer apple-press flex-shrink-0">
                <div class="relative">
                  <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs">AR</div>
                  <span class="absolute -bottom-0.5 -right-0.5 z-20 w-3 h-3 rounded-full bg-emerald-400 border-2 border-[#161233]"></span>
                </div>
                <span class="text-[10px] text-white/90 font-medium truncate w-11 text-center">Alex</span>
              </div>

              <!-- User 3: David -->
              <div onclick="selectSheetBeneficiary('david')" class="flex flex-col items-center gap-1.5 cursor-pointer apple-press flex-shrink-0">
                <div class="relative">
                  <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-purple-600 to-indigo-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs">DC</div>
                  <span class="absolute -bottom-0.5 -right-0.5 z-20 w-3 h-3 rounded-full bg-emerald-400 border-2 border-[#161233]"></span>
                </div>
                <span class="text-[10px] text-white/90 font-medium truncate w-11 text-center">David</span>
              </div>

              <!-- User 4: Omar -->
              <div onclick="selectSheetBeneficiary('omar')" class="flex flex-col items-center gap-1.5 cursor-pointer apple-press flex-shrink-0">
                <div class="relative">
                  <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-emerald-600 to-teal-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs">OM</div>
                  <span class="absolute -bottom-0.5 -right-0.5 z-20 w-3 h-3 rounded-full bg-emerald-400 border-2 border-[#161233]"></span>
                </div>
                <span class="text-[10px] text-white/90 font-medium truncate w-11 text-center">Omar</span>
              </div>

              <!-- User 5: Elena (IBAN) -->
              <div onclick="selectSheetBeneficiary('elena')" class="flex flex-col items-center gap-1.5 cursor-pointer apple-press flex-shrink-0">
                <div class="relative">
                  <div class="w-11 h-11 rounded-full bg-white/[0.08] border border-white/25 flex items-center justify-center text-white font-bold text-xs">ER</div>
                </div>
                <span class="text-[10px] text-white/90 font-medium truncate w-11 text-center">Elena</span>
              </div>
            </div>

            <!-- Search Filter Results List (Revealed when typing in search) -->
            <div id="sendSheetBeneficiariesPanel" class="hidden mt-3 pt-2.5 border-t border-white/10 max-h-[140px] overflow-y-auto divide-y divide-white/[0.06] scrollbar-none">
              <div data-sheet-ben-search="sarah jenkins @sarah.j +971 50 842 1920" onclick="selectSheetBeneficiary('sarah')" class="sheet-ben-row py-2.5 flex items-center justify-between hover:bg-white/[0.04] rounded-lg px-2 cursor-pointer transition">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-indigo-600 to-blue-500 flex items-center justify-center text-white font-bold text-[10px]">SJ</div>
                  <div class="flex flex-col">
                    <span class="text-xs font-semibold text-white">Sarah Jenkins</span>
                    <span class="text-[10.5px] text-[#9e94b8]">@sarah.j • Instant 0.00 AED Fee</span>
                  </div>
                </div>
              </div>

              <div data-sheet-ben-search="alex rivera @alex.r +971 52 391 0488" onclick="selectSheetBeneficiary('alex')" class="sheet-ben-row py-2.5 flex items-center justify-between hover:bg-white/[0.04] rounded-lg px-2 cursor-pointer transition">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-500 flex items-center justify-center text-white font-bold text-[10px]">AR</div>
                  <div class="flex flex-col">
                    <span class="text-xs font-semibold text-white">Alex Rivera</span>
                    <span class="text-[10.5px] text-[#9e94b8]">@alex.r • Instant 0.00 AED Fee</span>
                  </div>
                </div>
              </div>

              <div data-sheet-ben-search="david chen @david.c +971 55 901 2341" onclick="selectSheetBeneficiary('david')" class="sheet-ben-row py-2.5 flex items-center justify-between hover:bg-white/[0.04] rounded-lg px-2 cursor-pointer transition">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-600 to-indigo-500 flex items-center justify-center text-white font-bold text-[10px]">DC</div>
                  <div class="flex flex-col">
                    <span class="text-xs font-semibold text-white">David Chen</span>
                    <span class="text-[10.5px] text-[#9e94b8]">@david.c • Instant 0.00 AED Fee</span>
                  </div>
                </div>
              </div>

              <div data-sheet-ben-search="omar al maktoum @omar.m +971 50 112 7789" onclick="selectSheetBeneficiary('omar')" class="sheet-ben-row py-2.5 flex items-center justify-between hover:bg-white/[0.04] rounded-lg px-2 cursor-pointer transition">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white font-bold text-[10px]">OM</div>
                  <div class="flex flex-col">
                    <span class="text-xs font-semibold text-white">Omar Al Maktoum</span>
                    <span class="text-[10.5px] text-[#9e94b8]">@omar.m • Instant 0.00 AED Fee</span>
                  </div>
                </div>
              </div>

              <div data-sheet-ben-search="elena rostova emirates nbd ae4202600010158492019" onclick="selectSheetBeneficiary('elena')" class="sheet-ben-row py-2.5 flex items-center justify-between hover:bg-white/[0.04] rounded-lg px-2 cursor-pointer transition">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-white/[0.08] border border-white/20 flex items-center justify-center text-white font-bold text-[10px]">ER</div>
                  <div class="flex flex-col">
                    <span class="text-xs font-semibold text-white">Elena Rostova</span>
                    <span class="text-[10.5px] text-[#9e94b8]">Emirates NBD • AE42 •••• 2019</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Spacious Selected Recipient Card -->
          <div class="px-4 py-3.5 bg-white/[0.045] border border-white/10 rounded-[20px] flex items-center justify-between gap-3">
            <div class="flex items-center gap-3.5 min-w-0">
              <div id="sendRecipientAvatar" class="w-11 h-11 rounded-full bg-gradient-to-tr from-indigo-600 to-blue-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs flex-shrink-0">SJ</div>
              <div class="flex flex-col gap-0.5 min-w-0">
                <span id="sendRecipientName" class="text-[15px] font-bold text-white tracking-tight leading-snug truncate">Sarah Jenkins</span>
                <span id="sendRecipientHandle" class="text-[11.5px] text-[#9d93b8] leading-snug truncate">@sarah.j • Instant 0.00 AED Fee</span>
              </div>
            </div>
            <span id="sendRecipientBadge" class="flex-shrink-0 text-[9.5px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-blue-500/15 border border-blue-400/30 text-blue-300">Cashleap</span>
          </div>

          <!-- Amount Input -->
          <div>
            <div class="flex items-center justify-between mb-2 px-0.5">
              <label class="text-[11.5px] font-semibold text-[#9e94b8]">Transfer Amount</label>
              <span class="text-[11px] text-emerald-400 font-semibold">Avail: 3,350.60 AED</span>
            </div>
            <div class="relative flex items-center">
              <input 
                type="number" 
                id="sendMoneyAmountInput" 
                value="150.00" 
                class="w-full bg-white/[0.05] border border-white/15 rounded-[20px] px-4 py-3.5 text-xl font-extrabold font-mono text-white focus:outline-none focus:border-blue-500 transition" 
              />
              <span class="absolute right-4 text-xs font-bold text-[#9e94b8]">AED</span>
            </div>
          </div>

          <!-- Note / Reference Input -->
          <div>
            <input 
              type="text" 
              id="sendMoneyNoteInput" 
              placeholder="Add a note (e.g. Dinner split, rent, gift)..." 
              class="w-full bg-white/[0.04] border border-white/10 rounded-[18px] px-4 py-3 text-xs text-white placeholder-[#8e8ca8] focus:outline-none focus:border-blue-500 transition" 
            />
          </div>

          <!-- Animated "Slide to send" Interactive Slider -->
          <div class="pt-1">
            <div id="sendSliderTrack" onclick="completeSendSlideAnimation()" class="relative w-full h-[58px] rounded-full bg-[#110e2e]/90 border border-white/15 overflow-hidden flex items-center justify-between px-1.5 select-none cursor-pointer">
              <div id="sendSliderProgress" class="absolute left-0 top-0 bottom-0 bg-gradient-to-r from-blue-600/50 to-indigo-500/40 w-0 pointer-events-none transition-all duration-150"></div>
              <div id="sendSliderThumb" class="slide-send-thumb-idle w-11 h-11 rounded-full bg-gradient-to-r from-[#2d82ff] to-[#4f46e5] text-white flex items-center justify-center cursor-grab active:cursor-grabbing z-20 transition-transform duration-200 apple-press">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14M13 6l6 6-6 6"/>
                </svg>
              </div>
              <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                <span id="sendSliderLabel" class="slide-send-label text-[14px] font-semibold tracking-wide">
                  Slide to send
                </span>
              </div>
              <div id="sendSliderChevrons" class="flex items-center pr-4 pointer-events-none z-10 transition-opacity duration-200">
                <svg width="24" height="16" viewBox="0 0 28 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path class="chevron-1" d="M2 2L9 9L2 16" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                  <path class="chevron-2" d="M10 2L17 9L10 16" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                  <path class="chevron-3" d="M18 2L25 9L18 16" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL: WITHDRAW                            -->
    <!-- ========================================== -->
    <div id="withdrawModal" onclick="if(event.target === this) closeQuickActionModal('withdraw')" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="withdrawSheet" class="liquid-glass-sheet relative overflow-hidden w-full rounded-t-[34px] px-6 pt-5 pb-8 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col gap-4">
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <div class="flex flex-col items-center">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeQuickActionModal('withdraw')"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold tracking-tight text-white">ATM Cardless Cash</h3>
              <p class="text-xs text-[#9d93b8]">Instant withdrawal at any ATM</p>
            </div>
            <button onclick="closeQuickActionModal('withdraw')" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">✕</button>
          </div>
        </div>

        <div class="flex flex-col items-center py-4 bg-white/[0.035] border border-white/10 rounded-2xl">
          <span class="text-[11px] uppercase tracking-wider text-[#9d93b8]">One-Time ATM Security Code</span>
          <div class="text-[34px] font-mono font-bold tracking-[0.25em] text-white my-1">842 195</div>
          <span class="text-[11px] text-amber-400 font-medium">Expires in <span id="withdrawCountdown">14:59</span></span>
        </div>

        <div class="flex items-center justify-center p-3 bg-white/5 rounded-2xl">
          <div class="text-center text-xs text-white/80">
            Scan this code at any ATM screen or input the 6 digits to receive physical banknotes instantly.
          </div>
        </div>

        <button onclick="closeQuickActionModal('withdraw')" class="w-full py-3 rounded-2xl bg-white/[0.08] hover:bg-white/[0.14] text-white font-semibold text-xs transition apple-press">
          Done
        </button>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL: SCHEDULE                            -->
    <!-- ========================================== -->
    <div id="scheduleModal" onclick="if(event.target === this) closeQuickActionModal('schedule')" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="scheduleSheet" class="liquid-glass-sheet relative overflow-hidden w-full rounded-t-[34px] px-6 pt-5 pb-8 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col gap-3.5">
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <div class="flex flex-col items-center">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeQuickActionModal('schedule')"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold tracking-tight text-white">Scheduled Payments</h3>
              <p class="text-xs text-[#9d93b8]">Active Autopay & Subscriptions</p>
            </div>
            <button onclick="closeQuickActionModal('schedule')" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">✕</button>
          </div>
        </div>

        <div class="space-y-2 text-xs">
          <div class="flex items-center justify-between p-3 rounded-xl bg-white/[0.04] border border-white/10">
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-full bg-red-600 flex items-center justify-center font-black text-[9px] text-white">N</div>
              <div>
                <div class="font-semibold text-white">Netflix 4K UHD</div>
                <div class="text-[10px] text-slate-400">Due Nov 18 • 65.00 AED</div>
              </div>
            </div>
            <div onclick="toggleScheduleItem(this)" class="w-10 h-6 rounded-full bg-emerald-500 p-0.5 flex items-center justify-end cursor-pointer transition-colors apple-press">
              <div class="w-5 h-5 rounded-full bg-white shadow-sm"></div>
            </div>
          </div>

          <div class="flex items-center justify-between p-3 rounded-xl bg-white/[0.04] border border-white/10">
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-full bg-[#00a8e1] flex items-center justify-center font-bold text-[8px] text-white">prime</div>
              <div>
                <div class="font-semibold text-white">Amazon Prime</div>
                <div class="text-[10px] text-slate-400">Due Nov 22 • 16.00 AED</div>
              </div>
            </div>
            <div onclick="toggleScheduleItem(this)" class="w-10 h-6 rounded-full bg-emerald-500 p-0.5 flex items-center justify-end cursor-pointer transition-colors apple-press">
              <div class="w-5 h-5 rounded-full bg-white shadow-sm"></div>
            </div>
          </div>
        </div>

        <button onclick="closeQuickActionModal('schedule')" class="w-full py-3 rounded-2xl bg-white/[0.08] hover:bg-white/[0.14] text-white font-semibold text-xs transition apple-press">
          Close
        </button>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL: CARD DETAILS & CONTROLS             -->
    <!-- ========================================== -->
    <div id="cardDetailsModal" onclick="if(event.target === this) closeCardDetailsModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="cardDetailsSheet" class="liquid-glass-sheet relative overflow-hidden w-full rounded-t-[34px] px-6 pt-5 pb-8 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col gap-3.5">
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <div class="flex flex-col items-center">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeCardDetailsModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 id="cardDetailsTitle" class="text-[17px] font-bold tracking-tight text-white">Cashleap Mastercard</h3>
              <p id="cardDetailsSubtitle" class="text-xs text-[#9d93b8]">Card Controls & Apple Pay</p>
            </div>
            <button onclick="closeCardDetailsModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">✕</button>
          </div>
        </div>

        <div class="p-3.5 bg-white/[0.04] border border-white/10 backdrop-blur-md rounded-2xl flex items-center justify-between">
          <div>
            <div class="text-xs font-semibold text-white">Card Number</div>
            <div id="cardDetailsNum" class="text-sm font-mono tracking-widest text-slate-300 mt-0.5">5412 •••• •••• 0329</div>
          </div>
          <button onclick="copyCardNumber()" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/15 text-xs text-blue-400 font-semibold transition apple-press">
            Copy
          </button>
        </div>

        <div class="space-y-2 text-xs">
          <div class="flex items-center justify-between p-3 rounded-xl bg-white/[0.035] border border-white/10 backdrop-blur-md">
            <div>
              <div class="font-semibold text-white">Switch Active Card</div>
              <div class="text-[10px] text-slate-400">Select Debit Card or Balance Card</div>
            </div>
            <button onclick="closeCardDetailsModal(); openCardSelectionModal();" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/15 text-xs text-blue-400 font-semibold transition apple-press">
              Change
            </button>
          </div>
          <div class="flex items-center justify-between p-3 rounded-xl bg-white/[0.035] border border-white/10 backdrop-blur-md">
            <div>
              <div class="font-semibold text-white">Lock / Freeze Card</div>
              <div class="text-[10px] text-slate-400">Temporarily disable all transactions</div>
            </div>
            <div id="cardLockToggle" onclick="toggleCardLock(this)" class="w-10 h-6 rounded-full bg-white/20 p-0.5 flex items-center justify-start cursor-pointer transition-colors apple-press">
              <div class="w-5 h-5 rounded-full bg-white shadow-sm"></div>
            </div>
          </div>
          <div class="flex items-center justify-between p-3 rounded-xl bg-white/[0.035] border border-white/10 backdrop-blur-md">
            <div>
              <div class="font-semibold text-white">Contactless Apple Pay</div>
              <div class="text-[10px] text-slate-400">Ready for iPhone & Apple Watch</div>
            </div>
            <div class="w-10 h-6 rounded-full bg-emerald-500 p-0.5 flex items-center justify-end cursor-pointer transition-colors apple-press">
              <div class="w-5 h-5 rounded-full bg-white shadow-sm"></div>
            </div>
          </div>
        </div>

        <button onclick="closeCardDetailsModal()" class="w-full py-3 rounded-2xl bg-white/[0.08] hover:bg-white/[0.14] text-white font-semibold text-xs transition apple-press">
          Done
        </button>
      </div>
    </div>

<!-- ========================================== -->
        <!-- ========================================== -->
    <!-- ADD NEW PAYMENT CARD MODAL (LOGICAL FORM)  -->
    <!-- ========================================== -->
    <div id="addCardModal" onclick="if(event.target === this) closeAddCardModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="addCardSheet" class="liquid-glass-sheet relative overflow-hidden w-full max-h-[92%] rounded-t-[34px] px-5 pt-3.5 pb-6 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col">
        
        <!-- Specular top highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Sheet Drag Handle & Modal Header -->
        <div class="flex flex-col items-center mb-2.5 flex-shrink-0">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeAddCardModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold tracking-tight text-white">Add Payment Card</h3>
              <p class="text-[11px] text-[#9e94b8] mt-0.5">Enter your 16-digit card details to link to wallet</p>
            </div>
            <button onclick="closeAddCardModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
        </div>

        <!-- Scrollable Form with Live Card Preview -->
        <div class="overflow-y-auto flex-1 pr-0.5 space-y-3 scrollbar-none my-0.5">
          
          <!-- Live Interactive Card Preview -->
          <div id="newCardPreview" class="w-full h-[148px] rounded-[24px] p-4 flex flex-col justify-between text-white relative shadow-xl transition-all duration-300 overflow-hidden border border-white/15" style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 45%, #0f172a 100%);">
            <div class="flex items-center justify-between">
              <!-- EMV Chip & Contactless SVG -->
              <div class="flex items-center gap-2.5">
                <div class="w-8 h-6 rounded-md bg-gradient-to-br from-amber-200/90 via-yellow-400/80 to-amber-500/90 border border-white/30 flex items-center justify-center shadow-inner">
                  <div class="w-5 h-3.5 border border-amber-900/30 rounded-[2px] grid grid-cols-2"></div>
                </div>
                <svg class="w-4 h-4 text-white/70" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
                  <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z" class="hidden"/>
                  <path d="M6 9a6 6 0 0 1 0 6"/><path d="M9.5 7.5a9 9 0 0 1 0 9"/><path d="M13 6a12 12 0 0 1 0 12"/>
                </svg>
              </div>
              <div class="bg-black/35 backdrop-blur-md px-2.5 py-0.5 rounded-full border border-white/15 text-[9.5px] font-semibold text-white/90 tracking-wide">
                <span id="previewCardTypeBadge">Mastercard Debit</span>
              </div>
            </div>

            <div id="previewCardNumber" class="text-[15px] font-mono tracking-[0.18em] text-white font-semibold pt-1">
              5412  7512  3412  8821
            </div>

            <div class="flex items-center justify-between pt-0.5">
              <div>
                <span class="text-[6.5px] font-bold uppercase tracking-wider text-white/60 block">CARDHOLDER NAME</span>
                <span id="previewCardHolder" class="text-[11px] font-bold text-white tracking-wider">MARICE CERVANTES</span>
              </div>

              <div class="flex items-center gap-4">
                <div>
                  <span class="text-[6.5px] font-bold uppercase tracking-wider text-white/60 block">EXPIRES</span>
                  <span id="previewCardExpiry" class="text-[11px] font-bold text-white tracking-wider">08/28</span>
                </div>

                <!-- Mastercard Mark -->
                <div class="flex items-center">
                  <svg class="w-8 h-5" viewBox="0 0 38 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="13" cy="12" r="10.5" fill="#EB001B"/>
                    <circle cx="25" cy="12" r="10.5" fill="#F79E1B" fill-opacity="0.95"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- 1. Card Number Input (16 digits with auto-spacing & Scan button) -->
          <div>
            <div class="flex items-center justify-between mb-1">
              <label class="text-[11px] font-semibold text-[#9e94b8]">Card Number</label>
              <button type="button" onclick="simulateCardScanInModal()" class="text-[10.5px] font-semibold text-blue-400 hover:text-blue-300 flex items-center gap-1 transition cursor-pointer">
                <svg class="w-3 h-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8V5a1 1 0 0 1 1-1h3"/><path d="M4 16v3a1 1 0 0 0 1 1h3"/><path d="M16 4h3a1 1 0 0 1 1 1v3"/><path d="M16 20h3a1 1 0 0 0 1-1v-3"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
                Scan Card
              </button>
            </div>
            <div class="relative flex items-center">
              <svg class="w-4 h-4 text-[#9e94b8] absolute left-3.5 pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/>
              </svg>
              <input 
                type="text" 
                id="newCardNumberInput" 
                value="5412 7512 3412 8821" 
                maxlength="19"
                inputmode="numeric"
                oninput="formatCardNumberInput(this)" 
                class="w-full bg-white/[0.05] border border-white/15 rounded-xl pl-10 pr-10 py-2.5 text-xs font-mono text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 tracking-wider transition" 
                placeholder="0000 0000 0000 0000" 
              />
              <div class="absolute right-3 flex items-center pointer-events-none">
                <svg class="w-5 h-3.5" viewBox="0 0 38 24" fill="none">
                  <circle cx="13" cy="12" r="10.5" fill="#EB001B"/>
                  <circle cx="25" cy="12" r="10.5" fill="#F79E1B" fill-opacity="0.95"/>
                </svg>
              </div>
            </div>
          </div>

          <!-- 2. Cardholder Name Input -->
          <div>
            <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1">Cardholder Name</label>
            <div class="relative flex items-center">
              <svg class="w-4 h-4 text-[#9e94b8] absolute left-3.5 pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
              </svg>
              <input 
                type="text" 
                id="newCardNameInput" 
                value="Marice Cervantes" 
                oninput="updateNewCardPreview()" 
                class="w-full bg-white/[0.05] border border-white/15 rounded-xl pl-10 pr-3.5 py-2.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-medium tracking-wide transition" 
                placeholder="Name as shown on card" 
              />
            </div>
          </div>

          <!-- 3. Expiry Date (MM/YY) & Security Code (CVV) in 2-Column Grid -->
          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1">Expiry Date</label>
              <div class="relative flex items-center">
                <svg class="w-3.5 h-3.5 text-[#9e94b8] absolute left-3.5 pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
                <input 
                  type="text" 
                  id="newCardExpiryInput" 
                  value="08/28" 
                  maxlength="5"
                  inputmode="numeric"
                  oninput="formatCardExpiryInput(this)" 
                  class="w-full bg-white/[0.05] border border-white/15 rounded-xl pl-9 pr-3 py-2.5 text-xs font-mono text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 tracking-wider transition" 
                  placeholder="MM/YY" 
                />
              </div>
            </div>

            <div>
              <label class="text-[11px] font-semibold text-[#9e94b8] block mb-1">Security Code (CVV)</label>
              <div class="relative flex items-center">
                <svg class="w-3.5 h-3.5 text-[#9e94b8] absolute left-3.5 pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                </svg>
                <input 
                  type="password" 
                  id="newCardCvvInput" 
                  value="842" 
                  maxlength="4"
                  inputmode="numeric"
                  class="w-full bg-white/[0.05] border border-white/15 rounded-xl pl-9 pr-3 py-2.5 text-xs font-mono text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 tracking-widest transition" 
                  placeholder="•••" 
                />
              </div>
            </div>
          </div>

          <!-- 4. Compact Card Finish Row -->
          <div class="flex items-center justify-between pt-1 pb-0.5 px-0.5">
            <span class="text-[11px] font-semibold text-[#9e94b8]">Wallet Card Finish</span>
            <div class="flex items-center gap-2.5">
              <button type="button" onclick="setNewCardTheme('midnight')" id="theme-midnight" class="w-6 h-6 rounded-full border-2 border-white ring-2 ring-blue-400/50 shadow-sm transition transform scale-110 cursor-pointer" style="background: linear-gradient(135deg, #1e1b4b, #312e81);" title="Midnight Indigo"></button>
              <button type="button" onclick="setNewCardTheme('sunset')" id="theme-sunset" class="w-6 h-6 rounded-full border border-white/25 hover:scale-105 transition cursor-pointer" style="background: linear-gradient(135deg, #f59e0b, #ec4899);" title="Sunset Gold"></button>
              <button type="button" onclick="setNewCardTheme('emerald')" id="theme-emerald" class="w-6 h-6 rounded-full border border-white/25 hover:scale-105 transition cursor-pointer" style="background: linear-gradient(135deg, #059669, #0284c7);" title="Deep Teal"></button>
              <button type="button" onclick="setNewCardTheme('neon')" id="theme-neon" class="w-6 h-6 rounded-full border border-white/25 hover:scale-105 transition cursor-pointer" style="background: linear-gradient(135deg, #6d28d9, #4f46e5);" title="Royal Violet"></button>
            </div>
          </div>

          <!-- Submit Button (Clean Vector SVG, Zero Emojis) -->
          <button onclick="confirmAddNewCard()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 active:scale-98 text-white font-semibold text-xs transition cursor-pointer apple-press shadow-lg flex items-center justify-center gap-2 mt-1">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/>
            </svg>
            Link Card to Wallet
          </button>

        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- USER ACCOUNT & PROFILE MODAL               -->
    <!-- ========================================== -->
    <div id="userProfileModal" onclick="if(event.target === this) closeUserProfileModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="userProfileSheet" class="liquid-glass-sheet relative overflow-hidden w-full max-h-[88%] rounded-t-[34px] px-5 pt-3.5 pb-6 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col">
        
        <!-- Specular top highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Sheet Drag Handle & Header -->
        <div class="flex flex-col items-center mb-2 flex-shrink-0">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeUserProfileModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold tracking-tight text-white flex items-center gap-1.5">
                Account & Profile
                <span class="text-[9px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Verified</span>
              </h3>
              <p class="text-[11px] text-[#9e94b8] mt-0.5">Manage personal security, limits & wallet preferences</p>
            </div>
            <button onclick="closeUserProfileModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">
              ✕
            </button>
          </div>
        </div>

        <!-- Scrollable Profile Content -->
        <div class="overflow-y-auto flex-1 pr-0.5 space-y-3.5 scrollbar-none my-1">
          
          <!-- User Hero Card -->
          <div class="rounded-2xl bg-gradient-to-br from-white/[0.08] via-white/[0.04] to-transparent border border-white/15 p-3.5 backdrop-blur-xl relative overflow-hidden shadow-lg">
            <div class="flex items-center gap-3.5">
              <div class="w-14 h-14 rounded-full p-[2px] bg-gradient-to-tr from-amber-400 via-pink-500 to-cyan-400 shadow-md flex-shrink-0 relative">
                <img src="{avatar_b64}" alt="Marice Cervantes" class="w-full h-full rounded-full object-cover" />
                <div class="absolute -bottom-0.5 -right-0.5 z-20 w-4 h-4 rounded-full bg-emerald-400 border-2 border-[#120d2d] shadow-sm"></div>
              </div>
              <div class="flex flex-col flex-1">
                <div class="flex items-center justify-between">
                  <h4 class="text-[16px] font-extrabold text-white tracking-tight">Marice Cervantes</h4>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-gradient-to-r from-amber-500/20 to-yellow-500/20 border border-amber-400/40 text-amber-300">BLACK TIER</span>
                </div>
                <span class="text-[11px] text-[#9e94b8] mt-0.5">CustomerID: CL-8829-4102-AE</span>
                <div class="flex items-center gap-2 mt-1.5">
                  <span class="text-[10.5px] font-mono text-slate-300 bg-white/10 px-2 py-0.5 rounded-md truncate max-w-[190px]">AE07 0331 2345 6789 0123</span>
                  <button onclick="copyProfileIban()" class="text-[10px] text-blue-400 hover:text-blue-300 font-semibold cursor-pointer underline flex-shrink-0">Copy</button>
                </div>
              </div>
            </div>
          </div>

          <!-- 3-Stats Grid -->
          <div class="grid grid-cols-3 gap-2">
            <div class="rounded-xl bg-white/[0.04] border border-white/10 p-2.5 flex flex-col items-center text-center">
              <span class="text-[10px] text-[#9e94b8]">Total Net Worth</span>
              <span class="text-[13px] font-bold text-white mt-0.5">54,820 AED</span>
            </div>
            <div class="rounded-xl bg-white/[0.04] border border-white/10 p-2.5 flex flex-col items-center text-center">
              <span class="text-[10px] text-[#9e94b8]">Active Cards</span>
              <span id="profileCardsCountBadge" class="text-[13px] font-bold text-white mt-0.5">2 Cards</span>
            </div>
            <div class="rounded-xl bg-white/[0.04] border border-white/10 p-2.5 flex flex-col items-center text-center">
              <span class="text-[10px] text-[#9e94b8]">Safety Score</span>
              <span class="text-[13px] font-bold text-emerald-400 mt-0.5">99.8% (A+)</span>
            </div>
          </div>

          <!-- Contact & Residency -->
          <div class="rounded-2xl bg-white/[0.04] border border-white/10 p-3 flex flex-col gap-2">
            <span class="text-[11px] font-bold text-white/90 uppercase tracking-wider">Contact & Residency</span>
            <div class="flex items-center justify-between text-xs py-1 border-b border-white/[0.06]">
              <span class="text-[#9e94b8]">Email</span>
              <span class="text-white font-medium">marice.cervantes@cashleap.ae</span>
            </div>
            <div class="flex items-center justify-between text-xs py-1 border-b border-white/[0.06]">
              <span class="text-[#9e94b8]">Mobile Phone</span>
              <span class="text-white font-medium">+971 50 892 4102</span>
            </div>
            <div class="flex items-center justify-between text-xs py-1">
              <span class="text-[#9e94b8]">Residency</span>
              <span class="text-white font-medium">Dubai, United Arab Emirates</span>
            </div>
          </div>

          <!-- Security & Preferences -->
          <div class="rounded-2xl bg-white/[0.04] border border-white/10 p-3 flex flex-col gap-2.5">
            <span class="text-[11px] font-bold text-white/90 uppercase tracking-wider">Security & Biometrics</span>
            
            <div class="flex items-center justify-between py-1">
              <div class="flex flex-col">
                <span class="text-xs font-semibold text-white">Apple Face ID Login</span>
                <span class="text-[10px] text-[#9e94b8]">Biometric authentication for rapid unlocks</span>
              </div>
              <button onclick="toggleProfileFaceId()" id="profileFaceIdToggle" class="w-10 h-5 rounded-full bg-blue-600 transition-colors p-0.5 relative cursor-pointer">
                <div id="profileFaceIdKnob" class="w-4 h-4 rounded-full bg-white transition-transform transform translate-x-5"></div>
              </button>
            </div>

            <div class="flex items-center justify-between py-1 border-t border-white/[0.06]">
              <div class="flex flex-col">
                <span class="text-xs font-semibold text-white">6-Digit Secret Key</span>
                <span class="text-[10px] text-[#9e94b8]">High-security payment passcode</span>
              </div>
              <button onclick="triggerProfilePasscodeChange()" class="text-xs text-blue-400 hover:text-blue-300 font-semibold cursor-pointer">Manage</button>
            </div>

            <div class="flex items-center justify-between py-1 border-t border-white/[0.06]">
              <div class="flex flex-col">
                <span class="text-xs font-semibold text-white">Language / اللغة</span>
                <span id="profileLangSub" class="text-[10px] text-[#9e94b8]">Switch between English & Arabic</span>
              </div>
              <div class="flex items-center p-0.5 rounded-full bg-white/[0.08] border border-white/10">
                <button 
                  type="button" 
                  id="profileLangBtnEn" 
                  onclick="setAppLanguage('en')" 
                  class="px-2 py-0.5 rounded-full text-[10px] font-bold transition-all cursor-pointer bg-blue-600 text-white shadow-sm"
                >
                  EN
                </button>
                <button 
                  type="button" 
                  id="profileLangBtnAr" 
                  onclick="setAppLanguage('ar')" 
                  class="px-2 py-0.5 rounded-full text-[10px] font-medium text-[#9e94b8] hover:text-white transition-all cursor-pointer"
                >
                  عربي
                </button>
              </div>
            </div>
          </div>

          <!-- Limits & Statements -->
          <div class="rounded-2xl bg-white/[0.04] border border-white/10 p-3 flex flex-col gap-2">
            <span class="text-[11px] font-bold text-white/90 uppercase tracking-wider">Banking Limits</span>
            <div class="flex items-center justify-between text-xs py-1 border-b border-white/[0.06]">
              <span class="text-[#9e94b8]">Daily Transfer Cap</span>
              <span class="text-white font-semibold">50,000.00 AED</span>
            </div>
            <div class="flex items-center justify-between text-xs py-1 border-b border-white/[0.06]">
              <span class="text-[#9e94b8]">Monthly Spending Limit</span>
              <span class="text-white font-semibold">150,000.00 AED</span>
            </div>
            <button onclick="downloadOfficialStatement()" class="flex items-center justify-between py-1 text-xs text-cyan-400 hover:text-cyan-300 font-medium cursor-pointer">
              <span class="flex items-center gap-1.5"><svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><polyline points="9 15 12 18 15 15"/></svg>Download Official Statement (PDF)</span>
              <span>&rarr;</span>
            </button>
          </div>

          <!-- Sign Out Action -->
          <button onclick="closeUserProfileModal(); openSignOutConfirmation();" class="w-full py-3 rounded-2xl bg-rose-500/15 hover:bg-rose-500/25 border border-rose-500/30 text-rose-300 font-semibold text-xs flex items-center justify-center gap-2 transition cursor-pointer apple-press">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
            Sign Out of Cashleap
          </button>

        </div>
      </div>
    </div>

    <div id="selectCardModal" onclick="if(event.target === this) closeCardSelectionModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none">
      <div id="selectCardSheet" class="liquid-glass-sheet relative overflow-hidden w-full rounded-t-[34px] px-6 pt-5 pb-8 text-white transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)] flex flex-col gap-4">
        <!-- Liquid Glass Specular Top Highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Sheet Handle & Header -->
        <div class="flex flex-col items-center">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeCardSelectionModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold tracking-tight text-white">Select Debit Card</h3>
              <p class="text-xs text-slate-400 mt-0.5">Choose your active card for payments</p>
            </div>
            <button onclick="closeCardSelectionModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 text-xs transition cursor-pointer apple-press">
              ✕
            </button>
          </div>
        </div>

        <!-- Cards List -->
        <div class="space-y-2.5 my-1">
          
          <!-- Card 1 Option -->
          <div id="modal-card-opt-1" onclick="chooseModalCard(1)" class="flex items-center justify-between p-3 rounded-2xl border-2 border-blue-500 bg-blue-500/15 backdrop-blur-md transition cursor-pointer apple-press">
            <div class="flex items-center gap-3">
              <div class="w-12 h-8 rounded-lg debit-card-gradient flex items-center justify-center p-1 flex-shrink-0">
                <span class="text-[7.5px] font-bold text-white/90">0329</span>
              </div>
              <div class="flex flex-col">
                <div class="flex items-center gap-2">
                  <span class="text-sm font-semibold text-white leading-tight">Card Balance</span>
                  <span class="text-[10px] font-bold uppercase tracking-wider px-1.5 py-0.2 rounded bg-white/10 text-slate-300">Default</span>
                </div>
                <span class="text-xs text-slate-400 mt-0.5">3,350.60 AED • **** 0329</span>
              </div>
            </div>
            <div id="modal-radio-1" class="w-5 h-5 rounded-full border-2 border-blue-400 bg-blue-500 flex items-center justify-center text-white">
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
            </div>
          </div>

          <!-- Card 2 Option (The Uploaded PDF Debit Card) -->
          <div id="modal-card-opt-2" onclick="chooseModalCard(2)" class="flex items-center justify-between p-3 rounded-2xl border border-white/10 bg-white/[0.035] hover:bg-white/[0.08] backdrop-blur-md transition cursor-pointer apple-press">
            <div class="flex items-center gap-3">
              <div class="w-12 h-8 rounded-lg overflow-hidden flex-shrink-0">
                <img src="{card2_b64}" alt="Debit Card" class="w-full h-full object-cover" />
              </div>
              <div class="flex flex-col">
                <div class="flex items-center gap-2">
                  <span class="text-sm font-semibold text-white leading-tight">Debit Card</span>
                  <span class="text-[9.5px] font-bold uppercase tracking-wider px-1.5 py-0.2 rounded bg-pink-500/20 text-pink-300 border border-pink-500/30">Mastercard</span>
                </div>
                <span class="text-xs text-slate-400 mt-0.5">2,150.60 AED • **** 0319</span>
              </div>
            </div>
            <div id="modal-radio-2" class="w-5 h-5 rounded-full border-2 border-white/30 bg-transparent flex items-center justify-center text-transparent">
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
            </div>
          </div>

        </div>

        <!-- Confirm Action Button -->
        <button onclick="confirmCardSelection()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 active:scale-98 text-white font-semibold text-xs transition cursor-pointer apple-press mt-1">
          Select & Set as Active Card
        </button>

      </div>
    </div>

    <!-- ========================================== -->
    <!-- NATIVE iOS FACE ID FAILURE MODAL (image 6) -->
    <!-- ========================================== -->
    <!-- ======================================================== -->
    <!-- TRANSFER BETWEEN CARDS / ACCOUNTS MODAL (BESPOKE UI/UX)  -->
    <!-- ======================================================== -->
    <div id="transferModal" onclick="if(event.target === this) closeTransferModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none text-white select-none">
      <div id="transferSheet" class="liquid-glass-sheet relative overflow-hidden w-full rounded-t-[34px] px-5 pt-3.5 pb-6 flex flex-col max-h-[92%] transform translate-y-full transition-transform duration-350 ease-[cubic-bezier(0.32,0.72,0,1)]">
        
        <!-- Specular top highlight -->
        <div class="absolute top-0 left-8 right-8 h-[1px] bg-gradient-to-r from-transparent via-white/50 to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/[0.05] via-transparent to-transparent pointer-events-none"></div>

        <!-- Drag Handle & Header -->
        <div class="flex flex-col items-center mb-3 flex-shrink-0">
          <div class="w-11 h-1.5 bg-white/30 hover:bg-white/50 rounded-full mb-3 cursor-pointer transition-colors" onclick="closeTransferModal()"></div>
          <div class="flex items-center justify-between w-full">
            <div>
              <h3 class="text-[17px] font-bold text-white tracking-tight">Transfer Funds</h3>
              <p class="text-[11px] text-[#9e94b8] mt-0.5">Instant zero-fee transfer between your accounts</p>
            </div>
            <button onclick="closeTransferModal()" class="w-7 h-7 rounded-full bg-white/10 hover:bg-white/15 flex items-center justify-center text-slate-300 transition cursor-pointer apple-press">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
        </div>

        <div class="overflow-y-auto flex-1 pr-0.5 space-y-3 scrollbar-none">
          
          <!-- Connected From / Swap / To Account Stack -->
          <div class="relative space-y-2">
            
            <!-- FROM ACCOUNT CARD -->
            <div class="rounded-2xl bg-white/[0.04] border border-white/10 p-3 backdrop-blur-xl transition">
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10.5px] font-semibold uppercase tracking-wider text-[#9e94b8]">From Source</span>
                <span id="transferFromAvailBadge" class="text-[10.5px] font-medium text-emerald-400">Available: 3,350.60 AED</span>
              </div>

              <!-- Selected Source Display -->
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div id="transferFromCardArt" class="w-11 h-7 rounded-lg debit-card-gradient flex items-center justify-center p-1 shadow-sm flex-shrink-0 border border-white/20">
                    <span id="transferFromCardDigits" class="text-[8px] font-mono font-bold text-white">0329</span>
                  </div>
                  <div class="flex flex-col">
                    <span id="transferFromName" class="text-[13.5px] font-bold text-white leading-tight">Cashleap Mastercard</span>
                    <span id="transferFromSub" class="text-[11px] text-[#9e94b8] mt-0.5">Primary Wallet •••• 0329</span>
                  </div>
                </div>
                <div class="text-right">
                  <span id="transferFromBalance" class="text-[13px] font-bold text-white">3,350.60 AED</span>
                </div>
              </div>

              <!-- Quick Source Selector Pills -->
              <div class="grid grid-cols-3 gap-1.5 mt-2.5 pt-2 border-t border-white/[0.06]">
                <button type="button" onclick="selectTransferFrom('mastercard')" id="from-pill-mastercard" class="py-1.5 px-2 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[10.5px] font-semibold text-white transition cursor-pointer truncate">
                  Card •• 0329
                </button>
                <button type="button" onclick="selectTransferFrom('debit')" id="from-pill-debit" class="py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 hover:bg-white/[0.08] text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer truncate">
                  Debit •• 0319
                </button>
                <button type="button" onclick="selectTransferFrom('nbd')" id="from-pill-nbd" class="py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 hover:bg-white/[0.08] text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer truncate">
                  ENBD •• 8920
                </button>
              </div>
            </div>

            <!-- FLOATING SWAP ACCOUNTS BUTTON -->
            <div class="flex justify-center -my-3.5 relative z-20 pointer-events-none">
              <button 
                type="button" 
                onclick="swapTransferAccounts()" 
                id="transferSwapBtn"
                class="w-8 h-8 rounded-full bg-[#1b163c] hover:bg-[#251f52] border border-white/20 shadow-lg flex items-center justify-center text-blue-400 hover:text-white transition-all duration-300 cursor-pointer pointer-events-auto active:scale-90"
                title="Swap Source & Destination"
              >
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M7 16V4M7 4L3 8M7 4L11 8"/><path d="M17 8v12m0 0l4-4m-4 4l-4-4"/>
                </svg>
              </button>
            </div>

            <!-- TO DESTINATION ACCOUNT CARD -->
            <div class="rounded-2xl bg-white/[0.04] border border-white/10 p-3 backdrop-blur-xl transition">
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10.5px] font-semibold uppercase tracking-wider text-[#9e94b8]">To Destination</span>
                <span class="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-white/[0.06] text-slate-300">Instant Credit</span>
              </div>

              <!-- Selected Destination Display -->
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div id="transferToCardArt" class="w-11 h-7 rounded-lg bg-gradient-to-tr from-pink-500 via-purple-500 to-cyan-400 flex items-center justify-center p-1 shadow-sm flex-shrink-0 border border-white/20">
                    <span id="transferToCardDigits" class="text-[8px] font-mono font-bold text-white">0319</span>
                  </div>
                  <div class="flex flex-col">
                    <span id="transferToName" class="text-[13.5px] font-bold text-white leading-tight">Cashleap Debit</span>
                    <span id="transferToSub" class="text-[11px] text-[#9e94b8] mt-0.5">Secondary Card •••• 0319</span>
                  </div>
                </div>
                <div class="text-right">
                  <span id="transferToBalance" class="text-[13px] font-bold text-white">2,150.60 AED</span>
                </div>
              </div>

              <!-- Quick Destination Selector Pills -->
              <div class="grid grid-cols-3 gap-1.5 mt-2.5 pt-2 border-t border-white/[0.06]">
                <button type="button" onclick="selectTransferTo('debit')" id="to-pill-debit" class="py-1.5 px-2 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[10.5px] font-semibold text-white transition cursor-pointer truncate">
                  Debit •• 0319
                </button>
                <button type="button" onclick="selectTransferTo('mastercard')" id="to-pill-mastercard" class="py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 hover:bg-white/[0.08] text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer truncate">
                  Card •• 0329
                </button>
                <button type="button" onclick="selectTransferTo('vault')" id="to-pill-vault" class="py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 hover:bg-white/[0.08] text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer truncate">
                  Reserve Vault
                </button>
              </div>
            </div>

          </div>

          <!-- AMOUNT INPUT & PRESET CHIPS -->
          <div class="rounded-2xl bg-[#141033]/90 border border-white/12 p-3.5 backdrop-blur-xl shadow-inner">
            <div class="flex items-center justify-between mb-1.5">
              <span class="text-[11px] font-semibold text-[#9e94b8]">Transfer Amount</span>
              <span class="text-[10.5px] font-medium text-blue-400">No Transfer Fee</span>
            </div>

            <div class="flex items-baseline justify-between gap-2 pb-2.5 border-b border-white/[0.07]">
              <input 
                id="transferAmountInput" 
                type="number" 
                value="500.00" 
                step="50"
                class="w-full bg-transparent text-[26px] font-extrabold text-white tracking-tight outline-none leading-none" 
                placeholder="0.00"
              />
              <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-white/[0.08] text-white/90 tracking-wider flex-shrink-0">AED</span>
            </div>

            <!-- Preset Quick Amount Chips -->
            <div class="grid grid-cols-4 gap-1.5 pt-2.5">
              <button type="button" onclick="setTransferPresetAmount('100.00', this)" class="transfer-preset-chip py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 text-[11px] font-semibold text-slate-300 transition cursor-pointer">
                100
              </button>
              <button type="button" onclick="setTransferPresetAmount('250.00', this)" class="transfer-preset-chip py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 text-[11px] font-semibold text-slate-300 transition cursor-pointer">
                250
              </button>
              <button type="button" onclick="setTransferPresetAmount('500.00', this)" class="transfer-preset-chip py-1.5 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[11px] font-semibold text-white transition cursor-pointer">
                500
              </button>
              <button type="button" onclick="setTransferPresetAmount('1000.00', this)" class="transfer-preset-chip py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 text-[11px] font-semibold text-slate-300 transition cursor-pointer">
                1,000
              </button>
            </div>
          </div>

          <!-- Confirm Button -->
          <button onclick="executeTransfer()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 text-white font-semibold text-xs shadow-lg active:scale-[0.98] transition cursor-pointer apple-press flex items-center justify-center gap-2">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
            </svg>
            Confirm Instant Transfer
          </button>

        </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- CURRENCY EXCHANGE MODAL                                  -->
    <!-- ======================================================== -->
    <div id="exchangeModal" onclick="if(event.target === this) closeExchangeModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none text-white select-none">
      <div id="exchangeSheet" class="liquid-glass-sheet w-full rounded-t-[34px] p-5 flex flex-col max-h-[85%] transform translate-y-full transition-transform duration-400 ease-out">
        <div class="w-10 h-1 bg-white/30 rounded-full mx-auto mb-3 cursor-grab"></div>
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-[17px] font-bold text-white tracking-tight">Currency Exchange</h3>
          <button onclick="closeExchangeModal()" class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-white/80">✕</button>
        </div>

        <div class="bg-purple-500/10 border border-purple-500/20 rounded-xl p-2.5 mb-3 text-[11.5px] text-purple-300 flex items-center justify-between">
          <span>Live FX Rate: 1 USD = 3.6725 AED</span>
          <span class="text-[10px] text-emerald-400 font-bold">0% Commission</span>
        </div>

        <div class="space-y-2.5 mb-4">
          <div class="bg-white/[0.04] p-3 rounded-2xl border border-white/[0.08] flex items-center justify-between">
            <div>
              <span class="text-[10.5px] text-[#9e94b8] block">You Convert</span>
              <input id="exchangeFromInput" oninput="calculateExchange()" type="number" value="1000" class="w-32 bg-transparent text-[20px] font-extrabold text-white outline-none" />
            </div>
            <span class="text-sm font-bold px-3 py-1 bg-white/10 rounded-full">AED</span>
          </div>

          <div class="flex justify-center -my-2 relative z-10">
            <div class="w-7 h-7 rounded-full bg-[#181533] border border-white/20 flex items-center justify-center text-white text-xs">⇅</div>
          </div>

          <div class="bg-white/[0.04] p-3 rounded-2xl border border-white/[0.08] flex items-center justify-between">
            <div>
              <span class="text-[10.5px] text-[#9e94b8] block">You Receive</span>
              <span id="exchangeToOutput" class="text-[20px] font-extrabold text-emerald-400">272.29</span>
            </div>
            <span class="text-sm font-bold px-3 py-1 bg-white/10 rounded-full">USD</span>
          </div>
        </div>

        <button onclick="executeExchange()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-purple-600 to-pink-600 text-white font-bold text-sm shadow-lg active:scale-[0.98] transition apple-press">
          Convert to USD Now
        </button>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- LIVE SUPPORT CHAT MODAL                                  -->
    <!-- ======================================================== -->
    <div id="supportChatModal" onclick="if(event.target === this) closeSupportChat()" class="absolute inset-0 apple-sheet-backdrop z-50 flex flex-col justify-end transition-opacity duration-300 opacity-0 pointer-events-none text-white select-none">
      <div id="supportChatSheet" class="liquid-glass-sheet w-full rounded-t-[34px] p-4 flex flex-col h-[75%] transform translate-y-full transition-transform duration-400 ease-out">
        <div class="w-10 h-1 bg-white/30 rounded-full mx-auto mb-2 cursor-grab"></div>
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div class="flex items-center gap-2.5">
            <div class="w-9 h-9 rounded-full bg-gradient-to-tr from-cyan-400 to-blue-600 flex items-center justify-center font-bold text-sm shadow-sm">
              CL
            </div>
            <div>
              <h4 class="text-[14px] font-bold text-white leading-tight">Cashleap Concierge</h4>
              <span class="text-[11px] text-emerald-400 font-medium">● 24/7 Priority Support Agent</span>
            </div>
          </div>
          <button onclick="closeSupportChat()" class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-white/80">✕</button>
        </div>

        <div id="supportMessagesList" class="flex-1 overflow-y-auto py-3 space-y-2.5 text-[13px] scrollbar-none">
          <div class="flex justify-start">
            <div class="bg-white/10 rounded-2xl rounded-tl-sm px-3.5 py-2 max-w-[80%] text-white/90">
              Hello Marice! Welcome to Cashleap Priority Concierge. How can we assist you with your cards or account today?
            </div>
          </div>
        </div>

        <div class="flex items-center gap-2 pt-2 border-t border-white/10">
          <input id="supportChatInput" onkeydown="if(event.key==='Enter') sendSupportMessage()" placeholder="Type your message..." class="flex-1 bg-white/[0.06] border border-white/15 rounded-full px-4 py-2 text-sm text-white placeholder-white/40 outline-none" />
          <button onclick="sendSupportMessage()" class="w-9 h-9 rounded-full bg-blue-600 hover:bg-blue-500 flex items-center justify-center text-white shadow-md active:scale-95 transition">
            ➤
          </button>
        </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- SIGN OUT CONFIRMATION MODAL                              -->
    <!-- ======================================================== -->
    <div id="signOutModal" onclick="if(event.target === this) closeSignOutModal()" class="absolute inset-0 apple-sheet-backdrop z-50 flex items-center justify-center px-6 transition-opacity duration-300 opacity-0 pointer-events-none text-white select-none">
      <div class="liquid-glass-sheet w-full max-w-[320px] rounded-[28px] p-5 text-center shadow-2xl border border-white/15">
        <div class="w-12 h-12 rounded-full bg-rose-500/20 text-rose-400 flex items-center justify-center mx-auto mb-3">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
            <polyline points="16 17 21 12 16 7"></polyline>
            <line x1="21" y1="12" x2="9" y2="12"></line>
          </svg>
        </div>
        <h3 class="text-[17px] font-bold text-white mb-1">Sign Out?</h3>
        <p class="text-[12px] text-[#9e94b8] mb-4">You will need your biometric Face ID or 6-digit Secret Key to log back into Cashleap.</p>
        <div class="grid grid-cols-2 gap-2">
          <button onclick="closeSignOutModal()" class="py-2.5 rounded-xl bg-white/10 hover:bg-white/15 font-semibold text-xs text-white transition apple-press">
            Cancel
          </button>
          <button onclick="confirmSignOut()" class="py-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 font-bold text-xs text-white transition apple-press shadow-md">
            Sign Out
          </button>
        </div>
      </div>
    </div>\n\n

    <div id="iosFaceIdModal" class="absolute inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center px-8 transition-opacity duration-300 opacity-0 pointer-events-none">
      <div class="ios-modal-card w-full max-w-[280px] p-5 text-center flex flex-col items-center">
        <div class="w-12 h-12 rounded-full bg-red-500/15 border border-red-500/30 flex items-center justify-center text-red-400 mb-3">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
        </div>
        <h3 class="text-[17px] font-bold text-white tracking-tight">Face Not Recognized</h3>
        <p class="mt-1 text-xs text-slate-300 leading-normal">
          Try again or authenticate using your secret key.
        </p>
        <div class="w-full mt-4 space-y-2 border-t border-white/10 pt-3">
          <button 
            onclick="hideFaceIdFailureModal(); triggerFaceIdScan();" 
            class="w-full py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-xs transition cursor-pointer"
          >
            Try Face ID Again
          </button>
          <button 
            onclick="hideFaceIdFailureModal(); showScreen('secretkey');" 
            class="w-full py-2 rounded-xl bg-white/10 hover:bg-white/15 text-slate-300 font-medium text-xs transition cursor-pointer"
          >
            Enter Secret Key
          </button>
          <button 
            onclick="hideFaceIdFailureModal()" 
            class="w-full py-1 text-slate-400 hover:text-white text-xs transition cursor-pointer"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- TAB NAVIGATION SKELETON GRADIENT LOADING SCREEN          -->
    <!-- ======================================================== -->
    <div 
      id="tabSkeletonOverlay" 
      class="absolute inset-0 home-bg z-[38] flex flex-col justify-between pt-4 pb-0 px-0 overflow-hidden select-none pointer-events-none opacity-0"
      aria-hidden="true"
    >
      <!-- Upper Section Skeleton -->
      <div class="w-full px-4 pt-1 flex-shrink-0">
        <!-- Top Capsule Header Bar Shimmer -->
        <div class="w-full rounded-full bg-white/[0.035] px-3 py-1.5 flex items-center justify-between mb-3">
          <div class="flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-full skeleton-shimmer"></div>
            <div class="flex flex-col gap-1.5">
              <div class="w-10 h-2 rounded-full skeleton-shimmer"></div>
              <div class="w-24 h-3 rounded-full skeleton-shimmer"></div>
            </div>
          </div>
          <div class="flex items-center gap-1.5">
            <div class="w-7 h-7 rounded-full skeleton-shimmer"></div>
            <div class="w-7 h-7 rounded-full skeleton-shimmer"></div>
          </div>
        </div>

        <!-- 1. HOME TAB HERO SKELETON -->
        <div id="skelHeroHome" class="space-y-3">
          <div class="w-full h-[178px] rounded-[28px] skeleton-card-shimmer p-5 flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <div class="space-y-2">
                <div class="w-20 h-2.5 rounded-full skeleton-shimmer"></div>
                <div class="w-36 h-7 rounded-xl skeleton-shimmer"></div>
              </div>
              <div class="w-14 h-5 rounded-full skeleton-shimmer"></div>
            </div>
            <div class="w-48 h-3.5 rounded-full skeleton-shimmer"></div>
            <div class="flex items-center justify-between">
              <div class="w-16 h-3 rounded-full skeleton-shimmer"></div>
              <div class="w-9 h-5 rounded-full skeleton-shimmer"></div>
            </div>
          </div>
          <div class="flex justify-center gap-1.5 pt-0.5">
            <div class="w-6 h-1 rounded-full skeleton-shimmer"></div>
            <div class="w-3.5 h-1 rounded-full skeleton-shimmer"></div>
            <div class="w-3.5 h-1 rounded-full skeleton-shimmer"></div>
          </div>
          <div class="grid grid-cols-4 gap-3 px-2 pt-1">
            <div class="flex flex-col items-center gap-1.5"><div class="w-12 h-12 rounded-full skeleton-shimmer"></div><div class="w-8 h-2 rounded-full skeleton-shimmer"></div></div>
            <div class="flex flex-col items-center gap-1.5"><div class="w-12 h-12 rounded-full skeleton-shimmer"></div><div class="w-8 h-2 rounded-full skeleton-shimmer"></div></div>
            <div class="flex flex-col items-center gap-1.5"><div class="w-12 h-12 rounded-full skeleton-shimmer"></div><div class="w-10 h-2 rounded-full skeleton-shimmer"></div></div>
            <div class="flex flex-col items-center gap-1.5"><div class="w-12 h-12 rounded-full skeleton-shimmer"></div><div class="w-10 h-2 rounded-full skeleton-shimmer"></div></div>
          </div>
        </div>

        <!-- 2. FINANCE TAB HERO SKELETON -->
        <div id="skelHeroFinance" class="hidden space-y-3">
          <div class="py-1.5"><div class="w-36 h-6 rounded-xl skeleton-shimmer"></div></div>
          <div class="w-full h-[188px] rounded-[24px] skeleton-card-shimmer p-4 flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <div class="space-y-2">
                <div class="w-24 h-2.5 rounded-full skeleton-shimmer"></div>
                <div class="w-40 h-7 rounded-xl skeleton-shimmer"></div>
              </div>
              <div class="w-16 h-6 rounded-full skeleton-shimmer"></div>
            </div>
            <div class="grid grid-cols-2 gap-2.5 pt-2">
              <div class="h-12 rounded-xl skeleton-shimmer"></div>
              <div class="h-12 rounded-xl skeleton-shimmer"></div>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-1">
              <div class="h-8 rounded-xl skeleton-shimmer"></div>
              <div class="h-8 rounded-xl skeleton-shimmer"></div>
            </div>
          </div>
        </div>

        <!-- 3. STATISTICS TAB HERO SKELETON -->
        <div id="skelHeroStatistics" class="hidden space-y-3">
          <div class="py-1.5"><div class="w-40 h-6 rounded-xl skeleton-shimmer"></div></div>
          <div class="w-full h-[212px] rounded-[22px] skeleton-card-shimmer p-4 flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <div class="space-y-2">
                <div class="w-24 h-2.5 rounded-full skeleton-shimmer"></div>
                <div class="w-36 h-6 rounded-xl skeleton-shimmer"></div>
              </div>
              <div class="flex gap-2">
                <div class="w-5 h-4 rounded skeleton-shimmer"></div>
                <div class="w-5 h-4 rounded skeleton-shimmer"></div>
                <div class="w-5 h-4 rounded skeleton-shimmer"></div>
                <div class="w-5 h-4 rounded skeleton-shimmer"></div>
              </div>
            </div>
            <div class="w-full h-[96px] rounded-xl skeleton-shimmer"></div>
            <div class="flex justify-between pt-1">
              <div class="w-7 h-3 rounded-full skeleton-shimmer"></div>
              <div class="w-7 h-3 rounded-full skeleton-shimmer"></div>
              <div class="w-7 h-3 rounded-full skeleton-shimmer"></div>
              <div class="w-7 h-3 rounded-full skeleton-shimmer"></div>
              <div class="w-10 h-4 rounded-full skeleton-shimmer"></div>
              <div class="w-7 h-3 rounded-full skeleton-shimmer"></div>
              <div class="w-7 h-3 rounded-full skeleton-shimmer"></div>
            </div>
          </div>
        </div>

        <!-- 4. OTHERS TAB HERO SKELETON -->
        <div id="skelHeroOthers" class="hidden space-y-3">
          <div class="py-1.5"><div class="w-36 h-6 rounded-xl skeleton-shimmer"></div></div>
          <div class="w-full h-[185px] rounded-[24px] skeleton-card-shimmer p-4 flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <div class="space-y-2">
                <div class="w-28 h-3 rounded-full skeleton-shimmer"></div>
                <div class="w-44 h-5 rounded-lg skeleton-shimmer"></div>
              </div>
              <div class="w-10 h-10 rounded-2xl skeleton-shimmer"></div>
            </div>
            <div class="grid grid-cols-2 gap-2.5 pt-2">
              <div class="h-16 rounded-2xl skeleton-shimmer"></div>
              <div class="h-16 rounded-2xl skeleton-shimmer"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Sheet Skeleton (Borderless) -->
      <div class="bg-[#161136]/85 backdrop-blur-2xl w-full h-[380px] rounded-t-[34px] px-5 pt-3.5 pb-24 flex flex-col gap-3.5">
        <div class="w-11 h-1.5 rounded-full bg-white/15 mx-auto"></div>
        <div class="flex items-center justify-between pb-1">
          <div class="w-28 h-4 rounded-full skeleton-shimmer"></div>
          <div class="w-14 h-3 rounded-full skeleton-shimmer"></div>
        </div>
        <div class="space-y-3.5 pt-1">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full skeleton-shimmer flex-shrink-0"></div>
              <div class="space-y-2"><div class="w-28 h-3.5 rounded-full skeleton-shimmer"></div><div class="w-16 h-2.5 rounded-full skeleton-shimmer"></div></div>
            </div>
            <div class="w-20 h-4 rounded-full skeleton-shimmer"></div>
          </div>
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full skeleton-shimmer flex-shrink-0"></div>
              <div class="space-y-2"><div class="w-32 h-3.5 rounded-full skeleton-shimmer"></div><div class="w-20 h-2.5 rounded-full skeleton-shimmer"></div></div>
            </div>
            <div class="w-24 h-4 rounded-full skeleton-shimmer"></div>
          </div>
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full skeleton-shimmer flex-shrink-0"></div>
              <div class="space-y-2"><div class="w-24 h-3.5 rounded-full skeleton-shimmer"></div><div class="w-16 h-2.5 rounded-full skeleton-shimmer"></div></div>
            </div>
            <div class="w-20 h-4 rounded-full skeleton-shimmer"></div>
          </div>
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full skeleton-shimmer flex-shrink-0"></div>
              <div class="space-y-2"><div class="w-28 h-3.5 rounded-full skeleton-shimmer"></div><div class="w-14 h-2.5 rounded-full skeleton-shimmer"></div></div>
            </div>
            <div class="w-18 h-4 rounded-full skeleton-shimmer"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- GLOBAL PERSISTENT FOOTER TAB MENU (1 Single Dock)        -->
    <!-- ======================================================== -->
    <nav 
      id="globalBottomNav" 
      class="pill-bottom-nav nav-hidden select-none" 
      aria-label="Main Navigation"
    >
      <div class="grid grid-cols-4 h-full relative">
        
        <!-- 1. Home Tab -->
        <div id="dock-tab-home" onclick="selectDockTab('home')" class="dock-tab active">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.707 2.293a1 1 0 0 1 1.414 0l7 7A1 1 0 0 1 19.414 11H19v9a1 1 0 0 1-1 1h-3a1 1 0 0 1-1-1v-4a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v4a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-9h-.414a1 1 0 0 1-.707-1.707l7-7Z" fill="currentColor"/>
            <path d="M16 3h2v4.5l-2-2V3Z" fill="currentColor"/>
          </svg>
          <span class="text-[12px] font-semibold tracking-tight text-white">Home</span>
          <div id="bar-home" class="dock-active-bar"></div>
        </div>

        <!-- 2. Finance Tab -->
        <div id="dock-tab-finance" onclick="selectDockTab('finance')" class="dock-tab">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M5 7V4.5A1.5 1.5 0 0 1 6.5 3h11A1.5 1.5 0 0 1 19 4.5V7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            <rect x="2.5" y="7" width="19" height="13.5" rx="2.5" stroke="currentColor" stroke-width="1.8"/>
            <circle cx="16.5" cy="13.5" r="1.1" fill="currentColor"/>
          </svg>
          <span class="text-[12px] font-normal tracking-tight text-[#9e94b8]">Finance</span>
          <div id="bar-finance" class="dock-active-bar hidden"></div>
        </div>

        <!-- 3. Statistics Tab -->
        <div id="dock-tab-statistics" onclick="selectDockTab('statistics')" class="dock-tab">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/>
            <path d="M12 3.5 A8.5 8.5 0 0 1 20.5 11.2 H12 Z M12 12.8 H20.5 A8.5 8.5 0 0 1 12 20.5 Z" fill="currentColor"/>
          </svg>
          <span class="text-[12px] font-normal tracking-tight text-[#9e94b8]">Statistics</span>
          <div id="bar-statistics" class="dock-active-bar hidden"></div>
        </div>

        <!-- 4. Others Tab -->
        <div id="dock-tab-others" onclick="selectDockTab('others')" class="dock-tab">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="3.5" y="3.5" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.8"/>
            <rect x="13.5" y="3.5" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.8"/>
            <rect x="3.5" y="13.5" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.8"/>
            <rect x="13.5" y="13.5" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.8"/>
          </svg>
          <span class="text-[12px] font-normal tracking-tight text-[#9e94b8]">Others</span>
          <div id="bar-others" class="dock-active-bar hidden"></div>
        </div>

      </div>
    </nav>

  </div>

  <!-- Interactive Toast Notification -->
  <div id="homeToast" class="fixed bottom-6 bg-[#1a1835]/95 border border-white/15 backdrop-blur-xl text-white text-xs font-medium px-4 py-2.5 rounded-2xl shadow-2xl transition-all duration-300 opacity-0 translate-y-3 pointer-events-none z-50 flex items-center gap-2">
    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
    <span id="toastMsg">Action</span>
  </div>

  <script>
    /* Core Haptics, Audio & Notification Utilities */
    function playHapticTick() {{
      try {{
        if (navigator.vibrate) navigator.vibrate(12);
      }} catch (e) {{}}
    }}

    function playHapticFeedback(pattern = 18) {{
      try {{
        if (navigator.vibrate) navigator.vibrate(pattern);
      }} catch (e) {{}}
    }}

    function playSuccessChime() {{
      try {{
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(587.33, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.12);
        gain.gain.setValueAtTime(0.08, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.25);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.25);
      }} catch (e) {{}}
    }}

    function showToast(msg) {{
      const toast = document.getElementById('homeToast');
      const toastMsg = document.getElementById('toastMsg');
      if (!toast) return;
      if (toastMsg) toastMsg.textContent = msg;
      toast.classList.remove('opacity-0', 'translate-y-3', 'pointer-events-none');
      toast.classList.add('opacity-100', 'translate-y-0');
      setTimeout(() => {{
        toast.classList.add('opacity-0', 'translate-y-3', 'pointer-events-none');
        toast.classList.remove('opacity-100', 'translate-y-0');
      }}, 2400);
    }}

    function syncModalRadios(cardIdx) {{
      const radios = document.querySelectorAll('input[name="modalCardRadio"]');
      radios.forEach((r, idx) => {{
        r.checked = (idx + 1 === cardIdx);
      }});
    }}

    let currentScreen = 'splash'; // 'splash', 'login', 'faceid', 'secretkey', 'welcome', 'home'
    let selectedLoginOption = 'faceid'; // 'faceid' or 'secretkey'
    let splashTimer = null;
    let welcomeTimer = null;
    let pinCode = '';
    let isScanningFace = false;

    // Elements
    const splashScreen = document.getElementById('splashScreen');
    const loginScreen = document.getElementById('loginScreen');
    const faceidScreen = document.getElementById('faceidScreen');
    const secretkeyScreen = document.getElementById('secretkeyScreen');
    const welcomeScreen = document.getElementById('welcomeScreen');
    const homeScreen = document.getElementById('homeScreen');
    const cardDetailScreen = document.getElementById('cardDetailScreen');
    const statisticsScreen = document.getElementById('statisticsScreen');
    const financeScreen = document.getElementById('financeScreen');
    const othersScreen = document.getElementById('othersScreen');
    const vaultScreen = document.getElementById('vaultScreen');
    const sendMoneyScreen = document.getElementById('sendMoneyScreen');
    const screenIndicator = document.getElementById('screenIndicator');

    const screens = {{
      splash: splashScreen,
      login: loginScreen,
      faceid: faceidScreen,
      secretkey: secretkeyScreen,
      welcome: welcomeScreen,
      home: homeScreen,
      carddetail: cardDetailScreen,
      statistics: statisticsScreen,
      finance: financeScreen,
      others: othersScreen,
      vault: vaultScreen,
      sendmoney: sendMoneyScreen
    }};

    const chips = {{
      splash: document.getElementById('nav-chip-splash'),
      login: document.getElementById('nav-chip-login'),
      faceid: document.getElementById('nav-chip-faceid'),
      secretkey: document.getElementById('nav-chip-secretkey'),
      welcome: document.getElementById('nav-chip-welcome'),
      home: document.getElementById('nav-chip-home'),
      carddetail: document.getElementById('nav-chip-carddetail'),
      statistics: document.getElementById('nav-chip-statistics'),
      finance: document.getElementById('nav-chip-finance'),
      others: document.getElementById('nav-chip-others'),
      vault: document.getElementById('nav-chip-vault'),
      sendmoney: document.getElementById('nav-chip-sendmoney')
    }};

    function updateNavUI(target) {{
      const titles = {{
        splash: 'Screen 1: Splash',
        login: 'Screen 2: Login Type',
        faceid: 'Screen 3: Face ID',
        secretkey: 'Screen 4: Secret Key',
        welcome: 'Screen 5: Welcome Back',
        home: 'Screen 6: Home Screen',
        carddetail: 'Screen 7: Card Details',
        statistics: 'Screen 8: Statistics',
        finance: 'Screen 9: Finance Hub',
        others: 'Screen 10: Wallet Features',
        vault: 'Screen 11: Savings Vault',
        sendmoney: 'Screen 12: Send Money'
      }};
      if (screenIndicator) {{
        screenIndicator.textContent = titles[target] || target;
      }}

      Object.keys(chips).forEach(key => {{
        if (chips[key]) {{
          if (key === target) {{
            chips[key].className = 'px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-semibold shadow transition cursor-pointer whitespace-nowrap';
          }} else {{
            chips[key].className = 'px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 transition cursor-pointer whitespace-nowrap';
          }}
        }}
      }});
    }}

    function showScreen(target) {{
      clearTimeout(splashTimer);
      clearTimeout(welcomeTimer);
      hideFaceIdFailureModal();

      const screenKeys = Object.keys(screens);
      const prevIndex = screenKeys.indexOf(currentScreen);
      const nextIndex = screenKeys.indexOf(target);
      currentScreen = target;

      screenKeys.forEach((key, index) => {{
        const el = screens[key];
        el.classList.remove('screen-active', 'screen-hidden-left', 'screen-hidden-right');
        if (key === target) {{
          el.classList.add('screen-active');
        }} else if (index < nextIndex) {{
          el.classList.add('screen-hidden-left');
        }} else {{
          el.classList.add('screen-hidden-right');
        }}
      }});

      updateNavUI(target);

      // Synchronize single global footer bottom nav for all screens
      syncAllDockPills(target);

      if (target === 'statistics' && typeof setStatsPeriod === 'function') {{
        setStatsPeriod(currentStatsPeriod || 'W', false);
      }}

      if (target === 'splash') {{
        splashTimer = setTimeout(() => {{
          if (currentScreen === 'splash') {{
            showScreen('login');
          }}
        }}, 2200);
      }} else if (target === 'login') {{
        resetSliderPosition();
      }} else if (target === 'faceid') {{
        resetFaceIdUI();
        setTimeout(() => {{
          if (currentScreen === 'faceid') triggerFaceIdScan();
        }}, 450);
      }} else if (target === 'secretkey') {{
        resetPin();
      }} else if (target === 'welcome') {{
        welcomeTimer = setTimeout(() => {{
          if (currentScreen === 'welcome') {{
            showScreen('home');
          }}
        }}, 2000);
      }}
    }}

    function replaySplash() {{
      clearTimeout(splashTimer);
      clearTimeout(welcomeTimer);
      showScreen('splash');
      splashScreen.classList.remove('animate-splash');
      void splashScreen.offsetWidth;
      splashScreen.classList.add('animate-splash');

      splashTimer = setTimeout(() => {{
        showScreen('login');
      }}, 2750);
    }}

    function selectOption(method) {{
      selectedLoginOption = method;
      const faceCard = document.getElementById('option-faceid');
      const keyCard = document.getElementById('option-secretkey');
      const faceBadge = document.getElementById('badge-faceid');
      const keyBadge = document.getElementById('badge-secretkey');

      if (method === 'faceid') {{
        faceCard.classList.add('selected');
        faceCard.setAttribute('aria-checked', 'true');
        keyCard.classList.remove('selected');
        keyCard.setAttribute('aria-checked', 'false');

        faceBadge.classList.remove('scale-0', 'opacity-0');
        faceBadge.classList.add('scale-100', 'opacity-100');
        keyBadge.classList.remove('scale-100', 'opacity-100');
        keyBadge.classList.add('scale-0', 'opacity-0');
      }} else {{
        keyCard.classList.add('selected');
        keyCard.setAttribute('aria-checked', 'true');
        faceCard.classList.remove('selected');
        faceCard.setAttribute('aria-checked', 'false');

        keyBadge.classList.remove('scale-0', 'opacity-0');
        keyBadge.classList.add('scale-100', 'opacity-100');
        faceBadge.classList.remove('scale-100', 'opacity-100');
        faceBadge.classList.add('scale-0', 'opacity-0');
      }}
    }}

    /* Face ID Simulation Logic */
    function resetFaceIdUI() {{
      isScanningFace = false;
      const box = document.getElementById('faceidVisualBox');
      const defaultSvg = document.getElementById('faceidDefaultSvg');
      const successBadge = document.getElementById('faceidSuccessBadge');
      const heading = document.getElementById('faceidStatusHeading');
      const desc = document.getElementById('faceidStatusDesc');

      box.classList.add('is-scanning');
      defaultSvg.classList.remove('hidden');
      successBadge.classList.add('hidden');
      heading.textContent = 'Scanning Face ID...';
      heading.className = 'text-[22px] font-bold text-white tracking-tight';
      desc.textContent = 'Position your face in front of the camera to unlock Cashleap';
    }}

    function triggerFaceIdScan() {{
      if (isScanningFace) return;
      isScanningFace = true;
      resetFaceIdUI();

      const box = document.getElementById('faceidVisualBox');
      const defaultSvg = document.getElementById('faceidDefaultSvg');
      const successBadge = document.getElementById('faceidSuccessBadge');
      const heading = document.getElementById('faceidStatusHeading');
      const desc = document.getElementById('faceidStatusDesc');

      heading.textContent = 'Scanning Face ID...';

      setTimeout(() => {{
        if (currentScreen !== 'faceid') return;

        box.classList.remove('is-scanning');
        defaultSvg.classList.add('hidden');
        successBadge.classList.remove('hidden');

        heading.textContent = 'Face Recognized!';
        heading.className = 'text-[22px] font-bold text-emerald-400 tracking-tight';
        desc.textContent = 'Authentication successful. Redirecting...';

        setTimeout(() => {{
          if (currentScreen === 'faceid') {{
            showScreen('welcome');
          }}
        }}, 850);
      }}, 1300);
    }}

    function showFaceIdFailureModal() {{
      const modal = document.getElementById('iosFaceIdModal');
      modal.classList.remove('opacity-0', 'pointer-events-none');
      modal.classList.add('opacity-100', 'pointer-events-auto');
    }}

    function hideFaceIdFailureModal() {{
      const modal = document.getElementById('iosFaceIdModal');
      modal.classList.add('opacity-0', 'pointer-events-none');
      modal.classList.remove('opacity-100', 'pointer-events-auto');
    }}

    /* Secret Key Passcode Logic */
    function updatePasscodeDots() {{
      for (let i = 0; i < 6; i++) {{
        const dot = document.getElementById('pdot-' + i);
        if (i < pinCode.length) {{
          dot.classList.add('filled');
        }} else {{
          dot.classList.remove('filled');
        }}
      }}
    }}

    function pressPinKey(digit) {{
      if (pinCode.length < 6) {{
        pinCode += digit;
        updatePasscodeDots();

        if (pinCode.length === 6) {{
          verifyPin();
        }}
      }}
    }}

    function pressBackspace() {{
      if (pinCode.length > 0) {{
        pinCode = pinCode.slice(0, -1);
        updatePasscodeDots();
      }}
    }}

    function resetPin() {{
      pinCode = '';
      updatePasscodeDots();
    }}

    function quickFillPin() {{
      pinCode = '123456';
      updatePasscodeDots();
      verifyPin();
    }}

    function verifyPin() {{
      setTimeout(() => {{
        for (let i = 0; i < 6; i++) {{
          const dot = document.getElementById('pdot-' + i);
          dot.style.borderColor = '#10b981';
          dot.style.background = '#10b981';
          dot.style.boxShadow = '0 0 14px rgba(16, 185, 129, 0.9)';
        }}

        setTimeout(() => {{
          showScreen('welcome');
        }}, 500);
      }}, 250);
    }}


    /* ======================================================== */
    /* STATISTICS / MY EXPENSES INTERACTIVE ENGINE               */
    /* ======================================================== */
    let currentStatsPeriod = 'W';
    let currentStatsDayIndex = 4; // default 'Thu'

    const statsData = {{
      W: {{
        days: [
          {{ name: 'Sun', amount: '1,840.20 AED', val: '1,840.20', x: 18, y: 74 }},
          {{ name: 'Mon', amount: '2,120.00 AED', val: '2,120.00', x: 64, y: 68 }},
          {{ name: 'Tue', amount: '1,650.50 AED', val: '1,650.50', x: 112, y: 82 }},
          {{ name: 'Wed', amount: '2,490.80 AED', val: '2,490.80', x: 160, y: 58 }},
          {{ name: 'Thu', amount: '3,350.60 AED', val: '3,350.60', x: 208, y: 30 }},
          {{ name: 'Fri', amount: '2,780.00 AED', val: '2,780.00', x: 256, y: 50 }},
          {{ name: 'Sat', amount: '3,210.40 AED', val: '3,210.40', x: 296, y: 36 }}
        ],
        defaultIdx: 4,
        areaPath: 'M 0,72 C 9,72 12,74 18,74 C 36,74 46,68 64,68 C 82,68 94,82 112,82 C 130,82 142,60 160,58 C 178,56 192,30 208,30 C 224,30 240,50 256,50 C 272,50 282,36 296,36 L 310,44 L 310,120 L 0,120 Z',
        linePath: 'M 0,72 C 9,72 12,74 18,74 C 36,74 46,68 64,68 C 82,68 94,82 112,82 C 130,82 142,60 160,58 C 178,56 192,30 208,30 C 224,30 240,50 256,50 C 272,50 282,36 296,36 L 310,44'
      }},
      D: {{
        days: [
          {{ name: '12a', amount: '120.00 AED', val: '120.00', x: 18, y: 95 }},
          {{ name: '4a', amount: '50.00 AED', val: '50.00', x: 64, y: 104 }},
          {{ name: '8a', amount: '340.50 AED', val: '340.50', x: 112, y: 76 }},
          {{ name: '12p', amount: '680.00 AED', val: '680.00', x: 160, y: 52 }},
          {{ name: '4p', amount: '940.20 AED', val: '940.20', x: 208, y: 38 }},
          {{ name: '8p', amount: '810.00 AED', val: '810.00', x: 256, y: 46 }},
          {{ name: '11p', amount: '450.00 AED', val: '450.00', x: 296, y: 70 }}
        ],
        defaultIdx: 4,
        areaPath: 'M 0,90 C 9,90 12,95 18,95 C 36,95 46,104 64,104 C 82,104 94,78 112,76 C 130,74 142,54 160,52 C 178,48 192,38 208,38 C 224,38 240,46 256,46 C 272,46 282,68 296,70 L 310,76 L 310,120 L 0,120 Z',
        linePath: 'M 0,90 C 9,90 12,95 18,95 C 36,95 46,104 64,104 C 82,104 94,78 112,76 C 130,74 142,54 160,52 C 178,48 192,38 208,38 C 224,38 240,46 256,46 C 272,46 282,68 296,70 L 310,76'
      }},
      M: {{
        days: [
          {{ name: 'W1', amount: '2,900.00 AED', val: '2,900.00', x: 18, y: 64 }},
          {{ name: 'W2', amount: '3,450.00 AED', val: '3,450.00', x: 64, y: 48 }},
          {{ name: 'W3', amount: '4,100.00 AED', val: '4,100.00', x: 112, y: 34 }},
          {{ name: 'W4', amount: '3,350.60 AED', val: '3,350.60', x: 160, y: 50 }},
          {{ name: 'W5', amount: '4,800.00 AED', val: '4,800.00', x: 208, y: 26 }},
          {{ name: 'W6', amount: '3,900.00 AED', val: '3,900.00', x: 256, y: 42 }},
          {{ name: 'W7', amount: '4,200.00 AED', val: '4,200.00', x: 296, y: 32 }}
        ],
        defaultIdx: 4,
        areaPath: 'M 0,66 C 9,66 12,64 18,64 C 36,64 46,48 64,48 C 82,48 94,34 112,34 C 130,34 142,50 160,50 C 178,50 192,26 208,26 C 224,26 240,42 256,42 C 272,42 282,32 296,32 L 310,36 L 310,120 L 0,120 Z',
        linePath: 'M 0,66 C 9,66 12,64 18,64 C 36,64 46,48 64,48 C 82,48 94,34 112,34 C 130,34 142,50 160,50 C 178,50 192,26 208,26 C 224,26 240,42 256,42 C 272,42 282,32 296,32 L 310,36'
      }},
      Y: {{
        days: [
          {{ name: "'20", amount: '18,500 AED', val: '18,500.00', x: 18, y: 72 }},
          {{ name: "'21", amount: '24,200 AED', val: '24,200.00', x: 64, y: 56 }},
          {{ name: "'22", amount: '31,000 AED', val: '31,000.00', x: 112, y: 42 }},
          {{ name: "'23", amount: '39,400 AED', val: '39,400.00', x: 160, y: 30 }},
          {{ name: "'24", amount: '48,200 AED', val: '48,200.00', x: 208, y: 20 }},
          {{ name: "'25", amount: '42,000 AED', val: '42,000.00', x: 256, y: 34 }},
          {{ name: "'26", amount: '46,500 AED', val: '46,500.00', x: 296, y: 28 }}
        ],
        defaultIdx: 4,
        areaPath: 'M 0,76 C 9,76 12,72 18,72 C 36,72 46,56 64,56 C 82,56 94,42 112,42 C 130,42 142,30 160,30 C 178,30 192,20 208,20 C 224,20 240,34 256,34 C 272,34 282,28 296,28 L 310,30 L 310,120 L 0,120 Z',
        linePath: 'M 0,76 C 9,76 12,72 18,72 C 36,72 46,56 64,56 C 82,56 94,42 112,42 C 130,42 142,30 160,30 C 178,30 192,20 208,20 C 224,20 240,34 256,34 C 272,34 282,28 296,28 L 310,30'
      }}
    }};

    function setStatsPeriod(period, isUserClick = false) {{
      playHapticTick();
      if (isUserClick) {{
        // Dynamic island only triggered on explicit click
      }}
      currentStatsPeriod = period;
      ['D', 'W', 'M', 'Y'].forEach(p => {{
        const btn = document.getElementById('btn-period-' + p);
        if (!btn) return;
        if (p === period) {{
          btn.className = 'text-[13px] font-bold text-[#ff2a6d] relative flex flex-col items-center cursor-pointer px-1';
          btn.innerHTML = p + '<span class="w-1.5 h-1.5 rounded-full bg-[#ff2a6d] mt-0.5 shadow-[0_0_6px_#ff2a6d]"></span>';
        }} else {{
          btn.className = 'text-[13px] font-semibold text-[#8c82ab] hover:text-white transition cursor-pointer px-1';
          btn.innerHTML = p;
        }}
      }});

      const data = statsData[period] || statsData.W;
      const areaPath = document.getElementById('statsAreaPath');
      const linePath = document.getElementById('statsLinePath');
      if (areaPath) areaPath.setAttribute('d', data.areaPath);
      if (linePath) linePath.setAttribute('d', data.linePath);

      // Update days buttons text
      for (let i = 0; i < 7; i++) {{
        const dayBtn = document.getElementById('stats-day-' + i);
        if (dayBtn && data.days[i]) {{
          dayBtn.textContent = data.days[i].name;
        }}
      }}

      selectStatsDay(data.defaultIdx);
      // Dynamic island only triggered on explicit click
    }}

    function selectStatsDay(idx) {{
      playHapticFeedback('light');
      currentStatsDayIndex = idx;
      const data = statsData[currentStatsPeriod] || statsData.W;
      const pt = data.days[idx] || data.days[4];

      // Update active day button styling
      for (let i = 0; i < 7; i++) {{
        const dayBtn = document.getElementById('stats-day-' + i);
        if (!dayBtn) continue;
        if (i === idx) {{
          dayBtn.className = 'text-[12px] font-bold text-white bg-white/[0.14] border border-white/10 rounded-full px-3 py-1 cursor-pointer transition';
        }} else {{
          dayBtn.className = 'text-[12px] font-medium text-[#8c82ab] hover:text-white transition py-1 px-2 cursor-pointer';
        }}
      }}

      // Move vertical guideline
      const guideline = document.getElementById('statsActiveGuideline');
      if (guideline) {{
        guideline.setAttribute('x1', pt.x);
        guideline.setAttribute('x2', pt.x);
        guideline.setAttribute('y1', pt.y);
      }}

      // Move Halo & Dot
      const halo = document.getElementById('statsActiveHalo');
      const dot = document.getElementById('statsActiveDot');
      if (halo) {{
        halo.setAttribute('cx', pt.x);
        halo.setAttribute('cy', pt.y);
      }}
      if (dot) {{
        dot.setAttribute('cx', pt.x);
        dot.setAttribute('cy', pt.y);
      }}

      // Move Tooltip Badge
      const badge = document.getElementById('statsChartBadge');
      const badgeText = document.getElementById('statsBadgeText');
      if (badge) {{
        badge.style.left = pt.x + 'px';
        badge.style.top = (pt.y - 8) + 'px';
      }}
      if (badgeText) {{
        badgeText.textContent = pt.amount;
      }}

      // Update Current Balance
      const balEl = document.getElementById('statsBalanceAmount');
      if (balEl) {{
        balEl.textContent = pt.val;
      }}
    }}

    function handleCategoryClick(name, amount) {{
      playHapticFeedback('light');
      triggerDynamicIsland('icon-card', name, amount);
      showToast(name + ': ' + amount + ' spent this period');
    }}

    // Physical Keyboard Listener for Passcode
    window.addEventListener('keydown', (e) => {{
      if (currentScreen === 'secretkey') {{
        if (e.key >= '0' && e.key <= '9') {{
          pressPinKey(e.key);
        }} else if (e.key === 'Backspace') {{
          pressBackspace();
        }}
      }}
    }});

    /* ========================================================
       SCREEN 2: LOGIN SLIDE-TO-NEXT CONTROLLER (POINTER / TOUCH / CLICK)
       ======================================================== */
    let isSliderDragging = false;
    let sliderStartX = 0;
    let sliderCurrentX = 0;
    let sliderMaxSlide = 0;
    let sliderDragMoved = false;

    function getSliderMax() {{
      const track = document.getElementById('sliderTrack');
      const thumb = document.getElementById('sliderThumb');
      if (!track || !thumb) return 200;
      return Math.max(10, track.clientWidth - thumb.clientWidth - 12);
    }}

    function resetSliderPosition() {{
      sliderCurrentX = 0;
      isSliderDragging = false;
      sliderDragMoved = false;
      const thumb = document.getElementById('sliderThumb');
      const label = document.getElementById('sliderLabel');
      const chevrons = document.getElementById('sliderChevrons');
      if (thumb) {{
        thumb.classList.remove('dragging');
        thumb.style.transition = 'transform 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        thumb.style.transform = 'translateX(0px)';
      }}
      if (label) {{
        label.style.transition = 'opacity 0.25s ease';
        label.style.opacity = '1';
      }}
      if (chevrons) {{
        chevrons.style.transition = 'opacity 0.25s ease';
        chevrons.style.opacity = '1';
      }}
    }}

    function completeLoginSlide() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const thumb = document.getElementById('sliderThumb');
      const label = document.getElementById('sliderLabel');
      const chevrons = document.getElementById('sliderChevrons');
      sliderMaxSlide = getSliderMax();

      if (thumb) {{
        thumb.style.transition = 'transform 0.24s cubic-bezier(0.2, 0.9, 0.3, 1)';
        thumb.style.transform = 'translateX(' + sliderMaxSlide + 'px)';
      }}
      if (label) {{
        label.style.transition = 'opacity 0.18s ease';
        label.style.opacity = '0';
      }}
      if (chevrons) {{
        chevrons.style.transition = 'opacity 0.18s ease';
        chevrons.style.opacity = '0';
      }}

      setTimeout(() => {{
        if (selectedLoginOption === 'faceid') {{
          showScreen('faceid');
        }} else {{
          showScreen('secretkey');
        }}
      }}, 220);
    }}

    function initLoginSlider() {{
      const track = document.getElementById('sliderTrack');
      const thumb = document.getElementById('sliderThumb');
      const label = document.getElementById('sliderLabel');
      const chevrons = document.getElementById('sliderChevrons');
      if (!track || !thumb) return;

      function onPointerStart(e) {{
        e.preventDefault();
        e.stopPropagation();
        isSliderDragging = true;
        sliderDragMoved = false;
        sliderMaxSlide = getSliderMax();
        thumb.classList.add('dragging');
        thumb.style.transition = 'none';
        sliderStartX = e.clientX - sliderCurrentX;

        if (thumb.setPointerCapture && e.pointerId !== undefined) {{
          try {{ thumb.setPointerCapture(e.pointerId); }} catch(err) {{}}
        }}
      }}

      function onPointerMove(e) {{
        if (!isSliderDragging) return;
        e.preventDefault();
        const delta = e.clientX - sliderStartX;
        if (Math.abs(delta - sliderCurrentX) > 3) sliderDragMoved = true;
        sliderCurrentX = Math.max(0, Math.min(delta, sliderMaxSlide));
        thumb.style.transform = 'translateX(' + sliderCurrentX + 'px)';

        const progress = sliderMaxSlide > 0 ? (sliderCurrentX / sliderMaxSlide) : 0;
        if (label) label.style.opacity = String(Math.max(0, 1 - progress * 1.6));
        if (chevrons) chevrons.style.opacity = String(Math.max(0.12, 1 - progress));
      }}

      function onPointerEnd(e) {{
        if (!isSliderDragging) return;
        isSliderDragging = false;
        thumb.classList.remove('dragging');

        if (thumb.releasePointerCapture && e && e.pointerId !== undefined) {{
          try {{ thumb.releasePointerCapture(e.pointerId); }} catch(err) {{}}
        }}

        // If dragged > 38% across, complete slide; if user simply tapped/clicked, complete slide!
        if (!sliderDragMoved || sliderCurrentX > (sliderMaxSlide * 0.38)) {{
          completeLoginSlide();
        }} else {{
          resetSliderPosition();
        }}
      }}

      // Modern Pointer Events
      thumb.addEventListener('pointerdown', onPointerStart);
      thumb.addEventListener('pointermove', onPointerMove);
      thumb.addEventListener('pointerup', onPointerEnd);
      thumb.addEventListener('pointercancel', onPointerEnd);

      // Touch fallback with passive: false for seamless mobile drag
      thumb.addEventListener('touchstart', (e) => {{
        if (e.touches && e.touches[0]) {{
          e.preventDefault();
          onPointerStart({{
            clientX: e.touches[0].clientX,
            pointerId: undefined,
            preventDefault: () => {{}},
            stopPropagation: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchmove', (e) => {{
        if (!isSliderDragging) return;
        if (e.touches && e.touches[0]) {{
          if (e.cancelable) e.preventDefault();
          onPointerMove({{
            clientX: e.touches[0].clientX,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchend', (e) => {{
        if (isSliderDragging) onPointerEnd(e);
      }});

      // Mouse fallback
      thumb.addEventListener('mousedown', (e) => {{
        e.preventDefault();
        onPointerStart(e);
      }});
      window.addEventListener('mousemove', (e) => {{
        if (isSliderDragging) onPointerMove(e);
      }});
      window.addEventListener('mouseup', (e) => {{
        if (isSliderDragging) onPointerEnd(e);
      }});

      // Track tap-to-complete fallback
      track.addEventListener('click', (e) => {{
        if (e.target !== thumb && !thumb.contains(e.target)) {{
          completeLoginSlide();
        }}
      }});
    }}

    /* ========================================================
       DRAGGABLE CARD CAROUSEL, ADD CARD & USER PROFILE CONTROLLERS
       ======================================================== */
    let currentCardIndex = 1;
    let totalCards = 2;
    let isDraggingCard = false;
    let cardDragStartX = 0;
    let cardInitialTranslate = -11.5;
    let cardDragDeltaX = 0;
    let cardHasMoved = false;

    function getBaseCardTranslate(idx) {{
      return -11.5 - (idx - 1) * 322;
    }}

    function selectCardIndex(idx, showNotification = true) {{
      if (idx < 1) idx = 1;
      if (idx > totalCards) idx = totalCards;
      currentCardIndex = idx;
      
      const track = document.getElementById('cardCarouselTrack');
      if (!track) return;
      
      track.style.transition = 'transform 0.42s cubic-bezier(0.22, 1, 0.36, 1)';
      const targetX = getBaseCardTranslate(idx);
      track.style.transform = 'translateX(' + targetX + 'px)';

      // Synchronize all 4 pagination dots
      for (let i = 1; i <= 4; i++) {{
        const dot = document.getElementById('card-dot-' + i);
        if (dot) {{
          if (i === idx) {{
            dot.className = 'w-6 h-1 rounded-full bg-white cursor-pointer transition-all shadow-sm';
          }} else if (i <= totalCards) {{
            dot.className = 'w-3.5 h-1 rounded-full bg-white/20 hover:bg-white/40 cursor-pointer transition-all';
          }} else {{
            dot.className = 'w-3.5 h-1 rounded-full bg-white/10 transition-all';
          }}
        }}
      }}

      // Synchronize active badges
      for (let i = 1; i <= totalCards; i++) {{
        const badge = document.getElementById('card' + i + '-active-badge');
        if (badge) {{
          if (i === idx) {{
            badge.classList.remove('opacity-0');
            badge.classList.add('opacity-100');
          }} else {{
            badge.classList.remove('opacity-100');
            badge.classList.add('opacity-0');
          }}
        }}
      }}

      if (showNotification) {{
        if (idx === 1) showToast('Card Balance (0329) selected • 3,350.60 AED');
        else if (idx === 2) showToast('Debit Card (0319) selected • 2,150.60 AED');
        else if (idx === 3) showToast('Virtual Card (8821) selected • 1,500.00 AED');
        else if (idx === 4) showToast('Platinum Card (4412) selected • 5,000.00 AED');
      }}

      if (typeof syncModalRadios === 'function') syncModalRadios(idx);
    }}

    function handleCardClick(idx) {{
      if (!cardHasMoved) {{
        selectCardIndex(idx, false);
        openCardDetailsScreen(idx);
      }}
    }}

    // Real-time Dragging Gesture for Card Carousel (Pointer Events + Damping)
    function initCardCarouselDragging() {{
      const container = document.getElementById('cardCarouselContainer');
      const track = document.getElementById('cardCarouselTrack');
      if (!container || !track) return;

      function onCardPointerDown(e) {{
        if (e.target.closest('#addCardPillBtn') || e.target.closest('[id$="-active-badge"]')) return;
        isDraggingCard = true;
        cardHasMoved = false;
        cardDragStartX = e.clientX;
        cardDragDeltaX = 0;
        cardInitialTranslate = getBaseCardTranslate(currentCardIndex);
        track.style.transition = 'none';
        container.style.cursor = 'grabbing';

        if (container.setPointerCapture && e.pointerId !== undefined) {{
          try {{ container.setPointerCapture(e.pointerId); }} catch(err) {{}}
        }}
      }}

      function onCardPointerMove(e) {{
        if (!isDraggingCard) return;
        cardDragDeltaX = e.clientX - cardDragStartX;
        if (Math.abs(cardDragDeltaX) > 4) {{
          cardHasMoved = true;
          if (e.cancelable) e.preventDefault();
        }}

        let newX = cardInitialTranslate + cardDragDeltaX;
        const minTranslate = getBaseCardTranslate(totalCards);

        // Smooth rubber-band resistance at boundaries
        if (newX > 15) {{
          newX = 15 + (newX - 15) * 0.22;
        }} else if (newX < minTranslate - 20) {{
          newX = (minTranslate - 20) + (newX - (minTranslate - 20)) * 0.22;
        }}
        track.style.transform = 'translateX(' + newX + 'px)';
      }}

      function onCardPointerUp(e) {{
        if (!isDraggingCard) return;
        isDraggingCard = false;
        container.style.cursor = 'grab';

        if (container.releasePointerCapture && e && e.pointerId !== undefined) {{
          try {{ container.releasePointerCapture(e.pointerId); }} catch(err) {{}}
        }}

        track.style.transition = 'transform 0.4s cubic-bezier(0.22, 1, 0.36, 1)';

        if (cardHasMoved && Math.abs(cardDragDeltaX) > 35) {{
          if (cardDragDeltaX < -35) {{
            // Dragged Left -> Next Card
            if (currentCardIndex < totalCards) {{
              selectCardIndex(currentCardIndex + 1);
            }} else {{
              selectCardIndex(currentCardIndex, false);
            }}
          }} else if (cardDragDeltaX > 35) {{
            // Dragged Right -> Previous Card
            if (currentCardIndex > 1) {{
              selectCardIndex(currentCardIndex - 1);
            }} else {{
              selectCardIndex(currentCardIndex, false);
            }}
          }}
        }} else {{
          selectCardIndex(currentCardIndex, false);
        }}
      }}

      container.addEventListener('pointerdown', onCardPointerDown);
      container.addEventListener('pointermove', onCardPointerMove);
      container.addEventListener('pointerup', onCardPointerUp);
      container.addEventListener('pointercancel', onCardPointerUp);

      // Touch fallback
      container.addEventListener('touchstart', (e) => {{
        if (e.target.closest('#addCardPillBtn')) return;
        if (e.touches && e.touches[0]) {{
          onCardPointerDown({{
            clientX: e.touches[0].clientX,
            pointerId: undefined,
            target: e.target
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchmove', (e) => {{
        if (!isDraggingCard) return;
        if (e.touches && e.touches[0]) {{
          if (Math.abs(e.touches[0].clientX - cardDragStartX) > 5 && e.cancelable) {{
            e.preventDefault();
          }}
          onCardPointerMove({{
            clientX: e.touches[0].clientX,
            cancelable: e.cancelable,
            preventDefault: () => {{ if (e.cancelable) e.preventDefault(); }}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchend', (e) => {{
        if (isDraggingCard) onCardPointerUp(e);
      }});

      // Mouse fallback
      container.addEventListener('mousedown', (e) => {{
        if (e.target.closest('#addCardPillBtn')) return;
        e.preventDefault();
        onCardPointerDown(e);
      }});
      window.addEventListener('mousemove', (e) => {{
        if (isDraggingCard) onCardPointerMove(e);
      }});
      window.addEventListener('mouseup', (e) => {{
        if (isDraggingCard) onCardPointerUp(e);
      }});
    }}

    /* ========================================================
       ADD NEW CARD MODAL CONTROLLERS (LOGICAL CARD INPUTS)
       ======================================================== */
    let newCardTheme = 'midnight';
    let newCardType = 'debit';

    function openAddCardModal() {{
      playHapticTick();
      if (totalCards >= 4) {{
        showToast('Maximum wallet limit (4 cards) reached');
        return;
      }}
      const numInput = document.getElementById('newCardNumberInput');
      if (numInput) {{
        const nextSuffix = (totalCards === 2) ? '8821' : '4412';
        numInput.value = '5412 7512 3412 ' + nextSuffix;
      }}
      updateNewCardPreview();
      const modal = document.getElementById('addCardModal');
      const sheet = document.getElementById('addCardSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        requestAnimationFrame(() => {{
          sheet.classList.remove('translate-y-full');
        }});
      }}
    }}

    function closeAddCardModal() {{
      playHapticTick();
      const modal = document.getElementById('addCardModal');
      const sheet = document.getElementById('addCardSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
    }}

    function formatCardNumberInput(inputEl) {{
      if (!inputEl) return;
      let digits = inputEl.value.replace(/\D/g, '').substring(0, 16);
      let formatted = digits.replace(/(\d{{4}})(?=\d)/g, '$1 ');
      inputEl.value = formatted;
      updateNewCardPreview();
    }}

    function formatCardExpiryInput(inputEl) {{
      if (!inputEl) return;
      let digits = inputEl.value.replace(/\D/g, '').substring(0, 4);
      if (digits.length >= 3) {{
        inputEl.value = digits.substring(0, 2) + '/' + digits.substring(2, 4);
      }} else {{
        inputEl.value = digits;
      }}
      updateNewCardPreview();
    }}

    function simulateCardScanInModal() {{
      playHapticTick();
      const numInput = document.getElementById('newCardNumberInput');
      const expInput = document.getElementById('newCardExpiryInput');
      const cvvInput = document.getElementById('newCardCvvInput');
      const scannedSuffix = (totalCards === 2) ? '9042' : '6188';
      if (numInput) numInput.value = '5412 8890 1024 ' + scannedSuffix;
      if (expInput) expInput.value = '11/29';
      if (cvvInput) cvvInput.value = '915';
      updateNewCardPreview();
      showToast('Card details scanned via camera');
    }}

    function setNewCardType(type) {{
      playHapticTick();
      newCardType = type;
      const badge = document.getElementById('previewCardTypeBadge');
      if (badge) {{
        badge.textContent = (type === 'virtual') ? 'Virtual Card' : 'Mastercard Debit';
      }}
    }}

    function setNewCardTheme(theme) {{
      playHapticTick();
      newCardTheme = theme;
      const preview = document.getElementById('newCardPreview');
      const themes = ['midnight', 'sunset', 'emerald', 'neon'];
      themes.forEach(t => {{
        const btn = document.getElementById('theme-' + t);
        if (btn) {{
          if (t === theme) {{
            btn.className = 'w-6 h-6 rounded-full border-2 border-white ring-2 ring-blue-400/50 shadow-sm transition transform scale-110 cursor-pointer';
          }} else {{
            btn.className = 'w-6 h-6 rounded-full border border-white/25 hover:scale-105 transition cursor-pointer';
          }}
        }}
      }});

      const grads = {{
        midnight: 'linear-gradient(135deg, #1e1b4b 0%, #312e81 45%, #0f172a 100%)',
        sunset: 'linear-gradient(135deg, #f59e0b 0%, #ec4899 50%, #6366f1 100%)',
        emerald: 'linear-gradient(135deg, #059669 0%, #0d9488 45%, #0284c7 100%)',
        neon: 'linear-gradient(135deg, #6d28d9 0%, #9333ea 50%, #4f46e5 100%)'
      }};
      if (preview) preview.style.background = grads[theme] || grads.midnight;
    }}

    function updateNewCardPreview() {{
      const nameInput = document.getElementById('newCardNameInput');
      const numInput = document.getElementById('newCardNumberInput');
      const expInput = document.getElementById('newCardExpiryInput');
      const holderEl = document.getElementById('previewCardHolder');
      const numEl = document.getElementById('previewCardNumber');
      const expEl = document.getElementById('previewCardExpiry');

      if (nameInput && holderEl) {{
        holderEl.textContent = (nameInput.value.trim() || 'MARICE CERVANTES').toUpperCase();
      }}
      if (numInput && numEl) {{
        const raw = numInput.value.trim() || '5412 7512 3412 8821';
        numEl.textContent = raw.replace(/ /g, '  ');
      }}
      if (expInput && expEl) {{
        expEl.textContent = expInput.value.trim() || '08/28';
      }}
    }}

    function confirmAddNewCard() {{
      if (totalCards >= 4) {{
        closeAddCardModal();
        showToast('Maximum 4 cards already linked');
        return;
      }}

      playHapticTick();
      totalCards++;
      const newIdx = totalCards;
      const numInput = document.getElementById('newCardNumberInput');
      const expInput = document.getElementById('newCardExpiryInput');
      const rawDigits = (numInput && numInput.value) ? numInput.value.replace(/\D/g, '') : '';
      const lastFour = (rawDigits.length >= 4) ? rawDigits.slice(-4) : ((newIdx === 3) ? '8821' : '4412');
      const expiryVal = (expInput && expInput.value.trim()) ? expInput.value.trim() : '08/28';
      const balanceStr = (newIdx === 3) ? '4,200.00' : '6,850.00';

      const grads = {{
        midnight: 'linear-gradient(135deg, #1e1b4b 0%, #312e81 45%, #0f172a 100%)',
        sunset: 'linear-gradient(135deg, #f59e0b 0%, #ec4899 50%, #6366f1 100%)',
        emerald: 'linear-gradient(135deg, #059669 0%, #0d9488 45%, #0284c7 100%)',
        neon: 'linear-gradient(135deg, #6d28d9 0%, #9333ea 50%, #4f46e5 100%)'
      }};
      const chosenGrad = grads[newCardTheme] || grads.midnight;

      // Create & Append New Card Element to Carousel Track
      const track = document.getElementById('cardCarouselTrack');
      if (track) {{
        const cardEl = document.createElement('div');
        cardEl.id = 'card-item-' + newIdx;
        cardEl.className = 'w-[310px] h-[178px] rounded-[28px] p-5 flex flex-col justify-between text-white relative flex-shrink-0 cursor-pointer transition-all duration-300 hover:scale-[1.01] overflow-hidden apple-press border border-white/15';
        cardEl.style.background = chosenGrad;
        cardEl.setAttribute('onclick', 'handleCardClick(' + newIdx + ')');
        cardEl.innerHTML = `
          <div class="card-holographic-glint absolute inset-0 pointer-events-none rounded-[28px] opacity-0 transition-opacity duration-300"></div>
          <div id="card` + newIdx + `-active-badge" class="absolute top-3.5 right-4 bg-black/35 hover:bg-black/55 backdrop-blur-md px-2.5 py-0.5 rounded-full border border-white/20 text-[10px] font-semibold text-white flex items-center gap-1 transition-all">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            Active
          </div>
          <div>
            <span class="text-[11px] font-medium text-white/80 tracking-wide">Card Balance</span>
            <div class="flex items-baseline gap-1 mt-0.5">
              <span class="text-[29px] font-bold tracking-tight text-white leading-none">` + balanceStr + `</span>
              <span class="text-[13px] font-bold text-white/90">AED</span>
            </div>
          </div>
          <div class="text-[13.5px] font-mono tracking-[0.2em] text-white/90 font-medium">
            **** **** **** ` + lastFour + `
          </div>
          <div class="flex items-center justify-between pt-1">
            <div class="flex items-center gap-2">
              <div class="flex flex-col text-[7px] font-bold uppercase tracking-wider text-white/70 leading-tight">
                <span>VALID</span>
                <span>THRU</span>
              </div>
              <span class="text-[13px] font-bold text-white tracking-wide">` + expiryVal + `</span>
            </div>
            <div class="flex items-center" title="Mastercard">
              <svg class="w-9 h-5.5" viewBox="0 0 38 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="13" cy="12" r="10.5" fill="#EB001B"/>
                <circle cx="25" cy="12" r="10.5" fill="#F79E1B" fill-opacity="0.95"/>
              </svg>
            </div>
          </div>
        `;
        track.appendChild(cardEl);
      }}

      // Update profile badge
      const profileBadge = document.getElementById('profileCardsCountBadge');
      if (profileBadge) profileBadge.textContent = totalCards + ' Cards';

      closeAddCardModal();
      selectCardIndex(newIdx, false);

      if (typeof triggerDynamicIsland === 'function') {{
        triggerDynamicIsland('Card Linked', 'Mastercard •••• ' + lastFour);
      }}
      showToast('Card ending in ' + lastFour + ' linked to wallet');
    }}

    /* ========================================================
       USER ACCOUNT & PROFILE MODAL CONTROLLERS
       ======================================================== */
    let isProfileFaceIdActive = true;

    function openUserProfileModal() {{
      playHapticTick();
      const modal = document.getElementById('userProfileModal');
      const sheet = document.getElementById('userProfileSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        requestAnimationFrame(() => {{
          sheet.classList.remove('translate-y-full');
        }});
      }}
    }}

    function closeUserProfileModal() {{
      playHapticTick();
      const modal = document.getElementById('userProfileModal');
      const sheet = document.getElementById('userProfileSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
    }}

    function copyProfileIban() {{
      playHapticTick();
      const iban = 'AE07 0331 2345 6789 0123 456';
      if (navigator.clipboard) {{
        navigator.clipboard.writeText(iban).catch(() => {{}});
      }}
      if (typeof triggerDynamicIsland === 'function') {{
        triggerDynamicIsland('IBAN Copied', 'AE07 0331 2345 6789 0123');
      }}
      showToast('UAE IBAN copied to clipboard!');
    }}

    function toggleProfileFaceId() {{
      playHapticTick();
      isProfileFaceIdActive = !isProfileFaceIdActive;
      const toggle = document.getElementById('profileFaceIdToggle');
      const knob = document.getElementById('profileFaceIdKnob');
      if (toggle && knob) {{
        if (isProfileFaceIdActive) {{
          toggle.className = 'w-10 h-5 rounded-full bg-blue-600 transition-colors p-0.5 relative cursor-pointer';
          knob.className = 'w-4 h-4 rounded-full bg-white transition-transform transform translate-x-5';
          showToast('Face ID login enabled for Cashleap');
        }} else {{
          toggle.className = 'w-10 h-5 rounded-full bg-white/20 transition-colors p-0.5 relative cursor-pointer';
          knob.className = 'w-4 h-4 rounded-full bg-white transition-transform transform translate-x-0';
          showToast('Face ID login disabled');
        }}
      }}
    }}

    function triggerProfilePasscodeChange() {{
      playHapticTick();
      closeUserProfileModal();
      showScreen('secretkey');
      showToast('Enter current Secret Key to update passcode');
    }}

    function downloadOfficialStatement() {{
      playHapticTick();
      if (typeof triggerDynamicIsland === 'function') {{
        triggerDynamicIsland('Downloading Statement', 'November 2026 • PDF');
      }}
      showToast('Generating official monthly statement PDF...');
    }}

    /* Draggable & Expandable Bottom Sheet for Recent Transactions */
    let isSheetExpanded = false;
    let isDraggingSheet = false;
    let sheetDragStartY = 0;
    let sheetDragDeltaY = 0;
    let sheetInitialTranslate = 356; // 356px when collapsed, 0px when expanded
    let sheetHasMoved = false;

    const SHEET_COLLAPSED_Y = 356;
    const SHEET_EXPANDED_Y = 0;

    function setSheetExpanded(expanded) {{
      isSheetExpanded = expanded;
      const sheet = document.getElementById('recentTransactionsSheet');
      const toggleLabel = document.getElementById('sheetToggleLabel');
      const toggleChevron = document.getElementById('sheetToggleChevron');
      if (!sheet) return;

      sheet.style.transition = 'transform 0.42s cubic-bezier(0.16, 1, 0.3, 1)';
      
      if (isSheetExpanded) {{
        sheet.style.transform = `translateY(${{SHEET_EXPANDED_Y}}px)`;
        if (toggleLabel) toggleLabel.textContent = 'Collapse';
        if (toggleChevron) toggleChevron.style.transform = 'rotate(180deg)';
      }} else {{
        sheet.style.transform = `translateY(${{SHEET_COLLAPSED_Y}}px)`;
        if (toggleLabel) toggleLabel.textContent = 'See All';
        if (toggleChevron) toggleChevron.style.transform = 'rotate(0deg)';
      }}
    }}

    function toggleTransactionsSheet() {{
      setSheetExpanded(!isSheetExpanded);
    }}

    function initBottomSheetDragging() {{
      const sheet = document.getElementById('recentTransactionsSheet');
      const handleArea = document.getElementById('sheetDragHandleArea');
      if (!sheet || !handleArea) return;

      function onHSheetDown(e) {{
        if (e.target.closest('#sheetToggleBtn')) return;
        e.preventDefault();
        isDraggingSheet = true;
        sheetHasMoved = false;
        sheetDragStartY = e.clientY;
        sheetDragDeltaY = 0;
        sheetInitialTranslate = isSheetExpanded ? SHEET_EXPANDED_Y : SHEET_COLLAPSED_Y;
        sheet.style.transition = 'none';
        handleArea.style.cursor = 'grabbing';
        if (handleArea.setPointerCapture && e.pointerId !== undefined) {{
          try {{ handleArea.setPointerCapture(e.pointerId); }} catch(err) {{}}
        }}
      }}

      function onHSheetMove(e) {{
        if (!isDraggingSheet) return;
        e.preventDefault();
        sheetDragDeltaY = e.clientY - sheetDragStartY;
        if (Math.abs(sheetDragDeltaY) > 3) sheetHasMoved = true;

        let newY = sheetInitialTranslate + sheetDragDeltaY;
        if (newY < SHEET_EXPANDED_Y - 30) {{
          newY = (SHEET_EXPANDED_Y - 30) + (newY - (SHEET_EXPANDED_Y - 30)) * 0.2;
        }} else if (newY > SHEET_COLLAPSED_Y + 40) {{
          newY = (SHEET_COLLAPSED_Y + 40) + (newY - (SHEET_COLLAPSED_Y + 40)) * 0.2;
        }}
        sheet.style.transform = 'translateY(' + newY + 'px)';
      }}

      function onHSheetUp(e) {{
        if (!isDraggingSheet) return;
        isDraggingSheet = false;
        handleArea.style.cursor = 'grab';
        if (handleArea.releasePointerCapture && e && e.pointerId !== undefined) {{
          try {{ handleArea.releasePointerCapture(e.pointerId); }} catch(err) {{}}
        }}
        sheet.style.transition = 'transform 0.42s cubic-bezier(0.16, 1, 0.3, 1)';

        if (sheetHasMoved && Math.abs(sheetDragDeltaY) > 28) {{
          if (sheetDragDeltaY < -28) {{
            setSheetExpanded(true);
          }} else if (sheetDragDeltaY > 28) {{
            setSheetExpanded(false);
          }}
        }} else if (!sheetHasMoved) {{
          toggleTransactionsSheet();
        }} else {{
          setSheetExpanded(isSheetExpanded);
        }}
      }}

      handleArea.addEventListener('pointerdown', onHSheetDown);
      handleArea.addEventListener('pointermove', onHSheetMove);
      handleArea.addEventListener('pointerup', onHSheetUp);
      handleArea.addEventListener('pointercancel', onHSheetUp);

      handleArea.addEventListener('touchstart', (e) => {{
        if (e.target.closest('#sheetToggleBtn')) return;
        if (e.touches && e.touches[0]) {{
          e.preventDefault();
          onHSheetDown({{
            clientY: e.touches[0].clientY,
            pointerId: undefined,
            target: e.target,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchmove', (e) => {{
        if (!isDraggingSheet) return;
        if (e.touches && e.touches[0]) {{
          if (e.cancelable) e.preventDefault();
          onHSheetMove({{
            clientY: e.touches[0].clientY,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchend', (e) => {{
        if (isDraggingSheet) onHSheetUp(e);
      }});

      handleArea.addEventListener('mousedown', onHSheetDown);
      window.addEventListener('mousemove', (e) => {{
        if (isDraggingSheet) onHSheetMove(e);
      }});
      window.addEventListener('mouseup', (e) => {{
        if (isDraggingSheet) onHSheetUp(e);
      }});
    }}

    /* Draggable & Expandable Categories Bottom Sheet on Statistics Screen */
    let isStatsSheetExpanded = false;
    let isDraggingStatsSheet = false;
    let statsSheetDragStartY = 0;
    let statsSheetInitialTranslate = 338;
    let statsSheetDragDeltaY = 0;
    let statsSheetHasMoved = false;
    const STATS_SHEET_COLLAPSED_Y = 338;
    const STATS_SHEET_EXPANDED_Y = 0;

    function setStatsSheetExpanded(expanded) {{
      isStatsSheetExpanded = expanded;
      const sheet = document.getElementById('statsCategoriesSheet');
      const toggleLabel = document.getElementById('statsSheetToggleLabel');
      const toggleChevron = document.getElementById('statsSheetToggleChevron');
      if (!sheet) return;

      sheet.style.transition = 'transform 0.42s cubic-bezier(0.16, 1, 0.3, 1)';
      
      if (isStatsSheetExpanded) {{
        sheet.style.transform = 'translateY(' + STATS_SHEET_EXPANDED_Y + 'px)';
        if (toggleLabel) toggleLabel.textContent = 'Collapse';
        if (toggleChevron) toggleChevron.style.transform = 'rotate(180deg)';
      }} else {{
        sheet.style.transform = 'translateY(' + STATS_SHEET_COLLAPSED_Y + 'px)';
        if (toggleLabel) toggleLabel.textContent = 'See All';
        if (toggleChevron) toggleChevron.style.transform = 'rotate(0deg)';
      }}
    }}

    function toggleStatsCategoriesSheet() {{
      playHapticTick();
      setStatsSheetExpanded(!isStatsSheetExpanded);
    }}

    function initStatsBottomSheetDragging() {{
      const sheet = document.getElementById('statsCategoriesSheet');
      const handleArea = document.getElementById('statsSheetDragHandleArea');
      if (!sheet || !handleArea) return;

      function onPointerDown(e) {{
        if (e.target.closest('#statsSheetToggleBtn')) return;
        e.preventDefault();
        isDraggingStatsSheet = true;
        statsSheetHasMoved = false;
        statsSheetDragStartY = e.clientY;
        statsSheetDragDeltaY = 0;
        statsSheetInitialTranslate = isStatsSheetExpanded ? STATS_SHEET_EXPANDED_Y : STATS_SHEET_COLLAPSED_Y;
        sheet.style.transition = 'none';
        handleArea.style.cursor = 'grabbing';
        if (handleArea.setPointerCapture && e.pointerId !== undefined) {{
          try {{ handleArea.setPointerCapture(e.pointerId); }} catch(err) {{}}
        }}
      }}

      function onPointerMove(e) {{
        if (!isDraggingStatsSheet) return;
        e.preventDefault();
        statsSheetDragDeltaY = e.clientY - statsSheetDragStartY;
        if (Math.abs(statsSheetDragDeltaY) > 3) statsSheetHasMoved = true;

        let newY = statsSheetInitialTranslate + statsSheetDragDeltaY;
        if (newY < STATS_SHEET_EXPANDED_Y - 30) {{
          newY = (STATS_SHEET_EXPANDED_Y - 30) + (newY - (STATS_SHEET_EXPANDED_Y - 30)) * 0.2;
        }} else if (newY > STATS_SHEET_COLLAPSED_Y + 40) {{
          newY = (STATS_SHEET_COLLAPSED_Y + 40) + (newY - (STATS_SHEET_COLLAPSED_Y + 40)) * 0.2;
        }}
        sheet.style.transform = 'translateY(' + newY + 'px)';
      }}

      function onPointerUp(e) {{
        if (!isDraggingStatsSheet) return;
        isDraggingStatsSheet = false;
        handleArea.style.cursor = 'grab';
        if (handleArea.releasePointerCapture && e && e.pointerId !== undefined) {{
          try {{ handleArea.releasePointerCapture(e.pointerId); }} catch(err) {{}}
        }}
        sheet.style.transition = 'transform 0.42s cubic-bezier(0.16, 1, 0.3, 1)';

        if (statsSheetHasMoved && Math.abs(statsSheetDragDeltaY) > 28) {{
          if (statsSheetDragDeltaY < -28) {{
            setStatsSheetExpanded(true);
          }} else if (statsSheetDragDeltaY > 28) {{
            setStatsSheetExpanded(false);
          }}
        }} else if (!statsSheetHasMoved) {{
          toggleStatsCategoriesSheet();
        }} else {{
          setStatsSheetExpanded(isStatsSheetExpanded);
        }}
      }}

      // Modern Pointer Events
      handleArea.addEventListener('pointerdown', onPointerDown);
      handleArea.addEventListener('pointermove', onPointerMove);
      handleArea.addEventListener('pointerup', onPointerUp);
      handleArea.addEventListener('pointercancel', onPointerUp);

      // Touch fallback
      handleArea.addEventListener('touchstart', (e) => {{
        if (e.target.closest('#statsSheetToggleBtn')) return;
        if (e.touches && e.touches[0]) {{
          e.preventDefault();
          onPointerDown({{
            clientY: e.touches[0].clientY,
            pointerId: undefined,
            target: e.target,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchmove', (e) => {{
        if (!isDraggingStatsSheet) return;
        if (e.touches && e.touches[0]) {{
          if (e.cancelable) e.preventDefault();
          onPointerMove({{
            clientY: e.touches[0].clientY,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchend', (e) => {{
        if (isDraggingStatsSheet) onPointerUp(e);
      }});

      // Mouse fallback
      handleArea.addEventListener('mousedown', onPointerDown);
      window.addEventListener('mousemove', (e) => {{
        if (isDraggingStatsSheet) onPointerMove(e);
      }});
      window.addEventListener('mouseup', (e) => {{
        if (isDraggingStatsSheet) onPointerUp(e);
      }});
    }}


    /* ========================================================
       FINANCE & WALLET FEATURES BOTTOM SHEET DRAGGING ENGINES
       ======================================================== */
    let isFinanceSheetExpanded = false;
    let isDraggingFinanceSheet = false;
    let financeSheetDragStartY = 0;
    let financeSheetDragDeltaY = 0;
    let financeSheetInitialTranslate = 325;
    let financeSheetHasMoved = false;

    const FINANCE_SHEET_COLLAPSED_Y = 325;
    const FINANCE_SHEET_EXPANDED_Y = 0;

    function setFinanceSheetExpanded(expanded) {{
      playHapticTick();
      isFinanceSheetExpanded = expanded;
      const sheet = document.getElementById('financeBottomSheet');
      const label = document.getElementById('financeSheetToggleLabel');
      const chevron = document.getElementById('financeSheetToggleChevron');
      if (!sheet) return;
      sheet.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
      const targetY = expanded ? FINANCE_SHEET_EXPANDED_Y : FINANCE_SHEET_COLLAPSED_Y;
      sheet.style.transform = 'translateY(' + targetY + 'px)';
      if (label) label.textContent = expanded ? 'Collapse' : 'See All';
      if (chevron) chevron.style.transform = expanded ? 'rotate(180deg)' : 'rotate(0deg)';
    }}

    function toggleFinanceBottomSheet() {{
      setFinanceSheetExpanded(!isFinanceSheetExpanded);
    }}

    function initFinanceBottomSheetDragging() {{
      const sheet = document.getElementById('financeBottomSheet');
      const handleArea = document.getElementById('financeSheetDragHandleArea');
      if (!sheet || !handleArea) return;

      function onFSheetDown(e) {{
        if (e.target.closest('#financeSheetToggleBtn')) return;
        e.preventDefault();
        isDraggingFinanceSheet = true;
        financeSheetHasMoved = false;
        financeSheetDragStartY = e.clientY;
        financeSheetDragDeltaY = 0;
        financeSheetInitialTranslate = isFinanceSheetExpanded ? FINANCE_SHEET_EXPANDED_Y : FINANCE_SHEET_COLLAPSED_Y;
        sheet.style.transition = 'none';
        handleArea.style.cursor = 'grabbing';
        if (handleArea.setPointerCapture && e.pointerId !== undefined) {{
          try {{ handleArea.setPointerCapture(e.pointerId); }} catch(err) {{}}
        }}
      }}

      function onFSheetMove(e) {{
        if (!isDraggingFinanceSheet) return;
        e.preventDefault();
        financeSheetDragDeltaY = e.clientY - financeSheetDragStartY;
        if (Math.abs(financeSheetDragDeltaY) > 3) financeSheetHasMoved = true;

        let newY = financeSheetInitialTranslate + financeSheetDragDeltaY;
        if (newY < FINANCE_SHEET_EXPANDED_Y - 30) {{
          newY = (FINANCE_SHEET_EXPANDED_Y - 30) + (newY - (FINANCE_SHEET_EXPANDED_Y - 30)) * 0.2;
        }} else if (newY > FINANCE_SHEET_COLLAPSED_Y + 40) {{
          newY = (FINANCE_SHEET_COLLAPSED_Y + 40) + (newY - (FINANCE_SHEET_COLLAPSED_Y + 40)) * 0.2;
        }}
        sheet.style.transform = 'translateY(' + newY + 'px)';
      }}

      function onFSheetUp(e) {{
        if (!isDraggingFinanceSheet) return;
        isDraggingFinanceSheet = false;
        handleArea.style.cursor = 'grab';
        if (handleArea.releasePointerCapture && e && e.pointerId !== undefined) {{
          try {{ handleArea.releasePointerCapture(e.pointerId); }} catch(err) {{}}
        }}

        if (!financeSheetHasMoved) {{
          toggleFinanceBottomSheet();
          return;
        }}

        if (isFinanceSheetExpanded) {{
          if (financeSheetDragDeltaY > 40) {{
            setFinanceSheetExpanded(false);
          }} else {{
            setFinanceSheetExpanded(true);
          }}
        }} else {{
          if (financeSheetDragDeltaY < -40) {{
            setFinanceSheetExpanded(true);
          }} else {{
            setFinanceSheetExpanded(false);
          }}
        }}
      }}

      handleArea.addEventListener('pointerdown', onFSheetDown);
      handleArea.addEventListener('pointermove', onFSheetMove);
      handleArea.addEventListener('pointerup', onFSheetUp);
      handleArea.addEventListener('pointercancel', onFSheetUp);

      handleArea.addEventListener('touchstart', (e) => {{
        if (e.target.closest('#financeSheetToggleBtn')) return;
        if (e.touches && e.touches[0]) {{
          e.preventDefault();
          onFSheetDown({{
            clientY: e.touches[0].clientY,
            pointerId: undefined,
            target: e.target,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchmove', (e) => {{
        if (!isDraggingFinanceSheet) return;
        if (e.touches && e.touches[0]) {{
          if (e.cancelable) e.preventDefault();
          onFSheetMove({{
            clientY: e.touches[0].clientY,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchend', (e) => {{
        if (isDraggingFinanceSheet) onFSheetUp(e);
      }});

      handleArea.addEventListener('mousedown', onFSheetDown);
      window.addEventListener('mousemove', (e) => {{
        if (isDraggingFinanceSheet) onFSheetMove(e);
      }});
      window.addEventListener('mouseup', (e) => {{
        if (isDraggingFinanceSheet) onFSheetUp(e);
      }});
    }}

    /* OTHERS & WALLET FEATURES BOTTOM SHEET DRAGGING */
    let isOthersSheetExpanded = false;
    let isDraggingOthersSheet = false;
    let othersSheetDragStartY = 0;
    let othersSheetDragDeltaY = 0;
    let othersSheetInitialTranslate = 325;
    let othersSheetHasMoved = false;

    const OTHERS_SHEET_COLLAPSED_Y = 325;
    const OTHERS_SHEET_EXPANDED_Y = 0;

    function setOthersSheetExpanded(expanded) {{
      playHapticTick();
      isOthersSheetExpanded = expanded;
      const sheet = document.getElementById('othersBottomSheet');
      const label = document.getElementById('othersSheetToggleLabel');
      const chevron = document.getElementById('othersSheetToggleChevron');
      if (!sheet) return;
      sheet.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
      const targetY = expanded ? OTHERS_SHEET_EXPANDED_Y : OTHERS_SHEET_COLLAPSED_Y;
      sheet.style.transform = 'translateY(' + targetY + 'px)';
      if (label) label.textContent = expanded ? 'Collapse' : 'See All';
      if (chevron) chevron.style.transform = expanded ? 'rotate(180deg)' : 'rotate(0deg)';
    }}

    function toggleOthersBottomSheet() {{
      setOthersSheetExpanded(!isOthersSheetExpanded);
    }}

    function initOthersBottomSheetDragging() {{
      const sheet = document.getElementById('othersBottomSheet');
      const handleArea = document.getElementById('othersSheetDragHandleArea');
      if (!sheet || !handleArea) return;

      function onOSheetDown(e) {{
        if (e.target.closest('#othersSheetToggleBtn')) return;
        e.preventDefault();
        isDraggingOthersSheet = true;
        othersSheetHasMoved = false;
        othersSheetDragStartY = e.clientY;
        othersSheetDragDeltaY = 0;
        othersSheetInitialTranslate = isOthersSheetExpanded ? OTHERS_SHEET_EXPANDED_Y : OTHERS_SHEET_COLLAPSED_Y;
        sheet.style.transition = 'none';
        handleArea.style.cursor = 'grabbing';
        if (handleArea.setPointerCapture && e.pointerId !== undefined) {{
          try {{ handleArea.setPointerCapture(e.pointerId); }} catch(err) {{}}
        }}
      }}

      function onOSheetMove(e) {{
        if (!isDraggingOthersSheet) return;
        e.preventDefault();
        othersSheetDragDeltaY = e.clientY - othersSheetDragStartY;
        if (Math.abs(othersSheetDragDeltaY) > 3) othersSheetHasMoved = true;

        let newY = othersSheetInitialTranslate + othersSheetDragDeltaY;
        if (newY < OTHERS_SHEET_EXPANDED_Y - 30) {{
          newY = (OTHERS_SHEET_EXPANDED_Y - 30) + (newY - (OTHERS_SHEET_EXPANDED_Y - 30)) * 0.2;
        }} else if (newY > OTHERS_SHEET_COLLAPSED_Y + 40) {{
          newY = (OTHERS_SHEET_COLLAPSED_Y + 40) + (newY - (OTHERS_SHEET_COLLAPSED_Y + 40)) * 0.2;
        }}
        sheet.style.transform = 'translateY(' + newY + 'px)';
      }}

      function onOSheetUp(e) {{
        if (!isDraggingOthersSheet) return;
        isDraggingOthersSheet = false;
        handleArea.style.cursor = 'grab';
        if (handleArea.releasePointerCapture && e && e.pointerId !== undefined) {{
          try {{ handleArea.releasePointerCapture(e.pointerId); }} catch(err) {{}}
        }}

        if (!othersSheetHasMoved) {{
          toggleOthersBottomSheet();
          return;
        }}

        if (isOthersSheetExpanded) {{
          if (othersSheetDragDeltaY > 40) {{
            setOthersSheetExpanded(false);
          }} else {{
            setOthersSheetExpanded(true);
          }}
        }} else {{
          if (othersSheetDragDeltaY < -40) {{
            setOthersSheetExpanded(true);
          }} else {{
            setOthersSheetExpanded(false);
          }}
        }}
      }}

      handleArea.addEventListener('pointerdown', onOSheetDown);
      handleArea.addEventListener('pointermove', onOSheetMove);
      handleArea.addEventListener('pointerup', onOSheetUp);
      handleArea.addEventListener('pointercancel', onOSheetUp);

      handleArea.addEventListener('touchstart', (e) => {{
        if (e.target.closest('#othersSheetToggleBtn')) return;
        if (e.touches && e.touches[0]) {{
          e.preventDefault();
          onOSheetDown({{
            clientY: e.touches[0].clientY,
            pointerId: undefined,
            target: e.target,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchmove', (e) => {{
        if (!isDraggingOthersSheet) return;
        if (e.touches && e.touches[0]) {{
          if (e.cancelable) e.preventDefault();
          onOSheetMove({{
            clientY: e.touches[0].clientY,
            preventDefault: () => {{}}
          }});
        }}
      }}, {{ passive: false }});

      window.addEventListener('touchend', (e) => {{
        if (isDraggingOthersSheet) onOSheetUp(e);
      }});

      handleArea.addEventListener('mousedown', onOSheetDown);
      window.addEventListener('mousemove', (e) => {{
        if (isDraggingOthersSheet) onOSheetMove(e);
      }});
      window.addEventListener('mouseup', (e) => {{
        if (isDraggingOthersSheet) onOSheetUp(e);
      }});
    }}

    /* ========================================================
       SAVINGS VAULT SCREEN & INTERACTIVE FLOW CONTROLLERS
       ======================================================== */
    let isVaultSheetExpanded = false;
    const VAULT_SHEET_COLLAPSED_Y = 338;
    const VAULT_SHEET_EXPANDED_Y = 0;

    const vaultsState = {{
      emergency: {{ name: 'Emergency Reserve', balance: 12000, target: 15000, apy: '4.85% APY' }},
      tokyo: {{ name: 'Tokyo Vacation 2025', balance: 4200, target: 6000, apy: '4.50% APY' }},
      gold: {{ name: 'Gold & Yield Reserve', balance: 2200, target: 5000, apy: '5.10% APY' }}
    }};

    let currentVaultActionMode = 'deposit';
    let currentSelectedVaultKey = 'emergency';
    let isVaultAutoSaveOn = true;

    function setVaultSheetExpanded(expanded) {{
      playHapticTick();
      isVaultSheetExpanded = expanded;
      const sheet = document.getElementById('vaultGoalsSheet');
      const label = document.getElementById('vaultSheetToggleLabel');
      const chevron = document.getElementById('vaultSheetToggleChevron');
      if (!sheet) return;
      sheet.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
      const targetY = expanded ? VAULT_SHEET_EXPANDED_Y : VAULT_SHEET_COLLAPSED_Y;
      sheet.style.transform = 'translateY(' + targetY + 'px)';
      if (label) label.textContent = expanded ? 'Collapse' : 'See All';
      if (chevron) chevron.style.transform = expanded ? 'rotate(180deg)' : 'rotate(0deg)';
    }}

    function toggleVaultBottomSheet() {{
      setVaultSheetExpanded(!isVaultSheetExpanded);
    }}

    function refreshVaultTotalsUI() {{
      let totalBal = 0;
      let totalTarget = 0;
      Object.keys(vaultsState).forEach(k => {{
        const v = vaultsState[k];
        totalBal += v.balance;
        totalTarget += v.target;
        const pct = Math.min(100, Math.round((v.balance / Math.max(1, v.target)) * 100));
        const balEl = document.getElementById('vault-bal-' + k);
        const pctEl = document.getElementById('vault-pct-' + k);
        const barEl = document.getElementById('vault-bar-' + k);
        if (balEl) balEl.textContent = v.balance.toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }}) + ' AED';
        if (pctEl) pctEl.textContent = pct + '% of ' + v.target.toLocaleString('en-US');
        if (barEl) barEl.style.width = pct + '%';
      }});

      const formattedTotal = totalBal.toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
      const vaultTotalEl = document.getElementById('vaultTotalBalance');
      const financeVaultsEl = document.getElementById('financeVaultsBal');
      if (vaultTotalEl) vaultTotalEl.textContent = formattedTotal;
      if (financeVaultsEl) financeVaultsEl.textContent = formattedTotal + ' AED';

      const overallPct = Math.min(100, Math.round((totalBal / Math.max(1, totalTarget)) * 100));
      const overallLabel = document.getElementById('vaultOverallProgressLabel');
      const overallBar = document.getElementById('vaultOverallProgressBar');
      if (overallLabel) overallLabel.textContent = overallPct + '% of ' + totalTarget.toLocaleString('en-US') + ' AED';
      if (overallBar) overallBar.style.width = overallPct + '%';

      const countBadge = document.getElementById('vaultActiveCountBadge');
      if (countBadge) countBadge.textContent = Object.keys(vaultsState).length + ' Goals';
    }}

    function handleAccountClick(name, balance, desc) {{
      playHapticTick();
      if (name.toLowerCase().includes('vault') || name.toLowerCase().includes('tokyo') || name.toLowerCase().includes('emergency')) {{
        showScreen('vault');
        triggerDynamicIsland('Savings Vaults', name + ' • ' + balance);
      }} else {{
        triggerDynamicIsland(name, balance);
        showToast(name + ': ' + balance);
      }}
    }}

    function openCreateVaultModal() {{
      playHapticTick();
      const modal = document.getElementById('createVaultModal');
      const sheet = document.getElementById('createVaultSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        setTimeout(() => sheet.classList.remove('translate-y-full'), 10);
      }}
    }}

    function closeCreateVaultModal() {{
      playHapticTick();
      const modal = document.getElementById('createVaultModal');
      const sheet = document.getElementById('createVaultSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      setTimeout(() => {{
        if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
      }}, 300);
    }}

    function selectVaultCategory(cat, defaultName, defaultTarget) {{
      playHapticTick();
      const nameInput = document.getElementById('newVaultNameInput');
      const targetInput = document.getElementById('newVaultTargetInput');
      if (nameInput) nameInput.value = defaultName;
      if (targetInput) targetInput.value = defaultTarget;

      const map = {{ Travel: 'vault-cat-travel', Reserve: 'vault-cat-reserve', Purchase: 'vault-cat-tech', Wealth: 'vault-cat-wealth' }};
      Object.keys(map).forEach(k => {{
        const btn = document.getElementById(map[k]);
        if (!btn) return;
        if (k === cat) {{
          btn.className = 'vault-cat-pill py-2 px-1.5 rounded-xl bg-blue-600/25 border border-blue-500/60 text-white text-[10.5px] font-semibold flex flex-col items-center gap-1 transition cursor-pointer';
        }} else {{
          btn.className = 'vault-cat-pill py-2 px-1.5 rounded-xl bg-white/[0.04] border border-white/10 text-[#9e94b8] hover:text-white text-[10.5px] font-medium flex flex-col items-center gap-1 transition cursor-pointer';
        }}
      }});
    }}

    let selectedVaultTermRate = '4.50% APY';
    function selectVaultTerm(term) {{
      playHapticTick();
      const flexBtn = document.getElementById('vault-term-flex');
      const fixedBtn = document.getElementById('vault-term-fixed');
      if (term === 'flex') {{
        selectedVaultTermRate = '4.50% APY';
        if (flexBtn) flexBtn.className = 'p-2.5 rounded-xl bg-blue-600/20 border border-blue-500/60 text-left transition cursor-pointer';
        if (fixedBtn) fixedBtn.className = 'p-2.5 rounded-xl bg-white/[0.04] border border-white/10 text-left transition cursor-pointer';
      }} else {{
        selectedVaultTermRate = '5.10% APY';
        if (fixedBtn) fixedBtn.className = 'p-2.5 rounded-xl bg-emerald-600/20 border border-emerald-500/60 text-left transition cursor-pointer';
        if (flexBtn) flexBtn.className = 'p-2.5 rounded-xl bg-white/[0.04] border border-white/10 text-left transition cursor-pointer';
      }}
    }}

    function confirmCreateVault() {{
      playSuccessChime();
      const nameEl = document.getElementById('newVaultNameInput');
      const targetEl = document.getElementById('newVaultTargetInput');
      const initEl = document.getElementById('newVaultInitialInput');

      const name = (nameEl && nameEl.value.trim()) ? nameEl.value.trim() : 'Custom Savings Goal';
      const target = Math.max(500, parseFloat(targetEl ? targetEl.value : '8000') || 8000);
      const initial = Math.max(0, parseFloat(initEl ? initEl.value : '1000') || 1000);
      const pct = Math.min(100, Math.round((initial / target) * 100));
      const key = 'custom_' + Date.now() + '_' + Object.keys(vaultsState).length;

      vaultsState[key] = {{
        name: name,
        balance: initial,
        target: target,
        apy: selectedVaultTermRate
      }};

      const list = document.getElementById('vaultGoalsList');
      if (list) {{
        const row = document.createElement('div');
        row.className = 'py-3.5 hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press';
        row.onclick = function() {{ openVaultActionModal('deposit', key); }};
        row.innerHTML =
          '<div class="flex items-center justify-between mb-2">' +
            '<div class="flex items-center gap-3.5">' +
              '<div class="w-10 h-10 rounded-full bg-white/[0.06] border border-white/20 flex items-center justify-center text-white/90 shadow-sm flex-shrink-0">' +
                '<svg class="w-5 h-5 text-white/90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
                  '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>' +
                '</svg>' +
              '</div>' +
              '<div class="flex flex-col">' +
                '<span class="text-[14.5px] font-semibold text-white tracking-tight">' + name + '</span>' +
                '<span class="text-[11px] text-[#9e94b8]">' + selectedVaultTermRate + ' • Custom Goal</span>' +
              '</div>' +
            '</div>' +
            '<div class="flex flex-col items-end">' +
              '<span id="vault-bal-' + key + '" class="text-[14.5px] font-bold text-white tracking-tight whitespace-nowrap">' + initial.toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }}) + ' AED</span>' +
              '<span id="vault-pct-' + key + '" class="text-[10.5px] text-emerald-400 font-semibold">' + pct + '% of ' + target.toLocaleString('en-US') + '</span>' +
            '</div>' +
          '</div>' +
          '<div class="w-full h-1.5 rounded-full bg-white/[0.07] overflow-hidden">' +
            '<div id="vault-bar-' + key + '" class="h-full rounded-full bg-gradient-to-r from-blue-500 to-emerald-400 transition-all duration-500" style="width: ' + pct + '%;"></div>' +
          '</div>';
        list.insertBefore(row, list.firstChild);
      }}

      refreshVaultTotalsUI();
      closeCreateVaultModal();
      if (currentScreen !== 'vault') {{
        showScreen('vault');
      }}
      triggerDynamicIsland('Vault Created', name + ' (' + initial.toFixed(0) + ' AED)');
      showToast('Created "' + name + '" vault with ' + initial.toFixed(2) + ' AED');
    }}

    function openVaultActionModal(mode, vaultKey) {{
      playHapticTick();
      currentVaultActionMode = mode || 'deposit';
      currentSelectedVaultKey = (vaultKey && vaultsState[vaultKey]) ? vaultKey : 'emergency';
      setVaultActionMode(currentVaultActionMode);
      selectTargetVault(currentSelectedVaultKey);

      const modal = document.getElementById('vaultActionModal');
      const sheet = document.getElementById('vaultActionSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        setTimeout(() => sheet.classList.remove('translate-y-full'), 10);
      }}
    }}

    function closeVaultActionModal() {{
      playHapticTick();
      const modal = document.getElementById('vaultActionModal');
      const sheet = document.getElementById('vaultActionSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      setTimeout(() => {{
        if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
      }}, 300);
    }}

    function setVaultActionMode(mode) {{
      playHapticTick();
      currentVaultActionMode = mode;
      const depBtn = document.getElementById('vault-mode-deposit');
      const witBtn = document.getElementById('vault-mode-withdraw');
      const titleEl = document.getElementById('vaultActionModalTitle');
      const subEl = document.getElementById('vaultActionModalSub');
      const submitBtn = document.getElementById('vaultActionSubmitBtn');

      if (mode === 'deposit') {{
        if (depBtn) depBtn.className = 'py-2 rounded-lg bg-blue-600 text-white text-xs font-bold transition cursor-pointer';
        if (witBtn) witBtn.className = 'py-2 rounded-lg text-[#9e94b8] hover:text-white text-xs font-semibold transition cursor-pointer';
        if (titleEl) titleEl.textContent = 'Deposit to Vault';
        if (subEl) subEl.textContent = 'Instant transfer from Cashleap Mastercard (•••• 0329)';
        if (submitBtn) submitBtn.innerHTML = '<span>Confirm Instant Deposit</span>';
      }} else {{
        if (witBtn) witBtn.className = 'py-2 rounded-lg bg-indigo-600 text-white text-xs font-bold transition cursor-pointer';
        if (depBtn) depBtn.className = 'py-2 rounded-lg text-[#9e94b8] hover:text-white text-xs font-semibold transition cursor-pointer';
        if (titleEl) titleEl.textContent = 'Withdraw from Vault';
        if (subEl) subEl.textContent = 'Instant release back to Cashleap Mastercard (•••• 0329)';
        if (submitBtn) submitBtn.innerHTML = '<span>Confirm Instant Withdrawal</span>';
      }}
    }}

    function selectTargetVault(key) {{
      playHapticTick();
      if (!vaultsState[key]) key = 'emergency';
      currentSelectedVaultKey = key;
      const v = vaultsState[key];

      ['emergency', 'tokyo', 'gold'].forEach(k => {{
        const btn = document.getElementById('vault-sel-' + k);
        if (!btn) return;
        if (k === key) {{
          btn.className = 'py-2 px-2 rounded-xl bg-blue-600/25 border border-blue-500/60 text-[10.5px] font-semibold text-white truncate transition cursor-pointer';
        }} else {{
          btn.className = 'py-2 px-2 rounded-xl bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] truncate transition cursor-pointer';
        }}
      }});

      const nameLbl = document.getElementById('vaultSelectedNameLabel');
      const apyLbl = document.getElementById('vaultSelectedApyLabel');
      const balLbl = document.getElementById('vaultSelectedBalLabel');
      if (nameLbl) nameLbl.textContent = v.name;
      if (apyLbl) apyLbl.textContent = v.apy + ' • Goal: ' + v.target.toLocaleString('en-US') + ' AED';
      if (balLbl) balLbl.textContent = v.balance.toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }}) + ' AED';
    }}

    function setVaultPresetAmount(val) {{
      playHapticTick();
      const input = document.getElementById('vaultActionAmountInput');
      if (input) input.value = val;
    }}

    function executeVaultAction() {{
      playSuccessChime();
      const input = document.getElementById('vaultActionAmountInput');
      const amt = Math.max(10, parseFloat(input ? input.value : '500') || 500);
      const v = vaultsState[currentSelectedVaultKey] || vaultsState.emergency;

      if (currentVaultActionMode === 'deposit') {{
        v.balance += amt;
        triggerDynamicIsland('Vault Deposit', '+' + amt.toFixed(2) + ' AED to ' + v.name);
        showToast('Deposited ' + amt.toFixed(2) + ' AED into ' + v.name);
      }} else {{
        v.balance = Math.max(0, v.balance - amt);
        triggerDynamicIsland('Vault Withdrawal', '-' + amt.toFixed(2) + ' AED from ' + v.name);
        showToast('Withdrew ' + amt.toFixed(2) + ' AED to Mastercard •••• 0329');
      }}

      refreshVaultTotalsUI();
      closeVaultActionModal();
    }}

    function toggleVaultAutoSave() {{
      playHapticTick();
      isVaultAutoSaveOn = !isVaultAutoSaveOn;
      const lbl = document.getElementById('vaultAutoSaveQuickLabel');
      if (isVaultAutoSaveOn) {{
        if (lbl) {{
          lbl.textContent = 'Auto-Save';
          lbl.className = 'text-xs text-emerald-400 font-medium mt-1.5';
        }}
        triggerDynamicIsland('Auto-Save Enabled', '2x Spare Change Round-Up active');
        showToast('Spare change round-up enabled for active vaults');
      }} else {{
        if (lbl) {{
          lbl.textContent = 'Paused';
          lbl.className = 'text-xs text-[#a09bb8] font-medium mt-1.5';
        }}
        triggerDynamicIsland('Auto-Save Paused', 'Round-Up transfers paused');
        showToast('Spare change auto-save paused');
      }}
    }}

    /* ========================================================
       WALLET FEATURES INTERACTION HANDLERS (MODALS & ACTIONS)
       ======================================================== */
    let selectedBillProvider = 'DEWA Electricity & Water';
    function selectBillProvider(name) {{
      playHapticTick();
      selectedBillProvider = name;
      const pills = document.querySelectorAll('.bill-provider-pill');
      pills.forEach(p => {{
        p.classList.remove('active', 'border-blue-400', 'text-white');
        p.classList.add('border-white/10', 'text-[#9e94b8]');
      }});
      if (name.startsWith('DEWA')) {{
        const b = document.getElementById('provider-dewa');
        if (b) {{ b.classList.add('active', 'border-blue-400', 'text-white'); b.classList.remove('text-[#9e94b8]'); }}
        const l = document.getElementById('billAccountLabel');
        if (l) l.textContent = 'DEWA Premise Number';
        const a = document.getElementById('billAmountInput');
        if (a) a.value = '285.50';
      }} else if (name.startsWith('Salik')) {{
        const b = document.getElementById('provider-salik');
        if (b) {{ b.classList.add('active', 'border-blue-400', 'text-white'); b.classList.remove('text-[#9e94b8]'); }}
        const l = document.getElementById('billAccountLabel');
        if (l) l.textContent = 'Salik Tag Account PIN';
        const a = document.getElementById('billAmountInput');
        if (a) a.value = '100.00';
      }} else {{
        const b = document.getElementById('provider-telecom');
        if (b) {{ b.classList.add('active', 'border-blue-400', 'text-white'); b.classList.remove('text-[#9e94b8]'); }}
        const l = document.getElementById('billAccountLabel');
        if (l) l.textContent = 'Mobile Phone Number';
        const a = document.getElementById('billAmountInput');
        if (a) a.value = '150.00';
      }}
    }}

    function openBillPayModal() {{
      playHapticTick();
      const modal = document.getElementById('billPayModal');
      const sheet = document.getElementById('billPaySheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        setTimeout(() => sheet.classList.remove('translate-y-full'), 10);
      }}
    }}

    function closeBillPayModal() {{
      playHapticTick();
      const modal = document.getElementById('billPayModal');
      const sheet = document.getElementById('billPaySheet');
      if (sheet) sheet.classList.add('translate-y-full');
      setTimeout(() => {{ if (modal) modal.classList.add('opacity-0', 'pointer-events-none'); }}, 300);
    }}

    function executeBillPayment() {{
      const amt = document.getElementById('billAmountInput').value || '285.50';
      closeBillPayModal();
      playSuccessChime();
      triggerDynamicIsland('Bill Paid: ' + amt + ' AED', selectedBillProvider);
      showToast('Successfully paid ' + amt + ' AED for ' + selectedBillProvider);
    }}

    /* Split Bill Logic */
    let currentSplitCount = 4;
    function setSplitCount(cnt) {{
      playHapticTick();
      currentSplitCount = cnt;
      [2, 3, 4, 5].forEach(n => {{
        const btn = document.getElementById('split-' + n);
        if (btn) {{
          if (n === cnt) {{
            btn.className = 'split-btn active py-2 rounded-xl bg-white/[0.08] border border-blue-400 text-center text-sm font-bold text-white transition apple-press';
          }} else {{
            btn.className = 'split-btn py-2 rounded-xl bg-white/[0.04] border border-white/10 text-center text-sm font-semibold text-[#9e94b8] hover:text-white transition apple-press';
          }}
        }}
      }});
      updateSplitCalculation();
    }}

    function updateSplitCalculation() {{
      const total = parseFloat(document.getElementById('splitTotalInput').value) || 0;
      const each = (total / currentSplitCount).toFixed(2);
      const out = document.getElementById('splitEachAmount');
      if (out) out.textContent = each;
    }}

    function openSplitBillModal() {{
      playHapticTick();
      const modal = document.getElementById('splitBillModal');
      const sheet = document.getElementById('splitBillSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        setTimeout(() => sheet.classList.remove('translate-y-full'), 10);
      }}
    }}

    function closeSplitBillModal() {{
      playHapticTick();
      const modal = document.getElementById('splitBillModal');
      const sheet = document.getElementById('splitBillSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      setTimeout(() => {{ if (modal) modal.classList.add('opacity-0', 'pointer-events-none'); }}, 300);
    }}

    function generateSplitBillLink() {{
      closeSplitBillModal();
      playSuccessChime();
      const each = document.getElementById('splitEachAmount').textContent;
      triggerDynamicIsland('Split Link Copied', each + ' AED per person');
      showToast('Split link copied! Share with your ' + currentSplitCount + ' friends');
    }}

    /* Gift Cards & Vouchers */
    let currentVoucherFilter = 'all';
    function filterVouchers(category) {{
      playHapticTick();
      currentVoucherFilter = category;
      const pills = document.querySelectorAll('.voucher-cat-pill');
      pills.forEach(p => {{
        const cat = p.getAttribute('data-voucher-cat');
        if (cat === category) {{
          p.className = 'voucher-cat-pill px-3 py-1.5 rounded-full bg-blue-600/30 border border-blue-400/50 text-[11px] font-semibold text-white transition cursor-pointer flex-shrink-0';
        }} else {{
          p.className = 'voucher-cat-pill px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/10 text-[11px] font-medium text-[#9e94b8] hover:text-white transition cursor-pointer flex-shrink-0';
        }}
      }});
      const cards = document.querySelectorAll('#voucherCardsGrid .voucher-card');
      cards.forEach(card => {{
        const cardCat = card.getAttribute('data-voucher-cat');
        if (category === 'all' || cardCat === category) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    function openGiftCardsModal() {{
      playHapticTick();
      const modal = document.getElementById('giftCardsModal');
      const sheet = document.getElementById('giftCardsSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        setTimeout(() => sheet.classList.remove('translate-y-full'), 10);
      }}
    }}

    function closeGiftCardsModal() {{
      playHapticTick();
      const modal = document.getElementById('giftCardsModal');
      const sheet = document.getElementById('giftCardsSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      setTimeout(() => {{ if (modal) modal.classList.add('opacity-0', 'pointer-events-none'); }}, 300);
    }}

    function purchaseGiftCard(brand, amount) {{
      closeGiftCardsModal();
      playSuccessChime();
      updateBalanceCounter(amount, false);

      // Prepend transaction to Home Recent Transactions list
      const list = document.getElementById('sheetScrollArea');
      if (list) {{
        const row = document.createElement('div');
        row.className = 'flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] transition cursor-pointer rounded-xl px-2 -mx-2 select-none';
        row.innerHTML =
          '<div class="flex items-center gap-3.5">' +
            '<div class="w-11 h-11 rounded-full bg-gradient-to-tr from-purple-600 to-indigo-500 flex items-center justify-center text-white font-bold text-xs flex-shrink-0">VC</div>' +
            '<div>' +
              '<h4 class="text-sm font-semibold text-white leading-tight">' + brand + ' Voucher</h4>' +
              '<p class="text-xs text-[#8e8ca6] mt-0.5">Just now • Digital e-Card</p>' +
            '</div>' +
          '</div>' +
          '<span class="text-sm font-semibold text-white tracking-tight">-' + Number(amount).toFixed(2) + ' AED</span>';
        list.insertBefore(row, list.firstChild);
      }}

      triggerDynamicIsland(brand + ' e-Card', amount + ' AED Added to Wallet', '<span class="text-xs text-emerald-400">✓</span>');
      showToast('Purchased ' + amount + ' AED ' + brand + ' voucher');
    }}

    /* Rewards Points */
    function openRewardsModal() {{
      playHapticTick();
      const modal = document.getElementById('rewardsModal');
      const sheet = document.getElementById('rewardsSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        setTimeout(() => sheet.classList.remove('translate-y-full'), 10);
      }}
    }}

    function closeRewardsModal() {{
      playHapticTick();
      const modal = document.getElementById('rewardsModal');
      const sheet = document.getElementById('rewardsSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      setTimeout(() => {{ if (modal) modal.classList.add('opacity-0', 'pointer-events-none'); }}, 300);
    }}

    function redeemRewardsPoints() {{
      closeRewardsModal();
      playSuccessChime();
      triggerDynamicIsland('142.00 AED Redeemed', 'Cashback added to card balance');
      showToast('142.00 AED cashback deposited into your debit card!');
      // Update card balance dynamically
      const cardBal = document.getElementById('cardBalanceNum');
      if (cardBal) {{
        cardBal.textContent = '3,492.60';
      }}
      const statsBal = document.getElementById('statsBalanceAmount');
      if (statsBal) {{
        statsBal.textContent = '3,492.60';
      }}
    }}

    function handleAddToAppleWalletClick() {{
      playSuccessChime();
      triggerDynamicIsland('Apple Wallet Pass', 'Cashleap Debit ready in Apple Pay', '<span class="text-xs"></span>');
      showToast('Card verified in Apple Wallet for NFC payments');
    }}

    /* Camera QR & Barcode Scanner Controller */
    let isTorchOn = false;
    function openScannerModal() {{
      playHapticTick();
      const modal = document.getElementById('scannerModal');
      if (!modal) return;
      modal.classList.remove('opacity-0', 'pointer-events-none');
      triggerDynamicIsland('Camera Scanner', 'Align QR Code');
    }}

    function closeScannerModal() {{
      playHapticTick();
      const modal = document.getElementById('scannerModal');
      if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
      if (isTorchOn) toggleScannerTorch();
    }}

    function toggleScannerTorch() {{
      isTorchOn = !isTorchOn;
      playHapticTick();
      const btn = document.getElementById('scannerTorchBtn');
      if (isTorchOn) {{
        btn.className = 'w-10 h-10 rounded-full bg-amber-400 text-black flex items-center justify-center transition apple-press shadow-[0_0_16px_#f59e0b]';
        triggerDynamicIsland('Torch ON', 'Flashlight Active');
      }} else {{
        btn.className = 'w-10 h-10 rounded-full bg-white/15 hover:bg-white/25 flex items-center justify-center text-white transition apple-press';
        triggerDynamicIsland('Torch OFF', 'Normal mode');
      }}
    }}

    function simulateScanSuccess() {{
      playSuccessChime();
      const frame = document.getElementById('scannerFrame');
      const brackets = frame.querySelectorAll('div[class*="border-cyan-400"]');
      brackets.forEach(b => {{
        b.classList.remove('border-cyan-400');
        b.classList.add('border-emerald-400');
      }});

      triggerDynamicIsland('Merchant Verified', 'Starbucks Pay • 28.50 AED', '<span class="text-xs text-emerald-400">✓</span>');

      setTimeout(() => {{
        closeScannerModal();
        brackets.forEach(b => {{
          b.classList.remove('border-emerald-400');
          b.classList.add('border-cyan-400');
        }});
        openTxDetail('starbucks');
      }}, 700);
    }}

    function simulatePhotoScan() {{
      playHapticTick();
      triggerDynamicIsland('Photo Library', 'QR Detected ✓');
      setTimeout(() => simulateScanSuccess(), 600);
    }}

    /* Apple Notifications Center Controller */
    let unreadNotifCount = 3;
    function openNotificationsModal() {{
      playHapticTick();
      openModalWithSheet('notificationsModal', 'notificationsSheet');
      triggerDynamicIsland('Notification Center', `${{unreadNotifCount}} alerts`);
    }}

    function closeNotificationsModal() {{
      playHapticTick();
      const modal = document.getElementById('notificationsModal');
      const sheet = document.getElementById('notificationsSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
    }}

    function dismissNotification(el, title) {{
      playHapticTick();
      const dot = el.querySelector('.notif-unread-dot');
      if (dot && !dot.classList.contains('hidden')) {{
        dot.classList.add('hidden');
        unreadNotifCount = Math.max(0, unreadNotifCount - 1);
        updateNotifBadges();
      }}
      triggerDynamicIsland(title, 'Marked as read');
    }}

    function markAllNotificationsRead() {{
      playSuccessChime();
      unreadNotifCount = 0;
      updateNotifBadges();
      const dots = document.querySelectorAll('.notif-unread-dot');
      dots.forEach(d => d.classList.add('hidden'));
      triggerDynamicIsland('All Caught Up', '0 unread notifications', '<span class="text-xs text-emerald-400">✓</span>');
      setTimeout(() => closeNotificationsModal(), 400);
    }}

    function updateNotifBadges() {{
      const headerBadge = document.getElementById('headerNotificationBadge');
      const countBadge = document.getElementById('notifCountBadge');
      if (unreadNotifCount <= 0) {{
        if (headerBadge) headerBadge.classList.add('scale-0', 'opacity-0');
        if (countBadge) {{
          countBadge.textContent = '0 New';
          countBadge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-white/10 text-slate-400 border border-white/15';
        }}
      }} else {{
        if (headerBadge) headerBadge.classList.remove('scale-0', 'opacity-0');
        if (countBadge) {{
          countBadge.textContent = `${{unreadNotifCount}} New`;
          countBadge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-[#ff2a6d]/20 text-[#ff2a6d] border border-[#ff2a6d]/30';
        }}
      }}
    }}

        /* Apple Dynamic Island Controller */
    let dynamicIslandTimer = null;
    function triggerDynamicIsland(title, sub, iconHtml = null, duration = 2800) {{
      clearTimeout(dynamicIslandTimer);
      playHapticTick();
      const island = document.getElementById('dynamicIsland');
      const titleEl = document.getElementById('islandTitle');
      const subEl = document.getElementById('islandSub');
      const iconDot = document.getElementById('islandIconDot');
      if (!island) return;

      island.classList.remove('opacity-0');
      island.classList.add('dynamic-island-expanded', 'opacity-100');
      titleEl.textContent = title;
      titleEl.classList.remove('hidden');
      subEl.textContent = sub;
      subEl.className = 'text-[11px] font-bold text-white flex-shrink-0';
      if (iconHtml) {{
        iconDot.outerHTML = `<div id="islandIconDot" class="flex-shrink-0">${{iconHtml}}</div>`;
      }} else {{
        iconDot.className = 'w-2.5 h-2.5 rounded-full bg-emerald-400 flex-shrink-0 animate-pulse';
      }}

      dynamicIslandTimer = setTimeout(() => {{
        island.classList.remove('dynamic-island-expanded', 'opacity-100');
        island.classList.add('opacity-0');
        titleEl.classList.add('hidden');
        subEl.textContent = 'AED';
        subEl.className = 'text-[9.5px] font-mono font-medium text-emerald-400';
      }}, duration);
    }}

    function onDynamicIslandTap() {{
      triggerDynamicIsland('Cashleap Wallet', '● 3,350.60 AED', '<span class="text-xs"></span>');
    }}

    /* Apple Card 3D Tilt & Holographic Iridescence */
    function initCard3DParallax() {{
      const card1 = document.getElementById('card-item-1');
      const card2 = document.getElementById('card-item-2');
      [card1, card2].forEach(card => {{
        if (!card) return;
        card.addEventListener('mousemove', (e) => {{
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          const centerX = rect.width / 2;
          const centerY = rect.height / 2;
          const rotateX = ((y - centerY) / centerY) * -8;
          const rotateY = ((x - centerX) / centerX) * 8;
          card.style.transform = `perspective(900px) rotateX(${{rotateX}}deg) rotateY(${{rotateY}}deg) scale3d(1.02, 1.02, 1.02)`;

          const glint = card.querySelector('.card-holographic-glint');
          if (glint) {{
            glint.style.opacity = '0.35';
            glint.style.background = `radial-gradient(circle at ${{(x / rect.width) * 100}}% ${{(y / rect.height) * 100}}%, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.06) 50%, transparent 80%)`;
          }}
        }});
        card.addEventListener('mouseleave', () => {{
          card.style.transform = 'perspective(900px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
          const glint = card.querySelector('.card-holographic-glint');
          if (glint) glint.style.opacity = '0';
        }});
      }});
    }}

    /* Animated Balance Counter */
    let currentBalanceValue = 3350.60;
    function updateBalanceCounter(delta, isAdd = true) {{
      const el = document.getElementById('cardBalanceNum');
      if (!el) return;
      const start = currentBalanceValue;
      currentBalanceValue = isAdd ? start + delta : Math.max(0, start - delta);
      const end = currentBalanceValue;
      const duration = 500;
      const startTime = performance.now();

      el.classList.add('balance-pop');
      setTimeout(() => el.classList.remove('balance-pop'), 600);

      function step(now) {{
        const progress = Math.min((now - startTime) / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);
        const val = start + (end - start) * ease;
        el.textContent = val.toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
        if (progress < 1) requestAnimationFrame(step);
      }}
      requestAnimationFrame(step);
    }}

    /* Transactions Data & Apple Pay Receipt Sheet */
    const txReceipts = {{
      amazonPrime: {{ name: 'Amazon Prime Video', category: 'Streaming Subscription', amount: '-16.00 AED', bg: '#00a8e1', card: 'Cashleap Mastercard (•••• 0329)', time: 'Today at 20:00', ref: 'TX-89210921', logo: '<span class="text-sm font-black tracking-tighter">prime</span>' }},
      spotify: {{ name: 'Spotify Premium', category: 'Music Streaming', amount: '-5.00 AED', bg: '#1db954', card: 'Cashleap Mastercard (•••• 0329)', time: 'Today at 20:00', ref: 'TX-89210922', logo: '<svg width="22" height="22" viewBox="0 0 24 24" fill="black"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.586 14.424a.625.625 0 0 1-.86.207c-2.355-1.439-5.32-1.765-8.812-.966a.625.625 0 1 1-.278-1.219c3.826-.874 7.108-.5 9.743 1.118a.625.625 0 0 1 .207.86zm1.226-2.727a.782.782 0 0 1-1.077.257c-2.695-1.657-6.804-2.137-9.99-1.17a.782.782 0 0 1-.468-1.492c3.64-1.106 8.18-.574 11.278 1.328a.782.782 0 0 1 .257 1.077zm.106-2.84c-3.232-1.92-8.567-2.096-11.646-1.162a.938.938 0 1 1-.548-1.795c3.535-1.074 9.426-.867 13.155 1.347a.938.938 0 0 1-.961 1.61z"/></svg>' }},
      amazonStore: {{ name: 'Amazon Store', category: 'E-Commerce Retail', amount: '-5.00 AED', bg: '#ff9900', card: 'Cashleap Mastercard (•••• 0329)', time: 'Today at 20:00', ref: 'TX-89210923', logo: '<span class="text-base font-black">a</span>' }},
      ebay: {{ name: 'eBay Marketplace', category: 'Online Auction & Goods', amount: '-45.00 AED', bg: '#ffffff', card: 'Cashleap Debit (•••• 0319)', time: 'Yesterday at 18:42', ref: 'TX-89210842', logo: '<span class="text-xs font-black text-slate-900">ebay</span>' }},
      walmart: {{ name: 'Walmart Supercenter', category: 'Groceries & Household', amount: '-142.30 AED', bg: '#0071ce', card: 'Cashleap Mastercard (•••• 0329)', time: 'Oct 21 at 14:15', ref: 'TX-89210715', logo: '<span class="text-base font-bold text-amber-300">✱</span>' }},
      apple: {{ name: 'Apple Services', category: 'iCloud+ 2TB Storage', amount: '-39.99 AED', bg: '#1c1c1e', card: 'Cashleap Mastercard (•••• 0329)', time: 'Oct 20 at 09:30', ref: 'TX-89210630', logo: '<span class="text-base font-bold"></span>' }},
      starbucks: {{ name: 'Starbucks Coffee', category: 'Food & Beverage', amount: '-28.50 AED', bg: '#00704a', card: 'Cashleap Mastercard (•••• 0329)', time: 'Oct 19 at 08:24', ref: 'TX-89210524', logo: '<span class="text-xs font-bold">★</span>' }},
      netflix: {{ name: 'Netflix Ultra HD', category: 'Video Streaming', amount: '-65.00 AED', bg: '#141414', card: 'Cashleap Mastercard (•••• 0329)', time: 'Oct 18 at 22:10', ref: 'TX-89210410', logo: '<span class="text-base font-black text-red-600">N</span>' }}
    }};

    function openTxDetail(txKey) {{
      playHapticTick();
      const tx = txReceipts[txKey];
      if (!tx) return;
      document.getElementById('txDetailName').textContent = tx.name;
      document.getElementById('txDetailCategory').textContent = tx.category;
      document.getElementById('txDetailAmount').textContent = tx.amount;
      document.getElementById('txDetailCard').textContent = tx.card;
      document.getElementById('txDetailTime').textContent = tx.time;
      document.getElementById('txDetailRef').textContent = tx.ref;
      const logoEl = document.getElementById('txDetailLogo');
      logoEl.style.backgroundColor = tx.bg;
      logoEl.innerHTML = tx.logo;

      const modal = document.getElementById('txDetailModal');
      const sheet = document.getElementById('txDetailSheet');
      modal.classList.remove('opacity-0', 'pointer-events-none');
      requestAnimationFrame(() => {{
        sheet.classList.remove('translate-y-full');
      }});
      triggerDynamicIsland(tx.name, tx.amount, tx.logo);
    }}

    function closeTxDetail() {{
      playHapticTick();
      const modal = document.getElementById('txDetailModal');
      const sheet = document.getElementById('txDetailSheet');
      sheet.classList.add('translate-y-full');
      modal.classList.add('opacity-0', 'pointer-events-none');
    }}

    function repeatPaymentAction() {{
      playSuccessChime();
      closeTxDetail();
      triggerDynamicIsland('Payment Repeated', '-16.00 AED ✓', '<span class="text-xs text-emerald-400">✓</span>');
      updateBalanceCounter(16.00, false);
    }}

    function downloadReceiptAction() {{
      playHapticTick();
      closeTxDetail();
      triggerDynamicIsland('PDF Saved', 'Added to Files');
    }}

    /* Quick Action Modals Controller */
    let selectedAddAmount = 250;
    function triggerQuickAction(actionType) {{
      playHapticTick();
      if (actionType === 'add') {{
        openModalWithSheet('addFundsModal', 'addFundsSheet');
        triggerDynamicIsland('Add Funds', 'Select amount');
      }} else if (actionType === 'send') {{
        openModalWithSheet('sendMoneyModal', 'sendMoneySheet');
        triggerDynamicIsland('Send Money', 'Choose contact');
      }} else if (actionType === 'withdraw') {{
        openModalWithSheet('withdrawModal', 'withdrawSheet');
        triggerDynamicIsland('ATM Code Ready', '842 195');
      }} else if (actionType === 'schedule') {{
        openModalWithSheet('scheduleModal', 'scheduleSheet');
        triggerDynamicIsland('Autopay', '4 active items');
      }}
    }}

    function openModalWithSheet(modalId, sheetId) {{
      const modal = document.getElementById(modalId);
      const sheet = document.getElementById(sheetId);
      if (!modal || !sheet) return;
      modal.classList.remove('opacity-0', 'pointer-events-none');
      requestAnimationFrame(() => {{
        sheet.classList.remove('translate-y-full');
      }});
    }}

    function closeQuickActionModal(actionType) {{
      playHapticTick();
      const map = {{
        add: ['addFundsModal', 'addFundsSheet'],
        send: ['sendMoneyModal', 'sendMoneySheet'],
        withdraw: ['withdrawModal', 'withdrawSheet'],
        schedule: ['scheduleModal', 'scheduleSheet']
      }};
      if (!map[actionType]) return;
      const [modalId, sheetId] = map[actionType];
      const modal = document.getElementById(modalId);
      const sheet = document.getElementById(sheetId);
      if (sheet) sheet.classList.add('translate-y-full');
      if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
    }}

    function setAddAmount(val) {{
      playHapticTick();
      selectedAddAmount = val;
      const el = document.getElementById('addFundsValue');
      if (el) el.textContent = val.toFixed(2);
    }}

    function confirmAddFunds() {{
      playSuccessChime();
      closeQuickActionModal('add');
      updateBalanceCounter(selectedAddAmount, true);
      triggerDynamicIsland('Funds Added', `+${{selectedAddAmount}} AED ✓`, '<span class="text-xs text-emerald-400">✓</span>');
    }}

    /* ========================================================
       SEND MONEY & BENEFICIARIES SCREEN FLOW CONTROLLERS
       ======================================================== */
    let isSendSheetExpanded = false;
    const SEND_SHEET_COLLAPSED_Y = 338;
    const SEND_SHEET_EXPANDED_Y = 0;

    const beneficiariesDirectory = {{
      sarah: {{
        name: 'Sarah Jenkins',
        initials: 'SJ',
        type: 'cashleap',
        badge: 'Cashleap',
        handle: '@sarah.j • Instant 0.00 AED Fee',
        sub: '@sarah.j • +971 50 842 1920',
        avatarClass: 'w-11 h-11 rounded-full bg-gradient-to-tr from-indigo-600 to-blue-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs flex-shrink-0'
      }},
      alex: {{
        name: 'Alex Rivera',
        initials: 'AR',
        type: 'cashleap',
        badge: 'Cashleap',
        handle: '@alex.r • Instant 0.00 AED Fee',
        sub: '@alex.r • +971 52 391 0488',
        avatarClass: 'w-11 h-11 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs flex-shrink-0'
      }},
      david: {{
        name: 'David Chen',
        initials: 'DC',
        type: 'cashleap',
        badge: 'Cashleap',
        handle: '@david.c • Instant 0.00 AED Fee',
        sub: '@david.c • +971 55 901 2341',
        avatarClass: 'w-11 h-11 rounded-full bg-gradient-to-tr from-purple-600 to-indigo-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs flex-shrink-0'
      }},
      omar: {{
        name: 'Omar Al Maktoum',
        initials: 'OM',
        type: 'cashleap',
        badge: 'Cashleap',
        handle: '@omar.m • Instant 0.00 AED Fee',
        sub: '@omar.m • +971 50 112 7789',
        avatarClass: 'w-11 h-11 rounded-full bg-gradient-to-tr from-emerald-600 to-teal-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs flex-shrink-0'
      }},
      elena: {{
        name: 'Elena Rostova',
        initials: 'ER',
        type: 'iban',
        badge: 'IBAN',
        handle: 'Emirates NBD • AE42 •••• 2019',
        sub: 'Emirates NBD • AE42 •••• 2019',
        avatarClass: 'w-11 h-11 rounded-full bg-white/[0.08] border border-white/25 flex items-center justify-center text-white font-bold text-xs flex-shrink-0'
      }}
    }};

    let currentActiveBeneficiaryKey = 'sarah';
    let currentBeneficiaryFilter = 'all';
    let currentAddBenMode = 'cashleap';
    let selectedBenBankName = 'Emirates NBD';

    function setSendSheetExpanded(expanded) {{
      playHapticTick();
      isSendSheetExpanded = expanded;
      const sheet = document.getElementById('sendBeneficiariesSheet');
      const label = document.getElementById('sendSheetToggleLabel');
      const chevron = document.getElementById('sendSheetToggleChevron');
      if (!sheet) return;
      sheet.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
      const targetY = expanded ? SEND_SHEET_EXPANDED_Y : SEND_SHEET_COLLAPSED_Y;
      sheet.style.transform = 'translateY(' + targetY + 'px)';
      if (label) label.textContent = expanded ? 'Collapse' : 'See All';
      if (chevron) chevron.style.transform = expanded ? 'rotate(180deg)' : 'rotate(0deg)';
    }}

    function toggleSendBottomSheet() {{
      setSendSheetExpanded(!isSendSheetExpanded);
    }}

    function setBeneficiaryFilter(filterType) {{
      playHapticTick();
      currentBeneficiaryFilter = filterType;
      const map = {{ all: 'ben-filter-all', cashleap: 'ben-filter-cashleap', iban: 'ben-filter-iban' }};
      Object.keys(map).forEach(k => {{
        const btn = document.getElementById(map[k]);
        if (!btn) return;
        if (k === filterType) {{
          btn.className = 'px-3 py-1 rounded-full bg-blue-600/30 border border-blue-500/60 text-[10.5px] font-semibold text-white transition cursor-pointer';
        }} else {{
          btn.className = 'px-3 py-1 rounded-full bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] hover:text-white transition cursor-pointer';
        }}
      }});
      const searchEl = document.getElementById('sendBeneficiarySearchInput');
      filterSendBeneficiaries(searchEl ? searchEl.value : '');
    }}

    function filterSendBeneficiaries(query) {{
      const q = (query || '').toLowerCase().trim();
      const rows = document.querySelectorAll('#sendBeneficiariesList .beneficiary-row');
      rows.forEach(row => {{
        const rType = row.getAttribute('data-ben-type') || 'cashleap';
        const rSearch = (row.getAttribute('data-ben-search') || '').toLowerCase();
        const matchesType = (currentBeneficiaryFilter === 'all') || (rType === currentBeneficiaryFilter);
        const matchesQuery = !q || rSearch.includes(q);
        row.style.display = (matchesType && matchesQuery) ? 'flex' : 'none';
      }});
    }}

    function selectSheetBeneficiary(benKey) {{
      playHapticTick();
      const ben = beneficiariesDirectory[benKey] || beneficiariesDirectory.sarah;
      currentActiveBeneficiaryKey = benKey;

      const nameEl = document.getElementById('sendRecipientName');
      const avatarEl = document.getElementById('sendRecipientAvatar');
      const badgeEl = document.getElementById('sendRecipientBadge');
      const handleEl = document.getElementById('sendRecipientHandle');

      if (nameEl) nameEl.textContent = ben.name;
      if (avatarEl) {{
        avatarEl.textContent = ben.initials;
        avatarEl.className = ben.avatarClass;
      }}
      if (badgeEl) {{
        badgeEl.textContent = ben.badge;
        badgeEl.className = (ben.type === 'cashleap')
          ? 'flex-shrink-0 text-[9.5px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-blue-500/15 border border-blue-400/30 text-blue-300'
          : 'flex-shrink-0 text-[9.5px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-white/10 border border-white/15 text-[#9e94b8]';
      }}
      if (handleEl) handleEl.textContent = ben.handle;

      const panel = document.getElementById('sendSheetBeneficiariesPanel');
      const btn = document.getElementById('sendSheetBrowseToggleBtn');
      if (panel && !panel.classList.contains('hidden')) {{
        panel.classList.add('hidden');
        if (btn) btn.textContent = 'Directory ▾';
      }}
    }}

    function toggleSendSheetBeneficiariesList() {{
      playHapticTick();
      const panel = document.getElementById('sendSheetBeneficiariesPanel');
      const btn = document.getElementById('sendSheetBrowseToggleBtn');
      if (!panel) return;
      if (panel.classList.contains('hidden')) {{
        panel.classList.remove('hidden');
        if (btn) btn.textContent = 'Hide ▴';
      }} else {{
        panel.classList.add('hidden');
        if (btn) btn.textContent = 'Directory ▾';
      }}
    }}

    function filterSendSheetBeneficiaries(query) {{
      const q = (query || '').toLowerCase().trim();
      const panel = document.getElementById('sendSheetBeneficiariesPanel');
      const btn = document.getElementById('sendSheetBrowseToggleBtn');
      if (panel && q.length > 0 && panel.classList.contains('hidden')) {{
        panel.classList.remove('hidden');
        if (btn) btn.textContent = 'Hide ▴';
      }}
      const rows = document.querySelectorAll('#sendSheetBeneficiariesPanel .sheet-ben-row');
      rows.forEach(r => {{
        const s = (r.getAttribute('data-sheet-ben-search') || '').toLowerCase();
        r.style.display = (!q || s.includes(q)) ? 'flex' : 'none';
      }});
    }}

    function openSendToBeneficiary(benKey) {{
      selectSheetBeneficiary(benKey);
      const ben = beneficiariesDirectory[benKey] || beneficiariesDirectory.sarah;
      openModalWithSheet('sendMoneyModal', 'sendMoneySheet');
      triggerDynamicIsland('Send to ' + ben.name, ben.badge);
    }}

    function selectSendContact(name, initials) {{
      playHapticTick();
      const el = document.getElementById('sendRecipientName');
      if (el) el.textContent = name;
      const av = document.getElementById('sendRecipientAvatar');
      if (av && initials) av.textContent = initials;
      triggerDynamicIsland('To: ' + name, '150.00 AED');
    }}

    function setSendMoneyPreset(val) {{
      playHapticTick();
      const input = document.getElementById('sendMoneyAmountInput');
      if (input) input.value = val;
    }}

    function executeSendMoneyTransfer() {{
      playSuccessChime();
      const nameEl = document.getElementById('sendRecipientName');
      const amtEl = document.getElementById('sendMoneyAmountInput');
      const noteEl = document.getElementById('sendMoneyNoteInput');
      const recipient = (nameEl && nameEl.textContent) ? nameEl.textContent : 'Sarah Jenkins';
      const amt = Math.max(1, parseFloat(amtEl ? amtEl.value : '150') || 150);
      const note = (noteEl && noteEl.value.trim()) ? noteEl.value.trim() : 'Instant Cashleap Transfer';

      closeQuickActionModal('send');
      updateBalanceCounter(amt, false);
      if (noteEl) noteEl.value = '';

      // Prepend transaction to Home Recent Transactions list
      const list = document.getElementById('sheetScrollArea');
      if (list) {{
        const row = document.createElement('div');
        row.className = 'flex items-center justify-between py-3 border-b border-white/[0.08] hover:bg-white/[0.04] transition cursor-pointer rounded-xl px-2 -mx-2 select-none';
        const initials = recipient.split(' ').map(w => w[0]).join('').substring(0, 2).toUpperCase();
        row.innerHTML =
          '<div class="flex items-center gap-3.5">' +
            '<div class="w-11 h-11 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-500 flex items-center justify-center text-white font-bold text-xs flex-shrink-0">' + initials + '</div>' +
            '<div>' +
              '<h4 class="text-sm font-semibold text-white leading-tight">' + recipient + '</h4>' +
              '<p class="text-xs text-[#8e8ca6] mt-0.5">Just now • ' + note + '</p>' +
            '</div>' +
          '</div>' +
          '<span class="text-sm font-semibold text-white tracking-tight">-' + amt.toFixed(2) + ' AED</span>';
        list.insertBefore(row, list.firstChild);
      }}

      triggerDynamicIsland('Sent to ' + recipient, amt.toFixed(2) + ' AED', '<span class="text-xs text-emerald-400">✓</span>');
      showToast('Sent ' + amt.toFixed(2) + ' AED to ' + recipient);
    }}

    /* Add Beneficiary Modal Controllers */
    function openAddBeneficiaryModal(defaultMode) {{
      playHapticTick();
      if (defaultMode) setAddBeneficiaryMode(defaultMode);
      const modal = document.getElementById('addBeneficiaryModal');
      const sheet = document.getElementById('addBeneficiarySheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        setTimeout(() => sheet.classList.remove('translate-y-full'), 10);
      }}
    }}

    function closeAddBeneficiaryModal() {{
      playHapticTick();
      const modal = document.getElementById('addBeneficiaryModal');
      const sheet = document.getElementById('addBeneficiarySheet');
      if (sheet) sheet.classList.add('translate-y-full');
      setTimeout(() => {{
        if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
      }}, 300);
    }}

    function setAddBeneficiaryMode(mode) {{
      playHapticTick();
      currentAddBenMode = mode;
      const clBtn = document.getElementById('ben-mode-cashleap');
      const ibBtn = document.getElementById('ben-mode-iban');
      const clFields = document.getElementById('benCashleapFields');
      const ibFields = document.getElementById('benIbanFields');

      if (mode === 'cashleap') {{
        if (clBtn) clBtn.className = 'py-2 rounded-lg bg-blue-600 text-white text-xs font-bold transition cursor-pointer flex items-center justify-center gap-1.5';
        if (ibBtn) ibBtn.className = 'py-2 rounded-lg text-[#9e94b8] hover:text-white text-xs font-semibold transition cursor-pointer flex items-center justify-center gap-1.5';
        if (clFields) clFields.classList.remove('hidden');
        if (ibFields) ibFields.classList.add('hidden');
      }} else {{
        if (ibBtn) ibBtn.className = 'py-2 rounded-lg bg-blue-600 text-white text-xs font-bold transition cursor-pointer flex items-center justify-center gap-1.5';
        if (clBtn) clBtn.className = 'py-2 rounded-lg text-[#9e94b8] hover:text-white text-xs font-semibold transition cursor-pointer flex items-center justify-center gap-1.5';
        if (ibFields) ibFields.classList.remove('hidden');
        if (clFields) clFields.classList.add('hidden');
      }}
    }}

    function onBenLeapTagInput(val) {{
      const clean = (val || '').replace(/^@/, '').trim() || 'user';
      const subEl = document.getElementById('newBenPreviewSub');
      if (subEl) subEl.textContent = '@' + clean + ' • Instant P2P';
    }}

    function onBenFullNameInput(val) {{
      const name = (val || '').trim() || 'Cashleap User';
      const nameEl = document.getElementById('newBenPreviewName');
      const avEl = document.getElementById('newBenPreviewAvatar');
      if (nameEl) nameEl.textContent = name;
      if (avEl) {{
        avEl.textContent = name.split(' ').filter(Boolean).map(w => w[0]).join('').substring(0, 2).toUpperCase() || 'CU';
      }}
    }}

    function lookupCashleapUserTag() {{
      playSuccessChime();
      const tagEl = document.getElementById('newBenLeapTagInput');
      const raw = (tagEl && tagEl.value.trim()) ? tagEl.value.trim().replace(/^@/, '') : 'khalid.mansoor';
      showToast('Verified Cashleap user @' + raw);
      triggerDynamicIsland('User Verified', '@' + raw + ' on Cashleap');
    }}

    function selectBenBank(btnEl, bankName) {{
      playHapticTick();
      selectedBenBankName = bankName;
      document.querySelectorAll('.ben-bank-pill').forEach(b => {{
        b.className = 'ben-bank-pill py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 text-[10px] font-medium text-[#9e94b8] truncate cursor-pointer';
      }});
      if (btnEl) {{
        btnEl.className = 'ben-bank-pill py-1.5 px-2 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[10px] font-semibold text-white truncate cursor-pointer';
      }}
    }}

    function selectBenRelation(btnEl) {{
      playHapticTick();
      document.querySelectorAll('.ben-rel-pill').forEach(b => {{
        b.className = 'ben-rel-pill py-1.5 rounded-lg bg-white/[0.04] border border-white/10 text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer';
      }});
      if (btnEl) {{
        btnEl.className = 'ben-rel-pill py-1.5 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[10.5px] font-semibold text-white transition cursor-pointer';
      }}
    }}

    function confirmAddBeneficiary(sendImmediately) {{
      playSuccessChime();
      const fullNameEl = document.getElementById('newBenFullNameInput');
      const tagEl = document.getElementById('newBenLeapTagInput');
      const ibanEl = document.getElementById('newBenIbanInput');

      const fullName = (fullNameEl && fullNameEl.value.trim()) ? fullNameEl.value.trim() : 'Khalid Al Mansoor';
      const firstName = fullName.split(' ')[0];
      const initials = fullName.split(' ').filter(Boolean).map(w => w[0]).join('').substring(0, 2).toUpperCase() || 'CU';
      const cleanTag = (tagEl && tagEl.value.trim()) ? tagEl.value.trim().replace(/^@/, '') : 'khalid.mansoor';
      const rawIban = (ibanEl && ibanEl.value.trim()) ? ibanEl.value.trim() : 'AE07 0331 2345 6789 0123 456';
      const last4 = rawIban.replace(/\s+/g, '').slice(-4) || '3456';

      const key = 'ben_' + Date.now() + '_' + Object.keys(beneficiariesDirectory).length;
      const isCashleap = (currentAddBenMode === 'cashleap');

      beneficiariesDirectory[key] = {{
        name: fullName,
        initials: initials,
        type: isCashleap ? 'cashleap' : 'iban',
        badge: isCashleap ? 'Cashleap' : 'IBAN',
        handle: isCashleap ? ('@' + cleanTag + ' • Instant 0.00 AED Fee') : (selectedBenBankName + ' • AE07 •••• ' + last4),
        sub: isCashleap ? ('@' + cleanTag + ' • Verified Cashleap User') : (selectedBenBankName + ' • AE07 •••• ' + last4),
        avatarClass: 'w-11 h-11 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs flex-shrink-0'
      }};

      // 1. Add to horizontal Quick Cashleap Avatars Strip
      const avatarsRow = document.getElementById('sendQuickAvatarsRow');
      if (avatarsRow) {{
        const item = document.createElement('div');
        item.className = 'flex flex-col items-center gap-1 cursor-pointer apple-press flex-shrink-0';
        item.onclick = function() {{ openSendToBeneficiary(key); }};
        item.innerHTML =
          '<div class="relative">' +
            '<div class="w-11 h-11 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs shadow-sm">' + initials + '</div>' +
            (isCashleap ? '<span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center"><span class="w-2 h-2 rounded-full bg-emerald-400"></span></span>' : '') +
          '</div>' +
          '<span class="text-[10px] text-white/90 font-medium truncate w-12 text-center">' + firstName + '</span>';
        avatarsRow.insertBefore(item, avatarsRow.children[1] || null);
      }}

      // 2. Add to Saved Beneficiaries Bottom Sheet List
      const list = document.getElementById('sendBeneficiariesList');
      if (list) {{
        const row = document.createElement('div');
        row.setAttribute('data-ben-type', isCashleap ? 'cashleap' : 'iban');
        row.setAttribute('data-ben-search', (fullName + ' @' + cleanTag + ' ' + rawIban).toLowerCase());
        row.className = 'beneficiary-row py-3 flex items-center justify-between hover:bg-white/[0.04] active:bg-white/[0.08] transition cursor-pointer apple-press';
        row.onclick = function() {{ openSendToBeneficiary(key); }};
        row.innerHTML =
          '<div class="flex items-center gap-3.5">' +
            '<div class="relative flex-shrink-0">' +
              '<div class="w-10 h-10 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-500 border border-white/20 flex items-center justify-center text-white font-bold text-xs">' + initials + '</div>' +
              (isCashleap ? '<span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-[#141033] flex items-center justify-center"><span class="w-2 h-2 rounded-full bg-emerald-400"></span></span>' : '') +
            '</div>' +
            '<div class="flex flex-col">' +
              '<div class="flex items-center gap-1.5">' +
                '<span class="text-[14px] font-semibold text-white tracking-tight">' + fullName + '</span>' +
                '<span class="text-[9px] font-bold uppercase px-1.5 py-0.2 rounded ' + (isCashleap ? 'bg-blue-500/20 border border-blue-400/30 text-blue-300' : 'bg-white/10 border border-white/15 text-[#9e94b8]') + '">' + (isCashleap ? 'Cashleap' : 'IBAN') + '</span>' +
              '</div>' +
              '<span class="text-[11px] text-[#9e94b8]">' + beneficiariesDirectory[key].sub + '</span>' +
            '</div>' +
          '</div>' +
          '<div class="flex items-center gap-2">' +
            '<span class="text-[11.5px] font-semibold text-blue-400">Send</span>' +
            '<svg class="w-4 h-4 text-white/40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>' +
          '</div>';
        list.insertBefore(row, list.firstChild);
      }}

      // Update Saved count badges
      const totalCount = Object.keys(beneficiariesDirectory).length;
      const badge = document.getElementById('sendBeneficiariesCountBadge');
      if (badge) badge.textContent = totalCount + ' Saved';
      const sheetCount = document.getElementById('sendSheetCountBadge');
      if (sheetCount) sheetCount.textContent = String(totalCount);

      // 3. Add to Send Money Bottom Sheet Avatars Strip & Inline Directory
      const sheetAvatars = document.getElementById('sendSheetAvatarsRow');
      if (sheetAvatars) {{
        const sItem = document.createElement('div');
        sItem.className = 'flex flex-col items-center gap-1 cursor-pointer apple-press flex-shrink-0';
        sItem.onclick = function() {{ selectSheetBeneficiary(key); }};
        sItem.innerHTML =
          '<div class="relative">' +
            '<div class="w-10 h-10 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-500 border border-white/25 flex items-center justify-center text-white font-bold text-xs">' + initials + '</div>' +
            (isCashleap ? '<span class="absolute -bottom-0.5 -right-0.5 z-20 w-3 h-3 rounded-full bg-emerald-400 border-2 border-[#161233]"></span>' : '') +
          '</div>' +
          '<span class="text-[9.5px] text-white/90 font-medium truncate w-11 text-center">' + firstName + '</span>';
        sheetAvatars.insertBefore(sItem, sheetAvatars.children[1] || null);
      }}

      const sheetPanel = document.getElementById('sendSheetBeneficiariesPanel');
      if (sheetPanel) {{
        const sRow = document.createElement('div');
        sRow.setAttribute('data-sheet-ben-search', (fullName + ' @' + cleanTag + ' ' + rawIban).toLowerCase());
        sRow.className = 'sheet-ben-row py-2 flex items-center justify-between hover:bg-white/[0.04] rounded-lg px-1.5 cursor-pointer transition';
        sRow.onclick = function() {{ selectSheetBeneficiary(key); }};
        sRow.innerHTML =
          '<div class="flex items-center gap-2.5">' +
            '<div class="w-8 h-8 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-500 flex items-center justify-center text-white font-bold text-[10px]">' + initials + '</div>' +
            '<div class="flex flex-col">' +
              '<span class="text-xs font-semibold text-white">' + fullName + '</span>' +
              '<span class="text-[10px] text-[#9e94b8]">' + beneficiariesDirectory[key].handle + '</span>' +
            '</div>' +
          '</div>';
        sheetPanel.insertBefore(sRow, sheetPanel.firstChild);
      }}

      selectSheetBeneficiary(key);
      closeAddBeneficiaryModal();
      triggerDynamicIsland('Beneficiary Added', fullName + (isCashleap ? (' (@' + cleanTag + ')') : ''));
      showToast('Added ' + fullName + ' to Saved Beneficiaries');

      setTimeout(() => {{
        openSendToBeneficiary(key);
      }}, 320);
    }}

    /* Animated Slide to Send Gesture & Tap Animation */
    function completeSendSlideAnimation() {{
      const track = document.getElementById('sendSliderTrack');
      const thumb = document.getElementById('sendSliderThumb');
      const progress = document.getElementById('sendSliderProgress');
      const label = document.getElementById('sendSliderLabel');
      const chevrons = document.getElementById('sendSliderChevrons');
      if (!track || !thumb || !progress) {{
        executeSendMoneyTransfer();
        return;
      }}
      const maxSlide = Math.max(200, (track.offsetWidth || 310) - (thumb.offsetWidth || 44) - 12);
      thumb.classList.remove('slide-send-thumb-idle');
      thumb.style.transition = 'transform 0.28s cubic-bezier(0.22, 1, 0.36, 1)';
      thumb.style.transform = 'translateX(' + maxSlide + 'px)';
      progress.style.width = '100%';
      if (label) label.style.opacity = '0';
      if (chevrons) chevrons.style.opacity = '0';

      setTimeout(() => {{
        thumb.style.transition = 'none';
        thumb.style.transform = 'translateX(0px)';
        thumb.classList.add('slide-send-thumb-idle');
        progress.style.width = '0px';
        if (label) label.style.opacity = '1';
        if (chevrons) chevrons.style.opacity = '1';
        executeSendMoneyTransfer();
      }}, 260);
    }}

    function initSendSlider() {{
      const track = document.getElementById('sendSliderTrack');
      const thumb = document.getElementById('sendSliderThumb');
      const progress = document.getElementById('sendSliderProgress');
      const label = document.getElementById('sendSliderLabel');
      const chevrons = document.getElementById('sendSliderChevrons');
      if (!track || !thumb || !progress) return;

      let isDragging = false;
      let startX = 0;
      let maxSlide = 0;
      let hasMoved = false;

      function onDown(e) {{
        e.stopPropagation();
        isDragging = true;
        hasMoved = false;
        startX = e.touches ? e.touches[0].clientX : e.clientX;
        maxSlide = Math.max(180, (track.offsetWidth || 310) - (thumb.offsetWidth || 44) - 12);
        thumb.classList.remove('slide-send-thumb-idle');
        thumb.style.transition = 'none';
      }}

      function onMove(e) {{
        if (!isDragging) return;
        const currentX = e.touches ? e.touches[0].clientX : e.clientX;
        const delta = Math.max(0, Math.min(currentX - startX, maxSlide));
        if (delta > 4) hasMoved = true;
        thumb.style.transform = `translateX(${{delta}}px)`;
        progress.style.width = `${{delta + 24}}px`;
        const ratio = maxSlide > 0 ? (delta / maxSlide) : 0;
        if (label) label.style.opacity = String(Math.max(0, 1 - ratio * 1.6));
        if (chevrons) chevrons.style.opacity = String(Math.max(0.1, 1 - ratio));
      }}

      function onUp(e) {{
        if (!isDragging) return;
        isDragging = false;
        const currentX = (e.changedTouches && e.changedTouches[0]) ? e.changedTouches[0].clientX : e.clientX;
        const delta = currentX - startX;
        if (!hasMoved || delta >= maxSlide * 0.45) {{
          completeSendSlideAnimation();
        }} else {{
          playHapticTick();
          thumb.style.transition = 'transform 0.25s cubic-bezier(0.22, 1, 0.36, 1)';
          thumb.style.transform = 'translateX(0px)';
          setTimeout(() => thumb.classList.add('slide-send-thumb-idle'), 260);
          progress.style.width = '0px';
          if (label) label.style.opacity = '1';
          if (chevrons) chevrons.style.opacity = '1';
        }}
      }}

      thumb.addEventListener('mousedown', onDown);
      thumb.addEventListener('touchstart', onDown, {{ passive: true }});
      window.addEventListener('mousemove', onMove);
      window.addEventListener('touchmove', onMove, {{ passive: true }});
      window.addEventListener('mouseup', onUp);
      window.addEventListener('touchend', onUp);
    }}

    /* Card Details Sheet */
    function openCardDetailsModal(cardIdx = 1) {{
      playHapticTick();
      const title = document.getElementById('cardDetailsTitle');
      const sub = document.getElementById('cardDetailsSubtitle');
      const num = document.getElementById('cardDetailsNum');
      if (cardIdx === 2 || (!cardIdx && currentCardIndex === 2)) {{
        if (title) title.textContent = 'Cashleap Debit Card';
        if (sub) sub.textContent = 'Mastercard Debit • Active';
        if (num) num.textContent = '5412 •••• •••• 0319';
        triggerDynamicIsland('Debit Card 0319', 'Active ● Apple Pay');
      }} else {{
        if (title) title.textContent = 'Cashleap Mastercard';
        if (sub) sub.textContent = 'Card Controls & Apple Pay';
        if (num) num.textContent = '5412 •••• •••• 0329';
        triggerDynamicIsland('Mastercard 0329', 'Active ● Apple Pay');
      }}
      openModalWithSheet('cardDetailsModal', 'cardDetailsSheet');
    }}

    function closeCardDetailsModal() {{
      playHapticTick();
      const modal = document.getElementById('cardDetailsModal');
      const sheet = document.getElementById('cardDetailsSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
    }}

    /* Card Details Screen Controller (Matching Uploaded Design) */
    let isAccountFrozen = false;
    function openCardDetailsScreen(cardIdx = 1) {{
      playHapticTick();
      const balEl = document.getElementById('cdCurrentBalance');
      const creditEl = document.getElementById('cdCreditLimit');
      const minDueEl = document.getElementById('cdMinDue');
      const lastPayEl = document.getElementById('cdLastPayment');
      const cashbackEl = document.getElementById('cdCashback');
      
      if (cardIdx === 2 || (!cardIdx && currentCardIndex === 2)) {{
        if (balEl) balEl.textContent = '2,150.60';
        if (creditEl) creditEl.textContent = '25,000.00 AED';
        if (minDueEl) minDueEl.textContent = '450.00 AED';
        if (lastPayEl) lastPayEl.textContent = 'Oct 18, 2024';
        if (cashbackEl) cashbackEl.textContent = '125.00 AED';
        triggerDynamicIsland('Debit Card 0319', 'Account Details');
      }} else {{
        if (balEl) balEl.textContent = '3,350.60';
        if (creditEl) creditEl.textContent = '35,000.00 AED';
        if (minDueEl) minDueEl.textContent = '960.00 AED';
        if (lastPayEl) lastPayEl.textContent = 'May 25, 2024';
        if (cashbackEl) cashbackEl.textContent = '200.00 AED';
        triggerDynamicIsland('Cashleap Mastercard', 'Account Details');
      }}
      showScreen('carddetail');
    }}

    function handleCashbackClick() {{
      playHapticTick();
      const cb = (currentCardIndex === 2) ? '125.00 AED' : '200.00 AED';
      triggerDynamicIsland('Cashback Available', `${{cb}} • Tap to Redeem`);
    }}

    function handleStatementsClick() {{
      playHapticTick();
      triggerDynamicIsland('Statements', 'October 2024 • PDF Ready');
    }}

    function handleCustomizeCardClick() {{
      playHapticTick();
      openCardSelectionModal();
    }}

    function handleFreezeAccountClick() {{
      playHapticTick();
      isAccountFrozen = !isAccountFrozen;
      const label = document.getElementById('cdFreezeLabel');
      if (isAccountFrozen) {{
        if (label) {{
          label.textContent = 'Unfreeze my Account';
          label.classList.add('text-rose-400');
        }}
        triggerDynamicIsland('Account Frozen', 'All payments disabled');
      }} else {{
        if (label) {{
          label.textContent = 'Freeze my Account';
          label.classList.remove('text-rose-400');
        }}
        triggerDynamicIsland('Account Active', 'Ready for Apple Pay', '<span class="text-xs text-emerald-400">✓</span>');
      }}
    }}

    function handleAddAppleWalletClick() {{
      playSuccessChime();
      triggerDynamicIsland('Apple Wallet', 'Mastercard Verified with Face ID', '<span class="text-xs">Pay</span>');
    }}

    function handleCardTransactionsClick() {{
      playHapticTick();
      showScreen('home');
      setTimeout(() => setSheetExpanded(true), 350);
    }}

    let currentAppLanguage = 'en'; // 'en' or 'ar'
    function setAppLanguage(lang) {{
      if (typeof playHapticTick === 'function') playHapticTick();
      currentAppLanguage = lang;
      const isAr = (lang === 'ar');

      // Update Card Detail Segmented Buttons
      const btnEn = document.getElementById('langBtnEn');
      const btnAr = document.getElementById('langBtnAr');
      if (btnEn && btnAr) {{
        if (isAr) {{
          btnAr.className = 'px-2.5 py-1 rounded-full text-[11px] font-bold transition-all cursor-pointer bg-blue-600 text-white shadow-sm';
          btnEn.className = 'px-2.5 py-1 rounded-full text-[11px] font-medium text-[#9e94b8] hover:text-white transition-all cursor-pointer';
        }} else {{
          btnEn.className = 'px-2.5 py-1 rounded-full text-[11px] font-bold transition-all cursor-pointer bg-blue-600 text-white shadow-sm';
          btnAr.className = 'px-2.5 py-1 rounded-full text-[11px] font-medium text-[#9e94b8] hover:text-white transition-all cursor-pointer';
        }}
      }}

      // Update Profile Segmented Buttons
      const pBtnEn = document.getElementById('profileLangBtnEn');
      const pBtnAr = document.getElementById('profileLangBtnAr');
      if (pBtnEn && pBtnAr) {{
        if (isAr) {{
          pBtnAr.className = 'px-2 py-0.5 rounded-full text-[10px] font-bold transition-all cursor-pointer bg-blue-600 text-white shadow-sm';
          pBtnEn.className = 'px-2 py-0.5 rounded-full text-[10px] font-medium text-[#9e94b8] hover:text-white transition-all cursor-pointer';
        }} else {{
          pBtnEn.className = 'px-2 py-0.5 rounded-full text-[10px] font-bold transition-all cursor-pointer bg-blue-600 text-white shadow-sm';
          pBtnAr.className = 'px-2 py-0.5 rounded-full text-[10px] font-medium text-[#9e94b8] hover:text-white transition-all cursor-pointer';
        }}
      }}

      // Update Labels
      const cdLangSub = document.getElementById('cdLangSub');
      if (cdLangSub) {{
        cdLangSub.textContent = isAr ? 'اللغة العربية مفعلة' : 'English • العربية';
      }}
      const profileLangSub = document.getElementById('profileLangSub');
      if (profileLangSub) {{
        profileLangSub.textContent = isAr ? 'اللغة العربية مفعلة للواجهة' : 'Switch between English & Arabic';
      }}

      if (isAr) {{
        triggerDynamicIsland('تغيير اللغة', 'تم التبديل إلى العربية (Arabic)', '<span class="text-xs text-blue-400 font-bold">ع</span>');
        showToast('تم تحويل لغة التطبيق إلى العربية بنجاح');
      }} else {{
        triggerDynamicIsland('Language Changed', 'Switched to English (UAE)', '<span class="text-xs text-blue-400 font-bold">EN</span>');
        showToast('App language switched to English');
      }}
    }}

    function openCardSettingsAction() {{
      playHapticTick();
      const row = document.getElementById('cardLangRow');
      if (row) {{
        row.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        row.classList.add('bg-white/[0.08]');
        setTimeout(() => row.classList.remove('bg-white/[0.08]'), 800);
      }}
      triggerDynamicIsland('Card Controls', 'Language: ' + (currentAppLanguage === 'ar' ? 'العربية' : 'English'));
    }}

    /* Card Selection Sheet Controls */
    let pendingModalCardIdx = 1;
    function openCardSelectionModal() {{
      playHapticTick();
      const modal = document.getElementById('selectCardModal');
      const sheet = document.getElementById('selectCardSheet');
      chooseModalCard(currentCardIndex || 1);
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        requestAnimationFrame(() => {{
          sheet.classList.remove('translate-y-full');
        }});
      }}
    }}

    function closeCardSelectionModal() {{
      playHapticTick();
      const modal = document.getElementById('selectCardModal');
      const sheet = document.getElementById('selectCardSheet');
      if (sheet) sheet.classList.add('translate-y-full');
      if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
    }}

    function chooseModalCard(idx) {{
      playHapticTick();
      pendingModalCardIdx = idx;
      const opt1 = document.getElementById('modal-card-opt-1');
      const opt2 = document.getElementById('modal-card-opt-2');
      const radio1 = document.getElementById('modal-radio-1');
      const radio2 = document.getElementById('modal-radio-2');
      if (idx === 1) {{
        if (opt1) opt1.className = 'flex items-center justify-between p-3 rounded-2xl border-2 border-blue-500 bg-blue-500/15 backdrop-blur-md transition cursor-pointer apple-press';
        if (opt2) opt2.className = 'flex items-center justify-between p-3 rounded-2xl border border-white/10 bg-white/[0.035] hover:bg-white/[0.08] backdrop-blur-md transition cursor-pointer apple-press';
        if (radio1) {{
          radio1.className = 'w-5 h-5 rounded-full border-2 border-blue-400 bg-blue-500 flex items-center justify-center text-white';
          radio1.innerHTML = '<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>';
        }}
        if (radio2) {{
          radio2.className = 'w-5 h-5 rounded-full border-2 border-white/30 bg-transparent flex items-center justify-center text-transparent';
          radio2.innerHTML = '';
        }}
      }} else {{
        if (opt1) opt1.className = 'flex items-center justify-between p-3 rounded-2xl border border-white/10 bg-white/[0.035] hover:bg-white/[0.08] backdrop-blur-md transition cursor-pointer apple-press';
        if (opt2) opt2.className = 'flex items-center justify-between p-3 rounded-2xl border-2 border-pink-500 bg-pink-500/15 backdrop-blur-md transition cursor-pointer apple-press';
        if (radio1) {{
          radio1.className = 'w-5 h-5 rounded-full border-2 border-white/30 bg-transparent flex items-center justify-center text-transparent';
          radio1.innerHTML = '';
        }}
        if (radio2) {{
          radio2.className = 'w-5 h-5 rounded-full border-2 border-pink-400 bg-pink-500 flex items-center justify-center text-white';
          radio2.innerHTML = '<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>';
        }}
      }}
    }}

    function confirmCardSelection() {{
      selectCardIndex(pendingModalCardIdx, true);
      closeCardSelectionModal();
      triggerDynamicIsland('Card Selected', pendingModalCardIdx === 1 ? 'Cashleap Mastercard (0329)' : 'Debit Card (0319)');
    }}

    function copyCardNumber() {{
      playSuccessChime();
      triggerDynamicIsland('Card Number Copied', '5412 •••• 0329');
      if (navigator.clipboard) {{
        navigator.clipboard.writeText('5412849201920329').catch(() => {{}});
      }}
    }}

    let cardIsLocked = false;
    function toggleCardLock(btn) {{
      cardIsLocked = !cardIsLocked;
      playHapticTick();
      if (cardIsLocked) {{
        btn.className = 'w-10 h-6 rounded-full bg-red-500 p-0.5 flex items-center justify-end cursor-pointer transition-colors apple-press';
        triggerDynamicIsland('Card Frozen', 'Transactions blocked');
      }} else {{
        btn.className = 'w-10 h-6 rounded-full bg-white/20 p-0.5 flex items-center justify-start cursor-pointer transition-colors apple-press';
        triggerDynamicIsland('Card Unlocked', 'Ready to use', '<span class="text-xs text-emerald-400">✓</span>');
      }}
    }}

    function toggleScheduleItem(toggleEl) {{
      playHapticTick();
      const dot = toggleEl.querySelector('div');
      const isOn = toggleEl.classList.contains('justify-end');
      if (isOn) {{
        toggleEl.className = 'w-10 h-6 rounded-full bg-white/20 p-0.5 flex items-center justify-start cursor-pointer transition-colors apple-press';
        triggerDynamicIsland('Autopay Paused', 'Tap to resume');
      }} else {{
        toggleEl.className = 'w-10 h-6 rounded-full bg-emerald-500 p-0.5 flex items-center justify-end cursor-pointer transition-colors apple-press';
        triggerDynamicIsland('Autopay Active', 'Scheduled on due date');
      }}
    }}

    /* Tab Switch with Liquid Apple Pop */
    /* Master dock switcher consolidated */
    function syncAllDockPills(activeTab) {{
      const tabs = ['home', 'finance', 'statistics', 'others'];
      const effectiveTab = (activeTab === 'carddetail' || activeTab === 'sendmoney') ? 'home' : ((activeTab === 'vault') ? 'finance' : activeTab);
      
      const globalNav = document.getElementById('globalBottomNav');
      if (globalNav) {{
        // Nav is visible on the main app screens: Home, Card Details, Send Money, Finance, Vault, Statistics, Others
        const showNav = ['home', 'carddetail', 'sendmoney', 'statistics', 'finance', 'others', 'vault'].includes(activeTab);
        if (showNav) {{
          globalNav.classList.remove('nav-hidden');
          globalNav.classList.add('nav-visible');
        }} else {{
          globalNav.classList.remove('nav-visible');
          globalNav.classList.add('nav-hidden');
        }}
      }}

      tabs.forEach(tabName => {{
        const tabEl = document.getElementById('dock-tab-' + tabName);
        const barEl = document.getElementById('bar-' + tabName);

        if (tabEl) {{
          const labelEl = tabEl.querySelector('span');
          if (tabName === effectiveTab) {{
            tabEl.classList.add('active');
            if (labelEl) {{
              labelEl.className = 'text-[12px] font-semibold tracking-tight text-white';
            }}
          }} else {{
            tabEl.classList.remove('active');
            if (labelEl) {{
              labelEl.className = 'text-[12px] font-normal tracking-tight text-[#9e94b8]';
            }}
          }}
        }}

        if (barEl) {{
          if (tabName === effectiveTab) {{
            barEl.classList.remove('hidden');
          }} else {{
            barEl.classList.add('hidden');
          }}
        }}
      }});
    }}

    function selectDockTab(tab) {{
      playHapticTick();

      try {{
        if (typeof closeBillPayModal === 'function') closeBillPayModal();
        if (typeof closeSplitBillModal === 'function') closeSplitBillModal();
        if (typeof closeGiftCardsModal === 'function') closeGiftCardsModal();
        if (typeof closeRewardsModal === 'function') closeRewardsModal();
        if (typeof closeTransferModal === 'function') closeTransferModal();
        if (typeof closeExchangeModal === 'function') closeExchangeModal();
        if (typeof closeSupportChat === 'function') closeSupportChat();
        if (typeof closeSignOutModal === 'function') closeSignOutModal();
      }} catch (e) {{
        console.warn('Modal close error:', e);
      }}

      const screenMap = {{
        'home': 'home',
        'finance': 'finance',
        'statistics': 'statistics',
        'others': 'others'
      }};

      const target = screenMap[tab] || tab;
      syncAllDockPills(tab);
      triggerTabSkeletonLoader(target);
      showScreen(target);
    }}

    let tabSkeletonTimer = null;
    function triggerTabSkeletonLoader(targetTab) {{
      const overlay = document.getElementById('tabSkeletonOverlay');
      if (!overlay) return;

      const heroMap = {{
        'home': 'skelHeroHome',
        'finance': 'skelHeroFinance',
        'statistics': 'skelHeroStatistics',
        'others': 'skelHeroOthers'
      }};

      ['skelHeroHome', 'skelHeroFinance', 'skelHeroStatistics', 'skelHeroOthers'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{
          if (id === (heroMap[targetTab] || 'skelHeroHome')) {{
            el.classList.remove('hidden');
          }} else {{
            el.classList.add('hidden');
          }}
        }}
      }});

      clearTimeout(tabSkeletonTimer);
      overlay.style.transition = 'opacity 0.16s cubic-bezier(0.16, 1, 0.3, 1), transform 0.28s cubic-bezier(0.16, 1, 0.3, 1)';
      overlay.style.transform = 'scale(1)';
      overlay.classList.remove('opacity-0', 'pointer-events-none');
      overlay.classList.add('opacity-100');

      tabSkeletonTimer = setTimeout(() => {{
        overlay.style.transition = 'opacity 0.45s cubic-bezier(0.22, 1, 0.36, 1), transform 0.45s cubic-bezier(0.22, 1, 0.36, 1)';
        overlay.style.transform = 'scale(1.008)';
        overlay.classList.remove('opacity-100');
        overlay.classList.add('opacity-0', 'pointer-events-none');
      }}, 360);
    }}

    /* Finance Screen Stealth Mode Privacy Toggle */
    let isStealthModeActive = false;
    function toggleStealthMode() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      isStealthModeActive = !isStealthModeActive;
      const netWorthEl = document.getElementById('financeNetWorth');
      const toggleLabelEl = document.getElementById('stealthToggleLabel');
      const toggleIconEl = document.getElementById('stealthToggleIcon');

      if (isStealthModeActive) {{
        if (netWorthEl) netWorthEl.textContent = '••••••••';
        if (toggleLabelEl) toggleLabelEl.textContent = 'Hidden';
        if (toggleIconEl) {{
          toggleIconEl.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l18 18" />';
        }}
        if (typeof triggerDynamicIsland === 'function') {{
          triggerDynamicIsland('Privacy Mode', 'Balances hidden');
        }}
      }} else {{
        if (netWorthEl) netWorthEl.textContent = '23,901.20';
        if (toggleLabelEl) toggleLabelEl.textContent = 'Visible';
        if (toggleIconEl) {{
          toggleIconEl.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>';
        }}
        if (typeof triggerDynamicIsland === 'function') {{
          triggerDynamicIsland('Portfolio Visible', '23,901.20 AED');
        }}
      }}
    }}

    /* Transfer Modal Controls */
    function openTransferModal() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const modal = document.getElementById('transferModal');
      const sheet = document.getElementById('transferSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        sheet.classList.remove('translate-y-full');
      }}
    }}

    function closeTransferModal() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const modal = document.getElementById('transferModal');
      const sheet = document.getElementById('transferSheet');
      if (modal && sheet) {{
        sheet.classList.add('translate-y-full');
        modal.classList.add('opacity-0', 'pointer-events-none');
      }}
    }}

    const transferAccountsData = {{
      mastercard: {{
        name: 'Cashleap Mastercard',
        sub: 'Primary Wallet •••• 0329',
        digits: '0329',
        balance: '3,350.60 AED',
        artClass: 'w-11 h-7 rounded-lg debit-card-gradient flex items-center justify-center p-1 shadow-sm flex-shrink-0 border border-white/20'
      }},
      debit: {{
        name: 'Cashleap Debit',
        sub: 'Secondary Card •••• 0319',
        digits: '0319',
        balance: '2,150.60 AED',
        artClass: 'w-11 h-7 rounded-lg bg-gradient-to-tr from-pink-500 via-purple-500 to-cyan-400 flex items-center justify-center p-1 shadow-sm flex-shrink-0 border border-white/20'
      }},
      nbd: {{
        name: 'Emirates NBD Checking',
        sub: 'Linked Bank •••• 8920',
        digits: '8920',
        balance: '14,250.00 AED',
        artClass: 'w-11 h-7 rounded-lg bg-gradient-to-tr from-blue-700 to-cyan-500 flex items-center justify-center p-1 shadow-sm flex-shrink-0 border border-white/20'
      }},
      vault: {{
        name: 'Emergency Reserve Vault',
        sub: '4.8% APY Savings Vault',
        digits: 'VAULT',
        balance: '18,500.00 AED',
        artClass: 'w-11 h-7 rounded-lg bg-gradient-to-tr from-emerald-600 to-teal-400 flex items-center justify-center p-1 shadow-sm flex-shrink-0 border border-white/20'
      }}
    }};

    let currentTransferFrom = 'mastercard';
    let currentTransferTo = 'debit';
    let swapRotationDeg = 0;

    function selectTransferFrom(key) {{
      if (typeof playHapticTick === 'function') playHapticTick();
      currentTransferFrom = key;
      const info = transferAccountsData[key] || transferAccountsData.mastercard;

      const art = document.getElementById('transferFromCardArt');
      const digits = document.getElementById('transferFromCardDigits');
      const name = document.getElementById('transferFromName');
      const sub = document.getElementById('transferFromSub');
      const bal = document.getElementById('transferFromBalance');
      const avail = document.getElementById('transferFromAvailBadge');

      if (art) art.className = info.artClass;
      if (digits) digits.textContent = info.digits;
      if (name) name.textContent = info.name;
      if (sub) sub.textContent = info.sub;
      if (bal) bal.textContent = info.balance;
      if (avail) avail.textContent = 'Available: ' + info.balance;

      ['mastercard', 'debit', 'nbd'].forEach(k => {{
        const pill = document.getElementById('from-pill-' + k);
        if (pill) {{
          if (k === key) {{
            pill.className = 'py-1.5 px-2 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[10.5px] font-semibold text-white transition cursor-pointer truncate';
          }} else {{
            pill.className = 'py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 hover:bg-white/[0.08] text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer truncate';
          }}
        }}
      }});

      if (currentTransferTo === key) {{
        const fallback = (key === 'mastercard') ? 'debit' : 'mastercard';
        selectTransferTo(fallback);
      }}
    }}

    function selectTransferTo(key) {{
      if (typeof playHapticTick === 'function') playHapticTick();
      currentTransferTo = key;
      const info = transferAccountsData[key] || transferAccountsData.debit;

      const art = document.getElementById('transferToCardArt');
      const digits = document.getElementById('transferToCardDigits');
      const name = document.getElementById('transferToName');
      const sub = document.getElementById('transferToSub');
      const bal = document.getElementById('transferToBalance');

      if (art) art.className = info.artClass;
      if (digits) digits.textContent = info.digits;
      if (name) name.textContent = info.name;
      if (sub) sub.textContent = info.sub;
      if (bal) bal.textContent = info.balance;

      ['debit', 'mastercard', 'vault'].forEach(k => {{
        const pill = document.getElementById('to-pill-' + k);
        if (pill) {{
          if (k === key) {{
            pill.className = 'py-1.5 px-2 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[10.5px] font-semibold text-white transition cursor-pointer truncate';
          }} else {{
            pill.className = 'py-1.5 px-2 rounded-lg bg-white/[0.04] border border-white/10 hover:bg-white/[0.08] text-[10.5px] font-medium text-[#9e94b8] transition cursor-pointer truncate';
          }}
        }}
      }});
    }}

    function swapTransferAccounts() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      swapRotationDeg += 180;
      const btn = document.getElementById('transferSwapBtn');
      if (btn) btn.style.transform = 'rotate(' + swapRotationDeg + 'deg)';

      const prevFrom = currentTransferFrom;
      const prevTo = currentTransferTo;
      const validFrom = ['mastercard', 'debit', 'nbd'].includes(prevTo) ? prevTo : 'debit';
      const validTo = ['debit', 'mastercard', 'vault'].includes(prevFrom) ? prevFrom : 'mastercard';

      selectTransferFrom(validFrom);
      selectTransferTo(validTo);
    }}

    function setTransferPresetAmount(val, btnEl) {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const input = document.getElementById('transferAmountInput');
      if (input) input.value = val;

      const chips = document.querySelectorAll('.transfer-preset-chip');
      chips.forEach(c => {{
        c.className = 'transfer-preset-chip py-1.5 rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 text-[11px] font-semibold text-slate-300 transition cursor-pointer';
      }});
      if (btnEl) {{
        btnEl.className = 'transfer-preset-chip py-1.5 rounded-lg bg-blue-600/25 border border-blue-500/60 text-[11px] font-semibold text-white transition cursor-pointer';
      }}
    }}

    function executeTransfer() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const amtEl = document.getElementById('transferAmountInput');
      const amt = (amtEl && amtEl.value) ? parseFloat(amtEl.value).toFixed(2) : '500.00';
      const fromInfo = transferAccountsData[currentTransferFrom] || transferAccountsData.mastercard;
      const toInfo = transferAccountsData[currentTransferTo] || transferAccountsData.debit;
      closeTransferModal();
      if (typeof triggerDynamicIsland === 'function') {{
        triggerDynamicIsland('Transfer Complete', amt + ' AED to ' + toInfo.name);
      }}
      if (typeof showToast === 'function') {{
        showToast('Transferred ' + amt + ' AED from ' + fromInfo.name + ' to ' + toInfo.name);
      }}
    }}

    /* Currency Exchange Modal Controls */
    function openExchangeModal() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const modal = document.getElementById('exchangeModal');
      const sheet = document.getElementById('exchangeSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        sheet.classList.remove('translate-y-full');
      }}
      calculateExchange();
    }}

    function closeExchangeModal() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const modal = document.getElementById('exchangeModal');
      const sheet = document.getElementById('exchangeSheet');
      if (modal && sheet) {{
        sheet.classList.add('translate-y-full');
        modal.classList.add('opacity-0', 'pointer-events-none');
      }}
    }}

    function calculateExchange() {{
      const input = document.getElementById('exchangeFromInput');
      const output = document.getElementById('exchangeToOutput');
      if (input && output) {{
        const val = parseFloat(input.value) || 0;
        const converted = (val / 3.6725).toFixed(2);
        output.textContent = converted;
      }}
    }}

    function executeExchange() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const input = document.getElementById('exchangeFromInput');
      const output = document.getElementById('exchangeToOutput');
      const val = input ? input.value : '1000';
      const usd = output ? output.textContent : '272.29';
      closeExchangeModal();
      if (typeof triggerDynamicIsland === 'function') {{
        triggerDynamicIsland('FX Exchange', val + ' AED ➔ $' + usd + ' USD', '<span class="text-xs text-emerald-400">✓</span>');
      }}
      if (typeof showToast === 'function') {{
        showToast('Exchanged ' + val + ' AED to $' + usd + ' USD');
      }}
    }}

    /* 24/7 Concierge Support Chat */
    function openSupportChat() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const modal = document.getElementById('supportChatModal');
      const sheet = document.getElementById('supportChatSheet');
      if (modal && sheet) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        sheet.classList.remove('translate-y-full');
      }}
    }}

    function closeSupportChat() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const modal = document.getElementById('supportChatModal');
      const sheet = document.getElementById('supportChatSheet');
      if (modal && sheet) {{
        sheet.classList.add('translate-y-full');
        modal.classList.add('opacity-0', 'pointer-events-none');
      }}
    }}

    function sendSupportMessage() {{
      const input = document.getElementById('supportChatInput');
      const list = document.getElementById('supportMessagesList');
      if (!input || !list || !input.value.trim()) return;

      if (typeof playHapticTick === 'function') playHapticTick();
      const userText = input.value.trim();
      input.value = '';

      const userDiv = document.createElement('div');
      userDiv.className = 'flex justify-end';
      userDiv.innerHTML = `<div class="bg-blue-600 text-white rounded-2xl rounded-tr-sm px-3.5 py-2 max-w-[80%]">${{userText}}</div>`;
      list.appendChild(userDiv);
      list.scrollTop = list.scrollHeight;

      setTimeout(() => {{
        const agentDiv = document.createElement('div');
        agentDiv.className = 'flex justify-start';
        agentDiv.innerHTML = `<div class="bg-white/10 rounded-2xl rounded-tl-sm px-3.5 py-2 max-w-[80%] text-white/90">Thank you for reaching out, Marice. A senior representative is reviewing your request right now.</div>`;
        list.appendChild(agentDiv);
        list.scrollTop = list.scrollHeight;
        if (typeof triggerDynamicIsland === 'function') {{
          triggerDynamicIsland('Support Concierge', 'New reply received');
        }}
      }}, 900);
    }}

    /* Sign Out Dialog Controls */
    function closeSignOutModal() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      const modal = document.getElementById('signOutModal');
      if (modal) modal.classList.add('opacity-0', 'pointer-events-none');
    }}

    function confirmSignOut() {{
      if (typeof playHapticTick === 'function') playHapticTick();
      closeSignOutModal();
      showScreen('login');
      if (typeof triggerDynamicIsland === 'function') {{
        triggerDynamicIsland('Signed Out', 'Security lock enabled');
      }}
    }}

    /* ========================================================
       UNIVERSAL DRAGGABLE ENGINE FOR ALL BOTTOM SHEETS (PERSISTENT & MODAL)
       ======================================================== */
    function attachFullSheetDrag(sheetId, handleId, listId, getExpanded, setExpandedFn, collapsedY, expandedY, toggleBtnId) {{
      const sheet = document.getElementById(sheetId);
      const handleArea = document.getElementById(handleId);
      const listEl = listId ? document.getElementById(listId) : null;
      if (!sheet) return;

      let dragging = false;
      let startY = 0;
      let deltaY = 0;
      let initY = collapsedY;
      let moved = false;
      let startedOnHandle = false;

      function startDrag(clientY, target) {{
        if (toggleBtnId && target && target.closest('#' + toggleBtnId)) return false;
        startedOnHandle = !!(handleArea && target && handleArea.contains(target));
        // If touching inside the scrollable list when already expanded and scrolled down, let list scroll first
        if (!startedOnHandle && getExpanded() && listEl && listEl.scrollTop > 2) return false;
        dragging = true;
        moved = false;
        startY = clientY;
        deltaY = 0;
        initY = getExpanded() ? expandedY : collapsedY;
        sheet.style.transition = 'none';
        if (handleArea) handleArea.style.cursor = 'grabbing';
        return true;
      }}

      function moveDrag(clientY, e) {{
        if (!dragging) return;
        deltaY = clientY - startY;

        // If started on list body (not handle), only hijack into sheet drag if pulling up when collapsed, or pulling down at scrollTop<=0 when expanded
        if (!startedOnHandle) {{
          if (!getExpanded() && deltaY > 0) {{
            // Allow normal list scroll downward when collapsed
            dragging = false;
            return;
          }}
          if (getExpanded() && deltaY < 0) {{
            // Allow normal list scroll upward when expanded
            dragging = false;
            return;
          }}
        }}

        if (Math.abs(deltaY) > 4) {{
          moved = true;
          if (e && e.cancelable) e.preventDefault();
        }}
        if (!moved) return;

        let newY = initY + deltaY;
        if (newY < expandedY - 30) {{
          newY = (expandedY - 30) + (newY - (expandedY - 30)) * 0.22;
        }} else if (newY > collapsedY + 45) {{
          newY = (collapsedY + 45) + (newY - (collapsedY + 45)) * 0.22;
        }}
        sheet.style.transform = 'translateY(' + newY + 'px)';
      }}

      function endDrag() {{
        if (!dragging) return;
        dragging = false;
        if (handleArea) handleArea.style.cursor = 'grab';
        sheet.style.transition = 'transform 0.42s cubic-bezier(0.16, 1, 0.3, 1)';

        if (moved && Math.abs(deltaY) > 26) {{
          if (deltaY < -26) {{
            setExpandedFn(true);
          }} else {{
            setExpandedFn(false);
          }}
        }} else if (!moved && startedOnHandle) {{
          setExpandedFn(!getExpanded());
        }} else {{
          setExpandedFn(getExpanded());
        }}
      }}

      // Suppress accidental item click right after dragging the sheet
      sheet.addEventListener('click', (e) => {{
        if (moved) {{
          e.stopPropagation();
          e.preventDefault();
          moved = false;
        }}
      }}, true);

      sheet.addEventListener('pointerdown', (e) => {{
        if (startDrag(e.clientY, e.target)) {{
          if (startedOnHandle && e.cancelable) e.preventDefault();
        }}
      }});
      window.addEventListener('pointermove', (e) => {{
        if (dragging) moveDrag(e.clientY, e);
      }});
      window.addEventListener('pointerup', () => {{
        if (dragging) endDrag();
      }});
      window.addEventListener('pointercancel', () => {{
        if (dragging) endDrag();
      }});

      // Touch fallback for mobile Safari/Chrome
      sheet.addEventListener('touchstart', (e) => {{
        if (e.touches && e.touches[0]) {{
          startDrag(e.touches[0].clientY, e.target);
        }}
      }}, {{ passive: true }});
      window.addEventListener('touchmove', (e) => {{
        if (dragging && e.touches && e.touches[0]) {{
          moveDrag(e.touches[0].clientY, e);
        }}
      }}, {{ passive: false }});
      window.addEventListener('touchend', () => {{
        if (dragging) endDrag();
      }});
    }}

    function initAllModalSheetsDragging() {{
      // Attach smooth drag-to-dismiss & rubber-band physics to ALL modal bottom sheets
      const modalConfigs = [
        {{ modalId: 'transferModal', sheetId: 'transferSheet', closeFn: closeTransferModal }},
        {{ modalId: 'exchangeModal', sheetId: 'exchangeSheet', closeFn: closeExchangeModal }},
        {{ modalId: 'addCardModal', sheetId: 'addCardSheet', closeFn: closeAddCardModal }},
        {{ modalId: 'userProfileModal', sheetId: 'userProfileSheet', closeFn: closeUserProfileModal }},
        {{ modalId: 'selectCardModal', sheetId: 'selectCardSheet', closeFn: closeCardSelectionModal }},
        {{ modalId: 'cardDetailsModal', sheetId: 'cardDetailsSheet', closeFn: closeCardDetailsModal }},
        {{ modalId: 'txDetailModal', sheetId: 'txDetailSheet', closeFn: closeTxDetail }},
        {{ modalId: 'notificationsModal', sheetId: 'notificationsSheet', closeFn: closeNotificationsModal }},
        {{ modalId: 'addFundsModal', sheetId: 'addFundsSheet', closeFn: () => closeQuickActionModal('addFunds') }},
        {{ modalId: 'sendMoneyModal', sheetId: 'sendMoneySheet', closeFn: () => closeQuickActionModal('sendMoney') }},
        {{ modalId: 'withdrawModal', sheetId: 'withdrawSheet', closeFn: () => closeQuickActionModal('withdraw') }},
        {{ modalId: 'scheduleModal', sheetId: 'scheduleSheet', closeFn: () => closeQuickActionModal('schedule') }},
        {{ modalId: 'billPayModal', sheetId: 'billPaySheet', closeFn: closeBillPayModal }},
        {{ modalId: 'splitBillModal', sheetId: 'splitBillSheet', closeFn: closeSplitBillModal }},
        {{ modalId: 'giftCardsModal', sheetId: 'giftCardsSheet', closeFn: closeGiftCardsModal }},
        {{ modalId: 'rewardsModal', sheetId: 'rewardsSheet', closeFn: closeRewardsModal }},
        {{ modalId: 'supportChatModal', sheetId: 'supportChatSheet', closeFn: closeSupportChat }},
        {{ modalId: 'createVaultModal', sheetId: 'createVaultSheet', closeFn: closeCreateVaultModal }},
        {{ modalId: 'vaultActionModal', sheetId: 'vaultActionSheet', closeFn: closeVaultActionModal }},
        {{ modalId: 'addBeneficiaryModal', sheetId: 'addBeneficiarySheet', closeFn: closeAddBeneficiaryModal }}
      ];

      modalConfigs.forEach(cfg => {{
        const sheet = document.getElementById(cfg.sheetId);
        if (!sheet) return;

        let isDraggingModal = false;
        let startY = 0;
        let deltaY = 0;
        let hasMoved = false;

        function onStart(clientY, target) {{
          // Do not hijack interactive inputs, buttons, or sliders inside modals
          if (target && target.closest('input, select, textarea, button, #sendSlideThumb, #sendSlideTrack')) return;
          const scrollChild = target ? target.closest('.overflow-y-auto') : null;
          if (scrollChild && scrollChild.scrollTop > 2) return;

          isDraggingModal = true;
          hasMoved = false;
          startY = clientY;
          deltaY = 0;
          sheet.style.transition = 'none';
        }}

        function onMove(clientY, e) {{
          if (!isDraggingModal) return;
          deltaY = clientY - startY;
          if (Math.abs(deltaY) > 4) {{
            hasMoved = true;
            if (e && e.cancelable) e.preventDefault();
          }}
          if (!hasMoved) return;

          let newY = deltaY;
          if (newY < 0) {{
            // Rubber-band upward resistance
            newY = newY * 0.2;
          }}
          sheet.style.transform = 'translateY(' + newY + 'px)';
        }}

        function onEnd() {{
          if (!isDraggingModal) return;
          isDraggingModal = false;
          sheet.style.transition = 'transform 0.35s cubic-bezier(0.32, 0.72, 0, 1)';

          if (hasMoved && deltaY > 55) {{
            sheet.style.transform = '';
            if (typeof cfg.closeFn === 'function') cfg.closeFn();
          }} else {{
            sheet.style.transform = '';
          }}
        }}

        sheet.addEventListener('pointerdown', (e) => onStart(e.clientY, e.target));
        window.addEventListener('pointermove', (e) => {{ if (isDraggingModal) onMove(e.clientY, e); }});
        window.addEventListener('pointerup', () => {{ if (isDraggingModal) onEnd(); }});
        window.addEventListener('pointercancel', () => {{ if (isDraggingModal) onEnd(); }});

        sheet.addEventListener('touchstart', (e) => {{
          if (e.touches && e.touches[0]) onStart(e.touches[0].clientY, e.target);
        }}, {{ passive: true }});
        window.addEventListener('touchmove', (e) => {{
          if (isDraggingModal && e.touches && e.touches[0]) onMove(e.touches[0].clientY, e);
        }}, {{ passive: false }});
        window.addEventListener('touchend', () => {{ if (isDraggingModal) onEnd(); }});
      }});
    }}

    let appInitialized = false;
    function initCashleapPrototype() {{
      if (appInitialized) return;
      appInitialized = true;
      const params = new URLSearchParams(window.location.search);
      const initial = params.get('screen');
      try {{ initLoginSlider(); }} catch (e) {{ console.error(e); }}
      try {{ initCardCarouselDragging(); }} catch (e) {{ console.error(e); }}
      try {{ initCard3DParallax(); }} catch (e) {{ console.error(e); }}
      try {{ initSendSlider(); }} catch (e) {{ console.error(e); }}
      try {{ initBottomSheetDragging(); }} catch (e) {{ console.error(e); }}
      try {{ initStatsBottomSheetDragging(); }} catch (e) {{ console.error(e); }}
      try {{ initFinanceBottomSheetDragging(); }} catch (e) {{ console.error(e); }}
      try {{ initOthersBottomSheetDragging(); }} catch (e) {{ console.error(e); }}
      try {{
        attachFullSheetDrag('recentTransactionsSheet', 'sheetDragHandleArea', 'sheetScrollArea', () => isSheetExpanded, setSheetExpanded, SHEET_COLLAPSED_Y, SHEET_EXPANDED_Y, 'sheetToggleBtn');
        attachFullSheetDrag('statsCategoriesSheet', 'statsSheetDragHandleArea', 'statsCategoriesList', () => isStatsSheetExpanded, setStatsSheetExpanded, STATS_SHEET_COLLAPSED_Y, STATS_SHEET_EXPANDED_Y, 'statsSheetToggleBtn');
        attachFullSheetDrag('financeBottomSheet', 'financeSheetDragHandleArea', 'financeAccountsList', () => isFinanceSheetExpanded, setFinanceSheetExpanded, FINANCE_SHEET_COLLAPSED_Y, FINANCE_SHEET_EXPANDED_Y, 'financeSheetToggleBtn');
        attachFullSheetDrag('othersBottomSheet', 'othersSheetDragHandleArea', 'othersFeaturesList', () => isOthersSheetExpanded, setOthersSheetExpanded, OTHERS_SHEET_COLLAPSED_Y, OTHERS_SHEET_EXPANDED_Y, 'othersSheetToggleBtn');
        attachFullSheetDrag('vaultGoalsSheet', 'vaultSheetDragHandleArea', 'vaultGoalsList', () => isVaultSheetExpanded, setVaultSheetExpanded, VAULT_SHEET_COLLAPSED_Y, VAULT_SHEET_EXPANDED_Y, 'vaultSheetToggleBtn');
        attachFullSheetDrag('sendBeneficiariesSheet', 'sendSheetDragHandleArea', 'sendBeneficiariesList', () => isSendSheetExpanded, setSendSheetExpanded, SEND_SHEET_COLLAPSED_Y, SEND_SHEET_EXPANDED_Y, 'sendSheetToggleBtn');
        initAllModalSheetsDragging();
      }} catch (e) {{ console.error(e); }}

      if (initial && screens[initial]) {{
        showScreen(initial);
      }} else {{
        showScreen('splash');
      }}
      
      const openSheet = params.get('openSheet');
      if (openSheet === 'notifications') {{
        setTimeout(openNotificationsModal, 300);
      }} else if (openSheet === 'txDetail') {{
        setTimeout(() => openTxDetail('amazonPrime'), 300);
      }} else if (openSheet === 'add') {{
        setTimeout(() => triggerQuickAction('add'), 300);
      }} else if (openSheet === 'send') {{
        setTimeout(() => triggerQuickAction('send'), 300);
      }} else if (openSheet === 'withdraw') {{
        setTimeout(() => triggerQuickAction('withdraw'), 300);
      }} else if (openSheet === 'schedule') {{
        setTimeout(() => triggerQuickAction('schedule'), 300);
      }} else if (openSheet === 'cardDetails') {{
        setTimeout(openCardDetailsModal, 300);
      }} else if (openSheet === 'selectCard') {{
        setTimeout(openCardSelectionModal, 300);
      }} else if (openSheet === 'recentTransactions') {{
        setTimeout(() => setSheetExpanded(true), 300);
      }} else if (openSheet === 'statsCategories') {{
        setTimeout(() => setStatsSheetExpanded(true), 300);
      }} else if (openSheet === 'financeSheet') {{
        setTimeout(() => setFinanceSheetExpanded(true), 300);
      }} else if (openSheet === 'othersSheet') {{
        setTimeout(() => setOthersSheetExpanded(true), 300);
      }} else if (openSheet === 'billPay') {{
        setTimeout(openBillPayModal, 40);
      }} else if (openSheet === 'splitBill') {{
        setTimeout(openSplitBillModal, 40);
      }} else if (openSheet === 'giftCards') {{
        setTimeout(openGiftCardsModal, 40);
      }} else if (openSheet === 'rewards') {{
        setTimeout(openRewardsModal, 40);
      }} else if (openSheet === 'transfer') {{
        setTimeout(openTransferModal, 300);
      }} else if (openSheet === 'exchange') {{
        setTimeout(openExchangeModal, 300);
      }} else if (openSheet === 'support') {{
        setTimeout(openSupportChat, 300);
      }} else if (openSheet === 'signOut') {{
        setTimeout(openSignOutConfirmation, 300);
      }}
    }}
    window.addEventListener('DOMContentLoaded', initCashleapPrototype);
    if (document.readyState !== 'loading') {{
      initCashleapPrototype();
    }}
  </script>
</body>
</html>
"""

with open('cashleap_mobile_prototype.html', 'w') as f:
    f.write(html_content)

if os.path.islink('index.html'):
    os.unlink('index.html')
with open('index.html', 'w') as f:
    f.write(html_content)

print('Updated cashleap_mobile_prototype.html and index.html! Size:', len(html_content))
