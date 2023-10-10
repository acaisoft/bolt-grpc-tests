import grpc_user
from locust import task
import os
from urllib.parse import urlparse

import api_pb2_grpc, api_pb2


class ApiGrpcUser(grpc_user.GrpcUser):
    port = os.getenv("PORT", "50051")
    target_host = urlparse(os.getenv("HOST", "34.29.250.204"))
    stub_class = api_pb2_grpc.ApiStub

    @task
    def TriggerCounter(self):
        self.stub.TriggerCounter(api_pb2.ApiRequest(value=None))
