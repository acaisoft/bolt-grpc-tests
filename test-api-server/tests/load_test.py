import grpc_user
from locust import task
import sys
import os
from pathlib import Path

current_directory = Path(os.path.dirname(os.path.abspath(__file__))).parent.absolute()
proto_directory = os.path.join(current_directory, 'pb')
sys.path.append(proto_directory)

from pb import api_pb2_grpc, api_pb2


class ApiGrpcUser(grpc_user.GrpcUser):
    port = os.getenv("PORT", "50051")
    target_host = os.getenv("HOST", "34.29.250.204")
    host = f"{target_host}:{port}"
    stub_class = api_pb2_grpc.ApiStub

    @task
    def setValue(self):
        self.stub.SetValue(api_pb2.ApiRequest(value="Test"))
