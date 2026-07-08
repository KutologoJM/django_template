from drf_spectacular.openapi import AutoSchema


class MultiSerializerAutoSchema(AutoSchema):

    def get_request_serializer(self):
        view = self.view
        if hasattr(view, 'input_serializer_class'):
            return view.input_serializer_class()
        return super().get_request_serializer()

    def get_response_serializers(self):
        view = self.view
        if hasattr(view, 'output_serializer_class'):
            return view.output_serializer_class()
        return super().get_response_serializers()
