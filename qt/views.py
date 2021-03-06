from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import *
from models import Nonconformity
from pprint import pprint


def hp(request):
    return render_to_response('hp.html', {}, context_instance=RequestContext(request))

def backlog(request):
    return render_to_response('backlog.html', {}, context_instance=RequestContext(request))

def nonconformities(request):
    nc_list = Nonconformity.objects.all()
    if request.GET:
        search_form = NcSearchForm(request.GET)
        if search_form.is_valid():
            nc_list = nc_list.filter(status__in=search_form.cleaned_data['status'])
    else:
        search_form = NcSearchForm()
    return render_to_response(
        'nonconformities.html',
        {'list':nc_list, 'search_form':search_form},
        context_instance=RequestContext(request)
    )


def nc_add(request):
    if request.POST:
        print request.user
        form = NcAddForm(request.POST)
        if form.is_valid():
            nc = form.save(commit=False)
            nc.author = request.user
            nc.save()
            return render_to_response('popin/close_ok.html', {
                'text':'Nonconfirmity added',
                'update_function':"update_new('/nc/line/%s/');" % nc.id,
                }, context_instance=RequestContext(request))
    else:
        form = NcAddForm()
    return render_to_response('popin/form.html', {
        'form':form,
        'action':'/nc/add/',
        'title':'Add nonconfirmity',
    }, context_instance=RequestContext(request))

def nc_edit(request, nc_id):
    nc = Nonconformity.objects.get(id=nc_id)
    if request.POST:
        form = NcEditForm(request.POST, instance=nc)
        if form.is_valid():
            form.save()
            return render_to_response('popin/close_ok.html', {
                'text':'Nonconfirmity saved',
                'update_function':"update_item('/nc/line/%s/','#nc_item_%s');" % (nc.id, nc.id),
                }, context_instance=RequestContext(request))
    else:
        form = NcEditForm(instance=nc)
    return render_to_response('popin/form_nc_edit.html', {
        'form':form,
        'action':'/nc/edit/%s/' % nc_id,
        'title':'Edit nonconfirmity #%s' % nc.id,
        }, context_instance=RequestContext(request))

def nc_line(request, nc_id):
    return render_to_response('nc_line.html', {
        'item':Nonconformity.objects.get(id=nc_id),
        }, context_instance=RequestContext(request))

