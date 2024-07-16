# Import the grpc library for making gRPC calls
import grpc

# Import the generated protobuf classes and gRPC classes
import quadratic_pb2
import quadratic_pb2_grpc

# Define the main function to run the client
def run():
    # Create an insecure channel to communicate with the gRPC server
    # 'localhost:50051' indicates the server is running on the local machine on port 50051
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client) to call methods on the QuadraticSolver service
        # The stub is generated from the .proto file and provides methods for each RPC defined in the service
        stub = quadratic_pb2_grpc.QuadraticSolverStub(channel)
        
        # Define the coefficients of the quadratic equation
        # These are example values for the quadratic equation ax^2 + bx + c = 0
        a, b, c = 1.0, -3.0, 2.0
        
        # Create a QuadraticRequest message with the coefficients
        # This message is sent to the server
        request = quadratic_pb2.QuadraticRequest(a=a, b=b, c=c)
        
        # Call the Solve method on the stub with the request message
        # The server will process the request and return a QuadraticResponse message
        response = stub.Solve(request)
        
        # Print the solution returned by the server
        # The solution is a string describing the roots of the quadratic equation
        print("Quadratic equation solution: " + response.solution)

# If this script is run directly (not imported), execute the run function
if __name__ == "__main__":
    run()