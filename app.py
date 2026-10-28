import json
import os
import time
import streamlit as st

# إعدادات الصفحة والتجاوب مع شاشة الموبايل
st.set_page_config(
    page_title="المنظم الذكي",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# دعم الاتجاه من اليمين للشمال للغة العربية
st.markdown(
    """
    <style>
    body, div, input, textarea, button {
        direction: RTL;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

DB_FILE = "app_data.json"


# قراءة وحفظ البيانات
def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "tasks": [],
        "study_schedule": {},
        "lessons_schedule": {},
        "pomo_time": 25,
        "break_time": 5,
    }


def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


data = load_data()

# العنوان الرئيسي
st.title("✨ المنظم الذكي الشخصي")
st.write("برنامجك الخاص لتنظيم المذاكرة، المهام، والمواعيد")

# القائمة الرئيسية للاختيارات
option = st.selectbox(
    "اختر القائمة التي تريد فتحها:",
    [
        "⏱️ مؤقت البومودورو والاستراحة",
        "📅 جدول المهام اليومية",
        "📚 جدول المذاكرة الأسبوعي",
        "🏫 مواعيد الدروس الأسبوعية",
    ],
)

st.divider()

# --- 1. مؤقت البومودورو والاستراحة ---
if option == "⏱️ مؤقت البومودورو والاستراحة":
    st.header("⏱️ مؤقت البومودورو (تركيز واستراحة)")

    # إعدادات الأوقات
    col_set1, col_set2 = st.columns(2)
    with col_set1:
        pomo_mins = st.number_input(
            "وقت التركيز (بالدقائق):",
            min_value=1,
            max_value=120,
            value=data.get("pomo_time", 25),
        )
    with col_set2:
        break_mins = st.number_input(
            "وقت الاستراحة (بالدقائق):",
            min_value=1,
            max_value=60,
            value=data.get("break_time", 5),
        )

    if st.button("💾 حفظ إعدادات الأوقات"):
        data["pomo_time"] = pomo_mins
        data["break_time"] = break_mins
        save_data(data)
        st.success("تم حفظ الأوقات بنجاح!")

    st.divider()

    # اختيار وضع التشغيل (تركيز ولا استراحة)
    mode = st.radio(
        "اختر وضع المؤقت:",
        ["جلسة تركيز (Focus)", "وقت الاستراحة (Break)"],
        horizontal=True,
    )

    active_time = pomo_mins if "تركيز" in mode else break_mins

    st.subheader(f"الوضع الحالي: {mode} ({active_time} دقيقة)")

    if st.button("▶️ بدء العد التنازلي", type="primary"):
        ph = st.empty()
        # صوت تنبيه أو بدء
        for secs in range(int(active_time) * 60, -1, -1):
            mm, ss = divmod(secs, 60)
            ph.title(f"⏳ {mm:02d}:{ss:02d}")
            time.sleep(1)

        # تشغيل صوت التنبيه عبر كود HTML/JS متصفح خفي
        audio_html = """
            <audio autoplay>
              <source src="https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3" type="audio/mpeg">
            </audio>
            """
        st.markdown(audio_html, unsafe_allow_html=True)

        if "تركيز" in mode:
            st.balloons()
            st.success(
                "🎉 انتهى وقت التركيز! ممتاز، جاري الانتقال لوقت الاستراحة."
            )
        else:
            st.success(
                "🔔 انتهت الاستراحة! استعد لجلسة تركيز جديدة وقوية 💪."
            )

# --- 2. جدول المهام اليومية ---
elif option == "📅 جدول المهام اليومية":
    st.header("📅 جدول المهام اليومية")

    new_task = st.text_input("اكتب المهمة الجديدة هنا:")
    if st.button("➕ إضافة المهمة"):
        if new_task:
            data["tasks"].append(new_task)
            save_data(data)
            st.rerun()

    st.subheader("قائمة مهام اليوم:")
    for i, task in enumerate(list(data.get("tasks", []))):
        col_t, col_b = st.columns([4, 1])
        col_t.write(f"• {task}")
        if col_b.button("❌ حذف", key=f"del_{i}"):
            data["tasks"].pop(i)
            save_data(data)
            st.rerun()

# --- 3. جدول المذاكرة الأسبوعي ---
elif option == "📚 جدول المذاكرة الأسبوعي":
    st.header("📚 جدول المذاكرة الأسبوعي")

    days = [
        "السبت",
        "الأحد",
        "الإثنين",
        "الثلاثاء",
        "الأربعاء",
        "الخميس",
        "الجمعة",
    ]
    study_data = data.get("study_schedule", {})

    updated_study = {}
    for day in days:
        st.subheader(f"📌 {day}")
        day_vals = study_data.get(day, ["", "", ""])
        c1, c2, c3 = st.columns(3)
        p1 = c1.text_input(
            f"فترة 1", value=day_vals[0] if len(day_vals) > 0 else "", key=f"s1_{day}"
        )
        p2 = c2.text_input(
            f"فترة 2", value=day_vals[1] if len(day_vals) > 1 else "", key=f"s2_{day}"
        )
        p3 = c3.text_input(
            f"فترة 3", value=day_vals[2] if len(day_vals) > 2 else "", key=f"s3_{day}"
        )
        updated_study[day] = [p1, p2, p3]

    if st.button("💾 حفظ جدول المذاكرة بالكامل", type="primary"):
        data["study_schedule"] = updated_study
        save_data(data)
        st.success("تم حفظ جدول المذاكرة بنجاح!")

# --- 4. جدول مواعيد الدروس ---
elif option == "🏫 مواعيد الدروس الأسبوعية":
    st.header("🏫 مواعيد الدروس الأسبوعية")

    days = [
        "السبت",
        "الأحد",
        "الإثنين",
        "الثلاثاء",
        "الأربعاء",
        "الخميس",
        "الجمعة",
    ]
    lessons_data = data.get("lessons_schedule", {})

    updated_lessons = {}
    for day in days:
        st.subheader(f"🏫 {day}")
        day_vals = lessons_data.get(day, ["", ""])
        c1, c2 = st.columns(2)
        l1 = c1.text_input(
            f"درس 1 (المادة والموعد)",
            value=day_vals[0] if len(day_vals) > 0 else "",
            key=f"l1_{day}",
        )
        l2 = c2.text_input(
            f"درس 2 (المادة والموعد)",
            value=day_vals[1] if len(day_vals) > 1 else "",
            key=f"l2_{day}",
        )
        updated_lessons[day] = [l1, l2]

    if st.button("💾 حفظ مواعيد الدروس", type="primary"):
        data["lessons_schedule"] = updated_lessons
        save_data(data)
        st.success("تم حفظ مواعيد الدروس بنجاح!")