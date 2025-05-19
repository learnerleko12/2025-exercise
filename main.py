import streamlit as st

# ✅ Streamlit 설정
st.set_page_config(page_title="과학자 친구들 만나기", page_icon="🧑‍🔬")

# ✅ 타이틀
st.title("👩‍🔬 과학자 친구들 만나보기")
st.subheader("나랑 MBTI가 같은 과학자는 누구일까? 🤔")

# ✅ MBTI 딕셔너리 (16유형 + 일러스트 이미지)
scientist_data = {
    "INTJ": {
        "name": "스티븐 호킹",
        "desc": "나는 우주의 비밀을 풀기 위해 매일 생각했어! 몸이 불편해도 머릿속 상상력으로 블랙홀 연구를 했단다.",
        "emoji": "🧠🌌",
        "keywords": ["계획적", "똑똑함", "혼자 연구 좋아함"],
        "image_url": "https://cdn.pixabay.com/photo/2021/09/22/21/21/scientist-6648973_960_720.png"
    },
    "INTP": {
        "name": "앨런 튜링",
        "desc": "나는 컴퓨터의 기초를 만든 사람이야! 퍼즐 맞추듯 문제를 푸는 걸 좋아했지.",
        "emoji": "💻🧩",
        "keywords": ["논리적", "질문 많음", "발명 좋아함"],
        "image_url": "https://cdn.pixabay.com/photo/2021/08/31/08/02/computer-6590169_960_720.png"
    },
    "ENTJ": {
        "name": "제프 베조스",
        "desc": "나는 기술과 사업을 함께 꿈꿨어! 계획 세우고 이끄는 걸 좋아해.",
        "emoji": "📈🚀",
        "keywords": ["리더형", "체계적", "큰 꿈"],
        "image_url": "https://cdn.pixabay.com/photo/2017/01/31/20/23/businessman-2026386_960_720.png"
    },
    "ENTP": {
        "name": "리처드 파인만",
        "desc": "과학을 설명하는 게 정말 재밌었어! 새로운 걸 자꾸 궁금해했지.",
        "emoji": "🎸🔬",
        "keywords": ["말 잘함", "아이디어 넘침", "유쾌함"],
        "image_url": "https://cdn.pixabay.com/photo/2021/08/24/07/46/teacher-6569826_960_720.png"
    },
    "INFJ": {
        "name": "니콜라 테슬라",
        "desc": "나는 전기의 미래를 꿈꿨어! 조용하지만 상상력은 누구보다 컸지.",
        "emoji": "⚡🌠",
        "keywords": ["조용한 리더", "꿈 많음", "창의적"],
        "image_url": "https://cdn.pixabay.com/photo/2021/08/24/07/55/invention-6569832_960_720.png"
    },
    "INFP": {
        "name": "제인 구달",
        "desc": "나는 침팬지를 오랫동안 관찰하며 자연을 사랑했단다.",
        "emoji": "🐵🌿",
        "keywords": ["자연 사랑", "감성 풍부", "평화주의"],
        "image_url": "https://cdn.pixabay.com/photo/2021/09/15/20/48/nature-6628086_960_720.png"
    },
    "ENFJ": {
        "name": "칼 세이건",
        "desc": "나는 우주를 쉽게 설명해주는 걸 좋아했어! 사람들과 지식을 나누는 게 즐거웠지.",
        "emoji": "🌌📖",
        "keywords": ["설명 잘함", "배려심", "리더형 선생님"],
        "image_url": "https://cdn.pixabay.com/photo/2021/09/18/19/57/education-6635393_960_720.png"
    },
    "ENFP": {
        "name": "마리 퀴리",
        "desc": "새로운 걸 발견하는 게 너무 재밌었어! 노벨상도 두 번이나 받았단다.",
        "emoji": "🔬💡",
        "keywords": ["에너지 넘침", "모험 좋아함", "창의적"],
        "image_url": "https://cdn.pixabay.com/photo/2021/08/31/07/53/experiment-6590158_960_720.png"
    },
    "ISTJ": {
        "name": "팀 버너스리",
        "desc": "나는 인터넷을 만든 사람이야! 조용히, 꼼꼼하게 일하는 걸 좋아했지.",
        "emoji": "🌐📚",
        "keywords": ["정확함", "책임감", "실수 안 함"],
        "image_url": "https://cdn.pixabay.com/photo/2021/09/03/06/13/coding-6596817_960_720.png"
    },
    "ISFJ": {
        "name": "플로렌스 나이팅게일",
        "desc": "난 간호사였지만, 데이터를 모아 병원 환경을 바꿨단다.",
        "emoji": "🏥📊",
        "keywords": ["따뜻함", "섬세함", "봉사정신"],
        "image_url": "https://cdn.pixabay.com/photo/2021/08/31/08/07/nurse-6590181_960_720.png"
    },
    "ESTJ": {
        "name": "캐서린 존슨",
        "desc": "수학으로 우주선을 도왔어! NASA에서도 실력을 인정받았지.",
        "emoji": "📐🚀",
        "keywords": ["현실적", "책임감", "리더"],
        "image_url": "https://cdn.pixabay.com/photo/2021/10/12/04/02/mathematician-6700709_960_720.png"
    },
    "ESFJ": {
        "name": "알리스타 하디",
        "desc": "나는 바닷속 생물을 연구했어. 모두가 잘 지낼 수 있는 환경을 중요하게 생각했단다.",
        "emoji": "🐟🔬",
        "keywords": ["다정함", "도우미", "관심 많음"],
        "image_url": "https://cdn.pixabay.com/photo/2021/08/24/07/55/ocean-6569833_960_720.png"
    },
    "ISTP": {
        "name": "엘론 머스크",
        "desc": "나는 전기차와 로켓을 직접 만들었어! 말보다 행동이 먼저지.",
        "emoji": "🚗🚀",
        "keywords": ["만들기 좋아함", "조용함", "도전적"],
        "image_url": "https://cdn.pixabay.com/photo/2021/08/31/08/03/engineer-6590173_960_720.png"
    },
    "ISFP": {
        "name": "레이첼 카슨",
        "desc": "나는 바다와 생물을 사랑했어. 환경을 지키는 일이 중요하다고 알렸지.",
        "emoji": "🌊🐦",
        "keywords": ["자연 사랑", "조용하지만 따뜻함"],
        "image_url": "https://cdn.pixabay.com/photo/2022/04/26/05/42/nature-7157289_960_720.png"
    },
    "ESTP": {
        "name": "토머스 에디슨",
        "desc": "나는 실패해도 계속 실험했어. 전구도, 축음기도 만들었단다.",
        "emoji": "💡🔋",
        "keywords": ["에너지 넘침", "행동형", "현실적"],
        "image_url": "https://cdn.pixabay.com/photo/2022/10/25/03/33/experiment-7543064_960_720.png"
    },
    "ESFP": {
        "name": "빌 나이",
        "desc": "과학을 재미있게 알려주는 방송을 했어! 모두가 과학을 좋아하게 하고 싶었지.",
        "emoji": "🎤🧪",
        "keywords": ["발표력", "유쾌함", "사람 좋아함"],
        "image_url": "https://cdn.pixabay.com/photo/2022/11/07/06/13/presenter-7575611_960_720.png"
    }
}

# ✅ 사용자 입력
selected_mbti = st.selectbox("👉 너의 MBTI 유형을 선택해보세요!", list(scientist_data.keys()))

# ✅ 캐릭터 소개 출력
if selected_mbti:
    data = scientist_data[selected_mbti]
    st.image(data["image_url"], width=300, caption=data["name"])
    st.markdown(f"### {data['name']} {data['emoji']}")
    st.write(data["desc"])
    st.markdown("**성격 키워드:** " + ", ".join(data["keywords"]))
    st.success("🎉 너랑 성격이 비슷한 과학자 친구를 만났어요!")
