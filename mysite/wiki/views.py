from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Page, UserFileUpload
from .forms import UploadFileForm

import logging

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.all()


class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'


def view_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        page.counter += 1
        page.save()
        return render(request, 'wiki/detail.html', {'page': page})
    except Page.DoesNotExist:
        return render(request, 'wiki/create_page.html', {'page_name': pk})


@login_required(login_url='wiki:login')
def edit_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content = ''
    return render(request, 'wiki/edit_page.html', {'page_name': pk, 'content': content},)


@login_required(login_url='wiki:login')
def save_page(request, pk):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk=pk)
        page.content = content
    except Page.DoesNotExist:
        page = Page(title=pk, content=content)
    if 'Save' in request.POST:
        page.save()
    return redirect(page)


@login_required(login_url='wiki:login')
def delete_page(request, pk):
    page = Page.objects.get(pk=pk)
    template_name = 'wiki/delete.html'
    context = {"object": obj}
    return render(request, template_name, context)


def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render(request, 'wiki/upload.html', context)

