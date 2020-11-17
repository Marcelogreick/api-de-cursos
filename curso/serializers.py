from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Rating
        fields = (
            'id',
            'curso',
            'name',
            'email',
            'comments',
            'rating',
            'creation',
            'active'
        )

    def validade_rating(self, valor):
        if valor in range(1, 6):
            return valor
        return serializers.ValidationError('De 1 a 5 apenas')


class CursoSerializer(serializers.ModelSerializer):
    # rating = RatingSerializer(many=True, read_only=True)

    # rating = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rating-detail')

    rating = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_ratings = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'title',
            'url',
            'creation',
            'active',
            'rating',
            'media_ratings'
        )

    def get_media_ratings(self, obj):
        media = obj.rating.aggregate(Avg('rating')).get('rating__avg')

        if media is None:
            return 0
        return round(media * 2) / 2
