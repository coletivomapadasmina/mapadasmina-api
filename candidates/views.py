from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from candidates.models import Candidate, Party
from candidates.serializers import CandidateSerializer, PartySerializer

@csrf_exempt
def candidate_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def candidate_detail(request, pk):
    """
    Retrieve, update or delete a code candidate.
    """
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CandidateSerializer(candidate)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(candidate, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        candidate.delete()
        return HttpResponse(status=204)

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer