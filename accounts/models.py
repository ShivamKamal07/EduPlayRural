from django.db import models
from django.contrib.auth.models import User

LANG_CHOICES = [
    ("hi", "Hindi"),
    ("en", "English"),
    ("mr", "Marathi"),
    ("od", "Odiya"),
]

BOARD_CHOICES = [
    ("up", "UP Board"),
    ("cbse", "CBSE"),
    ("icse", "ICSE"),
]

CLASS_CHOICES = [
    ("6", "6th"),
    ("7", "7th"),
    ("8", "8th"),
    ("9", "9th"),
    ("10", "10th"),
    ("11", "11th"),
    ("12", "12th"),
]

class Subject(models.Model):
    name = models.CharField(max_length=100)
    board = models.CharField(max_length=20, choices=BOARD_CHOICES)
    student_class = models.CharField(max_length=5, choices=CLASS_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.board} - {self.student_class})"


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=LANG_CHOICES, default="en")
    roll_number = models.CharField(max_length=50, unique=True)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    student_class = models.CharField(max_length=5, choices=CLASS_CHOICES)
    board = models.CharField(max_length=20, choices=BOARD_CHOICES)
    subjects = models.ManyToManyField("Subject", blank=True)
    school_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.student_name} ({self.roll_number})"
