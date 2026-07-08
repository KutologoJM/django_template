"""
Automatically resolves to an input or output serializer based on the action.

Priority:
  1. Per-action override via `serializer_classes` dict
  2. `input_serializer_class` for write actions
  3. `output_serializer_class` for read actions
  4. Falls back to `serializer_class`

Usage:
    class MyViewSet(MultiSerializerMixin, ModelViewSet):
        input_serializer_class = MyModelInputSerializer
        output_serializer_class = MyModelOutputSerializer

    # Or with per-action overrides:
    class MyViewSet(MultiSerializerMixin, ModelViewSet):
        input_serializer_class = MyModelInputSerializer
        output_serializer_class = MyModelOutputSerializer
        serializer_classes = {
            "some_custom_action": MySpecialSerializer,
        }
"""


class MultiSerializerMixin:
    action: str
    serializer_class: type

    input_serializer_class = None
    output_serializer_class = None
    serializer_classes = {}

    WRITE_ACTIONS = frozenset({"create", "update", "partial_update", "destroy"})
    READ_ACTIONS = frozenset({"list", "retrieve"})

    def get_serializer_class(self):
        # 1. Per-action override
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]

        # 2. Auto-resolve write → input
        if self.action in self.WRITE_ACTIONS and self.input_serializer_class:
            return self.input_serializer_class

        # 3. Auto-resolve read → output
        if self.action in self.READ_ACTIONS and self.output_serializer_class:
            return self.output_serializer_class

        # 4. DRF default
        return super().get_serializer_class()
