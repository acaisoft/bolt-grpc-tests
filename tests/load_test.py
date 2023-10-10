import grpc_user
from locust import task

import api_pb2_grpc, api_pb2


class ApiGrpcUser(grpc_user.GrpcUser):
    stub_class = api_pb2_grpc.ApiStub

    @task
    def TriggerCounter(self):
        self.stub.TriggerCounter(api_pb2.ApiRequest(value=None))

    @task
    def GetCounter(self):
        self.stub.GetCounter(api_pb2.ApiRequest(value=None))

    @task
    def ResetCounter(self):
        self.stub.ResetCounter(api_pb2.ApiRequest(value=None))
