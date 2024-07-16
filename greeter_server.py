# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The Python implementation of the gRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

# Define the Greeter class, which implements the generated GreeterServicer class from the .proto file.
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    # Implement the SayHello method defined in the .proto file.
    def SayHello(self, request, context):
        # Create a HelloReply message with a greeting.
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

# Function to start the gRPC server.
def serve():
    port = "50051"  # Define the port on which the server will listen for requests.
    # Create a gRPC server with a thread pool to handle multiple requests concurrently.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add the Greeter service to the server.
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    # Bind the server to the specified port.
    server.add_insecure_port("[::]:" + port)
    # Start the server.
    server.start()
    print("Server started, listening on " + port)
    # Keep the server running and waiting for termination.
    server.wait_for_termination()

# Main entry point of the script.
if __name__ == "__main__":
    logging.basicConfig()  # Configure logging.
    serve()  # Start the server.