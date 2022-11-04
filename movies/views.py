from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django_filters import rest_framework as filters
from .models import Movie
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from rest_framework.permissions import IsAuthenticated
# Removes permissions from views


class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_queryset(self):
        if self.request.method != 'GET':
            self.queryset = Movie.objects.filter(creator=self.request.user)
        return super().get_queryset()
