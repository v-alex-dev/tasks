from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Task
from .serializers import TaskSerializer

class TaskFilter(filters.FilterSet):
    completed = filters.BooleanFilter(field_name='completed', lookup_expr='exact')
    due_date = filters.DateFilter(field_name='due_date', lookup_expr='lte')
    
    class Meta:
        model = Task
        fields = ['completed', 'due_date']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = TaskFilter  # Intégration du filtrage

    def perform_create(self, serializer):
        # Assigne l'utilisateur connecté à la tâche
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        """
        Exemple de filtrage dynamique, tu pourrais ajouter plus de filtres
        en fonction des besoins comme l'utilisateur connecté.
        """
        return super().get_queryset()

