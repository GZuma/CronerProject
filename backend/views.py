from django.http.response import HttpResponseRedirect, JsonResponse
from rest_framework import viewsets, permissions
from .serializer import DictionarySerializer
from .models import Dictionary
from rest_framework.decorators import api_view

class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # I think that this the way to redirect the request if the word is 
    # not in the Dictionary model.  I understand that it should take in the 
    # request, see if it is a 'GET', if it is in the model then just return
    # if not then it needs to make a 'GET' request from 
    # https://api.dictionaryapi.dev/api/v2/entries/en/
    # I am not sure that this is the way that it should be done
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
