from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()
config.load_incluster_config()
v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret_services = v1.list_namespaced_service(namespace="manu")

for i in ret_services.items:
    service_name = i.metadata.name
    namespace = i.metadata.namespace
    print("%20s%20s" % ("Namespace", "Service Name"))
    print("%20s%20s" % (namespace, service_name))
    print("%20s %10s %10s %10s" %
              ("Name", "Node Port", "Port", "Target Port"))
    for j in i.spec.ports:
        print("%20s %10s %10s %10s" %
              (j.name, j.node_port, j.port, j.target_port))