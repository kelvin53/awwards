from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects=Project.get_projects()

    return render(request,'index.html',{"projects":projects})

def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

def rate(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewRateForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            # project.profile = current_user
            # project.save()
        return redirect('project')

    else:
        form = NewRateForm()
    return render(request, 'rate.html', {"form": form})
