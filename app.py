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

        <!-- Header & Progress Bar Overlay -->
        <header class="glass-card rounded-2xl p-5 mb-8 flex flex-col gap-4">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
                <div class="flex items-center gap-3">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-cyan-500/30 animate-float text-2xl">
                        ✨
                    </div>
                    <div>
                        <h1 class="text-2xl font-black tracking-wide glow-text">المنظم الذكي</h1>
                        <p class="text-xs text-slate-400">نظام إنتاجية متطور لمتابعة الدروس والمتراكم والحل</p>
                    </div>
                </div>
            </div>

            <!-- Global Progress Tracker -->
            <div class="bg-slate-900/80 rounded-xl p-3 border border-slate-700/70">
                <div class="flex justify-between items-center mb-1.5 text-xs font-bold">
                    <span class="text-cyan-300">📊 نسبة الإنجاز الكلية للمهام والدروس</span>
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
                <h3 class="text-xl font-bold mb-1 text-amber-300">الدروس المتراكمة</h3>
                <p class="text-xs text-slate-400">تحديد فترة زمنية وإنقاذ الدروس المتأخرة</p>
            </div>

            <div onclick="switchSection('plans')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-cyan-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-cyan-500/20 rounded-full blur-2xl group-hover:bg-cyan-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-cyan-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">📚</div>
                <h3 class="text-xl font-bold mb-1 text-cyan-300">خطط الكتب والحل</h3>
                <p class="text-xs text-slate-400">متابعة الكتب الخارجية والمستهدف الشهرية</p>
            </div>

            <div onclick="switchSection('pomodoro')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-purple-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-purple-500/20 rounded-full blur-2xl group-hover:bg-purple-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-purple-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">⏱️</div>
                <h3 class="text-xl font-bold mb-1 text-purple-300">مؤقت البومودورو</h3>
                <p class="text-xs text-slate-400">جلسات تركيز واستراحة مع منبه صوتي</p>
            </div>

            <div onclick="switchSection('tasks')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-emerald-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-emerald-500/20 rounded-full blur-2xl group-hover:bg-emerald-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-emerald-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">✅</div>
                <h3 class="text-xl font-bold mb-1 text-emerald-300">المهام اليومية</h3>
                <p class="text-xs text-slate-400">قائمة مهام تفاعلية مريحة للعين</p>
            </div>

            <div onclick="switchSection('lessons')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-blue-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-blue-500/20 rounded-full blur-2xl group-hover:bg-blue-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-blue-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">🏫</div>
                <h3 class="text-xl font-bold mb-1 text-blue-300">جدول الدروس الأسبوعية</h3>
                <p class="text-xs text-slate-400">تنظيم المواعيد والحصص الأسبوعية</p>
            </div>

            <div onclick="switchSection('matrix')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-rose-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-rose-500/20 rounded-full blur-2xl group-hover:bg-rose-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-rose-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">📊</div>
                <h3 class="text-xl font-bold mb-1 text-rose-300">جدول المحاضرات</h3>
                <p class="text-xs text-slate-400">مصفوفة إكسل لتتبع محاضرات كل مادة</p>
            </div>
        </div>

        <!-- Back Button -->
        <div id="back-nav" class="mb-6 hidden">
            <button onclick="switchSection('home')" class="glass-btn px-5 py-2.5 rounded-xl font-bold text-sm flex items-center gap-2 text-cyan-300">
                ⬅️ <span>العودة للرئيسية</span>
            </button>
        </div>

        <!-- SECTION: BACKLOG -->
        <section id="section-backlog" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="max-w-3xl mx-auto space-y-6">
                <div>
                    <h2 class="text-2xl font-black text-amber-300 mb-2">⚠️ جدول الدروس المتراكمة</h2>
                    <p class="text-sm text-slate-400">اضف الدرس المتأخر وحدد له مهلة زمنية لإنجازه والتخلص منه.</p>
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
                <div>
                    <h2 class="text-2xl font-black text-cyan-300 mb-2">📚 خطة الحل المستهدفة والشهرية</h2>
                    <p class="text-sm text-slate-400">حدد الكتب المدرسية والأنشطة المقررة شهرياً وموعد إنهاء كل كتاب.</p>
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
                <div>
                    <h2 class="text-2xl font-black text-emerald-300 mb-2">✅ إدارة المهام اليومية</h2>
                    <p class="text-sm text-slate-400">اضف مهامك، اضغط على زر الإنجاز لتتحول للون الأخضر مع الشطب.</p>
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
                    <p class="text-sm text-slate-400">نظم مواعيد دروسك وحصصك لكل يوم في الأسبوع بتصميم فخم وسهل.</p>
                </div>

                <div id="lessons-days-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5"></div>
            </div>
        </section>

        <!-- SECTION: MATRIX -->
        <section id="section-matrix" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="space-y-6">
                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                    <div>
                        <h2 class="text-2xl font-black text-rose-300 mb-2">📊 مصفوفة المحاضرات التفاعلية</h2>
                        <p class="text-sm text-slate-400">اضغط على أي خلية لتغيير حالتها (رمادي ➡️ أحمر ➡️ أصفر).</p>
                    </div>
                    <div class="flex items-center gap-3">
                        <button type="button" onclick="addLectureRow()" class="glass-btn px-4 py-2 rounded-xl font-bold text-xs text-rose-300 cursor-pointer">➕ إضافة صف جديد</button>
                        <button type="button" onclick="resetMatrix()" class="glass-btn px-4 py-2 rounded-xl font-bold text-xs text-slate-400 cursor-pointer">🔄 إعادة ضبط</button>
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

        // --- GLOBAL PROGRESS LOGIC ---
        function calculateGlobalProgress() {
            let totalItems = 0;
            let completedItems = 0;

            tasks.forEach(t => { totalItems++; if(t.completed) completedItems++; });
            backlogItems.forEach(b => { totalItems++; if(b.completed) completedItems++; });
            planItems.forEach(p => { totalItems++; if(p.completed) completedItems++; });

            const percentage = totalItems === 0 ? 0 : Math.round((completedItems / totalItems) * 100);
            
            document.getElementById('global-progress-percent').textContent = `${percentage}%`;
            document.getElementById('global-progress-bar').style.width = `${percentage}%`;
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

        // --- ENTER KEY SUPPORT FOR FAST ADDING ---
        document.addEventListener('DOMContentLoaded', () => {
            renderBacklog();
            renderPlans();
            renderTasks();

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
