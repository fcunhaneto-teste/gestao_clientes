from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.utils import timezone

@login_required
def persons_list(request):
    persons = Person.objects.filter(id=1000)
    footer_message = 'Desenvolvimento web com Django 2.x'
    return render(request, 'person.html', {'persons': persons, 'footer_message': footer_message})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    footer_message = 'Desenvolvimento web com Django 2.x'
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form, 'footer_message': footer_message})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    footer_message = 'Desenvolvimento web com Django 2.x'
    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form, 'footer_message': footer_message})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    footer_message = 'Desenvolvimento web com Django 2.x'
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person, 'footer_message': footer_message})


class PersonList(ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_message'] = 'Footer Messager'
        return context

class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_message'] = 'Footer Messager'
        return context


class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']

    success_url = reverse_lazy('persons_list_cbv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_message'] = 'Footer Messager'
        return context


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    template_name_suffix = '_form_update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_message'] = 'Footer Messager'
        return context

    # success_url = reverse_lazy('persons_list_cbv')
    def get_success_url(self):
        return reverse_lazy('persons_list_cbv')


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons_list_cbv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_message'] = 'Footer Messager'
        return context