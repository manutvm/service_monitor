from kubernetes import config, client


class Kube:
    kube_client = None
    kube_namespaces = None
    kube_services = None
    kube_namespaced_services = {}

    def __init__(self):
        config.load_kube_config()
        self.kube_client = client.CoreV1Api()
        service_list = self.kube_client.list_service_for_all_namespaces()
        for service in service_list.items:
            self.kube_namespaced_services[service.metadata.namespace] = service

    def get_services(self, namespace):
        return self.kube_namespaced_services[namespace]


class ServiceMonitor():
    kube_client = None
    kube_services = None

    def __init__(self):
        self.kube_client = Kube()

    def get_namespaced_services(self, namespace):
        for service in self.kube_client.get_services(namespace=namespace):
            print(service.metadata.name)


if __name__ == "__main__":
    ServiceMonitor().get_namespaced_services(namespace="master")
