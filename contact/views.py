from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import ContactModelForm
from .models import Contact



class ContactCreateView(View):
    template_name = 'contact/contact_create.html'

    def get(self, request, *args, **kwargs):
        form = ContactModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class ContactListView(View):
    template_name= 'contact/contact_list.html'
    queryset = Contact.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'object_list': self.get_queryset})


class MyListView(ContactListView):
    queryset = Contact.objects.filter(id=1)


class ContactView(View):
    template_name = 'contact/contact_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Contact, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #    return render(request, 'about.html', {})


# class ContactView(View):
#     template_name = 'Contact.html'
#     def get(self, request, *args, **kwargs):
#         return (render(request, self.template_name, {}))


class ContactUpdateView(View):
    template_name = 'contact/contact_update.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Contact, id=id)
        return obj

    def get(self, request, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ContactModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ContactModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class ContactDeleteView(View):
    template_name = 'contact/contact_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Contact, id=id)
        return obj

    def get(self, request, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = obj
            return redirect('/contact/')
        return render(request, self.template_name, context)