from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import StudentRegisterForm
from .models import Subject
from django.http import JsonResponse

def register_view(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            # Create user
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=username, email=email, password=password)

            # Create student profile
            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            # ✅ Save selected subjects manually
            subjects_ids = request.POST.getlist("subjects")
            if subjects_ids:
                profile.subjects.set(subjects_ids)

            login(request, user)
            return redirect("/")
    else:
        form = StudentRegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def load_subjects(request):
    board = request.GET.get('board')
    student_class = request.GET.get('student_class')
    subjects = []
    if board and student_class:
        subjects = Subject.objects.filter(board=board, student_class=student_class).values('id', 'name')
    return JsonResponse(list(subjects), safe=False)