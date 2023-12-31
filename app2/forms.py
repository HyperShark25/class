from django.contrib.auth.forms import forms
from .models import Subject, Teacher, Enrollment, Track


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = "__all__"


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"
