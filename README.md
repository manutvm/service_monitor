# Prototype of Service Dependancy Monitor

Each microoservice is dependant on another microservice in the namespace. The microservices are contacting each other using the service name. For example, if a microservice interaction-layer having a depenancy on marketdata-service in master namespace, it contacts the service via marketdata-service.master.svc.cluster.local DNS entry which is resolved by Core DNS. If the market data service is not reachable, then we need to restart the pod associated with marketdata-service. We can probe

## Steps(Python Kubernetes Implementation):
1. START
2. Get all the namespaces in the cluster(excpet kube-system, kube-public, kube-node-lease, default and velero). We use python kubernetes API client.CoreV1Api().list_namespaces() function for this purpose.
```python
namespaces = v1.list_namespace().items

for namespace in namespaces:
    if re.match("^kube|^default|^elastic|^prometheus|^velero", namespace.metadata.name):
        continue
    namespace_name = namespace.metadata.name
```
3. Start Loop
4. Iterate for all the services namespace wise using the namespace name fetched from Steps(2)
```python
services = v1.list_namespaced_service(namespace=namespace_name).items
    for service in services:
```
5. Start Loop
6. Iterate over all service port and found the port having /actuator/health endpoint. Fetch the service_url variable with the correct service URL.
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
7. Parse the URL and get the JSON response.
8. Find the dependant services by parsing the Node `details` or `components`
```python
try:
    print(json_object["details"].keys())
except KeyError:
    print(json_object["components"].keys())
```
9. Iterate over all dependant services and it's component status.
10. If dependant services are running check the next service from step(6)
11. If the dependant service is not running, 