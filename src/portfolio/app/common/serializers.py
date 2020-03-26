from rest_framework import serializers


class PortfolioSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', )


class HorizonSerializer(PortfolioSerializer):
    start_month = serializers.IntegerField()
    end_month = serializers.IntegerField()
    start_year = serializers.IntegerField()
    end_year = serializers.IntegerField()
    current = serializers.BooleanField()

    class Meta:
        fields = PortfolioSerializer.Meta.fields + (
            'start_month', 'end_month', 'start_year', 'end_year', 'current')
