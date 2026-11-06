from textwrap import dedent

import streamlit as st

st.set_page_config(page_title="자기소개 페이지 | 이민주", page_icon="🌼", layout="wide")

st.html(
    dedent("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Jua&display=swap');

        :root {
                --pink: #f27aa5;
                --pink-light: #ffe4ed;
                --yellow: #ffe77a;
                --cream: #fffdf8;
                --ink: #41343b;
                --muted: #82757c;
                --line: #f0e5e6;
        }
        .stApp { background: var(--cream); color: var(--ink); }
        [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none; }
        .block-container { max-width: 1080px; padding: 1rem 2rem 4rem; }
        .intro, .intro * { box-sizing: border-box; }
        .intro { color: var(--ink); font-family: 'DM Sans', 'Jua', sans-serif; }
        .nav { display: flex; justify-content: space-between; align-items: center; padding: 16px 0; border-bottom: 1px solid var(--line); }
        .logo { font-family: 'Jua', sans-serif; font-size: 21px; color: var(--pink); }
        .nav-links { display: flex; gap: 24px; }
        .nav-links a { color: var(--ink); text-decoration: none; font-size: 13px; font-weight: 700; }
        .nav-links a:hover { color: var(--pink); }
        .hero { display: grid; grid-template-columns: 1.1fr .9fr; gap: 56px; align-items: center; padding: 64px 0 76px; }
        .hello { display: inline-block; padding: 7px 12px; background: var(--yellow); border-radius: 20px; font-size: 12px; font-weight: 700; }
        .hero h1 { margin: 20px 0 14px; font-family: 'Jua', sans-serif; font-size: clamp(42px, 6vw, 68px); line-height: 1.2; }
        .hero h1 span { color: var(--pink); }
        .hero-copy { max-width: 470px; color: var(--muted); font-size: 15px; line-height: 1.9; }
        .hero-link { display: inline-block; margin-top: 15px; padding: 12px 17px; background: var(--pink); color: white; text-decoration: none; font-size: 13px; font-weight: 700; border-radius: 5px; }
        .hero-link:hover { background: var(--ink); color: white; }
        .photo-wrap { position: relative; max-width: 390px; justify-self: end; width: 100%; }
        .photo-wrap img { display: block; width: 100%; height: 350px; object-fit: cover; border: 8px solid white; border-radius: 8px; box-shadow: 0 12px 30px #bd8f9b24; }
        .photo-label { position: absolute; right: -15px; bottom: 12px; padding: 11px 15px; background: var(--yellow); border: 3px solid white; border-radius: 5px; font-family: 'Jua', sans-serif; font-size: 14px; transform: rotate(3deg); }
        .section { padding: 56px 0; border-top: 1px solid var(--line); scroll-margin-top: 20px; }
        .section-title { margin-bottom: 24px; }
        .eyebrow { color: var(--pink); font-size: 11px; font-weight: 700; letter-spacing: 1px; }
        .section h2 { margin: 7px 0 0; font-family: 'Jua', sans-serif; font-size: 32px; }
        .subcopy { margin: 8px 0 24px; color: var(--muted); font-size: 14px; line-height: 1.8; }
        .info-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
        .info { padding: 20px; background: white; border: 1px solid var(--line); border-radius: 7px; }
        .info-label { color: var(--muted); font-size: 12px; }
        .info-value { margin-top: 9px; font-family: 'Jua', sans-serif; font-size: 19px; }
        .interest-list { display: flex; flex-wrap: wrap; gap: 10px; }
        .interest { padding: 10px 15px; background: var(--pink-light); border: 1px solid #f8c9d8; border-radius: 20px; font-size: 13px; font-weight: 700; }
        .interest:nth-child(even) { background: #fff4bf; border-color: #f5e594; }
        .music-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
        .song { display: flex; align-items: center; gap: 14px; padding: 15px; background: white; border: 1px solid var(--line); border-radius: 7px; }
        .album { display: grid; flex: 0 0 62px; width: 62px; height: 62px; place-items: center; background: var(--pink-light); border-radius: 5px; font-size: 27px; }
        .song:nth-child(2) .album { background: var(--yellow); }
        .song:nth-child(3) .album { background: #e8e8ff; }
        .song-title { font-family: 'Jua', sans-serif; font-size: 15px; }
        .artist { margin-top: 5px; color: var(--muted); font-size: 12px; }
        .music-note { margin-top: 17px; color: var(--muted); font-size: 12px; }
        .closing { display: flex; justify-content: space-between; align-items: center; gap: 20px; padding: 28px; background: var(--pink-light); border-radius: 8px; }
        .closing h2 { margin: 0; font-family: 'Jua', sans-serif; font-size: 25px; }
        .closing p { margin: 7px 0 0; color: var(--muted); font-size: 13px; }
        .closing-mark { font-size: 42px; }
        .footer { padding-top: 22px; color: var(--muted); text-align: center; font-size: 11px; }
        @media (max-width: 700px) {
                .block-container { padding: .5rem 1rem 2.5rem; }
                .nav-links { gap: 12px; }
                .nav-links a { font-size: 11px; }
                .hero { grid-template-columns: 1fr; gap: 32px; padding: 48px 0 56px; }
                .hero h1 { font-size: 48px; }
                .photo-wrap { justify-self: stretch; max-width: none; }
                .photo-wrap img { height: 280px; }
                .photo-label { right: 6px; }
                .section { padding: 42px 0; }
                .section h2 { font-size: 28px; }
                .info-grid, .music-grid { grid-template-columns: 1fr; }
                .closing { padding: 22px; }
        }
        </style>

        <main class="intro">
            <header class="nav">
                <div class="logo">✿ 나를 소개해요</div>
                <nav class="nav-links" aria-label="페이지 메뉴">
                    <a href="#profile">프로필</a><a href="#interest">관심사</a><a href="#music">좋아하는 음악</a>
                </nav>
            </header>

            <section class="hero">
                <div>
                    <span class="hello">반가워요! 오늘도 좋은 하루 🌼</span>
                    <h1>안녕!<br>나는 <span>이민주</span>야</h1>
                    <p class="hero-copy">[나를 소개하는 한 문장을 적어보세요.] 새로운 것을 배우고 좋아하는 것들을 나누는 걸 즐겨요.</p>
                    <a class="hero-link" href="#profile">나에 대해 더 보기 ↓</a>
                </div>
                <div class="photo-wrap">
                    <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&amp;fit=crop&amp;w=900&amp;q=85" alt="좋아하는 음악을 떠올리게 하는 헤드폰 사진">
                    <div class="photo-label">내 사진으로 바꿔주세요!</div>
                </div>
            </section>

            <section class="section" id="profile">
                <div class="section-title"><div class="eyebrow">A LITTLE ABOUT ME</div><h2>나를 소개할게</h2></div>
                <p class="subcopy">아래 내용을 내 정보로 바꿔보세요. 짧고 솔직한 소개도 충분히 멋져요!</p>
                <div class="info-grid">
                    <article class="info"><div class="info-label">이름</div><div class="info-value">이민주</div></article>
                    <article class="info"><div class="info-label">소속</div><div class="info-value">청주교육대학교</div></article>
                    <article class="info"><div class="info-label">나를 한마디로</div><div class="info-value">[나를 표현하는 말]</div></article>
                </div>
            </section>

            <section class="section" id="interest">
                <div class="section-title"><div class="eyebrow">THINGS I LOVE</div><h2>요즘 관심 있는 것</h2></div>
                <p class="subcopy">취미, 좋아하는 음식, 배우고 싶은 것처럼 나를 보여주는 관심사를 넣어보세요.</p>
                <div class="interest-list">
                    <span class="interest">[관심사 1]</span><span class="interest">[관심사 2]</span>
                    <span class="interest">[취미]</span><span class="interest">[요즘 배우는 것]</span>
                    <span class="interest">[좋아하는 장소]</span>
                </div>
            </section>

            <section class="section" id="music">
                <div class="section-title"><div class="eyebrow">ON REPEAT</div><h2>내가 좋아하는 음악</h2></div>
                <p class="subcopy">자주 듣는 노래나 요즘 빠져 있는 곡을 소개해요.</p>
                <div class="music-grid">
                    <article class="song"><div class="album">♫</div><div><div class="song-title">기쁨, 슬픔, 아름다운 마음</div><div class="artist">AKMU</div></div></article>
                    <article class="song"><div class="album">♪</div><div><div class="song-title">[좋아하는 노래 제목]</div><div class="artist">[아티스트 이름]</div></div></article>
                    <article class="song"><div class="album">♬</div><div><div class="song-title">[좋아하는 노래 제목]</div><div class="artist">[아티스트 이름]</div></div></article>
                </div>
                <div class="music-note">🎧 좋아하는 플레이리스트나 음악 서비스 링크를 여기에 추가해보세요.</div>
            </section>

            <section class="closing">
                <div><h2>읽어줘서 고마워! 💛</h2><p>[마지막으로 전하고 싶은 말을 적어보세요.]</p></div>
                <div class="closing-mark">🌷</div>
            </section>
            <footer class="footer">Made with ♡ by 이민주</footer>
        </main>
        """),
)
