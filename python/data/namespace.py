class Namespace:
    namespace_name = None

    def __init__(self, namespace_json):
        self.namespace_name = namespace_json.metadata.name

    def get_namespace_name(self):
        return self.namespace_name