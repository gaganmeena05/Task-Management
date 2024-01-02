from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskLists(APIView):
        
    def get(self, request, format=None):
        data = Task.objects.all()
        serializer = TaskSerializer(data, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TaskActions(APIView):

    def get(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        if task is not None:
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=200)
        return render(request, '404 page.html', status=404)

    def put(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        if task is not None:
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        return render(request, '404 page.html', status=404)

    def delete(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        if task is not None:
            task.delete()
            return Response({'Deletion successfull'}, status=204)
        return render(request, '404 page.html', status=404)