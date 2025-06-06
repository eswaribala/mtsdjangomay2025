from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from employee.models import Employee



@registry.register_document
class EmployeeDocument(Document):

    class Index:
        name = "mts_employee2025"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "salary"
        ]

