from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Resume


@registry.register_document
class ResumeDocument(Document):
    full_name = fields.TextField(attr="full_name")
    text = fields.TextField(attr="text")  # text of the resume

    class Index:
        name = 'resumes'  # Name of the Elasticsearch index

    class Django:
        model = Resume  # The model associated with this Document
        fields = [  # The fields of the model you want to be indexed in Elasticsearch
            'first_name',
            'last_name',
        ]
