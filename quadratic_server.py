# Import necessary modules
from concurrent import futures
import logging
import grpc
import quadratic_pb2  # Import the generated code from the .proto file
import quadratic_pb2_grpc  # Import the generated gRPC code from the .proto file
import math  # Import the math module to perform mathematical operations

# Define the QuadraticSolverServicer class
# This class implements the methods defined in the .proto file for the gRPC service
class QuadraticSolverServicer(quadratic_pb2_grpc.QuadraticSolverServicer):
    # Implement the Solve method defined in the .proto file
    # This method takes a QuadraticRequest and returns a QuadraticResponse
    def Solve(self, request, context):
        # Extract the coefficients a, b, and c from the request
        a, b, c = request.a, request.b, request.c
        
        # Calculate the discriminant of the quadratic equation
        discriminant = b**2 - 4*a*c
        
        # Determine the number of real roots based on the discriminant
        if discriminant < 0:
            solution = "No real roots"  # No real roots if the discriminant is less than 0
        elif discriminant == 0:
            root = -b / (2*a)  # One real root if the discriminant is 0
            solution = f"One real root: {root}"
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)  # Calculate the first root
            root2 = (-b - math.sqrt(discriminant)) / (2*a)  # Calculate the second root
            solution = f"Two real roots: {root1} and {root2}"  # Two real roots if the discriminant is greater than 0
        
        # Return the solution as a QuadraticResponse
        return quadratic_pb2.QuadraticResponse(solution=solution)

# Define the serve function to start the gRPC server
def serve():
    # Create a gRPC server with a thread pool to handle multiple requests concurrently
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add the QuadraticSolverServicer to the server
    quadratic_pb2_grpc.add_QuadraticSolverServicer_to_server(QuadraticSolverServicer(), server)
    
    # Bind the server to port 50051 to listen for requests
    server.add_insecure_port('[::]:50051')
    
    # Start the server
    server.start()
    print("Server started, listening on port 50051")
    
    # Keep the server running and wait for termination
    server.wait_for_termination()

# Main entry point of the script
if __name__ == "__main__":
    logging.basicConfig()  # Configure logging
    serve()  # Start the gRPC server