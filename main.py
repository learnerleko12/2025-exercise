import streamlit as st
import streamlit as st

# 🎨 과학자 MBTI 매핑 데이터
scientist_data = {
    "INTJ": {
        "name": "스티븐 호킹",
        "desc": "이론물리학의 거장! 미래를 내다보는 통찰력으로 우주를 탐험했어요.",
        "emoji": "🧠🌌",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Stephen_Hawking.StarChild.jpg"
    },
    "ENFP": {
        "name": "마리 퀴리",
        "desc": "과학에 대한 열정으로 방사능을 발견하고 두 개의 노벨상을 수상했어요!",
        "emoji": "🔬💡",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Marie_Curie_c1920.jpg"
    },
    "ISTP": {
        "name": "엘론 머스크",
        "desc": "문제를 해결하는 데 집중! 발명과 우주산업까지 도전한 혁신가예요.",
        "emoji": "🚀🛠️",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Elon_Musk_Royal_Society_%28crop2%29.jpg"
    },
    "INFJ": {
        "name": "니콜라 테슬라",
        "desc": "상상력과 창의력의 천재! 전기의 미래를 그린 선구자예요.",
        "emoji": "⚡🌠",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/N.Tesla.JPG"
    },
    "ESTJ": {
        "name": "캐서린 존슨",
        "desc": "수학으로 우주비행을 이끈 현실주의자! NASA의 숨은 영웅이에요.",
        "emoji": "📐🚀",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Katherine_Johnson_1983.jpg"
    }
}

# 🖥️ Streamlit UI
st.set_page_config(page_title="과학자 친구들 만나기", page_icon="🧑‍🔬")
st.title("👩‍🔬 과학자 친구들 만나보기")
st.subheader("나랑 MBTI가 같은 과학자는 누구일까? 🤔")

mbti_list = list(scientist_data.keys())
selected_mbti = st.selectbox("👉 너의 MBTI 유형을 선택해보세요!", mbti_list)

if selected_mbti:
    data = scientist_data[selected_mbti]
    st.image(data["image_url"], width=250, caption=f"{data['name']} 님")
    st.markdown(f"### {data['name']} {data['emoji']}")
    st.write(data["desc"])
    st.success("🎉 너랑 성격이 비슷한 과학자 친구를 만났어요!")
