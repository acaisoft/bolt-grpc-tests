from __future__ import print_function

import logging

import grpc

import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
proto_directory = os.path.join(current_directory, 'pb')
sys.path.append(proto_directory)

from pb import api_pb2
from pb import api_pb2_grpc


def run():
    with grpc.insecure_channel("34.29.250.204:50051") as channel:
        stub = api_pb2_grpc.ApiStub(channel)
        response = stub.TriggerCounter(api_pb2.ApiRequest(value=None))
        print(f"received: {response.value}")

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = api_pb2_grpc.ApiStub(channel)
        response = stub.GetCounter(api_pb2.ApiRequest(value=None))
        print(f"received: {response.value}")

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = api_pb2_grpc.ApiStub(channel)
        response = stub.ResetCounter(api_pb2.ApiRequest(value=None))
        print(f"received: {response.message}")


if __name__ == "__main__":
    logging.basicConfig()
    run()

