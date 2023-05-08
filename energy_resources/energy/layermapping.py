from django.contrib.gis.utils.layermapping import LayerMapError


class CustomLayerMapping(LayerMapError):
    def __init__(self, *args, **kwargs):
        self.last_user_id = kwargs.pop('last_user_id', None)
        super(CustomLayerMapping, self).__init__(*args, **kwargs)

        def feature_kwargs(self, feature):
            kwargs = super(CustomLayerMapping, self).feature_kwargs(feature)
            kwargs['last_user_id'] = self.last_user_id
            return kwargs

