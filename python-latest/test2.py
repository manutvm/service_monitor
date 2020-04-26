from kubernetes import client, config
import re
from utils.url_utils import get_url_contents
from utils.json_utils import parse_json

config.load_incluster_config()
# config.load_kube_config()

v1 = client.CoreV1Api()
namespaces = v1.list_namespace().items

for namespace in namespaces:
    if re.match("^kube|^default|^elastic|^prometheus|^velero", namespace.metadata.name):
        continue
    namespace_name = namespace.metadata.name

    print(namespace_name)
    services = v1.list_namespaced_service(namespace=namespace_name).items
    for service in services:
        service_url = None
        response_message = None
        print(service.metadata.name)
        for port in service.spec.ports:
            # print("%20s%20s%20s%20s" % (port.name, port.port,
            #                             port.node_port, port.target_port))
            url = "http://%s.%s.svc.cluster.local:%s/actuator/health" % (
                service.metadata.name, service.metadata.namespace, port.port)
            response_code, response_message = get_url_contents(url=url)
            if response_code != 200:
                continue
            else:
                service_url = url
                break
        print(service_url)
        json_object = parse_json(response_message)
        if json_object is None:
            continue
        try:
            print(json_object["details"].keys())
        except KeyError:
            print(json_object["components"].keys())
