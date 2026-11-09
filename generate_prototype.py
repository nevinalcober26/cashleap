import os

with open('marice_avatar_b64.txt') as f:
    avatar_b64 = f.read().strip()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CASHLEAP - Mobile Prototype Previewer</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    body {{
      font-family: var(--font-main);
      background: radial-gradient(circle at 50% 20%, #1e1b38 0%, #090814 100%);
      min-height: 100vh;
      margin: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      overflow-x: hidden;
      user-select: none;
      -webkit-user-select: none;
    }}

    /* Phone Frame Styling */
    .phone-frame {{
      width: 375px;
      height: 812px;
      border-radius: 44px;
      position: relative;
      overflow: hidden;
      box-shadow: 
        0 0 0 10px #191826,
        0 0 0 12px #2e2c44,
        0 30px 70px -10px rgba(0, 0, 0, 0.75),
        0 0 80px rgba(88, 46, 180, 0.25);
      background: #0d0c2b;
      transform-origin: center center;
    }}

    @media (max-height: 920px) {{
      .phone-frame {{
        transform: scale(0.88);
        margin-top: -28px;
        margin-bottom: -28px;
      }}
    }}
    @media (max-height: 780px) {{
      .phone-frame {{
        transform: scale(0.76);
        margin-top: -75px;
        margin-bottom: -75px;
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

    /* Screen 5: Welcome Screen gradient precisely matched to uploaded image */
    .welcome-bg {{
      background-color: #382c7a;
      background-image: 
        radial-gradient(circle at 95% 42%, rgba(135, 70, 130, 0.75) 0%, rgba(135, 70, 130, 0) 55%),
        radial-gradient(circle at 8% 88%, rgba(44, 62, 160, 0.88) 0%, rgba(44, 62, 160, 0) 58%),
        radial-gradient(circle at 88% 8%, rgba(105, 41, 140, 0.68) 0%, rgba(105, 41, 140, 0) 45%),
        linear-gradient(160deg, #654480 0%, #52357a 32%, #3d3480 65%, #2c3e9b 100%);
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
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      transition: opacity 0.55s cubic-bezier(0.22, 1, 0.36, 1), transform 0.55s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .screen-hidden-left {{
      opacity: 0;
      transform: translateX(-24px) scale(0.97);
      pointer-events: none;
    }}
    .screen-hidden-right {{
      opacity: 0;
      transform: translateX(24px) scale(0.97);
      pointer-events: none;
    }}
    .screen-active {{
      opacity: 1;
      transform: translate(0, 0) scale(1);
      pointer-events: auto;
    }}

    /* Login Cards */
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
      box-shadow: 0 12px 30px -8px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.1);
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
      box-shadow: 0 0 0 4px rgba(255, 42, 109, 0.22), 0 4px 12px rgba(255, 42, 109, 0.55);
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
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45), inset 0 1px 1px rgba(255, 255, 255, 0.05);
      backdrop-filter: blur(16px);
    }}
    .slider-thumb {{
      width: 72px;
      height: 72px;
      border-radius: 9999px;
      background: linear-gradient(145deg, #2d82ff 0%, #1c6ef2 100%);
      box-shadow: 0 6px 20px rgba(36, 120, 255, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.35);
      touch-action: none;
      transition: transform 0.25s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.25s ease;
    }}
    .slider-thumb.dragging {{
      transition: none;
      box-shadow: 0 8px 26px rgba(36, 120, 255, 0.75), inset 0 1px 2px rgba(255, 255, 255, 0.5);
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
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.1);
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
    .passcode-dot.error {{
      background: #ff2a6d;
      border-color: #ff2a6d;
      box-shadow: 0 0 14px rgba(255, 42, 109, 0.85);
    }}

    /* Welcome Screen Concentric Rings (exact to uploaded image) */
    .concentric-ring-1 {{
      width: 132px;
      height: 132px;
      border-radius: 9999px;
      border: 1px solid rgba(210, 195, 245, 0.22);
      box-shadow: 0 0 25px rgba(180, 150, 230, 0.1);
    }}
    .concentric-ring-2 {{
      width: 164px;
      height: 164px;
      border-radius: 9999px;
      border: 1px solid rgba(210, 195, 245, 0.15);
    }}
    .concentric-ring-3 {{
      width: 202px;
      height: 202px;
      border-radius: 9999px;
      border: 1px solid rgba(210, 195, 245, 0.10);
    }}
    .concentric-ring-4 {{
      width: 244px;
      height: 244px;
      border-radius: 9999px;
      border: 1px solid rgba(210, 195, 245, 0.05);
    }}

    @keyframes subtleBreath {{
      0%, 100% {{ transform: scale(1); opacity: 0.85; }}
      50% {{ transform: scale(1.035); opacity: 1; }}
    }}
    .ring-pulse {{
      animation: subtleBreath 4s ease-in-out infinite;
    }}

    /* Native iOS Alert Modal */
    .ios-modal-card {{
      background: rgba(30, 28, 54, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.14);
      backdrop-filter: blur(28px);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
      border-radius: 20px;
    }}
  </style>
</head>
<body class="py-4 px-3">

  <!-- Prototype Header Navigation Bar with Interactive Screen Pills -->
  <div class="w-full max-w-[480px] mb-3 flex flex-col gap-2 bg-[#151427]/90 border border-white/10 backdrop-blur-md px-4 py-2.5 rounded-2xl shadow-xl z-30">
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="relative flex h-2.5 w-2.5">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-purple-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-purple-500"></span>
        </span>
        <span id="screenIndicator" class="text-xs font-semibold tracking-wide text-slate-200">
          Screen 1: Splash
        </span>
      </div>

      <div class="flex items-center gap-1.5">
        <button 
          onclick="replaySplash()"
          class="flex items-center gap-1 text-[11px] font-semibold bg-white/10 hover:bg-white/15 active:scale-95 text-white px-2.5 py-1 rounded-lg border border-white/10 transition cursor-pointer"
          title="Restart from Splash"
        >
          <svg class="w-3 h-3 text-purple-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Restart
        </button>
      </div>
    </div>

    <!-- Quick Screen Selector Chips -->
    <div class="flex items-center gap-1.5 overflow-x-auto pb-0.5 pt-1 text-[11px] font-medium">
      <button id="nav-chip-splash" onclick="showScreen('splash')" class="px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-semibold shadow transition cursor-pointer">1. Splash</button>
      <button id="nav-chip-login" onclick="showScreen('login')" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 transition cursor-pointer">2. Login Type</button>
      <button id="nav-chip-faceid" onclick="showScreen('faceid')" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 transition cursor-pointer">3. Face ID</button>
      <button id="nav-chip-secretkey" onclick="showScreen('secretkey')" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 transition cursor-pointer">4. Secret Key</button>
      <button id="nav-chip-welcome" onclick="showScreen('welcome')" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 transition cursor-pointer">5. Welcome</button>
    </div>
  </div>

  <!-- Mobile Device Viewport Frame -->
  <div class="phone-frame" id="phoneFrame">

    <!-- Persistent iOS Status Bar -->
    <div class="absolute top-0 inset-x-0 h-11 px-7 flex items-center justify-between z-40 pointer-events-none text-white">
      <div class="flex items-center gap-1.5">
        <svg width="17" height="11" viewBox="0 0 17 11" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="0.5" y="7" width="2.6" height="3.5" rx="0.8" fill="white"/>
          <rect x="4.6" y="5" width="2.6" height="5.5" rx="0.8" fill="white"/>
          <rect x="8.7" y="2.8" width="2.6" height="7.7" rx="0.8" fill="white"/>
          <rect x="12.8" y="0.5" width="2.6" height="10" rx="0.8" fill="white" fill-opacity="0.35"/>
        </svg>
        <span class="text-[12.5px] font-medium tracking-tight leading-none">Service</span>
      </div>

      <div class="absolute left-1/2 -translate-x-1/2 text-[13.5px] font-semibold tracking-tight">
        19:02
      </div>

      <div class="flex items-center gap-2">
        <svg width="15" height="11" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8 9.4C8.75 9.4 9.35 10 9.35 10.75C9.35 11.5 8.75 12.1 8 12.1C7.25 12.1 6.65 11.5 6.65 10.75C6.65 10 7.25 9.4 8 9.4ZM4.25 7.45C6.35 5.65 9.65 5.65 11.75 7.45L10.55 8.75C9.1 7.5 6.9 7.5 5.45 8.75L4.25 7.45ZM1.5 4.7C5.15 1.5 10.85 1.5 14.5 4.7L13.3 6C10.3 3.4 5.7 3.4 2.7 6L1.5 4.7Z" fill="white"/>
        </svg>
        <svg width="24" height="12" viewBox="0 0 25 12" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="0.5" y="1" width="21" height="10" rx="2.5" stroke="white" stroke-opacity="0.45" stroke-width="1"/>
          <rect x="2" y="2.5" width="14.5" height="7" rx="1.3" fill="white"/>
          <path d="M23 4.2V7.8C23.8 7.4 24.3 6.75 24.3 6C24.3 5.25 23.8 4.6 23 4.2Z" fill="white" fill-opacity="0.45"/>
        </svg>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SCREEN 1: SPLASH SCREEN                    -->
    <!-- ========================================== -->
    <div id="splashScreen" class="screen-layer splash-bg screen-active animate-splash flex flex-col items-center justify-center">
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
    <div id="loginScreen" class="screen-layer login-bg screen-hidden-right flex flex-col justify-between pt-28 pb-7 px-6">
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
          <!-- Option: Face ID -->
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

          <!-- Option: Secret Key -->
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
      <div class="relative w-full">
        <div id="sliderTrack" class="slider-track w-full flex items-center justify-between px-1.5 relative overflow-hidden">
          <button 
            id="sliderThumb"
            type="button"
            aria-label="Next"
            class="slider-thumb flex items-center justify-center text-white z-20 cursor-grab active:cursor-grabbing focus:outline-none"
          >
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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
    <div id="faceidScreen" class="screen-layer auth-bg screen-hidden-right flex flex-col justify-between pt-16 pb-8 px-6">
      <!-- Top Navigation -->
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

      <!-- Center Biometric Scanner View -->
      <div class="flex flex-col items-center justify-center my-auto">
        <!-- Scanner Frame -->
        <div id="faceidVisualBox" class="faceid-frame flex items-center justify-center is-scanning relative">
          <!-- Expanding Radar Pulses -->
          <div class="faceid-radar"></div>
          <div class="faceid-radar-2"></div>

          <!-- Corner Brackets -->
          <div class="corner-bracket corner-tl"></div>
          <div class="corner-bracket corner-tr"></div>
          <div class="corner-bracket corner-bl"></div>
          <div class="corner-bracket corner-br"></div>

          <!-- Laser Scan Beam -->
          <div class="scanning-laser"></div>

          <!-- Face ID Glyph -->
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

            <!-- Success Checkmark (hidden initially) -->
            <div id="faceidSuccessBadge" class="hidden flex items-center justify-center w-20 h-20 rounded-full bg-emerald-500/20 border-2 border-emerald-400 shadow-[0_0_30px_rgba(52,211,153,0.6)] animate-bounce">
              <svg class="w-10 h-10 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Scanning Status Text -->
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
        <!-- Main Authenticate Trigger -->
        <button 
          id="btnTriggerFaceId"
          onclick="triggerFaceIdScan()"
          class="w-full h-14 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:opacity-95 active:scale-[0.98] text-white font-semibold text-[15px] tracking-wide shadow-[0_10px_25px_rgba(37,99,235,0.4)] flex items-center justify-center gap-2 transition cursor-pointer"
        >
          <svg class="w-5 h-5 text-blue-200" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
          </svg>
          <span>Verify Face ID</span>
        </button>

        <!-- Secondary: Fallback to Secret Key or Failure Edge-case -->
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
    <div id="secretkeyScreen" class="screen-layer auth-bg screen-hidden-right flex flex-col justify-between pt-16 pb-6 px-6">
      <!-- Top Navigation -->
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

      <!-- Title & Passcode Dots Indicator -->
      <div class="flex flex-col items-center text-center mt-2">
        <!-- Glowing Key Icon Badge -->
        <div class="w-14 h-14 rounded-2xl bg-white/[0.08] border border-white/15 backdrop-blur-md flex items-center justify-center shadow-[0_10px_25px_rgba(0,0,0,0.3)] mb-3 text-purple-300">
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

        <!-- 6 Passcode Dots -->
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

      <!-- iOS-Style Custom Numeric Keypad -->
      <div class="grid grid-cols-3 gap-x-5 gap-y-3.5 mx-auto max-w-[260px] pb-1">
        <!-- 1 -->
        <button onclick="pressPinKey('1')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">1</span>
          <span class="text-[8px] font-semibold text-transparent leading-none mt-1">-</span>
        </button>
        <!-- 2 -->
        <button onclick="pressPinKey('2')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">2</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">ABC</span>
        </button>
        <!-- 3 -->
        <button onclick="pressPinKey('3')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">3</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">DEF</span>
        </button>
        <!-- 4 -->
        <button onclick="pressPinKey('4')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">4</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">GHI</span>
        </button>
        <!-- 5 -->
        <button onclick="pressPinKey('5')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">5</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">JKL</span>
        </button>
        <!-- 6 -->
        <button onclick="pressPinKey('6')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">6</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">MNO</span>
        </button>
        <!-- 7 -->
        <button onclick="pressPinKey('7')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">7</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">PQRS</span>
        </button>
        <!-- 8 -->
        <button onclick="pressPinKey('8')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">8</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">TUV</span>
        </button>
        <!-- 9 -->
        <button onclick="pressPinKey('9')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">9</span>
          <span class="text-[8px] font-semibold text-slate-400 leading-none mt-1 tracking-widest">WXYZ</span>
        </button>
        <!-- Face ID shortcut -->
        <button onclick="showScreen('faceid')" class="keypad-btn text-blue-400 hover:text-white" title="Use Face ID">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
        <!-- 0 -->
        <button onclick="pressPinKey('0')" class="keypad-btn">
          <span class="text-2xl font-semibold text-white leading-none">0</span>
          <span class="text-[8px] font-semibold text-transparent leading-none mt-1">-</span>
        </button>
        <!-- Backspace -->
        <button onclick="pressBackspace()" class="keypad-btn text-slate-300 hover:text-white" title="Delete">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2M3 12l6.414 6.414a2 2 0 001.414.586H19a2 2 0 002-2V7a2 2 0 00-2-2h-8.172a2 2 0 00-1.414.586L3 12z" />
          </svg>
        </button>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SCREEN 5: WELCOME SCREEN (Uploaded Image)  -->
    <!-- ========================================== -->
    <div id="welcomeScreen" class="screen-layer welcome-bg screen-hidden-right flex flex-col justify-between pt-24 pb-8 px-6">
      
      <!-- Center Content: Avatar + Concentric Rings + Greeting -->
      <div class="flex flex-col items-center justify-center my-auto relative">
        
        <!-- Concentric Pulsing Ripples Frame -->
        <div class="relative flex items-center justify-center ring-pulse mb-6">
          <!-- Outermost ring 4 -->
          <div class="absolute concentric-ring-4"></div>
          <!-- Ring 3 -->
          <div class="absolute concentric-ring-3"></div>
          <!-- Ring 2 -->
          <div class="absolute concentric-ring-2"></div>
          <!-- Ring 1 -->
          <div class="absolute concentric-ring-1"></div>

          <!-- Marice's Circular Avatar Image (embedded high-res base64) -->
          <div class="relative z-10 w-[110px] h-[110px] rounded-full overflow-hidden shadow-[0_12px_35px_rgba(0,0,0,0.55)] border-2 border-white/20">
            <img 
              id="mariceAvatarImg"
              src="{avatar_b64}" 
              alt="Marice" 
              class="w-full h-full object-cover"
            />
          </div>
        </div>

        <!-- Typography matching uploaded image 100% -->
        <div class="text-center mt-2">
          <p class="text-[#beb8d1] text-[16px] font-normal tracking-wide">
            Welcome back,
          </p>
          <h1 class="text-white text-[34px] font-bold tracking-tight mt-1 leading-tight">
            Marice!
          </h1>
        </div>
      </div>

      <!-- Bottom Interactive Actions & Home Indicator -->
      <div class="flex flex-col items-center space-y-4">
        <div class="flex items-center gap-2.5">
          <button 
            onclick="replaySplash()"
            class="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/15 active:scale-95 text-white/90 text-xs font-semibold backdrop-blur-md border border-white/10 transition cursor-pointer flex items-center gap-1.5"
          >
            <svg class="w-3.5 h-3.5 text-purple-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Restart Prototype
          </button>

          <button 
            onclick="showScreen('login')"
            class="px-4 py-2 rounded-xl bg-indigo-600/80 hover:bg-indigo-600 active:scale-95 text-white text-xs font-semibold backdrop-blur-md transition cursor-pointer flex items-center gap-1.5 shadow-[0_4px_16px_rgba(79,70,229,0.4)]"
          >
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
            Lock Screen
          </button>
        </div>

        <!-- iOS Home Indicator Bar -->
        <div class="w-32 h-1 bg-white/25 rounded-full pointer-events-none mt-2"></div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- NATIVE iOS FACE ID FAILURE MODAL (image 6) -->
    <!-- ========================================== -->
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

  </div>

  <!-- Footer Help Info -->
  <p class="mt-3 text-xs text-slate-400/80 text-center max-w-md">
    Interactive Flow: <b>Splash</b> &rarr; <b>Login Type</b> &rarr; [Slide Next] &rarr; <b>Face ID</b> / <b>Secret Key</b> &rarr; [Verify] &rarr; <b>Welcome Marice!</b>
  </p>

  <script>
    let currentScreen = 'splash'; // 'splash', 'login', 'faceid', 'secretkey', 'welcome'
    let selectedLoginOption = 'faceid'; // 'faceid' or 'secretkey'
    let splashTimer = null;
    let pinCode = '';
    let isScanningFace = false;

    // Elements
    const splashScreen = document.getElementById('splashScreen');
    const loginScreen = document.getElementById('loginScreen');
    const faceidScreen = document.getElementById('faceidScreen');
    const secretkeyScreen = document.getElementById('secretkeyScreen');
    const welcomeScreen = document.getElementById('welcomeScreen');
    const screenIndicator = document.getElementById('screenIndicator');

    const screens = {{
      splash: splashScreen,
      login: loginScreen,
      faceid: faceidScreen,
      secretkey: secretkeyScreen,
      welcome: welcomeScreen
    }};

    const chips = {{
      splash: document.getElementById('nav-chip-splash'),
      login: document.getElementById('nav-chip-login'),
      faceid: document.getElementById('nav-chip-faceid'),
      secretkey: document.getElementById('nav-chip-secretkey'),
      welcome: document.getElementById('nav-chip-welcome')
    }};

    function updateNavUI(target) {{
      const titles = {{
        splash: 'Screen 1: Splash',
        login: 'Screen 2: Login Type',
        faceid: 'Screen 3: Face ID',
        secretkey: 'Screen 4: Secret Key',
        welcome: 'Screen 5: Welcome Back'
      }};
      screenIndicator.textContent = titles[target] || target;

      Object.keys(chips).forEach(key => {{
        if (key === target) {{
          chips[key].className = 'px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-semibold shadow transition cursor-pointer';
        }} else {{
          chips[key].className = 'px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 transition cursor-pointer';
        }}
      }});
    }}

    function showScreen(target) {{
      clearTimeout(splashTimer);
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

      if (target === 'login') {{
        resetSliderPosition();
      }} else if (target === 'faceid') {{
        resetFaceIdUI();
        // Automatically start scanning after 450ms for realistic biometric experience
        setTimeout(() => {{
          if (currentScreen === 'faceid') triggerFaceIdScan();
        }}, 450);
      }} else if (target === 'secretkey') {{
        resetPin();
      }}
    }}

    function replaySplash() {{
      clearTimeout(splashTimer);
      showScreen('splash');
      splashScreen.classList.remove('animate-splash');
      void splashScreen.offsetWidth; // trigger reflow
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

      // Simulate biometric match after 1.2 seconds
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
          dot.classList.remove('filled', 'error');
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
      // Any 6 digits authenticate successfully for prototype flow
      setTimeout(() => {{
        // Flash success
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

    /* Bottom Slider Drag & Click Interaction */
    const sliderTrack = document.getElementById('sliderTrack');
    const sliderThumb = document.getElementById('sliderThumb');
    const sliderLabel = document.getElementById('sliderLabel');
    const sliderChevrons = document.getElementById('sliderChevrons');

    let isDragging = false;
    let startX = 0;
    let currentX = 0;
    let maxSlide = 0;
    let dragMoved = false;

    function getMaxSlide() {{
      return sliderTrack.clientWidth - sliderThumb.clientWidth - 12;
    }}

    function startDrag(e) {{
      isDragging = true;
      dragMoved = false;
      maxSlide = getMaxSlide();
      startX = (e.touches ? e.touches[0].clientX : e.clientX) - currentX;
      sliderThumb.classList.add('dragging');
    }}

    function onDrag(e) {{
      if (!isDragging) return;
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const delta = clientX - startX;
      if (Math.abs(delta) > 5) dragMoved = true;

      currentX = Math.max(0, Math.min(delta, maxSlide));
      sliderThumb.style.transform = `translateX(${{currentX}}px)`;

      const progress = maxSlide > 0 ? currentX / maxSlide : 0;
      sliderLabel.style.opacity = String(Math.max(0, 1 - progress * 1.5));
      sliderChevrons.style.opacity = String(Math.max(0.15, 1 - progress));
    }}

    function endDrag() {{
      if (!isDragging) return;
      isDragging = false;
      sliderThumb.classList.remove('dragging');

      if (!dragMoved || currentX > maxSlide * 0.5) {{
        maxSlide = getMaxSlide();
        sliderThumb.style.transform = `translateX(${{maxSlide}}px)`;
        sliderLabel.style.opacity = '0';

        setTimeout(() => {{
          // Navigate to Face ID or Secret Key based on selected option!
          if (selectedLoginOption === 'faceid') {{
            showScreen('faceid');
          }} else {{
            showScreen('secretkey');
          }}
        }}, 220);
      }} else {{
        resetSliderPosition();
      }}
    }}

    function resetSliderPosition() {{
      currentX = 0;
      sliderThumb.style.transform = 'translateX(0px)';
      sliderLabel.style.opacity = '1';
      sliderChevrons.style.opacity = '1';
    }}

    sliderThumb.addEventListener('mousedown', startDrag);
    window.addEventListener('mousemove', onDrag);
    window.addEventListener('mouseup', endDrag);

    sliderThumb.addEventListener('touchstart', startDrag, {{ passive: true }});
    window.addEventListener('touchmove', onDrag, {{ passive: true }});
    window.addEventListener('touchend', endDrag);

    // Initial load: Splash -> Login Type auto transition
    window.addEventListener('DOMContentLoaded', () => {{
      splashTimer = setTimeout(() => {{
        showScreen('login');
      }}, 2750);
    }});
  </script>
</body>
</html>
"""

with open('cashleap_mobile_prototype.html', 'w') as f:
    f.write(html_content)

print('Updated cashleap_mobile_prototype.html successfully, size:', len(html_content))
