import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="المنظم الذكي | Smart Organizer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>المنظم الذكي | Smart Organizer</title>
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

        <!-- Header & Global Progress -->
        <header class="glass-card rounded-2xl p-5 mb-8 flex flex-col gap-4">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
                <div class="flex items-center gap-3">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-cyan-500/30 animate-float text-2xl">
                        ✨
                    </div>
                    <div>
                        <h1 class="text-2xl font-black tracking-wide glow-text" id="app-title">المنظم الذكي</h1>
                        <p class="text-xs text-slate-400" id="app-subtitle">نظام إنتاجية متطور مع إحصاءات الإنجاز الشاملة</p>
                    </div>
                </div>

                <div class="flex items-center gap-3">
                    <button onclick="toggleLanguage()" class="glass-btn px-4 py-2 rounded-xl font-bold text-sm flex items-center gap-2 shadow-md cursor-pointer">
                        🌐 <span id="lang-btn-text">English</span>
                    </button>
                </div>
            </div>

            <!-- Global Progress Tracker -->
            <div class="bg-slate-900/80 rounded-xl p-3 border border-slate-700/70">
                <div class="flex justify-between items-center mb-1.5 text-xs font-bold">
                    <span class="text-cyan-300" id="global-prog-label">📊 نسبة الإنجاز الإجمالية للتطبيق</span>
                    <span id="global-progress-percent" class="text-emerald-400 font-black">0%</span>
                </div>
                <div class="w-full bg-slate-800 h-3 rounded-full overflow-hidden p-0.5 border border-slate-700">
                    <div id="global-progress-bar" class="bg-gradient-to-r from-cyan-500 via-emerald-400 to-green-500 h-full rounded-full transition-all duration-500" style="width: 0%"></div>
                </div>
            </div>
        </header>

        <!-- Dashboard Home Cards -->
        <div id="home-dashboard" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 mb-8">
            <div onclick="switchSection('backlog')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-amber-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-amber-500/20 rounded-full blur-2xl group-hover:bg-amber-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-amber-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">⚠️</div>
                <h3 class="text-xl font-bold mb-1 text-amber-300" id="card-backlog-title">الدروس المتراكمة</h3>
                <p class="text-xs text-slate-400" id="card-backlog-desc">تحديد فترة زمنية وإنقاذ الدروس المتأخرة</p>
            </div>

            <div onclick="switchSection('plans')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-cyan-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-cyan-500/20 rounded-full blur-2xl group-hover:bg-cyan-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-cyan-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">📚</div>
                <h3 class="text-xl font-bold mb-1 text-cyan-300" id="card-plans-title">خطط الكتب والحل</h3>
                <p class="text-xs text-slate-400" id="card-plans-desc">متابعة الكتب الخارجية والمستهدفات الشهرية</p>
            </div>

            <div onclick="switchSection('pomodoro')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-purple-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-purple-500/20 rounded-full blur-2xl group-hover:bg-purple-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-purple-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">⏱️</div>
                <h3 class="text-xl font-bold mb-1 text-purple-300" id="card-pomo-title">مؤقت البومودورو</h3>
                <p class="text-xs text-slate-400" id="card-pomo-desc">جلسات تركيز واستراحة مع منبه صوتي</p>
            </div>

            <div onclick="switchSection('tasks')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-emerald-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-emerald-500/20 rounded-full blur-2xl group-hover:bg-emerald-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-emerald-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">✅</div>
                <h3 class="text-xl font-bold mb-1 text-emerald-300" id="card-tasks-title">المهام اليومية</h3>
                <p class="text-xs text-slate-400" id="card-tasks-desc">قائمة مهام تفاعلية مريحة للعين</p>
            </div>

            <div onclick="switchSection('lessons')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-blue-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-blue-500/20 rounded-full blur-2xl group-hover:bg-blue-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-blue-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">🏫</div>
                <h3 class="text-xl font-bold mb-1 text-blue-300" id="card-lessons-title">جدول الدروس الأسبوعية</h3>
                <p class="text-xs text-slate-400" id="card-lessons-desc">تنظيم المواعيد والحصص الأسبوعية</p>
            </div>

            <div onclick="switchSection('matrix')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-rose-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-rose-500/20 rounded-full blur-2xl group-hover:bg-rose-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-rose-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">📊</div>
                <h3 class="text-xl font-bold mb-1 text-rose-300" id="card-matrix-title">جدول المحاضرات</h3>
                <p class="text-xs text-slate-400" id="card-matrix-desc">مصفوفة إكسل لتتبع محاضرات كل مادة</p>
            </div>
        </div>

        <!-- Back Button -->
        <div id="back-nav" class="mb-6 hidden">
            <button onclick="switchSection('home')" class="glass-btn px-5 py-2.5 rounded-xl font-bold text-sm flex items-center gap-2 text-cyan-300 cursor-pointer">
                ⬅️ <span id="back-home-text">العودة للرئيسية</span>
            </button>
        </div>

        <!-- SECTION: BACKLOG -->
        <section id="section-backlog" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="max-w-3xl mx-auto space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                    <div>
                        <h2 class="text-2xl font-black text-amber-300 mb-1">⚠️ جدول الدروس المتراكمة</h2>
                        <p class="text-sm text-slate-400">اضف الدرس المتأخر وحدد له مهلة زمنية لإنجازه.</p>
                    </div>
                    <div class="bg-slate-900/90 border border-amber-500/40 px-4 py-2 rounded-2xl text-center">
                        <span class="text-xs text-slate-400 block">نسبة الإنجاز</span>
                        <span id="backlog-progress-val" class="text-lg font-bold text-amber-300">0%</span>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    <input type="text" id="backlog-subject" placeholder="الدرس / المادة (مثال: باب الفيزياء)" class="sm:col-span-1 bg-slate-900 border border-slate-700 rounded-2xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-500">
                    <input type="date" id="backlog-deadline" class="sm:col-span-1 bg-slate-900 border border-slate-700 rounded-2xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-500">
                    <button type="button" onclick="addBacklogItem()" class="sm:col-span-1 px-6 py-3 bg-amber-600 hover:bg-amber-500 text-white rounded-2xl font-bold shadow-lg shadow-amber-600/30 transition-all flex items-center justify-center gap-2 cursor-pointer">
                        ➕ إضافة درس متراكم
                    </button>
                </div>

                <div id="backlog-container" class="space-y-3 max-h-[450px] overflow-y-auto pr-1"></div>
            </div>
        </section>

        <!-- SECTION: MONTHLY PLANS -->
        <section id="section-plans" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="max-w-3xl mx-auto space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                    <div>
                        <h2 class="text-2xl font-black text-cyan-300 mb-1">📚 خطة الحل المستهدفة والشهرية</h2>
                        <p class="text-sm text-slate-400">حدد الكتب المدرسية والأنشطة المقررة شهرياً وموعد إنهاء كل كتاب.</p>
                    </div>
                    <div class="bg-slate-900/90 border border-cyan-500/40 px-4 py-2 rounded-2xl text-center">
                        <span class="text-xs text-slate-400 block">نسبة الإنجاز</span>
                        <span id="plans-progress-val" class="text-lg font-bold text-cyan-300">0%</span>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    <input type="text" id="plan-book" placeholder="اسم الكتاب (مثال: كتاب الامتحان)" class="sm:col-span-1 bg-slate-900 border border-slate-700 rounded-2xl px-4 py-3 text-white text-sm focus:outline-none focus:border-cyan-500">
                    <input type="text" id="plan-target" placeholder="المستهدف (مثال: حل الفصول 1 و 2)" class="sm:col-span-1 bg-slate-900 border border-slate-700 rounded-2xl px-4 py-3 text-white text-sm focus:outline-none focus:border-cyan-500">
                    <button type="button" onclick="addPlanItem()" class="sm:col-span-1 px-6 py-3 bg-cyan-600 hover:bg-cyan-500 text-white rounded-2xl font-bold shadow-lg shadow-cyan-600/30 transition-all flex items-center justify-center gap-2 cursor-pointer">
                        🎯 إضافة خطة كتاب
                    </button>
                </div>

                <div id="plans-container" class="space-y-3 max-h-[450px] overflow-y-auto pr-1"></div>
            </div>
        </section>

        <!-- SECTION: POMODORO -->
        <section id="section-pomodoro" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="flex flex-col md:flex-row items-center justify-between gap-8">
                <div class="w-full md:w-1/2 space-y-6">
                    <div>
                        <h2 class="text-2xl font-black text-purple-300 mb-2">⏱️ مؤقت البومودورو الدائري</h2>
                        <p class="text-sm text-slate-400">اضبط وقت التركيز والاستراحة وابدأ جلسة الإنتاجية.</p>
                    </div>

                    <div class="grid grid-cols-3 gap-3">
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1">تركيز (د)</label>
                            <input type="number" id="input-focus" value="25" min="1" max="120" onchange="resetPomodoro()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1">استراحة قصيرة</label>
                            <input type="number" id="input-short" value="5" min="1" max="60" onchange="resetPomodoro()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1">استراحة طويلة</label>
                            <input type="number" id="input-long" value="15" min="1" max="60" onchange="resetPomodoro()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                    </div>

                    <div class="flex gap-3">
                        <button type="button" onclick="setPomoMode('focus')" id="mode-focus-btn" class="flex-1 py-2.5 rounded-xl font-bold text-sm bg-purple-600 text-white shadow-lg shadow-purple-600/30 transition-all cursor-pointer">جلسة تركيز</button>
                        <button type="button" onclick="setPomoMode('break')" id="mode-break-btn" class="flex-1 py-2.5 rounded-xl font-bold text-sm bg-slate-800 text-slate-300 border border-slate-700 hover:bg-slate-700 transition-all cursor-pointer">استراحة</button>
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
                        <button type="button" onclick="startPomodoro()" class="px-6 py-3 bg-gradient-to-r from-purple-600 to-indigo-600 text-white rounded-2xl font-bold shadow-lg shadow-purple-600/30 transition-all cursor-pointer">▶️ بدء</button>
                        <button type="button" onclick="pausePomodoro()" class="px-6 py-3 bg-slate-800 text-amber-300 border border-slate-700 rounded-2xl font-bold cursor-pointer">⏸️ إيقاف</button>
                        <button type="button" onclick="resetPomodoro()" class="px-6 py-3 bg-slate-800 text-rose-400 border border-slate-700 rounded-2xl font-bold cursor-pointer">🔄 إعادة</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION: TASKS -->
        <section id="section-tasks" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="max-w-2xl mx-auto space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                    <div>
                        <h2 class="text-2xl font-black text-emerald-300 mb-1">✅ إدارة المهام اليومية</h2>
                        <p class="text-sm text-slate-400">اضف مهامك، اضغط على زر الإنجاز لتتبع الإنجاز.</p>
                    </div>
                    <div class="bg-slate-900/90 border border-emerald-500/40 px-4 py-2 rounded-2xl text-center">
                        <span class="text-xs text-slate-400 block">نسبة الإنجاز</span>
                        <span id="tasks-progress-val" class="text-lg font-bold text-emerald-300">0%</span>
                    </div>
                </div>

                <div class="flex gap-3">
                    <input type="text" id="task-input" placeholder="اكتب المهمة الجديدة هنا..." class="flex-1 bg-slate-900/90 border border-slate-700 rounded-2xl px-4 py-3 text-white focus:outline-none focus:border-emerald-500 shadow-inner">
                    <button type="button" onclick="addTask()" class="px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white rounded-2xl font-bold shadow-lg shadow-emerald-600/30 transition-all cursor-pointer">➕ إضافة</button>
                </div>

                <div id="tasks-container" class="space-y-3 max-h-[400px] overflow-y-auto pr-1"></div>
            </div>
        </section>

        <!-- SECTION: LESSONS SCHEDULE -->
        <section id="section-lessons" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="space-y-6">
                <div>
                    <h2 class="text-2xl font-black text-blue-300 mb-2">🏫 جدول مواعيد الدروس الأسبوعية</h2>
                    <p class="text-sm text-slate-400">نظم مواعيد دروسك وحصصك لكل يوم في الأسبوع.</p>
                </div>

                <div id="lessons-days-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5"></div>
            </div>
        </section>

        <!-- Lesson Modal -->
        <div id="lesson-modal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-md flex items-center justify-center z-50 hidden p-4">
            <div class="glass-card rounded-3xl p-6 sm:p-8 max-w-md w-full border border-blue-500/30 space-y-5 shadow-2xl relative">
                <div class="flex items-center justify-between border-b border-slate-700 pb-3">
                    <h3 id="modal-title" class="text-xl font-bold text-blue-300">إضافة / تعديل درس</h3>
                    <button onclick="closeLessonModal()" class="text-slate-400 hover:text-white text-xl cursor-pointer">✕</button>
                </div>

                <div class="space-y-4">
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">اسم المادة / الدرس</label>
                        <input type="text" id="modal-lesson-subject" placeholder="مثال: فيزياء - د/ أحمد" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">الموعد والوقت</label>
                        <input type="text" id="modal-lesson-time" placeholder="مثال: 04:00 مساءً" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-blue-500">
                    </div>
                </div>

                <div class="flex gap-3 pt-2">
                    <button type="button" onclick="saveLessonFromModal()" class="flex-1 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-bold transition-all shadow-lg shadow-blue-600/30 cursor-pointer">
                        💾 حفظ الدرس
                    </button>
                    <button type="button" onclick="closeLessonModal()" class="px-5 py-3 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl font-bold transition-all border border-slate-700 cursor-pointer">
                        إلغاء
                    </button>
                </div>
            </div>
        </div>

        <!-- SECTION: MATRIX -->
        <section id="section-matrix" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="space-y-6">
                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                    <div>
                        <h2 class="text-2xl font-black text-rose-300 mb-1">📊 مصفوفة المحاضرات التفاعلية</h2>
                        <p class="text-sm text-slate-400">الأصفر = تم الإنجاز ✅ | الأحمر = غير منجز ❌</p>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="bg-slate-900/90 border border-rose-500/40 px-3 py-1.5 rounded-xl text-center">
                            <span class="text-[10px] text-slate-400 block">إنجاز المحاضرات</span>
                            <span id="matrix-progress-val" class="text-sm font-bold text-rose-300">0%</span>
                        </div>
                        <button type="button" onclick="addLectureRow()" class="glass-btn px-3 py-2 rounded-xl font-bold text-xs text-rose-300 cursor-pointer">➕ صف جديد</button>
                        <button type="button" onclick="resetMatrix()" class="glass-btn px-3 py-2 rounded-xl font-bold text-xs text-slate-400 cursor-pointer">🔄 إعادة</button>
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
                app_subtitle: "نظام إنتاجية متطور مع إحصاءات الإنجاز الشاملة",
                lang_btn_text: "English",
                global_prog_label: "📊 نسبة الإنجاز الإجمالية للتطبيق",
                back_home_text: "العودة للرئيسية",
                card_backlog_title: "الدروس المتراكمة",
                card_backlog_desc: "تحديد فترة زمنية وإنقاذ الدروس المتأخرة",
                card_plans_title: "خطط الكتب والحل",
                card_plans_desc: "متابعة الكتب الخارجية والمستهدفات الشهرية",
                card_pomo_title: "مؤقت البومودورو",
                card_pomo_desc: "جلسات تركيز واستراحة مع منبه صوتي",
                card_tasks_title: "المهام اليومية",
                card_tasks_desc: "قائمة مهام تفاعلية مريحة للعين",
                card_lessons_title: "جدول الدروس الأسبوعية",
                card_lessons_desc: "تنظيم المواعيد والحصص الأسبوعية",
                card_matrix_title: "جدول المحاضرات",
                card_matrix_desc: "مصفوفة إكسل لتتبع محاضرات كل مادة",
                sat: "السبت", sun: "الأحد", mon: "الإثنين", tue: "الثلاثاء", wed: "الأربعاء", thu: "الخميس", fri: "الجمعة"
            },
            en: {
                app_title: "Smart Organizer",
                app_subtitle: "Advanced Productivity System with Comprehensive Progress",
                lang_btn_text: "العربية",
                global_prog_label: "📊 Overall Application Progress",
                back_home_text: "Back to Dashboard",
                card_backlog_title: "Backlog Lessons",
                card_backlog_desc: "Set timeframes and conquer overdue lessons",
                card_plans_title: "Books & Study Plans",
                card_plans_desc: "Track external books and monthly targets",
                card_pomo_title: "Pomodoro Timer",
                card_pomo_desc: "Focus and break sessions with audio chime",
                card_tasks_title: "Daily Tasks",
                card_tasks_desc: "Interactive task list to keep you on track",
                card_lessons_title: "Weekly Lessons",
                card_lessons_desc: "Organize weekly subject times and classes",
                card_matrix_title: "Lecture Matrix",
                card_matrix_desc: "Excel-like matrix to track lectures per subject",
                sat: "Saturday", sun: "Sunday", mon: "Monday", tue: "Tuesday", wed: "Wednesday", thu: "Thursday", fri: "Friday"
            }
        };

        let currentLang = localStorage.getItem('smart_org_lang') || 'ar';

        function applyLanguage() {
            document.documentElement.lang = currentLang;
            document.documentElement.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
            
            const t = translations[currentLang];
            document.getElementById('app-title').textContent = t.app_title;
            document.getElementById('app-subtitle').textContent = t.app_subtitle;
            document.getElementById('lang-btn-text').textContent = t.lang_btn_text;
            document.getElementById('global-prog-label').textContent = t.global_prog_label;
            document.getElementById('back-home-text').textContent = t.back_home_text;
            
            document.getElementById('card-backlog-title').textContent = t.card_backlog_title;
            document.getElementById('card-backlog-desc').textContent = t.card_backlog_desc;
            document.getElementById('card-plans-title').textContent = t.card_plans_title;
            document.getElementById('card-plans-desc').textContent = t.card_plans_desc;
            document.getElementById('card-pomo-title').textContent = t.card_pomo_title;
            document.getElementById('card-pomo-desc').textContent = t.card_pomo_desc;
            document.getElementById('card-tasks-title').textContent = t.card_tasks_title;
            document.getElementById('card-tasks-desc').textContent = t.card_tasks_desc;
            document.getElementById('card-lessons-title').textContent = t.card_lessons_title;
            document.getElementById('card-lessons-desc').textContent = t.card_lessons_desc;
            document.getElementById('card-matrix-title').textContent = t.card_matrix_title;
            document.getElementById('card-matrix-desc').textContent = t.card_matrix_desc;

            renderLessons();
        }

        function toggleLanguage() {
            currentLang = currentLang === 'ar' ? 'en' : 'ar';
            localStorage.setItem('smart_org_lang', currentLang);
            applyLanguage();
        }

        const dayKeys = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri'];

        function switchSection(sectionId) {
            const dashboard = document.getElementById('home-dashboard');
            const backNav = document.getElementById('back-nav');
            const sections = ['backlog', 'plans', 'pomodoro', 'tasks', 'lessons', 'matrix'];

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

        // --- GLOBAL & SECTIONAL PROGRESS LOGIC ---
        function calculateGlobalProgress() {
            let total = 0;
            let completed = 0;

            // 1. Tasks Progress
            let tasksTotal = tasks.length;
            let tasksDone = tasks.filter(t => t.completed).length;
            let tasksPct = tasksTotal === 0 ? 0 : Math.round((tasksDone / tasksTotal) * 100);
            const tasksValEl = document.getElementById('tasks-progress-val');
            if(tasksValEl) tasksValEl.textContent = `${tasksPct}%`;

            // 2. Backlog Progress
            let backlogTotal = backlogItems.length;
            let backlogDone = backlogItems.filter(b => b.completed).length;
            let backlogPct = backlogTotal === 0 ? 0 : Math.round((backlogDone / backlogTotal) * 100);
            const backlogValEl = document.getElementById('backlog-progress-val');
            if(backlogValEl) backlogValEl.textContent = `${backlogPct}%`;

            // 3. Plans Progress
            let plansTotal = planItems.length;
            let plansDone = planItems.filter(p => p.completed).length;
            let plansPct = plansTotal === 0 ? 0 : Math.round((plansDone / plansTotal) * 100);
            const plansValEl = document.getElementById('plans-progress-val');
            if(plansValEl) plansValEl.textContent = `${plansPct}%`;

            // 4. Matrix Progress (Calculated ONLY on active recorded lectures: Yellow vs Red)
            let matrixActiveCells = 0;
            let matrixYellowCells = 0;

            for(let key in matrixData) {
                if(matrixData[key] === 2) {
                    matrixYellowCells++;
                    matrixActiveCells++;
                } else if(matrixData[key] === 1) {
                    matrixActiveCells++;
                }
            }

            let matrixPct = matrixActiveCells === 0 ? 0 : Math.round((matrixYellowCells / matrixActiveCells) * 100);
            const matrixValEl = document.getElementById('matrix-progress-val');
            if(matrixValEl) matrixValEl.textContent = `${matrixPct}%`;

            // Combined Global Progress
            total = tasksTotal + backlogTotal + plansTotal + matrixActiveCells;
            completed = tasksDone + backlogDone + plansDone + matrixYellowCells;

            const globalPct = total === 0 ? 0 : Math.round((completed / total) * 100);
            
            document.getElementById('global-progress-percent').textContent = `${globalPct}%`;
            document.getElementById('global-progress-bar').style.width = `${globalPct}%`;
        }

        // --- BACKLOG LOGIC ---
        let backlogItems = JSON.parse(localStorage.getItem('smart_org_backlog')) || [
            { id: 1, subject: "باب الفيزياء الكهربية", deadline: "2026-11-10", completed: false }
        ];

        function renderBacklog() {
            const container = document.getElementById('backlog-container');
            if(!container) return;
            container.innerHTML = '';
            backlogItems.forEach(item => {
                const div = document.createElement('div');
                div.className = `p-4 rounded-2xl flex items-center justify-between border transition-all ${
                    item.completed ? 'bg-emerald-950/40 border-emerald-500/50 text-emerald-200' : 'bg-slate-900/90 border-amber-500/30 text-slate-100'
                }`;
                div.innerHTML = `
                    <div class="flex items-center gap-3">
                        <button type="button" onclick="toggleBacklog(${item.id})" class="w-8 h-8 rounded-xl flex items-center justify-center font-bold text-sm cursor-pointer ${
                            item.completed ? 'bg-emerald-500 text-slate-950' : 'bg-slate-800 border border-amber-500/50 text-amber-400'
                        }">
                            ${item.completed ? '✓' : '✕'}
                        </button>
                        <div>
                            <div class="${item.completed ? 'line-through text-emerald-400/80 font-bold' : 'font-bold text-amber-300'}">${item.subject}</div>
                            <div class="text-xs text-slate-400">📅 مهلة الإنجاز: ${item.deadline || 'غير محدد'}</div>
                        </div>
                    </div>
                    <button type="button" onclick="deleteBacklog(${item.id})" class="text-slate-500 hover:text-rose-400 cursor-pointer">🗑️</button>
                `;
                container.appendChild(div);
            });
            localStorage.setItem('smart_org_backlog', JSON.stringify(backlogItems));
            calculateGlobalProgress();
        }

        function addBacklogItem() {
            const subjectInput = document.getElementById('backlog-subject');
            const deadlineInput = document.getElementById('backlog-deadline');
            const subject = subjectInput.value.trim();
            const deadline = deadlineInput.value;
            if (!subject) return;
            backlogItems.push({ id: Date.now(), subject, deadline, completed: false });
            subjectInput.value = '';
            deadlineInput.value = '';
            renderBacklog();
        }

        function toggleBacklog(id) {
            backlogItems = backlogItems.map(b => b.id === id ? { ...b, completed: !b.completed } : b);
            renderBacklog();
        }

        function deleteBacklog(id) {
            backlogItems = backlogItems.filter(b => b.id !== id);
            renderBacklog();
        }

        // --- MONTHLY PLANS LOGIC ---
        let planItems = JSON.parse(localStorage.getItem('smart_org_plans')) || [
            { id: 1, book: "كتاب الامتحان كيمياء", target: "إنهاء أجزاء العضوية", completed: false }
        ];

        function renderPlans() {
            const container = document.getElementById('plans-container');
            if(!container) return;
            container.innerHTML = '';
            planItems.forEach(item => {
                const div = document.createElement('div');
                div.className = `p-4 rounded-2xl flex items-center justify-between border transition-all ${
                    item.completed ? 'bg-emerald-950/40 border-emerald-500/50 text-emerald-200' : 'bg-slate-900/90 border-cyan-500/30 text-slate-100'
                }`;
                div.innerHTML = `
                    <div class="flex items-center gap-3">
                        <button type="button" onclick="togglePlan(${item.id})" class="w-8 h-8 rounded-xl flex items-center justify-center font-bold text-sm cursor-pointer ${
                            item.completed ? 'bg-emerald-500 text-slate-950' : 'bg-slate-800 border border-cyan-500/50 text-cyan-400'
                        }">
                            ${item.completed ? '✓' : '✕'}
                        </button>
                        <div>
                            <div class="${item.completed ? 'line-through text-emerald-400/80 font-bold' : 'font-bold text-cyan-300'}">${item.book}</div>
                            <div class="text-xs text-slate-400">🎯 المستهدف: ${item.target}</div>
                        </div>
                    </div>
                    <button type="button" onclick="deletePlan(${item.id})" class="text-slate-500 hover:text-rose-400 cursor-pointer">🗑️</button>
                `;
                container.appendChild(div);
            });
            localStorage.setItem('smart_org_plans', JSON.stringify(planItems));
            calculateGlobalProgress();
        }

        function addPlanItem() {
            const bookInput = document.getElementById('plan-book');
            const targetInput = document.getElementById('plan-target');
            const book = bookInput.value.trim();
            const target = targetInput.value.trim();
            if (!book) return;
            planItems.push({ id: Date.now(), book, target, completed: false });
            bookInput.value = '';
            targetInput.value = '';
            renderPlans();
        }

        function togglePlan(id) {
            planItems = planItems.map(p => p.id === id ? { ...p, completed: !p.completed } : p);
            renderPlans();
        }

        function deletePlan(id) {
            planItems = planItems.filter(p => p.id !== id);
            renderPlans();
        }

        // --- TASKS LOGIC ---
        let tasks = JSON.parse(localStorage.getItem('smart_org_tasks')) || [
            { id: 1, text: "مراجعة المحاضرة الأولى فيزياء", completed: true }
        ];

        function renderTasks() {
            const container = document.getElementById('tasks-container');
            if(!container) return;
            container.innerHTML = '';
            tasks.forEach(task => {
                const item = document.createElement('div');
                item.className = `p-4 rounded-2xl flex items-center justify-between border ${
                    task.completed ? 'bg-emerald-950/40 border-emerald-500/50 text-emerald-200' : 'bg-rose-950/30 border-rose-500/30 text-slate-200'
                }`;
                item.innerHTML = `
                    <div class="flex items-center gap-3">
                        <button type="button" onclick="toggleTask(${task.id})" class="w-8 h-8 rounded-xl flex items-center justify-center font-bold text-sm cursor-pointer ${
                            task.completed ? 'bg-emerald-500 text-slate-950' : 'bg-slate-800 border border-rose-500/50 text-rose-400'
                        }">
                            ${task.completed ? '✓' : '✕'}
                        </button>
                        <span class="${task.completed ? 'line-through text-emerald-400/80' : 'font-semibold'}">${task.text}</span>
                    </div>
                    <button type="button" onclick="deleteTask(${task.id})" class="text-slate-500 hover:text-rose-400 cursor-pointer">🗑️</button>
                `;
                container.appendChild(item);
            });
            localStorage.setItem('smart_org_tasks', JSON.stringify(tasks));
            calculateGlobalProgress();
        }

        function addTask() {
            const input = document.getElementById('task-input');
            if (!input || !input.value.trim()) return;
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

        // --- LESSONS SCHEDULE LOGIC ---
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
                            <button type="button" onclick="openEditLessonModal('${day}', ${l.id})" class="p-1 text-slate-400 hover:text-blue-400 text-xs cursor-pointer">✏️</button>
                            <button type="button" onclick="deleteLesson('${day}', ${l.id})" class="p-1 text-slate-400 hover:text-rose-400 text-xs cursor-pointer">🗑️</button>
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
                    <button type="button" onclick="openAddLessonModal('${day}')" class="mt-4 w-full py-2 bg-blue-600/20 hover:bg-blue-600/40 text-blue-300 border border-blue-500/30 rounded-xl font-bold text-xs transition-all flex items-center justify-center gap-1 cursor-pointer">
                        ➕ إضافة درس
                    </button>
                `;
                grid.appendChild(dayCard);
            });
            localStorage.setItem('smart_org_lessons', JSON.stringify(lessons));
        }

        function openAddLessonModal(day) {
            activeTargetDay = day;
            activeTargetLessonId = null;
            document.getElementById('modal-title').textContent = 'إضافة درس';
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
                
                let rowCells = `<td class="p-3 font-bold text-slate-400 bg-slate-900/60 border-r border-slate-700/80">المحاضرة ${r}</td>`;
                
                for (let c = 0; c < 5; c++) {
                    const key = `${r}_${c}`;
                    const state = matrixData[key] || 0;
                    
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
            calculateGlobalProgress();
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

        // --- INIT & ENTER KEY SUPPORT ---
        window.addEventListener('DOMContentLoaded', () => {
            applyLanguage();
            renderBacklog();
            renderPlans();
            renderTasks();
            renderLessons();
            renderMatrixHeaders();
            renderMatrixBody();

            const taskInput = document.getElementById('task-input');
            if(taskInput) {
                taskInput.addEventListener('keypress', function(e) {
                    if(e.key === 'Enter') addTask();
                });
            }

            const backlogSubject = document.getElementById('backlog-subject');
            if(backlogSubject) {
                backlogSubject.addEventListener('keypress', function(e) {
                    if(e.key === 'Enter') addBacklogItem();
                });
            }

            const planBook = document.getElementById('plan-book');
            if(planBook) {
                planBook.addEventListener('keypress', function(e) {
                    if(e.key === 'Enter') addPlanItem();
                });
            }
        });

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
            pomoTotalTime = (mode === 'focus' ? focusMin : breakMin) * 60;
            pomoTimeLeft = pomoTotalTime;
            updatePomoDisplay();
        }

        function updatePomoDisplay() {
            const minutes = Math.floor(pomoTimeLeft / 60);
            const seconds = pomoTimeLeft % 60;
            const display = document.getElementById('pomo-timer-display');
            if(display) display.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            
            const ring = document.getElementById('pomo-progress-ring');
            if(ring) {
                const circumference = 2 * Math.PI * 110;
                const offset = circumference - (pomoTimeLeft / pomoTotalTime) * circumference;
                ring.style.strokeDashoffset = offset;
            }
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
                    setPomoMode(pomoCurrentMode === 'focus' ? 'break' : 'focus');
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
    </script>
</body>
</html>
"""

components.html(html_code, height=950, scrolling=True)
