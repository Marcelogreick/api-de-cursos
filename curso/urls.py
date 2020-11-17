from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CursoAPIView,
    CursosAPIView,
    RatingAPIView,
    RatingsAPIView,
    CursoViewSet,
    RatingViewSet,
)

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/ratings', RatingsAPIView.as_view(), name='curso_ratings'),
    path('cursos/<int:curso_pk>/ratings/<int:rating_pk>/', RatingAPIView.as_view(), name='curso_rating'),

    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    path('ratings/<int:rating_pk>/', RatingAPIView.as_view(), name='rating'),
]
