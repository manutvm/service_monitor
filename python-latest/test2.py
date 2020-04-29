from kubernetes import client, config
import re
from utils.url_utils import get_url_contents
import sys
from data.objects import Service


def initialize_kube_connection(connection_type):
    if connection_type == "in_cluster":
        config.load_incluster_config()
    elif connection_type == "out_cluster":
        config.load_kube_config()


def service_monitor():
    v1 = client.CoreV1Api()
    services_list = []
    current_namespace = open(
        "/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()

    services = v1.list_namespaced_service(namespace=current_namespace).items
    for service in services:
        services_list.append(Service(service_meta=service))

    for service in services_list:
        service.get_service_details()
        service.check_service_status()

if __name__ == "__main__":
    initialize_kube_connection(connection_type=sys.argv[1])
    service_monitor()
