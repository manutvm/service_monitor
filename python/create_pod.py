from kubernetes import client, config


def list_pods(v1):
    print("\nListing pods in namespace: default")
    ret = v1.list_namespaced_pod(namespace="default")
    for i in ret.items:
        print("%s  %s  %s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


config.load_incluster_config()

pod = client.V1Pod()
v1 = client.CoreV1Api()

container = client.V1Container(name="busybox")
container.image = "busybox"
container.args = ["sleep", "3600"]
container.name = "busybox"

spec = client.V1PodSpec(containers=[container])
pod.metadata = client.V1ObjectMeta(name="busybox")

pod.spec = spec

list_pods(v1)

v1.create_namespaced_pod(namespace="default", body=pod)

list_pods(v1)
v1.delete_namespaced_pod(
    name="busybox", namespace="default", body=client.V1DeleteOptions())