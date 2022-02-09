from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import MovieForm
from . models import Movie
# Create your views here.



def fn_Index(request):
    movie_obj=Movie.objects.all()
    context={
        'movie_list':movie_obj
    }
    return render(request,'index.html',context)

def fn_Detail(request,movie_id):
    movie_obj=Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie_list': movie_obj})
    # return HttpResponse('this movie id is %s' % movie_id)

def fn_add(request):
    if request.method == 'POST':
        name=request.POST.get('txtName')
        desc=request.POST.get('txtDesc')
        year=request.POST.get('txtYear')
        image=request.FILES['img']
        movie_obj=Movie(name=name,desc=desc,year=year,image=image)
        movie_obj.save()
        return redirect('/')
    return render(request,'addmovie.html')
def fn_Update(request,id):
    movie_obj=Movie.objects.get(id=id)
    form_obj=MovieForm(request.POST or None, request.FILES, instance=movie_obj)
    if form_obj.is_valid():
        form_obj.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form_obj,'movie':movie_obj})

def fn_Delete(request,id):
    if request.method=='POST':
        movie_obj=Movie.objects.get(id=id)
        movie_obj.delete()
        return redirect('/')
    return render(request,'delete.html')
