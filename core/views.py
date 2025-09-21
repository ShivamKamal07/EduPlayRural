from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import StudentProfile
import os
from django.conf import settings
from django.utils.html import escape
from django.http import JsonResponse


@login_required
def dashboard(request):
    profile = request.user.studentprofile
    default_subjects = ["Hindi", "English", "Math", "Science"]  # ✅ default list
    return render(request, "core/dashboard.html", {
        "profile": profile,
        "default_subjects": default_subjects,
    })


@login_required
def profile_view(request):
    profile = request.user.studentprofile
    default_subjects = ["Hindi", "English", "Math", "Science"]  # ✅ Python list
    return render(request, "core/profile.html", {
        "profile": profile,
        "default_subjects": default_subjects
    })

@login_required
def subjects_view(request):
    subjects = ["Math", "English", "Hindi", "Science"]
    return render(request, "core/subjects.html", {"subjects": subjects})

@login_required
def lessons_view(request, subject_name):
    lessons = [f"Lesson {i}" for i in range(1, 7)]  # 6 lessons each
    return render(request, "core/lessons.html", {
        "subject_name": subject_name,
        "lessons": lessons
    })

def lesson_detail(request, subject_name, lesson_no):
    template_name = f"core/lessons/{subject_name.lower()}_lesson{lesson_no}.html"
    try:
        return render(request, template_name, {
            "subject_name": subject_name,
            "lesson_no": lesson_no
        })
    except:
        return render(request, "core/lessons/lesson_not_found.html", {
            "subject_name": subject_name,
            "lesson_no": lesson_no
        })

def quizzes_subjects(request):
    subjects = ["Math", "English", "Hindi", "Science"]
    return render(request, "core/quizzes_subjects.html", {"subjects": subjects})

def quiz_list(request, subject_name):
    # Dummy: har subject ke liye 3 quizzes
    quizzes = [f"Quiz {i}" for i in range(1, 4)]
    return render(request, "core/quiz_list.html", {
        "subject_name": subject_name,
        "quizzes": quizzes
    })

def quiz_detail(request, subject_name, quiz_no):
    subject_name = subject_name.lower()
    template_path = f"core/quizzes/{subject_name}/quiz{quiz_no}.html"

    # check file exists
    abs_path = os.path.join(settings.BASE_DIR, "templates", template_path)
    if os.path.exists(abs_path):
        return render(request, template_path, {
            "subject_name": subject_name.title(),
            "quiz_no": quiz_no
        })
    else:
        return render(request, "core/quizzes/quiz_not_found.html", {
            "subject_name": subject_name.title(),
            "quiz_no": quiz_no
        })

  
@login_required
def progress_view(request):
    # Dummy progress values, later link with actual quiz/lesson completion
    progress = {
        "Math": 0,
        "English": 0,
        "Hindi": 0,
        "Science": 0
    }
    return render(request, "core/progress.html", {"progress": progress})

@login_required
def notebook_view(request):
    return render(request, "core/notebook.html")

def leaderboard_view(request):
    leaderboard = [
        {"name": "Amit Sharma", "class": "10th", "school": "DPS School", "points": 980, "progress": 95},
        {"name": "Riya Verma", "class": "9th", "school": "KV Public", "points": 870, "progress": 88},
        {"name": "Rahul Mehta", "class": "8th", "school": "St. Xavier's", "points": 820, "progress": 80},
        {"name": "Sneha Gupta", "class": "10th", "school": "DAV School", "points": 750, "progress": 70},
    ]
    return render(request, "core/leaderboard.html", {"leaderboard": leaderboard})


def chatbot_view(request):
    return render(request, "core/chatbot.html")


@login_required
def chatbot_api(request):
    """Responds to AJAX chatbot requests"""
    q = request.GET.get("q", "").lower().strip()
    user = request.user
    profile = getattr(user, "studentprofile", None)

    if not q:
        return JsonResponse({"reply": "Please type something!"})

    # Rule-based responses (later can be AI/DB powered)
    if "hi" in q or "hello" in q or "hey" in q:
        return JsonResponse({"reply": f"Hello {escape(profile.student_name if profile else user.username)} 👋! How can I help?"})

    if "subject" in q:
        subjects = [s.name for s in profile.subjects.all()] if profile and profile.subjects.exists() else ["Hindi", "English", "Math", "Science"]
        return JsonResponse({"reply": "Your subjects: " + ", ".join(subjects)})

    if "quiz" in q:
        return JsonResponse({"reply": "You can practice quizzes here 👉 <a href='/quizzes/'>Open Quizzes</a>"})

    if "progress" in q:
        return JsonResponse({"reply": "Check your progress here 👉 <a href='/progress/'>Progress</a>"})

    if "leaderboard" in q:
        return JsonResponse({"reply": "View top coders 👉 <a href='/leaderboard/'>Leaderboard</a>"})

    if "note" in q:
        return JsonResponse({"reply": "Access your smart notebook 👉 <a href='notebook/'>Notebook</a>"})

    # fallback
    return JsonResponse({"reply": "Sorry 😅, I didn’t understand. Try asking about subjects, quizzes, progress, leaderboard, or notes."})