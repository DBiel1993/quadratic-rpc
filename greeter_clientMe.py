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

"""The Python implementation of the gRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

# Function to run the gRPC client.
def run():
    print("Will try to greet world ...")
    # Establish a connection to the gRPC server at localhost on port 50051.
    with grpc.insecure_channel("localhost:50051") as channel:
        # Create a stub (client) for the Greeter service.
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        # Call the SayHello method on the stub with a HelloRequest containing the name 'you'.
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="Dylan Bielser"))
    # Print the response from the server.
    print("Greeter client received: " + response.message)

# Main entry point of the script.
if __name__ == "__main__":
    logging.basicConfig()  # Configure logging.
    run()  # Run the client.