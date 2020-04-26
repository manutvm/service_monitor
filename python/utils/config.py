import yaml


class Config:
    service_list = None
    check_interval = None

    def __init__(self):
        with open("cfg/config.yaml") as cfg_file:
            yaml_file = yaml.load(stream=cfg_file, Loader=yaml.FullLoader)
            self.service_list = yaml_file['frp']['services']
            self.check_interval = yaml_file['frp']['checkinterval']


    def get_service_list(self):
        return self.service_list

    def get_check_interval(self):
        return self.check_interval
