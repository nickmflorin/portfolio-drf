from rest_framework import serializers


class PortfolioSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        fields = ('id', 'date_created', 'date_modified')


class HorizonSerializer(PortfolioSerializer):
    start_month = serializers.IntegerField()
    end_month = serializers.IntegerField()
    start_year = serializers.IntegerField()
    end_year = serializers.IntegerField()
    current = serializers.BooleanField()

    class Meta:
        fields = PortfolioSerializer.Meta.fields + (
            'start_month', 'end_month', 'start_year', 'end_year', 'current')
