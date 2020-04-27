# Prototype of Service Dependancy Monitor

Each microoservice is dependant on another microservice in the namespace. The microservices are contacting each other using the service name. For example, if a microservice interaction-layer having a depenancy on marketdata-service in master namespace, it contacts the service via marketdata-service.master.svc.cluster.local DNS entry which is resolved by Core DNS. If the market data service is not reachable, then we need to restart the pod associated with marketdata-service. We can probe

## Steps(Python Kubernetes Implementation):
1. START
1. Get all the namespaces in the cluster(excpet kube-system, kube-public, kube-node-lease, default and velero). We use python kubernetes API client.CoreV1Api().list_namespaces() function for this purpose.
```python
namespaces = v1.list_namespace().items

for namespace in namespaces:
    if re.match("^kube|^default|^elastic|^prometheus|^velero", namespace.metadata.name):
        continue
    namespace_name = namespace.metadata.name
```
1. Start Loop
1. Iterate for all the services namespace wise using the namespace name fetched from Steps(2)
```python
services = v1.list_namespaced_service(namespace=namespace_name).items
    for service in services:
```
1. Start Loop
1. Iterate over all service port and found the port having /actuator/health endpoint. Fetch the service_url variable with the correct service URL.
```python
for port in service.spec.ports:
    url = "http://%s.%s.svc.cluster.local:%s/actuator/health" % (
        service.metadata.name, service.metadata.namespace, port.port)
    response_code, response_message = get_url_contents(url=url)
    if response_code != 200:
        continue
    else:
        service_url = url
        break
```
1. End Loop (5)
1. 
