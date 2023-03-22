from django import forms
from django.shortcuts import render

# Create your views here.
tasks=[]
class NewTaskForms(forms.Form):
    task=forms.CharField(label="New Task")
    #clientside validation
    priority=forms.IntegerField(label="Priority",min_value=1,max_value=5)
def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks
    })

def add(request):
    if request.method=="POST":
        form =NewTaskForms(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    return render(request,"tasks/add.html",{
        "form":NewTaskForms()
    })
