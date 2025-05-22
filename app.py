import streamlit as st

# Import feature modules (no Firebase)
from features.AI_analyzer import ai_analyzer
from features.Co2_estimator import co2_estimator
from features.CSR_dashboard import csr_dashboard
from features.Ecosnap_camera import eco_snap_camera
from features.Leaderboards import leaderboard
from features.Personal_dashboard import personal_dashboard
from features.Reward_center import reward_center
from features.Streak_tracker import streak_tracker

# Main App Layout
def main():
    st.set_page_config(page_title="EcoSnap 🌿", layout="wide")
    st.title("🌱 Welcome to EcoSnap")
    st.markdown("Track your eco-actions, estimate CO₂ savings, and earn rewards!")

    # Sidebar navigation
    pages = {
        "🏠 Home": None,
        "📸 EcoSnap Camera": eco_snap_camera,
        "🤖 AI Analyzer": ai_analyzer,
        "🌍 CO₂ Estimator": co2_estimator,
        "🔥 Streak Tracker": streak_tracker,
        "🏆 Leaderboards": leaderboard,
        "🎁 Reward Center": reward_center,
        "📊 CSR Dashboard": csr_dashboard,
        "📈 Personal Dashboard": personal_dashboard,
    }

    choice = st.sidebar.radio("Go to", list(pages.keys()))

    if choice == "🏠 Home":
        st.header("Get Started")
        st.write("Upload an image, track your actions, and explore the impact of your eco-friendly choices!")
    else:
        selected_page = pages[choice]
        if selected_page:
            selected_page()

if __name__ == "__main__":
    main()
