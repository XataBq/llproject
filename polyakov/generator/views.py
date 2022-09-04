from django.shortcuts import render, redirect
from .models import Variant
from .generate_task import new_variant
from .forms import VarForm, AnswerForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = VarForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['variant']:
                variant = Variant.objects.get(pk=form.cleaned_data['variant'])
                return redirect(variant)
            else:
                return redirect('/gen/')
    else:
        form = VarForm()
    return render(request, 'generator/index.html', {'form': form})


def gen(request):
    # variant = Variant.objects.get(pk=1)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answers = form.cleaned_data
            for key in answers:
                if answers[key] == '':
                    answers[key] = 'None'
            context = {'variant': new_variant, 'answers': answers}
            if request.user.is_authenticated:
                return render(request, 'generator/answer.html', context)
            else:
                redirect('/admin/')
    else:
        form = AnswerForm()
    context = {'variant': new_variant(), 'form': form}
    return render(request, 'generator/gen.html', context)


def ready_var(request, pk):
    variant = Variant.objects.get(pk=pk)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answers = form.cleaned_data
            for key in answers:
                if answers[key] == '':
                    answers[key] = 'None'
            context = {'variant': variant, 'answers': answers}
            if request.user.is_authenticated:
                return render(request, 'generator/answer.html', context)
            else:
                return redirect('/admin/')
    else:
        form = AnswerForm()
    context = {'variant': variant, 'form': form}
    return render(request, 'generator/ready_var.html', context)