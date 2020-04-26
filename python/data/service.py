class Port:
    name = None
    node_port = None
    port = None
    target_port = None

    def __init__(self, port_json):
        self.name = port_json.name
        self.node_port = port_json.node_port
        self.port = port_json.port
        self.target_port = port_json.target_port

    def get_port_info(self):
        print("%20s%20s%20s%20s" %
              (self.name, self.node_port, self.port, self.target_port))


class Service:
    service_name = None
    namespace = None
    ports = []

    def __init__(self, service_json):
        self.service_name = service_json.metadata.name
        self.namespace = service_json.metadata.namespace
        for i in service_json.spec.ports:
            self.ports.append(Port(port_json=i))

    def get_ports(self):
        for port in self.ports:
            port.get_port_info()
