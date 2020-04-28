#from utils.json_utils import parse_json_file
#
#
# with open("sample.json") as fl:
#
#     data = parse_json_file(json_data=fl)
#

#
# for component in data['details']:
#
#     print("%30s%20s" % (component, data['details'][component]['status']))
#

from kubernetes import client,config

config.load_kube_config()
config.load_incluster_config()

v1=client.CoreV1Api()
print(v1.read_namespace(name=name).items)

svc=v1.list_namespaced_service(namespace="master")

print(svc.items[10].spec.cluster_ip)
