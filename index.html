import streamlit as st

# 페이지 레이아웃 설정
st.set_page_config(layout="wide", page_title="AI 추천 전략 대시보드")

st.title("📊 AI 추천 전략 성과 비교 대시보드")
st.caption("기존 ML, 100% LLM, 그리고 하이브리드 AI 전략의 비용 및 성능을 실시간으로 비교합니다.")

# ------------------------------------------------------------------
# 1. 상단 전략 선택 (라디오 버튼을 통해 3가지 모드 전환)
# ------------------------------------------------------------------
st.markdown("### 🎯 추천 전략 선택")
selected_strategy = st.radio(
    "화면에서 확인할 AI 추천 전략을 선택하세요:",
    ["기존 ML", "100% LLM", "하이브리드(제안)"],
    horizontal=True
)

# 전략별 고정 성능 데이터 (하이브리드의 장점을 극대화하여 비교)
strategy_metrics = {
    "기존 ML": {"conversion": "2.1%", "latency": "450 ms", "cost_desc": "저비용 / 저효율"},
    "100% LLM": {"conversion": "6.0%", "latency": "1,800 ms", "cost_desc": "초고비용 / 병목현상 심함"},
    "하이브리드(제안)": {"conversion": "5.8%", "latency": "140 ms", "cost_desc": "합리적 비용 / 초고속"}
}

# 하단 슬라이더 연동을 위해 방문자 수 슬라이더를 먼저 선언합니다.
st.markdown("---")
st.subheader("💵 방문자 수에 따른 월간 비용 시뮬레이션 (단위: 원)")
visitor_count = st.slider("방문자 수 설정 (명)", min_value=100000, max_value=2000000, value=1030000, step=10000)

# 비용 계산 로직 (기존 비율 유지)
ml_cost = int(visitor_count * 35)
llm_cost = int(visitor_count * 850)
hybrid_cost = int(visitor_count * 135)

# 현재 선택된 전략의 비용 확정
if selected_strategy == "기존 ML":
    current_cost = ml_cost
elif selected_strategy == "100% LLM":
    current_cost = llm_cost
else:
    current_cost = hybrid_cost

# ------------------------------------------------------------------
# 2. 최상단 실시간 메트릭 표시 (선택된 전략에 따라 변동)
# ------------------------------------------------------------------
st.markdown("### 📈 선택된 전략의 실시간 기대 성과")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="예상 전환율", value=strategy_metrics[selected_strategy]["conversion"])
with col2:
    st.metric(label="평균 응답 속도", value=strategy_metrics[selected_strategy]["latency"])
with col3:
    st.metric(label="월간 예상 비용", value=f"₩{current_cost:,}")

# ------------------------------------------------------------------
# 3. 정보 흐름 시각화 시뮬레이션 (CSS 애니메이션 핵심 구문)
# ------------------------------------------------------------------
st.markdown("### 🔄 데이터 흐름 및 처리 속도 비교")

# 선택된 전략에 따른 CSS 클래스 매핑
animation_class = ""
if selected_strategy == "기존 ML":
    animation_class = "ml-flow"
elif selected_strategy == "100% LLM":
    animation_class = "llm-flow"
else:
    animation_class = "hybrid-flow"

# CSS 및 HTML 주입
st.markdown(f"""
<style>
.flow-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #fdfdfd;
    padding: 50px 80px;
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    border: 1px solid #eaeaea;
    margin-bottom: 20px;
}}
.flow-node {{
    background: #ffffff;
    padding: 18px 30px;
    border-radius: 30px;
    font-weight: bold;
    font-size: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    z-index: 2;
    border: 2px solid #e0e0e0;
}}
.center-node {{
    background: #f5f5f5;
    border: 2px solid #9e9e9e;
    color: #333333;
    transition: all 0.3s ease;
}}
/* 하이브리드 전략일 때 중앙 노드 강조 */
.hybrid-node {{
    background: #e3f2fd !important;
    border: 2px solid #2196f3 !important;
    color: #0d47a1 !important;
    box-shadow: 0 4px 15px rgba(33, 150, 243, 0.3) !important;
}}

/* 정보 입자 (파란색 구체) 기본 스타일 */
.info-particle {{
    position: absolute;
    top: 52%;
    width: 14px;
    height: 14px;
    background-color: #2196f3;
    border-radius: 50%;
    transform: translateY(-50%);
    z-index: 1;
    box-shadow: 0 0 10px #2196f3;
}}

/* 1. 기존 ML: 정보가 일정하게 느린 속도로 지나감 (6초) */
.ml-flow {{
    animation: moveLinear 6s infinite linear;
}}

/* 2. 하이브리드: 정보가 매우 빠르게 통과함 (1초) */
.hybrid-flow {{
    animation: moveLinear 1s infinite linear;
    background-color: #00e676 !important; /* 하이브리드는 입자 색상도 더 밝게 강조 */
    box-shadow: 0 0 12px #00e676 !important;
}}

/* 3. 100% LLM: 중간에 멈추고 버벅거리다가 지나감 (4초) */
.llm-flow {{
    animation: moveStutter 4s infinite ease-in-out;
    background-color: #ff1744 !important; /* LLM 병목은 붉은 빛으로 경고 효과 */
    box-shadow: 0 0 12px #ff1744 !important;
}}

/* 여러 개의 정보가 연속적으로 보이도록 딜레이 설정 */
.p2 {{ animation-delay: 0.3s; }}
.p3 {{ animation-delay: 0.6s; }}
.p4 {{ animation-delay: 0.9s; }}

/* 기본 선형 이동 키프레임 (기존 ML 및 하이브리드용) */
@keyframes moveLinear {{
    0% {{ left: 10%; opacity: 0; }}
    10% {{ opacity: 1; }}
    90% {{ opacity: 1; }}
    100% {{ left: 90%; opacity: 0; }}
}}

/* 버벅거림/끊김 현상 키프레임 (100% LLM용) */
@keyframes moveStutter {{
    0% {{ left: 10%; opacity: 0; }}
    10% {{ opacity: 1; }}
    /* 35%~70% 구간에서 중앙 노드 근처에 걸려 버벅거리는 효과 구현 */
    35% {{ left: 45%; }}
    45% {{ left: 43%; }} /* 살짝 뒤로 밀리는 렉(Lag) 현상 표현 */
    60% {{ left: 48%; }}
    70% {{ left: 46%; }} /* 한 번 더 출렁임 */
    85% {{ left: 55%; }}
    100% {{ left: 90%; opacity: 0; }}
}}
</style>

<div class="flow-container">
    <div class="flow-node">🔹 사용자 유입</div>
    <div class="flow-node center-node {'hybrid-node' if selected_strategy == '하이브리드(제안)' else ''}">
        ⚙️ {selected_strategy}
    </div>
    <div class="flow-node">✅ 구매 전환</div>
    
    <div class="info-particle {animation_class} p1"></div>
    <div class="info-particle {animation_class} p2"></div>
    <div class="info-particle {animation_class} p3"></div>
    <div class="info-particle {animation_class} p4"></div>
</div>
""", unsafe_allow_html=True)

# 하이브리드 AI의 우수성을 강조하는 분석 코멘트
if selected_strategy == "하이브리드(제안)":
    st.success("🌟 **하이브리드 AI 추천의 압도적 우위:** LLM 수준의 높은 전환율(**5.8%**)을 달성하면서도, 정보 처리 속도는 **140 ms**로 가장 빠르고 비용은 LLM 대비 **84%나 절감**됩니다.")
elif selected_strategy == "기존 ML":
    st.info("ℹ️ **기존 ML 분석:** 비용은 가장 저렴하지만, 데이터 분석 알고리즘의 한계로 인해 정보 처리 속도가 무겁고 **전환율이 2.1%로 매우 낮습니다.**")
elif selected_strategy == "100% LLM":
    st.warning("⚠️ **100% LLM 분석:** 전환율은 6.0%로 미세하게 높지만, 실시간 연산 시 **모델 병목 현상(중간 끊김 및 버벅거림)**이 발생하여 이탈률이 생길 수 있으며, 비용이 폭발적으로 증가합니다.")


# ------------------------------------------------------------------
# 4. 하단 비용 시뮬레이션 차트 시각화 (기존 비용 데이터 유지)
# ------------------------------------------------------------------
# 세 전략의 비용을 한눈에 비교할 수 있는 가로 바 플롯 디자인
st.markdown(f"**현재 설정된 방문자 수:** {visitor_count:,} 명")

# 최대 비용을 기준으로 비율 계산
max_cost = max(ml_cost, llm_cost, hybrid_cost)

st.markdown(f"""
<div style="background-color: #f9f9f9; padding: 20px; border-radius: 15px; border: 1px solid #eee;">
    <p style="margin-bottom:5px;">🟡 <b>기존 ML 비용:</b> ₩{ml_cost:,}</p>
    <div style="background-color: #e0e0e0; border-radius: 8px; width: 100%; margin-bottom: 15px;">
        <div style="background-color: #ffb74d; width: {(ml_cost/max_cost)*100}%; height: 20px; border-radius: 8px;"></div>
    </div>
    
    <p style="margin-bottom:5px;">🔴 <b>100% LLM 비용:</b> ₩{llm_cost:,} <span style="color:#ff1744; font-size:12px;">(하이브리드의 약 6.3배!)</span></p>
    <div style="background-color: #e0e0e0; border-radius: 8px; width: 100%; margin-bottom: 15px;">
        <div style="background-color: #e57373; width: {(llm_cost/max_cost)*100}%; height: 20px; border-radius: 8px;"></div>
    </div>
    
    <p style="margin-bottom:5px;">🔵 <b>하이브리드(제안) 비용:</b> ₩{hybrid_cost:,} <span style="color:#2196f3; font-size:12px;">(최적의 가성비)</span></p>
    <div style="background-color: #e0e0e0; border-radius: 8px; width: 100%;">
        <div style="background-color: #64b5f6; width: {(hybrid_cost/max_cost)*100}%; height: 20px; border-radius: 8px;"></div>
    </div>
</div>
""", unsafe_allow_html=True)
