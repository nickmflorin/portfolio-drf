from rest_framework import serializers


class PortfolioSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', )

    def __init__(self, *args, **kwargs):
        super(PortfolioSerializer, self).__init__(*args, **kwargs)

        context = kwargs.get('context')
        if context:
            collapsed = context.get('collapsed')
            if collapsed is False:
                extended_fields = getattr(self.Meta, 'extended_fields', {})
                for k, v in extended_fields:
                    if isinstance(v, tuple):
                        self.fields[k] = v[0](context=kwargs['context'], **v[1])
                    else:
                        self.fields[k] = v(context=kwargs['context'])

    def to_representation(self, instance):
        if self.context.get('collapsed') is True:
            collapsed_serializer = getattr(self.Meta, 'collapsed', None)
            if collapsed_serializer:
                return collapsed_serializer(instance).data
        return super(PortfolioSerializer, self).to_representation(instance)


class HorizonSerializer(PortfolioSerializer):
    start_month = serializers.IntegerField()
    end_month = serializers.IntegerField()
    start_year = serializers.IntegerField()
    end_year = serializers.IntegerField()
    current = serializers.BooleanField()

    class Meta:
        fields = PortfolioSerializer.Meta.fields + (
            'start_month', 'end_month', 'start_year', 'end_year', 'current')
