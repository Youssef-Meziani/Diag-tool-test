import tabulate
import kubernetes
import argparse
from argparse import Namespace, _MutuallyExclusiveGroup

parser = argparse.ArgumentParser()
group: _MutuallyExclusiveGroup = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-o", "--ocid", type=str, help="The Kafka Cluster OCID to diagnose")
group.add_argument("-n", "--namespace", type=str, help="The Kafka Cluster Namespace to diagnose")
args: Namespace = parser.parse_args()


print("Hello from the python script")
