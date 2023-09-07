import json
import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

channel = grpc.insecure_channel("localhost:30018")
stub = location_pb2_grpc.LocationServiceStub(channel)

def sendmsg(person_id, lat, lon):
    """Send gRPC Location Message"""
    location = location_pb2.LocationMessage(
        person_id=person_id,
        latitude=lat,
        longitude=lon
    )

    response = stub.Create(location)
    print(response)


stub.Get(location_pb2.Empty())

sendmsg(36, 41.9, -87.7)





