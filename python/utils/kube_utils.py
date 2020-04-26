from kubernetes import client, config
from data.namespace import Namespace
from data.service import Service

kube_client = None
services = []
namespaces = []


class Kube:
    def __init__(self):
        config.load_kube_config()
        self.kube_client = client.CoreV1Api()

        for namespace_json in self.kube_client.list_namespace().items:
            namespaces.append(Namespace(namespace_json=namespace_json))

        for service_json in self.kube_client.list_service_for_all_namespaces().items:
            services.append(Service(service_json=service_json))

    def get_namespace_services(namespace):
        services = kube_client.get_namespace_services(namespace=namespace)
        return services

    def get_namespaces(self):
        for namespace in namespaces:
            print(namespace.get_namespace_name())
