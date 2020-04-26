class Service:
    service_name = None
    namespace = None

    def __init__(self, service_json):
        service_name = service_json.metadata.name
        namespace = service_json.metadata.namespace
        