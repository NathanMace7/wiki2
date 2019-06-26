from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse
from .models import UserFileUpload, Page
from .forms import UploadFileForm

import logging

logger = logging.getLogger(__name__)

#Directs user to the Index page
class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.all()

#Directs User to the Detail page
class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'

#This is the view counter at the bottom of the Detail page
def view_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        page.counter += 1
        # page.counter = F('counter') + 1
        # page.save(update_fields=['counter'])
        page.save()
        return render(request, 'wiki/detail.html', {'page': page})
    except Page.DoesNotExist:
        return render(request, 'wiki/create_page.html', {'page_name': pk})

#Login is required for this page
@login_required(login_url='wiki:login')

#This allows you to edit the page
def edit_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content = ''
    return render(request, 'wiki/edit_page.html', {'page_name': pk, 'content': content},)

#Login is required for this page
@login_required(login_url='wiki:login')
#This allows you to save the changed you have made
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

#Login is required for this page
@login_required(login_url='wiki:login')
#Thi allows you to delete the page
def delete_page(request, pk):
    page = Page.objects.get(pk=pk)
    template_name = 'wiki/delete.html'
    context = {"object": obj}
    return render(request, template_name, context)

#Login is required for this page
@login_required(login_url='wiki:login')
#This allows you to upload files
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


#Error Tests
def test_500_error(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=500)

def test_404_error(request):
    # Return an "Internal Server Error" 404 response code.
    return HttpResponse(status=404)

def test_401_error(request):
    # Return an "Internal Server Error" 401 response code.
    return HttpResponse(status=401)

def test_502_error(request):
    # Return an "Internal Server Error" 502 response code.
    return HttpResponse(status=502)