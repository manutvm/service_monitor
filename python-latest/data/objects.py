from utils.url_utils import get_url_contents
from utils.json_utils import parse_json_data


class Service:
    service_name = None
    namespace = None
    service_url = None
    actuator_port = None

    def __init__(self, service_meta):
        self.service_name = service_meta.metadata.name
        self.namespace = service_meta.metadata.namespace

        for port in service_meta.spec.ports:
            url = "http://%s.%s.svc.cluster.local:%s/actuator/health" % (
                self.service_name, self.namespace, port.port)
            response_code, response_message = get_url_contents(url=url)

            if response_code != 200:
                continue
            else:
                self.service_url = url
                self.actuator_port = port.port

    def get_service_details(self):
        print("Service Name: %s" % (self.service_name))
        print("Namespace: %s" % (self.namespace))
        print("Service URL: %s" % (self.service_url))
        print("Service port: %s" % (self.actuator_port))

    def check_dependant_svc_status(self, service_name, service_url):
        actuator_ep = "%s/actuator/health" % (service_url)
        response_code, response_message = get_url_contents(url=actuator_ep)
        json_response = parse_json_data(json_data=response_message)

        if json_response is not None and json_response["status"] != "UP":
            print("Dependant Service %s is not running. Need to restart the dependant service" % (
                service_name))
        else:
            print("Dependant Service %s is running fine. Seems like the problem with Actual service %s" % (
                service_name, self.service_name))

    def check_service_status(self):
        response_code, response_message = get_url_contents(
            url=self.service_url)

        json_response = parse_json_data(json_data=response_message)
        if json_response is None:
            return

        for dependant_svc in json_response["details"]:
            if json_response["details"][dependant_svc]["status"] != "UP":
                dependant_svc_url = json_response["details"][dependant_svc]["%s.url" % (
                    dependant_svc)]
                check_dependant_svc_status(
                    service_name=dependant_svc, service_url=dependant_svc_url)
            else:
                continue
