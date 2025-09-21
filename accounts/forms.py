from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile, Subject

class StudentRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentProfile
        fields = [
            "language", "roll_number", "student_name", "father_name",
            "mobile_number", "address", "pincode",
            "student_class", "board", "subjects", "school_name"
        ]
        widgets = {
            "subjects": forms.CheckboxSelectMultiple
        }

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['subjects'].queryset = Subject.objects.none()  # default empty

    if 'board' in self.data and 'student_class' in self.data:
        board = self.data.get('board')
        student_class = self.data.get('student_class')
        if board and student_class:
            self.fields['subjects'].queryset = Subject.objects.filter(
                board=board,
                student_class=student_class
            )
    elif self.instance.pk:
        # edit case: already selected profile
        self.fields['subjects'].queryset = self.instance.subjects.all()



        if 'board' in self.data and 'student_class' in self.data:
            board = self.data.get('board')
            student_class = self.data.get('student_class')
            if board and student_class:
                self.fields['subjects'].queryset = Subject.objects.filter(
                    board=board, student_class=student_class
                )
        elif self.instance.pk:
            # when editing existing student
            self.fields['subjects'].queryset = self.instance.subjects.all()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password != confirm:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
