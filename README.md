# 🌱 EcoSnap: An AI-Powered Sustainability Companion

EcoSnap is a gamified, AI-integrated web application that empowers individuals and communities to take measurable climate-positive actions. By combining real-time image classification, carbon footprint estimation, behavior tracking, and reward-based engagement, EcoSnap transforms everyday eco-friendly habits into a rewarding, data-driven experience.

🔗 Live Demo: [Launch EcoSnap](https://ecosnapdemo.streamlit.app/)  

---

## 📌 Key Features

- 📸 EcoSnap Camera: Capture or upload images of eco-friendly actions
- 🤖 AI Analyzer: Classify sustainability actions using a custom-trained TensorFlow Lite model
- 🌍 CO₂ Estimator: Calculate carbon savings per action using verified emission data
- 🔥 Streak Tracker: Log daily eco-behaviors and unlock habit-based milestones
- 🎁 Reward Center: Redeem achievements for eco-vouchers and digital certificates
- 🏆 Leaderboards: Compete regionally, globally, or within CSR teams
- 📈 Personal Dashboard: Visualize impact over time with trend graphs and CO₂ summaries
- 🏢 CSR Dashboard: View institutional impact and campaign engagement

---

## 🎯 Objective

EcoSnap aims to promote sustainable lifestyle choices by bridging the gap between climate awareness and action. Through interactive features and real-time feedback, the platform encourages long-term behavior change using habit science and community engagement principles.

---

## 🛠️ Tech Stack

| Layer         | Technology                          |
|--------------|-------------------------------------|
| Frontend     | Streamlit                           |
| Backend AI   | TensorFlow Lite                     |
| Visualization| Matplotlib, Plotly                  |
| Image Input  | Pillow, OpenCV                      |
| Data Tools   | NumPy, Scikit-learn, Pandas         |
| Geolocation  | Geopy (for future location-based features) |
| Dataset Tools| bing-image-downloader, gdown        |

---

## 🧠 AI Model

- A Convolutional Neural Network trained on 6 eco-action categories
- Trained using TensorFlow 2.x and exported to TensorFlow Lite for efficient inference
- Classes include:
  - Reusable bags
  - Tree planting
  - Cycling
  - Composting
  - Public transport usage
  - Cloth packaging over plastic

---

## 🧩 Application Flow

1. User uploads an image of an eco-action
2. AI Analyzer classifies the image and returns confidence score
3. CO₂ Estimator calculates emission savings using predefined mappings
4. The action is confirmed and logged
5. Streak and rewards are updated accordingly
6. Dashboard and leaderboards reflect the new impact

---

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/sruthykbenni/ecosnap_demo.git
cd ecosnap_demo
````

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Launch the app:

```bash
streamlit run app.py
```

---

## 🗂️ Folder Structure

```
ecosnap_demo/
├── app.py
├── requirements.txt
├── features/
│   ├── AI_analyzer.py
│   ├── Ecosnap_camera.py
│   ├── Co2_estimator.py
│   ├── Streak_tracker.py
│   ├── Leaderboards.py
│   ├── Reward_center.py
│   ├── Personal_dashboard.py
│   └── CSR_dashboard.py
├── models/
│   ├── eco_model.tflite
│   ├── eco_model.h5
│   └── class_labels.txt
└── dataset/
```

---

## 📊 Impact Goals

* Raise climate literacy by turning abstract actions into measurable contributions
* Support CSR-led green campaigns with visual analytics
* Encourage sustained eco-friendly behavior through habit loops and community

---

## 🌍 Future Scope

* Mobile app development with Flutter
* Integration with Google Fit & Maps for dynamic CO₂ estimation
* Multilingual support and voice feedback
* Emotion-aware and location-aware feedback systems
* Community-based campaign challenges

---

## 🙌 Acknowledgments

* Developed as part of the DACE Project at Digital University Kerala
* Inspired by the goal of empowering individuals and organizations to combat climate change through tech innovation

---

## 🤝 Let’s Build a Greener Future Together

EcoSnap is just the beginning of what’s possible when technology meets purpose. We welcome feedback, ideas, and collaboration from developers, researchers, environmentalists, and organizations who share our vision for sustainability.

If you’re interested in contributing features, improving our AI model, integrating APIs, or scaling this solution for larger communities — we’d love to connect!

🌐 Reach out via GitHub Issues or Discussions  

Together, we can make sustainability measurable, habitual, and rewarding for all. 🌱💡
