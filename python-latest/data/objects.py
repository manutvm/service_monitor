from utils.url_utils import get_url_contents


class Service:
    service_name = None
    namespace = None
    service_url = None
    dependant_service_list = []

    def __init__(self, service_json):
        self.service_name = service_json.metadata.name
        self.namespace = service_json.metadata.namespace

        for port in service_json.spec.ports:
            url = "http://%s.%s.svc.cluster.local:%s/actuator/health" % (
                self.service_name, self.namespace, port.port)
            response_code, response_message = get_url_contents(url=url)

            if response_code != 200:
                continue
            else:
                self.service_url = url

    def get_service_details(self):
        print("Service Name: %s" % (self.service_name))
        print("Namespace: %s" % (self.namespace))
        print("Service URL: %s" % (self.service_url))

    def check_service_status(self):
        self.get_service_details()
        if self.service_url is not None:
            response_code, response_message = get_url_contents(
                url=self.service_url)
            if response_code == 200:
                