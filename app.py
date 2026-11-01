import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة لتكون بعرض كامل وبدون حواف
st.set_page_config(
    page_title="المنظم الذكي | Smart Organizer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. إخفاء الهيدر والفتر الافتراضيين لـ Streamlit للحصول على مظهر تطبيق نيتف احترافي
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. كود الـ HTML المتكامل والكامل للمنظم الذكي
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>المنظم الذكي | Smart Organizer</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        darkBg: '#0f172a',
                        cardBg: 'rgba(30, 41, 59, 0.7)',
                        glassBorder: 'rgba(255, 255, 255, 0.1)',
                    }
                }
            }
        }
    </script>
    <!-- Google Font: Inter & Cairo -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Cairo', 'Inter', sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            overflow-x: hidden;
        }
        .glass-card {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.75) 0%, rgba(15, 23, 42, 0.85) 100%);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }
        .glass-btn {
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.2) 0%, rgba(14, 116, 144, 0.3) 100%);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(56, 189, 248, 0.3);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .glass-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.4);
            border-color: rgba(56, 189, 248, 0.6);
        }
        .glow-text {
            text-shadow: 0 0 20px rgba(56, 189, 248, 0.5), 0 0 40px rgba(56, 189, 248, 0.2);
        }
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }
        .animate-float {
            animation: float 5s ease-in-out infinite;
        }
    </style>
</head>
<body class="min-h-screen bg-[#0f172a] text-slate-100 relative selection:bg-cyan-500 selection:text-white">

    <div class="absolute top-0 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/3 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute bottom-10 left-1/3 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>

    <div class="container mx-auto px-4 py-6 max-w-6xl relative z-10">

        <!-- Header -->
        <header class="flex flex-col sm:flex-row items-center justify-between glass-card rounded-2xl p-5 mb-8 gap-4">
            <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-cyan-500/30 animate-float text-2xl">
                    ✨
                </div>
                <div>
                    <h1 class="text-2xl font-black tracking-wide glow-text" id="app-title" data-i18n="app_title">المنظم الذكي</h1>
                    <p class="text-xs text-slate-400" id="app-subtitle" data-i18n="app_subtitle">نظام إنتاجية متطور مع تصميم ثلاثي الأبعاد</p>
                </div>
            </div>

            <div class="flex items-center gap-3">
                <button onclick="toggleLanguage()" class="glass-btn px-4 py-2 rounded-xl font-bold text-sm flex items-center gap-2 shadow-md">
                    🌐 <span id="lang-btn-text">English</span>
                </button>
            </div>
        </header>

        <!-- Dashboard Home Cards -->
        <div id="home-dashboard" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 mb-8">
            <div onclick="switchSection('pomodoro')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-purple-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-purple-500/20 rounded-full blur-2xl group-hover:bg-purple-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-purple-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">⏱️</div>
                <h3 class="text-xl font-bold mb-1 text-purple-300" data-i18n="pomo_title">مؤقت البومودورو</h3>
                <p class="text-xs text-slate-400" data-i18n="pomo_desc">جلسات تركيز واستراحة مع منبه صوتي دائري</p>
            </div>

            <div onclick="switchSection('tasks')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-emerald-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-emerald-500/20 rounded-full blur-2xl group-hover:bg-emerald-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-emerald-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">✅</div>
                <h3 class="text-xl font-bold mb-1 text-emerald-300" data-i18n="tasks_title">المهام اليومية</h3>
                <p class="text-xs text-slate-400" data-i18n="tasks_desc">قائمة مهام تفاعلية مع تتبع المنجز وغير المنجز</p>
            </div>

            <div onclick="switchSection('lessons')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-blue-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-blue-500/20 rounded-full blur-2xl group-hover:bg-blue-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-blue-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">🏫</div>
                <h3 class="text-xl font-bold mb-1 text-blue-300" data-i18n="lessons_title">مواعيد الدروس الأسبوعية</h3>
                <p class="text-xs text-slate-400" data-i18n="lessons_desc">جدول فخم لتنظيم مواعيد الدروس والحصص</p>
            </div>

            <div onclick="switchSection('sounds')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-amber-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-amber-500/20 rounded-full blur-2xl group-hover:bg-amber-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-amber-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">🌧️</div>
                <h3 class="text-xl font-bold mb-1 text-amber-300" data-i18n="sounds_title">أصوات الاسترخاء</h3>
                <p class="text-xs text-slate-400" data-i18n="sounds_desc">توليد أصوات المطر والتركيز الطبيعية للمذاكرة</p>
            </div>

            <div onclick="switchSection('matrix')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-rose-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-rose-500/20 rounded-full blur-2xl group-hover:bg-rose-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-rose-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">📊</div>
                <h3 class="text-xl font-bold mb-1 text-rose-300" data-i18n="matrix_title">جدول المحاضرات الذكي</h3>
                <p class="text-xs text-slate-400" data-i18n="matrix_desc">مصفوفة متقدمة تشبه إكسل لتتبع المحاضرات لكل مادة</p>
            </div>
        </div>

        <!-- Back Button -->
        <div id="back-nav" class="mb-6 hidden">
            <button onclick="switchSection('home')" class="glass-btn px-5 py-2.5 rounded-xl font-bold text-sm flex items-center gap-2 text-cyan-300">
                ⬅️ <span data-i18n="back_home">العودة للرئيسية</span>
            </button>
        </div>

        <!-- SECTION 1: POMODORO -->
        <section id="section-pomodoro" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="flex flex-col md:flex-row items-center justify-between gap-8">
                <div class="w-full md:w-1/2 space-y-6">
                    <div>
                        <h2 class="text-2xl font-black text-purple-300 mb-2" data-i18n="pomo_header">⏱️ مؤقت البومودورو الدائري</h2>
                        <p class="text-sm text-slate-400" data-i18n="pomo_sub">اضبط وقت التركيز والاستراحة وابدأ جلسة الإنتاجية.</p>
                    </div>

                    <div class="grid grid-cols-3 gap-3">
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1" data-i18n="focus_time">تركيز (د)</label>
                            <input type="number" id="input-focus" value="25" min="1" max="120" onchange="resetPomodoro()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1" data-i18n="short_break">استراحة قصيرة</label>
                            <input type="number" id="input-short" value="5" min="1" max="60" onchange="resetPomodoro()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1" data-i18n="long_break">استراحة طويلة</label>
                            <input type="number" id="input-long" value="15" min="1" max="60" onchange="resetPomodoro()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                    </div>

                    <div class="flex gap-3">
                        <button onclick="setPomoMode('focus')" id="mode-focus-btn" class="flex-1 py-2.5 rounded-xl font-bold text-sm bg-purple-600 text-white shadow-lg shadow-purple-600/30 transition-all" data-i18n="btn_focus">جلسة تركيز</button>
                        <button onclick="setPomoMode('break')" id="mode-break-btn" class="flex-1 py-2.5 rounded-xl font-bold text-sm bg-slate-800 text-slate-300 border border-slate-700 hover:bg-slate-700 transition-all" data-i18n="btn_break">استراحة</button>
                    </div>
                </div>

                <div class="w-full md:w-1/2 flex flex-col items-center justify-center">
                    <div class="relative w-64 h-64 flex items-center justify-center">
                        <svg class="w-full h-full transform -rotate-90">
                            <circle cx="128" cy="128" r="110" stroke="currentColor" stroke-width="12" class="text-slate-800" fill="none"></circle>
                            <circle id="pomo-progress-ring" cx="128" cy="128" r="110" stroke="currentColor" stroke-width="12" class="text-purple-500 transition-all duration-1000" fill="none" stroke-dasharray="691" stroke-dashoffset="0" stroke-linecap="round"></circle>
                        </svg>
                        <div class="absolute flex flex-col items-center justify-center text-center">
                            <span id="pomo-timer-display" class="text-4xl sm:text-5xl font-black tracking-wider text-white">25:00</span>
                            <span id="pomo-status-label" class="text-xs uppercase tracking-widest text-purple-300 mt-1 font-bold">Focus</span>
                        </div>
                    </div>

                    <div class="flex items-center gap-3 mt-6">
                        <button onclick="startPomodoro()" id="pomo-start-btn" class="px-6 py-3 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white rounded-2xl font-bold shadow-lg shadow-purple-600/30 transition-all flex items-center gap-2">
                            ▶️ <span data-i18n="start">بدء</span>
                        </button>
                        <button onclick="pausePomodoro()" class="px-6 py-3 bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 rounded-2xl font-bold transition-all flex items-center gap-2">
                            ⏸️ <span data-i18n="pause">إيقاف مؤقت</span>
                        </button>
                        <button onclick="resetPomodoro()" class="px-6 py-3 bg-slate-800 hover:bg-slate-700 text-rose-400 border border-slate-700 rounded-2xl font-bold transition-all flex items-center gap-2">
                            🔄 <span data-i18n="reset">إعادة ضبط</span>
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 2: TASKS MANAGER -->
        <section id="section-tasks" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="max-w-2xl mx-auto space-y-6">
                <div>
                    <h2 class="text-2xl font-black text-emerald-300 mb-2" data-i18n="tasks_header">✅ إدارة المهام اليومية</h2>
                    <p class="text-sm text-slate-400" data-i18n="tasks_sub">اضف مهامك، اضغط على زر الإنجاز لتتحول للون الأخضر المشع مع شطبها.</p>
                </div>

                <div class="flex gap-3">
                    <input type="text" id="task-input" data-i18n-placeholder="task_placeholder" placeholder="اكتب المهمة الجديدة هنا..." class="flex-1 bg-slate-900/90 border border-slate-700 rounded-2xl px-4 py-3 text-white focus:outline-none focus:border-emerald-500 shadow-inner">
                    <button onclick="addTask()" class="px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white rounded-2xl font-bold shadow-lg shadow-emerald-600/30 transition-all flex items-center gap-2">
                        ➕ <span data-i18n="add_btn">إضافة</span>
                    </button>
                </div>

                <div id="tasks-container" class="space-y-3 max-h-[400px] overflow-y-auto pr-1"></div>
            </div>
        </section>

        <!-- SECTION 3: LESSONS SCHEDULE -->
        <section id="section-lessons" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="space-y-6">
                <div>
                    <h2 class="text-2xl font-black text-blue-300 mb-2" data-i18n="lessons_header">🏫 جدول مواعيد الدروس الأسبوعية</h2>
                    <p class="text-sm text-slate-400" data-i18n="lessons_sub">نظم مواعيد دروسك وحصصك لكل يوم في الأسبوع بتصميم فخم وسهل.</p>
                </div>

                <div id="lessons-days-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5"></div>
            </div>
        </section>

        <!-- Lesson Modal -->
        <div id="lesson-modal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-md flex items-center justify-center z-50 hidden p-4">
            <div class="glass-card rounded-3xl p-6 sm:p-8 max-w-md w-full border border-blue-500/30 space-y-5 shadow-2xl relative">
                <div class="flex items-center justify-between border-b border-slate-700 pb-3">
                    <h3 id="modal-title" class="text-xl font-bold text-blue-300">إضافة / تعديل درس</h3>
                    <button onclick="closeLessonModal()" class="text-slate-400 hover:text-white text-xl">✕</button>
                </div>

                <div class="space-y-4">
                    <div>
                        <label class="block text-xs text-slate-400 mb-1" data-i18n="lesson_name">اسم المادة / الدرس</label>
                        <input type="text" id="modal-lesson-subject" placeholder="مثال: فيزياء - د/ أحمد" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1" data-i18n="lesson_time">الموعد والوقت</label>
                        <input type="text" id="modal-lesson-time" placeholder="مثال: 04:00 مساءً" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-blue-500">
                    </div>
                </div>

                <div class="flex gap-3 pt-2">
                    <button onclick="saveLessonFromModal()" class="flex-1 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-bold transition-all shadow-lg shadow-blue-600/30">
                        💾 حفظ الدرس
                    </button>
                    <button onclick="closeLessonModal()" class="px-5 py-3 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl font-bold transition-all border border-slate-700">
                        إلغاء
                    </button>
                </div>
            </div>
        </div>

        <!-- SECTION 4: AMBIENT SOUNDS -->
        <section id="section-sounds" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="max-w-2xl mx-auto text-center space-y-6">
                <div>
                    <h2 class="text-2xl font-black text-amber-300 mb-2" data-i18n="sounds_header">🌧️ أصوات المطر والتركيز الطبيعية</h2>
                    <p class="text-sm text-slate-400" data-i18n="sounds_sub">شغل أصوات الاسترخاء الطبيعية المعالجة عبر المتصفح لتعزيز تركيزك أثناء المذاكرة.</p>
                </div>

                <div class="p-8 rounded-3xl bg-slate-900/80 border border-amber-500/30 shadow-2xl relative overflow-hidden flex flex-col items-center justify-center gap-6">
                    <div class="absolute -top-12 -right-12 w-40 h-40 bg-amber-500/10 rounded-full blur-3xl"></div>
                    <div class="text-6xl animate-bounce">☔</div>
                    <div>
                        <h3 id="sound-status-title" class="text-xl font-bold text-white" data-i18n="sound_off">المشغل متوقف</h3>
                        <p class="text-xs text-slate-400 mt-1" data-i18n="sound_desc">مولد ترددات صوت المطر الأبيض التفاعلي</p>
                    </div>

                    <div class="w-full max-w-xs space-y-2">
                        <div class="flex justify-between text-xs text-slate-400">
                            <span data-i18n="volume">مستوى الصوت</span>
                            <span id="volume-val">50%</span>
                        </div>
                        <input type="range" id="volume-slider" min="0" max="100" value="50" oninput="updateVolume(this.value)" class="w-full accent-amber-500 cursor-pointer">
                    </div>

                    <button onclick="toggleRainSound()" id="sound-toggle-btn" class="px-8 py-3.5 bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white rounded-2xl font-bold shadow-lg shadow-amber-600/30 transition-all flex items-center gap-3">
                        🔊 <span id="sound-btn-text" data-i18n="play_sound">تشغيل أصوات المطر</span>
                    </button>
                </div>
            </div>
        </section>

        <!-- SECTION 5: LECTURE MATRIX -->
        <section id="section-matrix" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="space-y-6">
                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                    <div>
                        <h2 class="text-2xl font-black text-rose-300 mb-2" data-i18n="matrix_header">📊 مصفوفة المحاضرات التفاعلية</h2>
                        <p class="text-sm text-slate-400" data-i18n="matrix_sub">اضغط على أي خلية لتغيير حالتها (رمادي فارغ ➡️ أحمر غير منجز ➡️ أصفر منجز).</p>
                    </div>
                    <div class="flex items-center gap-3">
                        <button onclick="addLectureRow()" class="glass-btn px-4 py-2 rounded-xl font-bold text-xs text-rose-300">
                            ➕ <span data-i18n="add_row">إضافة محاضرة جديدة</span>
                        </button>
                        <button onclick="resetMatrix()" class="glass-btn px-4 py-2 rounded-xl font-bold text-xs text-slate-400">
                            🔄 <span data-i18n="reset_matrix">إعادة ضبط الجدول</span>
                        </button>
                    </div>
                </div>

                <div class="overflow-x-auto rounded-2xl border border-slate-700/80 shadow-2xl">
                    <table class="w-full text-center border-collapse">
                        <thead>
                            <tr id="matrix-header-row" class="bg-slate-900/90 text-slate-200 text-sm font-bold border-b border-slate-700"></tr>
                        </thead>
                        <tbody id="matrix-body" class="divide-y divide-slate-800 text-sm"></tbody>
                    </table>
                </div>
            </div>
        </section>

    </div>

    <script>
        const translations = {
            ar: {
                app_title: "المنظم الذكي",
                app_subtitle: "نظام إنتاجية متطور مع تصميم ثلاثي الأبعاد",
                lang_btn_text: "English",
                pomo_title: "مؤقت البومودورو",
                pomo_desc: "جلسات تركيز واستراحة مع منبه صوتي دائري",
                tasks_title: "المهام اليومية",
                tasks_desc: "قائمة مهام تفاعلية مع تتبع المنجز وغير المنجز",
                lessons_title: "مواعيد الدروس الأسبوعية",
                lessons_desc: "جدول فخم لتنظيم مواعيد الدروس والحصص",
                sounds_title: "أصوات الاسترخاء",
                sounds_desc: "توليد أصوات المطر والتركيز الطبيعية للمذاكرة",
                matrix_title: "جدول المحاضرات الذكي",
                matrix_desc: "مصفوفة متقدمة تشبه إكسل لتتبع المحاضرات لكل مادة",
                back_home: "العودة للرئيسية",
                pomo_header: "⏱️ مؤقت البومودورو الدائري",
                pomo_sub: "اضبط وقت التركيز والاستراحة وابدأ جلسة الإنتاجية.",
                focus_time: "تركيز (د)",
                short_break: "استراحة قصيرة",
                long_break: "استراحة طويلة",
                btn_focus: "جلسة تركيز",
                btn_break: "استراحة",
                start: "بدء",
                pause: "إيقاف مؤقت",
                reset: "إعادة ضبط",
                tasks_header: "✅ إدارة المهام اليومية",
                tasks_sub: "اضف مهامك، اضغط على زر الإنجاز لتتحول للون الأخضر المشع مع شطبها.",
                task_placeholder: "اكتب المهمة الجديدة هنا...",
                add_btn: "إضافة",
                lessons_header: "🏫 جدول مواعيد الدروس الأسبوعية",
                lessons_sub: "نظم مواعيد دروسك وحصصك لكل يوم في الأسبوع بتصميم فخم وسهل.",
                add_lesson: "إضافة درس",
                lesson_name: "اسم المادة / الدرس",
                lesson_time: "الموعد والوقت",
                sounds_header: "🌧️ أصوات المطر والتركيز الطبيعية",
                sounds_sub: "شغل أصوات الاسترخاء الطبيعية المعالجة عبر المتصفح لتعزيز تركيزك أثناء المذاكرة.",
                sound_off: "المشغل متوقف",
                sound_on: "مشغل المطر يعمل بنجاح 🌧️",
                sound_desc: "مولد ترددات صوت المطر الأبيض التفاعلي",
                volume: "مستوى الصوت",
                play_sound: "تشغيل أصوات المطر",
                stop_sound: "إيقاف الأصوات",
                matrix_header: "📊 مصفوفة المحاضرات التفاعلية",
                matrix_sub: "اضغط على أي خلية لتغيير حالتها (رمادي فارغ ➡️ أحمر غير منجز ➡️ أصفر منجز).",
                add_row: "إضافة محاضرة جديدة",
                reset_matrix: "إعادة ضبط الجدول",
                lecture: "المحاضرة",
                sat: "السبت", sun: "الأحد", mon: "الإثنين", tue: "الثلاثاء", wed: "الأربعاء", thu: "الخميس", fri: "الجمعة"
            },
            en: {
                app_title: "Smart Organizer",
                app_subtitle: "Advanced 3D Glassmorphism Productivity System",
                lang_btn_text: "العربية",
                pomo_title: "Pomodoro Timer",
                pomo_desc: "Focus & break sessions with interactive circular chime",
                tasks_title: "Daily Tasks",
                tasks_desc: "Interactive task list with completion toggle & glowing badges",
                lessons_title: "Weekly Lessons",
                lessons_desc: "Luxury schedule to organize weekly classes and lessons",
                sounds_title: "Ambient Sounds",
                sounds_desc: "Natural rain & focus white-noise audio generator",
                matrix_title: "Lecture Matrix",
                matrix_desc: "Excel-like advanced matrix to track lectures per subject",
                back_home: "Back to Dashboard",
                pomo_header: "⏱️ 3D Circular Pomodoro Timer",
                pomo_sub: "Set your focus and break intervals and boost productivity.",
                focus_time: "Focus (m)",
                short_break: "Short Break",
                long_break: "Long Break",
                btn_focus: "Focus Session",
                btn_break: "Break",
                start: "Start",
                pause: "Pause",
                reset: "Reset",
                tasks_header: "✅ Daily Tasks Manager",
                tasks_sub: "Add tasks and toggle completion to turn them vibrant green with strike-through.",
                task_placeholder: "Type a new task here...",
                add_btn: "Add Task",
                lessons_header: "🏫 Weekly Lesson Schedule",
                lessons_sub: "Organize your subject times and lessons for each day of the week effortlessly.",
                add_lesson: "Add Lesson",
                lesson_name: "Subject / Lesson Name",
                lesson_time: "Time & Slot",
                sounds_header: "🌧️ Natural Rain & Focus Sounds",
                sounds_sub: "Play browser-synthesized relaxing rain audio to enhance your study concentration.",
                sound_off: "Player Stopped",
                sound_on: "Rain Audio Playing 🌧️",
                sound_desc: "Interactive white-noise rain frequency generator",
                volume: "Volume",
                play_sound: "Play Rain Sound",
                stop_sound: "Stop Sound",
                matrix_header: "📊 Interactive Lecture Matrix",
                matrix_sub: "Click any cell to toggle its status (Empty ➡️ Incomplete/Red ➡️ Completed/Yellow).",
                add_row: "Add New Lecture Row",
                reset_matrix: "Reset Matrix",
                lecture: "Lecture",
                sat: "Saturday", sun: "Sunday", mon: "Monday", tue: "Tuesday", wed: "Wednesday", thu: "Thursday", fri: "Friday"
            }
        };

        let currentLang = localStorage.getItem('smart_org_lang') || 'ar';

        function applyLanguage() {
            document.documentElement.lang = currentLang;
            document.documentElement.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[currentLang][key]) {
                    el.textContent = translations[currentLang][key];
                }
            });
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
                const key = el.getAttribute('data-i18n-placeholder');
                if (translations[currentLang][key]) {
                    el.placeholder = translations[currentLang][key];
                }
            });
            document.getElementById('lang-btn-text').textContent = translations[currentLang]['lang_btn_text'];
            renderLessons();
            renderMatrixHeaders();
        }

        function toggleLanguage() {
            currentLang = currentLang === 'ar' ? 'en' : 'ar';
            localStorage.setItem('smart_org_lang', currentLang);
            applyLanguage();
            renderTasks();
            renderMatrixBody();
        }

        function switchSection(sectionId) {
            const dashboard = document.getElementById('home-dashboard');
            const backNav = document.getElementById('back-nav');
            const sections = ['pomodoro', 'tasks', 'lessons', 'sounds', 'matrix'];

            sections.forEach(s => {
                document.getElementById(`section-${s}`).classList.add('hidden');
            });

            if (sectionId === 'home') {
                dashboard.classList.remove('hidden');
                backNav.classList.add('hidden');
            } else {
                dashboard.classList.add('hidden');
                backNav.classList.remove('hidden');
                document.getElementById(`section-${sectionId}`).classList.remove('hidden');
            }
        }

        // --- POMODORO LOGIC ---
        let pomoTimeLeft = 25 * 60;
        let pomoTotalTime = 25 * 60;
        let pomoTimerInterval = null;
        let pomoIsRunning = false;
        let pomoCurrentMode = 'focus';

        function setPomoMode(mode) {
            pomoCurrentMode = mode;
            pausePomodoro();
            const focusMin = parseInt(document.getElementById('input-focus').value) || 25;
            const breakMin = parseInt(document.getElementById('input-short').value) || 5;
            
            if (mode === 'focus') {
                pomoTotalTime = focusMin * 60;
                document.getElementById('mode-focus-btn').className = "flex-1 py-2.5 rounded-xl font-bold text-sm bg-purple-600 text-white shadow-lg shadow-purple-600/30 transition-all";
                document.getElementById('mode-break-btn').className = "flex-1 py-2.5 rounded-xl font-bold text-sm bg-slate-800 text-slate-300 border border-slate-700 hover:bg-slate-700 transition-all";
                document.getElementById('pomo-status-label').textContent = currentLang === 'ar' ? 'تركيز' : 'Focus';
            } else {
                pomoTotalTime = breakMin * 60;
                document.getElementById('mode-break-btn').className = "flex-1 py-2.5 rounded-xl font-bold text-sm bg-purple-600 text-white shadow-lg shadow-purple-600/30 transition-all";
                document.getElementById('mode-focus-btn').className = "flex-1 py-2.5 rounded-xl font-bold text-sm bg-slate-800 text-slate-300 border border-slate-700 hover:bg-slate-700 transition-all";
                document.getElementById('pomo-status-label').textContent = currentLang === 'ar' ? 'استراحة' : 'Break';
            }
            pomoTimeLeft = pomoTotalTime;
            updatePomoDisplay();
        }

        function updatePomoDisplay() {
            const minutes = Math.floor(pomoTimeLeft / 60);
            const seconds = pomoTimeLeft % 60;
            document.getElementById('pomo-timer-display').textContent = 
                `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            
            const ring = document.getElementById('pomo-progress-ring');
            const circumference = 2 * Math.PI * 110;
            const offset = circumference - (pomoTimeLeft / pomoTotalTime) * circumference;
            ring.style.strokeDashoffset = offset;
        }

        function startPomodoro() {
            if (pomoIsRunning) return;
            pomoIsRunning = true;
            pomoTimerInterval = setInterval(() => {
                if (pomoTimeLeft > 0) {
                    pomoTimeLeft--;
                    updatePomoDisplay();
                } else {
                    pausePomodoro();
                    playChimeSound();
                    if (pomoCurrentMode === 'focus') {
                        setPomoMode('break');
                    } else {
                        setPomoMode('focus');
                    }
                    startPomodoro();
                }
            }, 1000);
        }

        function pausePomodoro() {
            pomoIsRunning = false;
            clearInterval(pomoTimerInterval);
        }

        function resetPomodoro() {
            pausePomodoro();
            setPomoMode(pomoCurrentMode);
        }

        function playChimeSound() {
            try {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(587.33, ctx.currentTime);
                gain.gain.setValueAtTime(0.3, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 1.5);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 1.5);
            } catch(e) {}
        }

        // --- TASKS LOGIC ---
        let tasks = JSON.parse(localStorage.getItem('smart_org_tasks')) || [
            { id: 1, text: "مراجعة المحاضرة الأولى فيزياء", completed: true },
            { id: 2, text: "حل أسئلة الكيمياء العضوية", completed: false }
        ];

        function renderTasks() {
            const container = document.getElementById('tasks-container');
            container.innerHTML = '';
            tasks.forEach(task => {
                const item = document.createElement('div');
                item.className = `p-4 rounded-2xl flex items-center justify-between transition-all duration-300 border ${
                    task.completed 
                    ? 'bg-emerald-950/40 border-emerald-500/50 text-emerald-200' 
                    : 'bg-rose-950/30 border-rose-500/30 text-slate-200'
                }`;
                item.innerHTML = `
                    <div class="flex items-center gap-3">
                        <button onclick="toggleTask(${task.id})" class="w-8 h-8 rounded-xl flex items-center justify-center font-bold text-sm transition-all ${
                            task.completed ? 'bg-emerald-500 text-slate-950 shadow-lg shadow-emerald-500/40' : 'bg-slate-800 border border-rose-500/50 text-rose-400'
                        }">
                            ${task.completed ? '✓' : '✕'}
                        </button>
                        <span class="${task.completed ? 'line-through text-emerald-400/80 font-medium' : 'font-semibold'}">${task.text}</span>
                    </div>
                    <button onclick="deleteTask(${task.id})" class="text-slate-500 hover:text-rose-400 p-1 transition-colors">🗑️</button>
                `;
                container.appendChild(item);
            });
            localStorage.setItem('smart_org_tasks', JSON.stringify(tasks));
        }

        function addTask() {
            const input = document.getElementById('task-input');
            if (!input.value.trim()) return;
            tasks.push({ id: Date.now(), text: input.value.trim(), completed: false });
            input.value = '';
            renderTasks();
        }

        function toggleTask(id) {
            tasks = tasks.map(t => t.id === id ? { ...t, completed: !t.completed } : t);
            renderTasks();
        }

        function deleteTask(id) {
            tasks = tasks.filter(t => t.id !== id);
            renderTasks();
        }

        // --- LESSONS LOGIC ---
        const dayKeys = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri'];
        let lessons = JSON.parse(localStorage.getItem('smart_org_lessons')) || {
            sat: [{ id: 1, subject: 'فيزياء - د/ أحمد', time: '04:00 مساءً' }],
            sun: [{ id: 2, subject: 'كيمياء - د/ محمود', time: '06:00 مساءً' }],
            mon: [], tue: [], wed: [], thu: [], fri: []
        };
        let activeTargetDay = null;
        let activeTargetLessonId = null;

        function renderLessons() {
            const grid = document.getElementById('lessons-days-grid');
            if (!grid) return;
            grid.innerHTML = '';
            dayKeys.forEach(day => {
                const dayCard = document.createElement('div');
                dayCard.className = "glass-card rounded-2xl p-5 border border-slate-700/60 flex flex-col justify-between";
                const dayLessons = lessons[day] || [];
                
                let listHtml = dayLessons.map(l => `
                    <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-700/80 flex items-center justify-between mb-2">
                        <div>
                            <div class="font-bold text-sm text-blue-300">${l.subject}</div>
                            <div class="text-xs text-slate-400 mt-0.5">⏰ ${l.time}</div>
                        </div>
                        <div class="flex items-center gap-1">
                            <button onclick="openEditLessonModal('${day}', ${l.id})" class="p-1 text-slate-400 hover:text-blue-400 text-xs">✏️</button>
                            <button onclick="deleteLesson('${day}', ${l.id})" class="p-1 text-slate-400 hover:text-rose-400 text-xs">🗑️</button>
                        </div>
                    </div>
                `).join('');

                dayCard.innerHTML = `
                    <div>
                        <div class="flex items-center justify-between border-b border-slate-700 pb-3 mb-3">
                            <h4 class="font-bold text-lg text-slate-100">${translations[currentLang][day]}</h4>
                            <span class="text-xs bg-blue-500/20 text-blue-300 px-2.5 py-1 rounded-lg font-bold">${dayLessons.length}</span>
                        </div>
                        <div class="space-y-2 max-h-48 overflow-y-auto">${listHtml || '<p class="text-xs text-slate-500 py-2">لا يوجد دروس مضافة</p>'}</div>
                    </div>
                    <button onclick="openAddLessonModal('${day}')" class="mt-4 w-full py-2 bg-blue-600/20 hover:bg-blue-600/40 text-blue-300 border border-blue-500/30 rounded-xl font-bold text-xs transition-all flex items-center justify-center gap-1">
                        ➕ ${translations[currentLang]['add_lesson']}
                    </button>
                `;
                grid.appendChild(dayCard);
            });
            localStorage.setItem('smart_org_lessons', JSON.stringify(lessons));
        }

        function openAddLessonModal(day) {
            activeTargetDay = day;
            activeTargetLessonId = null;
            document.getElementById('modal-title').textContent = translations[currentLang]['add_lesson'];
            document.getElementById('modal-lesson-subject').value = '';
            document.getElementById('modal-lesson-time').value = '';
            document.getElementById('lesson-modal').classList.remove('hidden');
        }

        function openEditLessonModal(day, id) {
            activeTargetDay = day;
            activeTargetLessonId = id;
            const target = (lessons[day] || []).find(l => l.id === id);
            if (!target) return;
            document.getElementById('modal-title').textContent = 'تعديل درس';
            document.getElementById('modal-lesson-subject').value = target.subject;
            document.getElementById('modal-lesson-time').value = target.time;
            document.getElementById('lesson-modal').classList.remove('hidden');
        }

        function closeLessonModal() {
            document.getElementById('lesson-modal').classList.add('hidden');
        }

        function saveLessonFromModal() {
            const subject = document.getElementById('modal-lesson-subject').value.trim();
            const time = document.getElementById('modal-lesson-time').value.trim();
            if (!subject || !time || !activeTargetDay) return;

            if (!lessons[activeTargetDay]) lessons[activeTargetDay] = [];

            if (activeTargetLessonId) {
                lessons[activeTargetDay] = lessons[activeTargetDay].map(l => 
                    l.id === activeTargetLessonId ? { ...l, subject, time } : l
                );
            } else {
                lessons[activeTargetDay].push({ id: Date.now(), subject, time });
            }

            closeLessonModal();
            renderLessons();
        }

        function deleteLesson(day, id) {
            if (!lessons[day]) return;
            lessons[day] = lessons[day].filter(l => l.id !== id);
            renderLessons();
        }

        // --- AMBIENT SOUND LOGIC ---
        let audioCtx = null;
        let noiseNode = null;
        let gainNode = null;
        let isRainPlaying = false;

        function toggleRainSound() {
            if (isRainPlaying) {
                stopRainSound();
            } else {
                startRainSound();
            }
        }

        function startRainSound() {
            try {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                const bufferSize = 2 * audioCtx.sampleRate;
                const noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                const output = noiseBuffer.getChannelData(0);
                let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
                
                for (let i = 0; i < bufferSize; i++) {
                    let white = Math.random() * 2 - 1;
                    b0 = 0.99886 * b0 + white * 0.0555179;
                    b1 = 0.99332 * b1 + white * 0.0750759;
                    b2 = 0.96900 * b2 + white * 0.1538520;
                    b3 = 0.86650 * b3 + white * 0.3104856;
                    b4 = 0.55000 * b4 + white * 0.5329522;
                    b5 = -0.7616 * b5 - white * 0.0168980;
                    output[i] = b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362;
                    output[i] *= 0.11;
                    b6 = white * 0.115926;
                }

                noiseNode = audioCtx.createBufferSource();
                noiseNode.buffer = noiseBuffer;
                noiseNode.loop = true;

                gainNode = audioCtx.createGain();
                const val = document.getElementById('volume-slider').value;
                gainNode.gain.setValueAtTime(val / 100 * 0.3, audioCtx.currentTime);

                noiseNode.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                noiseNode.start();

                isRainPlaying = true;
                document.getElementById('sound-status-title').textContent = translations[currentLang]['sound_on'];
                document.getElementById('sound-btn-text').textContent = translations[currentLang]['stop_sound'];
                document.getElementById('sound-toggle-btn').className = "px-8 py-3.5 bg-rose-600 hover:bg-rose-500 text-white rounded-2xl font-bold shadow-lg shadow-rose-600/30 transition-all flex items-center gap-3";
            } catch(e) {}
        }

        function stopRainSound() {
            if (noiseNode) {
                try { noiseNode.stop(); } catch(e){}
            }
            isRainPlaying = false;
            document.getElementById('sound-status-title').textContent = translations[currentLang]['sound_off'];
            document.getElementById('sound-btn-text').textContent = translations[currentLang]['play_sound'];
            document.getElementById('sound-toggle-btn').className = "px-8 py-3.5 bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white rounded-2xl font-bold shadow-lg shadow-amber-600/30 transition-all flex items-center gap-3";
        }

        function updateVolume(val) {
            document.getElementById('volume-val').textContent = `${val}%`;
            if (gainNode && audioCtx) {
                gainNode.gain.setValueAtTime(val / 100 * 0.3, audioCtx.currentTime);
            }
        }

        // --- LECTURE MATRIX LOGIC ---
        let matrixSubjects = JSON.parse(localStorage.getItem('smart_org_matrix_subjects')) || ['رياضة', 'عربي', 'كيمياء', 'فيزياء', 'أحياء'];
        let matrixRowsCount = parseInt(localStorage.getItem('smart_org_matrix_rows')) || 18;
        let matrixData = JSON.parse(localStorage.getItem('smart_org_matrix_data')) || {};

        function renderMatrixHeaders() {
            const tr = document.getElementById('matrix-header-row');
            if (!tr) return;
            tr.innerHTML = `<th class="p-3 border-r border-slate-700 bg-slate-900 w-24">#</th>`;
            matrixSubjects.forEach((sub, idx) => {
                tr.innerHTML += `
                    <th class="p-3 border-r border-slate-700 min-w-[120px]">
                        <input type="text" value="${sub}" onchange="updateMatrixSubject(${idx}, this.value)" class="bg-transparent text-center font-bold text-white focus:outline-none focus:bg-slate-800 rounded px-1 w-full">
                    </th>
                `;
            });
        }

        function updateMatrixSubject(index, value) {
            matrixSubjects[index] = value;
            localStorage.setItem('smart_org_matrix_subjects', JSON.stringify(matrixSubjects));
        }

        function renderMatrixBody() {
            const tbody = document.getElementById('matrix-body');
            if (!tbody) return;
            tbody.innerHTML = '';

            for (let r = 1; r <= matrixRowsCount; r++) {
                const tr = document.createElement('tr');
                tr.className = "hover:bg-slate-800/40 transition-colors";
                
                let rowCells = `<td class="p-3 font-bold text-slate-400 bg-slate-900/60 border-r border-slate-700/80">${translations[currentLang]['lecture']} ${r}</td>`;
                
                for (let c = 0; c < 5; c++) {
                    const key = `${r}_${c}`;
                    const state = matrixData[key] || 0; // 0: empty, 1: red, 2: yellow
                    
                    let bgClass = "bg-slate-800/30 text-slate-500 hover:bg-slate-800/80";
                    let stateText = "";
                    if (state === 1) {
                        bgClass = "bg-rose-600 font-bold text-white shadow-inner";
                        stateText = `المحاضرة ${r}`;
                    } else if (state === 2) {
                        bgClass = "bg-amber-400 font-black text-slate-950 shadow-inner";
                        stateText = `المحاضرة ${r}`;
                    }

                    rowCells += `
                        <td onclick="cycleCellState(${r}, ${c})" class="p-3 border-r border-slate-700/80 cursor-pointer transition-all duration-200 select-none ${bgClass}">
                            ${stateText}
                        </td>
                    `;
                }

                tr.innerHTML = rowCells;
                tbody.appendChild(tr);
            }

            localStorage.setItem('smart_org_matrix_data', JSON.stringify(matrixData));
            localStorage.setItem('smart_org_matrix_rows', matrixRowsCount);
        }

        function cycleCellState(row, col) {
            const key = `${row}_${col}`;
            const currentState = matrixData[key] || 0;
            const newState = (currentState + 1) % 3;
            matrixData[key] = newState;
            renderMatrixBody();
        }

        function addLectureRow() {
            matrixRowsCount++;
            renderMatrixBody();
        }

        function resetMatrix() {
            matrixData = {};
            renderMatrixBody();
        }

        // INITIALIZATION
        window.addEventListener('DOMContentLoaded', () => {
            applyLanguage();
            renderTasks();
            renderLessons();
            renderMatrixHeaders();
            renderMatrixBody();
        });
    </script>
</body>
</html>
"""

# 4. تضمين الكود بأقصى ارتفاع ملائم للموبايل والكمبيوتر
components.html(html_code, height=950, scrolling=True)
