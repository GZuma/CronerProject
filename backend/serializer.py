from rest_framework import serializers
from .models import Dictionary

# It will take in the Dictionay object as its 
# argument an returns the serialized data

class DictionarySerializer(serializers.Serializer):
    word = serializers.CharField()
    phonetics = serializers.JSONField()
    meanings = serializers.JSONField()
    class Meta:
        model = Dictionary
        fields = ['word','phonetics','meanings']

    def create(self, validated_data):
        return Dictionary(**validated_data)
    
    def update(self, instance, validated_data):
        instance.word = validated_data.get('word', instance.word)
        instance.phonetics = validated_data.get('phonetics', instance.phonetics)
        instance.meanings = validated_data.get('meanings', instance.meanings)
        return instance
    
   



    

   