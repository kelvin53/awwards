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

def projectdetails(request,project_id):

    project=Project.objects.get(id=project_id)

    return render(request,"projectdetails.html",{"project":project})

def project(request,project_id):
   project = Project.objects.get(id=project_id)
   rating = round(((project.design + project.usability + project.content)/3),2)
   if request.method == 'POST':
       form = NewRateForm(request.POST,request.FILES)
       if form.is_valid:
           if project.design == 0:
               project.design = int(request.POST['design'])
           else:
               project.design = (project.design + int(request.POST['design']))/2
           if project.usability == 0:
               project.usability = int(request.POST['usability'])
           else:
               project.usability = (project.design + int(request.POST['usability']))/2
           if project.content == 0:
               project.content = int(request.POST['content'])
           else:
               project.content = (project.design + int(request.POST['content']))/2
           project.save()

   else:
       form = NewRateForm()
   return render(request,'project.html',{'form':form,'project':project,'rating':rating})


def profile(request):
    current_user=request.user
    projects=Project.objects.filter(profile=current_user).all()
    profile = Profile.objects.filter(user=current_user)

    if len(profile)<1:
        profile = "No profile"
    else:
        profile = Profile.objects.get(user=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})

def edit_profile(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        form=NewProfileForm()
    return render(request,'edit_profile.html',{"form":form})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects=Project.objects.all()
        serializers=ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)


class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles=Profile.objects.all()
        serializers=ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)
