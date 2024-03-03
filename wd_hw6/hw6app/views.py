from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from .models import Tree
import json


def index(request):
    return JsonResponse({
        "info": "Welcome to the Tree API.",
        "endpoints": {
            "1": "get tree : Display list of trees ",
            "2": "get tree/:id : View tree profile",
            "3": "post tree/ : Create a new tree",
            "4": "delete tree/:id : Delete a tree"
        }
    })


class TreeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=10)

    class Meta:
        model = Tree
        fields = ["id", "height", "age", "typeOf"]


@csrf_exempt
def tree_main(request):
    if request.method == 'GET':
        trees = Tree.objects.all()
        serializer = TreeSerializer(trees, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in request body"}, status=400)
        serializer = TreeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400, safe=False)


@csrf_exempt
def tree_by_id(request, pk):
    tree = get_object_or_404(Tree, pk=pk)
    serializer = TreeSerializer(tree)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def tree_delete(request, pk):
    tree = get_object_or_404(Tree, pk=pk)
    tree.delete()
    return JsonResponse({'success': 'Tree deleted successfully'}, status=204, safe=False)
