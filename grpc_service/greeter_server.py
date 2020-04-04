from concurrent import futures
import grpc
import time
import helloworld_pb2
import helloworld_pb2_grpc
import requests
import json

def getIP():
    ip= requests.get("https://api.ipify.org/?format=json")
    ip=json.loads(ip.text)
    return ip['ip']

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        responseMsg="127.0.0.1"
        name=request.name
        if(name=='ip'):
            responseMsg=getIP()
        return helloworld_pb2.HelloReply(message='IP, %s!' % responseMsg)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()