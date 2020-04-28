from kubernetes import client, config
import re
from utils.url_utils import get_url_contents
from utils.json_utils import parse_json

function check_service_status(service_name,cluster_ip)
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
            continue

        for dep_service in json_object["details"]:
            dep_serv_name = dep_service
            dep_serv_status = json_object["details"][dep_service]['status']
            print("%30s%20s" %
                  (dep_service, dep_serv_status)

            if dep_serv_status != "UP":
                check_service_status(service_name=dep_serv_name,)
