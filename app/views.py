from django.shortcuts import render
from app.models import Task

# Create your views here.
def home(request):
    context = {'Taded':False}
    if(request.method=='POST'):
        #Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context = {'Taded':True}
    
    return render(request,'home.html',context)

def tasks(request):
    allTasks = Task.objects.all()
    # for item in allTasks:
    #     print(item.taskTitle,item.taskDesc)
    context = {'tasks':allTasks}
    return render(request,'tasks.html',context)