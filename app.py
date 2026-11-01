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
        /* Custom Scrollbar */
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

    <!-- Ambient Glow Background Blobs -->
    <div class="absolute top-0 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/3 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute bottom-10 left-1/3 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>

    <!-- Main Container -->
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
                <!-- Language Switcher -->
                <button onclick="toggleLanguage()" class="glass-btn px-4 py-2 rounded-xl font-bold text-sm flex items-center gap-2 shadow-md">
                    🌐 <span id="lang-btn-text">English</span>
                </button>
            </div>
        </header>

        <!-- Navigation Menu Cards (Dashboard Home) -->
        <div id="home-dashboard" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 mb-8">
            <!-- Card 1: Pomodoro -->
            <div onclick="switchSection('pomodoro')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-purple-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-purple-500/20 rounded-full blur-2xl group-hover:bg-purple-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-purple-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">⏱️</div>
                <h3 class="text-xl font-bold mb-1 text-purple-300" data-i18n="pomo_title">مؤقت البومودورو</h3>
                <p class="text-xs text-slate-400" data-i18n="pomo_desc">جلسات تركيز واستراحة مع منبه صوتي دائري</p>
            </div>

            <!-- Card 2: Tasks -->
            <div onclick="switchSection('tasks')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-emerald-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-emerald-500/20 rounded-full blur-2xl group-hover:bg-emerald-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-emerald-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">✅</div>
                <h3 class="text-xl font-bold mb-1 text-emerald-300" data-i18n="tasks_title">المهام اليومية</h3>
                <p class="text-xs text-slate-400" data-i18n="tasks_desc">قائمة مهام تفاعلية مع تتبع المنجز وغير المنجز</p>
            </div>

            <!-- Card 3: Lessons Schedule -->
            <div onclick="switchSection('lessons')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-blue-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-blue-500/20 rounded-full blur-2xl group-hover:bg-blue-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-blue-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">🏫</div>
                <h3 class="text-xl font-bold mb-1 text-blue-300" data-i18n="lessons_title">مواعيد الدروس الأسبوعية</h3>
                <p class="text-xs text-slate-400" data-i18n="lessons_desc">جدول فخم لتنظيم مواعيد الدروس والحصص</p>
            </div>

            <!-- Card 4: Ambient Sounds -->
            <div onclick="switchSection('sounds')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-amber-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-amber-500/20 rounded-full blur-2xl group-hover:bg-amber-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-amber-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">🌧️</div>
                <h3 class="text-xl font-bold mb-1 text-amber-300" data-i18n="sounds_title">أصوات الاسترخاء</h3>
                <p class="text-xs text-slate-400" data-i18n="sounds_desc">توليد أصوات المطر والتركيز الطبيعية للمذاكرة</p>
            </div>

            <!-- Card 5: Lecture Matrix -->
            <div onclick="switchSection('matrix')" class="glass-card rounded-2xl p-6 cursor-pointer hover:border-rose-500/50 transition-all duration-300 group relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-rose-500/20 rounded-full blur-2xl group-hover:bg-rose-500/40 transition-all"></div>
                <div class="text-3xl mb-3 p-3 bg-rose-500/20 w-fit rounded-xl group-hover:scale-110 transition-transform">📊</div>
                <h3 class="text-xl font-bold mb-1 text-rose-300" data-i18n="matrix_title">جدول المحاضرات الذكي</h3>
                <p class="text-xs text-slate-400" data-i18n="matrix_desc">مصفوفة متقدمة تشبه إكسل لتتبع المحاضرات لكل مادة</p>
            </div>
        </div>

        <!-- Back to Dashboard Button (Hidden by default) -->
        <div id="back-nav" class="mb-6 hidden">
            <button onclick="switchSection('home')" class="glass-btn px-5 py-2.5 rounded-xl font-bold text-sm flex items-center gap-2 text-cyan-300">
                ⬅️ <span data-i18n="back_home">العودة للرئيسية</span>
            </button>
        </div>

        <!-- ================= SECTION 1: POMODORO ================= -->
        <section id="section-pomodoro" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="flex flex-col md:flex-row items-center justify-between gap-8">
                <!-- Settings & Info -->
                <div class="w-full md:w-1/2 space-y-6">
                    <div>
                        <h2 class="text-2xl font-black text-purple-300 mb-2" data-i18n="pomo_header">⏱️ مؤقت البومودورو الدائري</h2>
                        <p class="text-sm text-slate-400" data-i18n="pomo_sub">اضبط وقت التركيز والاستراحة وابدأ جلسة الإنتاجية.</p>
                    </div>

                    <!-- Input Controls -->
                    <div class="grid grid-cols-3 gap-3">
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1" data-i18n="focus_time">تركيز (د)</label>
                            <input type="number" id="input-focus" value="25" min="1" max="120" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1" data-i18n="short_break">استراحة قصيرة</label>
                            <input type="number" id="input-short" value="5" min="1" max="60" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                        <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700">
                            <label class="block text-xs text-slate-400 mb-1" data-i18n="long_break">استراحة طويلة</label>
                            <input type="number" id="input-long" value="15" min="1" max="60" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-center font-bold text-white focus:outline-none focus:border-purple-500">
                        </div>
                    </div>

                    <div class="flex gap-3">
                        <button onclick="setPomoMode('focus')" id="mode-focus-btn" class="flex-1 py-2.5 rounded-xl font-bold text-sm bg-purple-600 text-white shadow-lg shadow-purple-600/30 transition-all" data-i18n="btn_focus">جلسة تركيز</button>
                        <button onclick="setPomoMode('break')" id="mode-break-btn" class="flex-1 py-2.5 rounded-xl font-bold text-sm bg-slate-800 text-slate-300 border border-slate-700 hover:bg-slate-700 transition-all" data-i18n="btn_break">استراحة</button>
                    </div>
                </div>

                <!-- Circular Timer Display -->
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

                    <!-- Timer Action Buttons -->
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

        <!-- ================= SECTION 2: TASKS MANAGER ================= -->
        <section id="section-tasks" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="max-w-2xl mx-auto space-y-6">
                <div>
                    <h2 class="text-2xl font-black text-emerald-300 mb-2" data-i18n="tasks_header">✅ إدارة المهام اليومية</h2>
                    <p class="text-sm text-slate-400" data-i18n="tasks_sub">اضف مهامك، اضغط على زر الإنجاز لتتحول للون الأخضر المشع مع شطبها.</p>
                </div>

                <!-- Add Task Form -->
                <div class="flex gap-3">
                    <input type="text" id="task-input" data-i18n-placeholder="task_placeholder" placeholder="اكتب المهمة الجديدة هنا..." class="flex-1 bg-slate-900/90 border border-slate-700 rounded-2xl px-4 py-3 text-white focus:outline-none focus:border-emerald-500 shadow-inner">
                    <button onclick="addTask()" class="px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white rounded-2xl font-bold shadow-lg shadow-emerald-600/30 transition-all flex items-center gap-2">
                        ➕ <span data-i18n="add_btn">إضافة</span>
                    </button>
                </div>

                <!-- Tasks List Container -->
                <div id="tasks-container" class="space-y-3 max-h-[400px] overflow-y-auto pr-1">
                    <!-- Tasks injected dynamically -->
                </div>
            </div>
        </section>

        <!-- ================= SECTION 3: LESSONS SCHEDULE ================= -->
        <section id="section-lessons" class="glass-card rounded-3xl p-6 sm:p-8 hidden">
            <div class="space-y-6">
                <div>
                    <h2 class="text-2xl font-black text-blue-300 mb-2" data-i18n="lessons_header">🏫 جدول مواعيد الدروس الأسبوعية</h2>
                    <p class="text-sm text-slate-400" data-i18n="lessons_sub">نظم مواعيد دروسك وحصصك لكل يوم في الأسبوع بتصميم فخم وسهل.</p>
                </div>

                <!-- Days Cards Grid -->
                <div id="lessons-days-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
                    <!-- Dynamic Days injected here -->
                </div>
            </div>
        </section>

        <!-- Modal for Adding/Editing Lesson -->
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

        <!-- ================= SECTION 4: AMBIENT SOUNDS ================= -->
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

        <!-- ================= SECTION 5: LECTURE MATRIX ================= -->
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

                <!-- Excel Matrix Table Container -->
                <div class="overflow-x-auto rounded-2xl border border-slate-700/80 shadow-2xl">
                    <table class="w-full text-center border-collapse">
                        <thead>
                            <tr id="matrix-header-row" class="bg-slate-900/90 text-slate-200 text-sm font-bold border-b border-slate-700">
                                <!-- Headers injected dynamically -->
                            </tr>
                        </thead>
                        <tbody id="matrix-body" class="divide-y divide-slate-800 text-sm">
                            <!-- Rows injected dynamically -->
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

    </div>

    <!-- JavaScript Application Logic -->
    <script>
        // --- TRANSLATIONS DICTIONARY ---
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

        // --- NAVIGATION BETWEEN SECTIONS ---
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

        // --- SECTION 1: POMODORO LOGIC ---
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
            const mins = Math.floor(pomoTimeLeft / 60);
            const secs = pomoTimeLeft % 60;
            document.getElementById('pomo-timer-display').textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            
            const circumference = 691;
            const offset = circumference - (pomoTimeLeft / pomoTotalTime) * circumference;
            document.getElementById('pomo-progress-ring').style.strokeDashoffset = offset;
        }

        function startPomodoro() {
            if (pomoIsRunning) return;
            pomoIsRunning = true;
            pomoTimerInterval = setInterval(() => {
                if (pomoTimeLeft > 0) {
                    pomoTimeLeft--;
                    updatePomoDisplay();
                } else {
                    clearInterval(pomoTimerInterval);
                    pomoIsRunning = false;
                    playAudioChime();
                    if (pomoCurrentMode === 'focus') {
                        setPomoMode('break');
                        startPomodoro();
                    } else {
                        setPomoMode('focus');
                    }
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

        function playAudioChime() {
            try {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(587.33, ctx.currentTime);
                gain.gain.setValueAtTime(0.2, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.5);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 1.5);
            } catch (e) {
                console.log('Audio chime not supported');
            }
        }

        // --- SECTION 2: TASKS MANAGER LOGIC ---
        let tasks = JSON.parse(localStorage.getItem('smart_org_tasks')) || [
            { text: 'مراجعة محاضرة الفيزياء الأولى', completed: true },
            { text: 'حل واجب الرياضيات', completed: false },
            { text: 'قراءة فصلين من الكتاب', completed: false }
        ];

        function saveTasks() {
            localStorage.setItem('smart_org_tasks', JSON.stringify(tasks));
        }

        function addTask() {
            const input = document.getElementById('task-input');
            const text = input.value.trim();
            if (text) {
                tasks.push({ text: text, completed: false });
                input.value = '';
                saveTasks();
                renderTasks();
            }
        }

        function toggleTask(index) {
            tasks[index].completed = !tasks[index].completed;
            saveTasks();
            renderTasks();
        }

        function deleteTask(index) {
            tasks.splice(index, 1);
            saveTasks();
            renderTasks();
        }

        function renderTasks() {
            const container = document.getElementById('tasks-container');
            container.innerHTML = '';
            if (tasks.length === 0) {
                container.innerHTML = `<p class="text-center text-slate-500 py-4 text-sm">${currentLang === 'ar' ? 'لا توجد مهام حالياً. أضف مهمة جديدة!' : 'No tasks yet. Add a new task!'}</p>`;
                return;
            }

            tasks.forEach((task, index) => {
                const item = document.createElement('div');
                item.className = `flex items-center justify-between p-4 rounded-2xl border transition-all ${
                    task.completed 
                    ? 'bg-emerald-950/40 border-emerald-500/40 text-emerald-300 shadow-lg shadow-emerald-900/20' 
                    : 'bg-rose-950/30 border-rose-500/40 text-rose-200 shadow-lg shadow-rose-950/20'
                }`;

                item.innerHTML = `
                    <div class="flex items-center gap-3 flex-1 cursor-pointer" onclick="toggleTask(${index})">
                        <div class="w-6 h-6 rounded-lg border-2 flex items-center justify-center transition-all ${
                            task.completed ? 'bg-emerald-500 border-emerald-400 text-white' : 'border-rose-400/80 bg-slate-900'
                        }">
                            ${task.completed ? '✓' : ''}
                        </div>
                        <span class="font-medium text-sm sm:text-base ${task.completed ? 'line-through opacity-75' : ''}">${task.text}</span>
                    </div>
                    <button onclick="deleteTask(${index})" class="text-slate-400 hover:text-rose-400 p-2 transition-colors">🗑️</button>
                `;
                container.appendChild(item);
            });
        }

        // --- SECTION 3: LESSONS SCHEDULE LOGIC ---
        const daysKeys = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri'];
        let lessonsData = JSON.parse(localStorage.getItem('smart_org_lessons')) || {
            sat: [{ subject: 'فيزياء', time: '04:00 PM' }, { subject: 'رياضيات', time: '06:30 PM' }],
            sun: [{ subject: 'كيمياء', time: '05:00 PM' }],
            mon: [{ subject: 'عربي', time: '03:00 PM' }],
            tue: [{ subject: 'أحياء', time: '04:30 PM' }],
            wed: [{ subject: 'فيزياء', time: '05:00 PM' }],
            thu: [{ subject: 'لغة إنجليزية', time: '06:00 PM' }],
            fri: []
        };

        let currentEditingDay = null;
        let currentEditingIndex = null;

        function saveLessons() {
            localStorage.setItem('smart_org_lessons', JSON.stringify(lessonsData));
        }

        function openLessonModal(dayKey, index = null) {
            currentEditingDay = dayKey;
            currentEditingIndex = index;

            const modal = document.getElementById('lesson-modal');
            const modalTitle = document.getElementById('modal-title');
            const subjectInput = document.getElementById('modal-lesson-subject');
            const timeInput = document.getElementById('modal-lesson-time');

            if (index !== null) {
                const item = lessonsData[dayKey][index];
                modalTitle.textContent = currentLang === 'ar' ? 'تعديل بيانات الدرس' : 'Edit Lesson Details';
                subjectInput.value = item.subject || '';
                timeInput.value = item.time || '';
            } else {
                modalTitle.textContent = currentLang === 'ar' ? 'إضافة درس جديد' : 'Add New Lesson';
                subjectInput.value = '';
                timeInput.value = '';
            }

            modal.classList.remove('hidden');
        }

        function closeLessonModal() {
            document.getElementById('lesson-modal').classList.add('hidden');
            currentEditingDay = null;
            currentEditingIndex = null;
        }

        function saveLessonFromModal() {
            const subject = document.getElementById('modal-lesson-subject').value.trim();
            const time = document.getElementById('modal-lesson-time').value.trim();

            if (!subject) return;

            if (!lessonsData[currentEditingDay]) lessonsData[currentEditingDay] = [];

            if (currentEditingIndex !== null) {
                lessonsData[currentEditingDay][currentEditingIndex] = { subject, time };
            } else {
                lessonsData[currentEditingDay].push({ subject, time });
            }

            saveLessons();
            renderLessons();
            closeLessonModal();
        }

        function deleteLesson(dayKey, index) {
            lessonsData[dayKey].splice(index, 1);
            saveLessons();
            renderLessons();
        }

        function renderLessons() {
            const grid = document.getElementById('lessons-days-grid');
            if (!grid) return;
            grid.innerHTML = '';

            daysKeys.forEach(dayKey => {
                const dayCard = document.createElement('div');
                dayCard.className = "glass-card rounded-2xl p-5 space-y-4 border border-blue-500/20 hover:border-blue-500/40 transition-all";
                
                const list = lessonsData[dayKey] || [];
                let listHtml = '';

                list.forEach((item, idx) => {
                    listHtml += `
                        <div class="flex items-center justify-between p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 hover:border-blue-500/30 transition-all group">
                            <div class="flex-1 cursor-pointer" onclick="openLessonModal('${dayKey}', ${idx})">
                                <h4 class="font-bold text-sm text-blue-200 group-hover:text-blue-400 transition-colors">${item.subject}</h4>
                                <span class="text-xs text-slate-400">⏰ ${item.time || '--:--'}</span>
                            </div>
                            <div class="flex items-center gap-1">
                                <button onclick="openLessonModal('${dayKey}', ${idx})" class="text-slate-400 hover:text-blue-300 p-1 text-xs transition-colors" title="تعديل">✏️</button>
                                <button onclick="deleteLesson('${dayKey}', ${idx})" class="text-slate-400 hover:text-rose-400 p-1 text-xs transition-colors" title="حذف">🗑️</button>
                            </div>
                        </div>
                    `;
                });

                dayCard.innerHTML = `
                    <div class="flex items-center justify-between border-b border-slate-700/60 pb-3">
                        <h3 class="font-black text-blue-400 text-lg">📌 ${translations[currentLang][dayKey]}</h3>
                        <button onclick="openLessonModal('${dayKey}')" class="px-3 py-1.5 bg-blue-600/30 hover:bg-blue-600/50 text-blue-300 border border-blue-500/40 rounded-xl text-xs font-bold transition-all shadow-md">
                            ➕ ${translations[currentLang]['add_lesson']}
                        </button>
                    </div>
                    <div class="space-y-2 max-h-56 overflow-y-auto pr-1">
                        ${listHtml || `<p class="text-xs text-slate-500 py-3 text-center">${currentLang === 'ar' ? 'لا توجد دروس مضافة' : 'No lessons added'}</p>`}
                    </div>
                `;

                grid.appendChild(dayCard);
            });
        }

        // --- SECTION 4: AMBIENT RAIN SOUND GENERATOR ---
        let audioCtx = null;
        let rainSource = null;
        let rainGain = null;
        let isPlayingRain = false;

        function toggleRainSound() {
            if (!isPlayingRain) {
                try {
                    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                    const bufferSize = 2 * audioCtx.sampleRate;
                    const noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                    const output = noiseBuffer.getChannelData(0);
                    for (let i = 0; i < bufferSize; i++) {
                        output[i] = Math.random() * 2 - 1;
                    }
                    rainSource = audioCtx.createBufferSource();
                    rainSource.buffer = noiseBuffer;
                    rainSource.loop = true;

                    const filter = audioCtx.createBiquadFilter();
                    filter.type = 'lowpass';
                    filter.frequency.value = 600;

                    rainGain = audioCtx.createGain();
                    const sliderVal = document.getElementById('volume-slider').value;
                    rainGain.gain.value = (sliderVal / 100) * 0.25;

                    rainSource.connect(filter);
                    filter.connect(rainGain);
                    rainGain.connect(audioCtx.destination);
                    rainSource.start();

                    isPlayingRain = true;
                    document.getElementById('sound-status-title').textContent = translations[currentLang]['sound_on'];
                    document.getElementById('sound-btn-text').textContent = translations[currentLang]['stop_sound'];
                } catch (e) {
                    console.log('Audio error');
                }
            } else {
                if (rainSource) {
                    rainSource.stop();
                    rainSource.disconnect();
                }
                if (audioCtx) {
                    audioCtx.close();
                }
                isPlayingRain = false;
                document.getElementById('sound-status-title').textContent = translations[currentLang]['sound_off'];
                document.getElementById('sound-btn-text').textContent = translations[currentLang]['play_sound'];
            }
        }

        function updateVolume(val) {
            document.getElementById('volume-val').textContent = val + '%';
            if (rainGain && audioCtx) {
                rainGain.gain.setValueAtTime((val / 100) * 0.25, audioCtx.currentTime);
            }
        }

        // --- SECTION 5: EXCEL-LIKE LECTURE MATRIX LOGIC ---
        let matrixData = JSON.parse(localStorage.getItem('smart_org_matrix')) || {
            headers: ['رياضيات', 'عربي', 'كيمياء', 'فيزياء', 'أحياء'],
            cells: Array(15).fill(0).map(() => Array(5).fill(0))
        };

        function saveMatrix() {
            localStorage.setItem('smart_org_matrix', JSON.stringify(matrixData));
        }

        function renderMatrixHeaders() {
            const headerRow = document.getElementById('matrix-header-row');
            headerRow.innerHTML = `<th class="p-3.5 border-b border-slate-700 w-20">#</th>`;
            matrixData.headers.forEach((header, index) => {
                headerRow.innerHTML += `
                    <th class="p-3.5 border-b border-slate-700">
                        <input type="text" value="${header}" onchange="updateHeader(${index}, this.value)" class="w-full bg-transparent text-center font-bold text-slate-100 focus:outline-none focus:bg-slate-800 rounded-lg py-1">
                    </th>
                `;
            });
        }

        function updateHeader(index, val) {
            matrixData.headers[index] = val;
            saveMatrix();
        }

        function renderMatrixBody() {
            const tbody = document.getElementById('matrix-body');
            tbody.innerHTML = '';
            matrixData.cells.forEach((row, rIndex) => {
                let tr = document.createElement('tr');
                tr.innerHTML = `<td class="p-3 font-bold text-slate-400 bg-slate-900/50 border-r border-slate-800">${translations[currentLang]['lecture']} ${rIndex + 1}</td>`;
                
                row.forEach((state, cIndex) => {
                    let td = document.createElement('td');
                    td.className = "p-3 border border-slate-800/80 cursor-pointer transition-all hover:opacity-80 select-none text-center font-bold h-12";
                    
                    if (state === 1) {
                        td.className += " bg-red-600 text-white shadow-md";
                        td.textContent = `${translations[currentLang]['lecture']} ${rIndex + 1}`;
                    } else if (state === 2) {
                        td.className += " bg-amber-400 text-slate-950 shadow-md";
                        td.textContent = `${translations[currentLang]['lecture']} ${rIndex + 1}`;
                    } else {
                        td.className += " bg-slate-900/40 text-slate-500 hover:bg-slate-800/60";
                        td.textContent = `${translations[currentLang]['lecture']} ${rIndex + 1}`;
                    }

                    td.onclick = () => {
                        matrixData.cells[rIndex][cIndex] = (matrixData.cells[rIndex][cIndex] + 1) % 3;
                        saveMatrix();
                        renderMatrixBody();
                    };

                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });
        }

        function addLectureRow() {
            matrixData.cells.push(Array(matrixData.headers.length).fill(0));
            saveMatrix();
            renderMatrixBody();
        }

        function resetMatrix() {
            matrixData.cells = Array(15).fill(0).map(() => Array(matrixData.headers.length).fill(0));
            saveMatrix();
            renderMatrixBody();
        }

        // --- INITIALIZE APP ON LOAD ---
        window.onload = function() {
            applyLanguage();
            updatePomoDisplay();
            renderTasks();
            renderLessons();
            renderMatrixHeaders();
            renderMatrixBody();
        };
    </script>
</body>
</html>
