from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from .models import Book
from .forms import BookForm

class BookList(TemplateView):
    model=Book
    template_name = 'book/booklist.html'
    context={}
    def get(self, request, *args, **kwargs):
        books=self.model.objects.all()
        self.context['books']=books
        return render(request,self.template_name,self.context)

class BookCreate(TemplateView):
    model=Book
    form_class=BookForm
    template_name = 'book/bookcreate.html'
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            self.context['form']=form
            return render(request,self.template_name,self.context)

class BookUpdate(TemplateView):
    model=Book
    form_class=BookForm
    template_name = 'book/bookupdate.html'
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        # book=self.model.objects.get(id=kwargs['id'])
        book=self.get_object(kwargs['id'])
        self.context['form']=self.form_class(instance=book)
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        # book=self.model.objects.get(id=kwargs['id'])
        book=self.get_object(kwargs['id'])
        form=self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            self.context['form']=form
            return render(request,self.template_name,self.context)

class BookView(TemplateView):
    model=Book
    template_name = 'book/detail.html'
    context={}
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs['id'])
        self.context['book']=book
        return render(request,self.template_name,self.context)

class BookDelete(TemplateView):
    model=Book
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs['pk'])
        book.delete()
        return redirect('list')
