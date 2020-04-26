from utils.json_utils import parse_json

json_object=parse_json("""
{"status":"UP","details":{"instrumentService":{"status":"UP","details":{"instrument.service.url":"http://instrument-management-service:8080"}},"computationService":{"status":"UP","details":{"computation.service.url":"http://computation-service:8080"}},"portfolioService":{"status":"UP","details":{"portfolioService.url":"http://portfolio-service:8080"}},"replicationService":{"status":"UP","details":{"replication.service.url":"http://replication-service:8080"}},"diskSpace":{"status":"UP","details":{"total":124693463040,"free":72352378880,"threshold":10485760}},"refreshScope":{"status":"UP"},"hystrix":{"status":"UP"}}}
""")

print(json_object["details"].keys())