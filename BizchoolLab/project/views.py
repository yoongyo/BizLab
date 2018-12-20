from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project/project_list.html', {
        'projects': projects,
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project/project_detail.html', {
        'project': project
    })

def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            Project = form.save()
            return redirect(Project)
    else:
        form = ProjectForm()

    return render(request, 'project/project_new.html', {
        'form': form
    })

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect(project)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'project/project_edit.html', {
        'form': form,
    })

