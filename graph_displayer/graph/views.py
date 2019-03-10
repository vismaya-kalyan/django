from django.shortcuts import render
from django.contrib import messages
from .models import Post


import networkx as nx


def home(request):
    if request.method == "POST":

        nodes = request.POST.get('nodes_count','')
        obj = Post(count = nodes)
        obj.save()
        if obj:
            messages.success(request, f'No. of nodes: { obj }')
            return render(request, 'graph/sol.html',{'count': obj })
      
        
    return render(request, 'graph/home.html',{'title':'Graphs'})
       