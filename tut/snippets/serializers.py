from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

# class SnippetSerializer(serializers.Serializer):
#     # The first part of the serializer class defines the fields that get serialized/deserialized
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


#     # The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()
#     def create(self, validate_date):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validate_date)


#     def update(self, instance, validate_date):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validate_data.get('title', instance.title)
#         instance.code = validate_date.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validate_date.get('language', instance.language)
#         instance.style = validate_date.get('style', instance.style)
#         instance.save()
#         return instance