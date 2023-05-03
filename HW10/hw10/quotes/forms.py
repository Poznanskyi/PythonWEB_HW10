from django.forms import ModelForm, CharField, TextInput, ModelMultipleChoiceField, SelectMultiple, ModelChoiceField, \
    DateField, SelectDateWidget, Select
from .models import Quote, Author, Tag


class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput())
    tag = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'), required=True, widget=SelectMultiple())
    author = ModelChoiceField(queryset=Author.objects.all().order_by('name'), required=True, widget=Select)

    class Meta:
        model = Quote
        fields = ['quote', 'tag', 'author']


class AuthorForm(ModelForm):
    name = CharField(min_length=2, required=True, widget=TextInput())
    born_date = CharField(required=True, widget=TextInput())
    born_location = CharField(max_length=250, required=True, widget=TextInput())
    description = CharField(min_length=2, widget=TextInput())

    class Meta:
        model = Author
        fields = ['name', 'born_date', 'born_location', 'description']


class TagForm(ModelForm):
    name = CharField(max_length=255, widget=TextInput)

    class Meta:
        model = Tag
        fields = ['name']