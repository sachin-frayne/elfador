# Elfador - ELasticsearch FAke Data generatOR

from elasticsearch import Elasticsearch, helpers
from random import getrandbits, randint
from ipaddress import IPv4Address
from essential_generators import DocumentGenerator
from faker import Faker

bulk_request_size = 10
number_of_bulk_requests = 10
random_number_limit = 1000
index = "index"

elasticsearch_password = ""
elasticsearch_url = "http://localhost:9200"
elasticsearch_user = ""
verify_certs=False

elastic = Elasticsearch([elasticsearch_url],http_auth=(elasticsearch_user, elasticsearch_password),verify_certs=verify_certs)
gen = DocumentGenerator()
fake = Faker()

for value in range(0, number_of_bulk_requests):
    actions = [
        {
            "text_field": gen.sentence(),
            "number_field": randint(0, random_number_limit),
            "keyword_field": gen.word(),
            "ip_field": str(IPv4Address(getrandbits(32))),
            "date_field": fake.date_time_between(start_date='-14d', end_date='now')
        }
        for doc in range(bulk_request_size)
    ]

    response = helpers.bulk(elastic, actions, index=index)
