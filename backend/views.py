from django.http.response import HttpResponseRedirect, JsonResponse
from rest_framework import viewsets, permissions
from .serializer import DictionarySerializer
from .models import Dictionary
from rest_framework.decorators import api_view



class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [permissions.IsAuthenticated]
    

@api_view
def word_detail(request, pk):
    if request.method == 'GET':
        sample = Dictionary.objects.all()
        word = request.GET.get(pk=pk)
        if word is not None:
            sample = sample.filter(word = word)
        else:
            word = HttpResponseRedirect("https://api.dictionaryapi.dev/api/v2/entries/en/").get(pk=pk)
            sample.create(word)
            sample.save()
            return sample
        
        serializer = DictionarySerializer(sample, many= True)
        return JsonResponse(serializer.data, safe=False)
