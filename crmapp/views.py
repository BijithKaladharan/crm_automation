from django.shortcuts import render, redirect, HttpResponse
from .models import Course,Batch, Enquiry, Admissions,Payment
from django.views.generic import TemplateView
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date


class Course_Registration(TemplateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'crmapp/ch_course_reg.html'
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        self.context = {
            "form":self.form_class,
            "courses":courses
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            courses = Course.objects.all()
            self.context = {
                "form": self.form_class,
                "courses": courses
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form":self.form_class
            }
            return render(request, self.template_name, self.context)


class Course_edit(TemplateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'crmapp/ch_course_reg.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        courses = self.get_object(id)
        form = self.form_class(instance=courses)
        self.context = {
            "form":form,

        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        courses = self.get_object(id)
        form = self.form_class(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('course')
        return render(request, self.template_name, self.context)

class Course_delete(TemplateView):
    model = Course
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        course = self.get_object(id)
        course.delete()
        return redirect('course')

class Batch_Creation(TemplateView):
    model = Batch
    form_class = BatchCreateForm
    template_name = 'crmapp/ch_batch_creation.html'

    def get(self, request, *args, **kwargs):
        batches = Batch.objects.all()
        self.context = {
            "form": self.form_class,
            "batches": batches
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            batches = Batch.objects.all()
            self.context = {
                "form": self.form_class,
                "batches": batches
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)

class Batch_edit(TemplateView):
    model = Batch
    form_class = BatchCreateForm
    template_name = 'crmapp/ch_batch_creation.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batches = self.get_object(id)
        form = self.form_class(instance=batches)
        self.context = {
            "form":form,

        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batches = self.get_object(id)
        form = self.form_class(request.POST, instance=batches)
        if form.is_valid():
            form.save()
            return redirect('batch')
        return render(request, self.template_name, self.context)

class Batch_delete(TemplateView):
    model = Batch
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batch = self.get_object(id)
        batch.delete()
        return redirect('batch')