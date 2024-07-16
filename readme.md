# How this works: This program implements a gRPC service that solves quadratic equations. It consists of a server and a client. The server, implemented in quadratic_server.py, listens for incoming gRPC requests and computes the roots of a quadratic equation based on the coefficients provided by the client. It uses the quadratic formula to determine the roots and returns the result. The client, implemented in quadratic_client.py, connects to the server via a gRPC channel, sends the coefficients of the quadratic equation, and receives the solution. The client then prints the solution, which includes the roots of the equation. The project also involves generating necessary gRPC code from a .proto file that defines the service and message formats used for communication between the client and server.

# gRPC Quadratic Equation Solver

This project demonstrates a simple gRPC service that solves quadratic equations. The server receives coefficients from the client, computes the solution, and returns it to the client.

## Prerequisites

- Python 3.x
- `grpcio` and `grpcio-tools` packages

## Setup and Running the Program

### 1. Install gRPC and Protocol Buffers

To install the necessary gRPC packages, run:

```sh
pip install grpcio grpcio-tools

### 2. Install gRPC and Protocol Buffers

 # Navigate to the project directory and generate the gRPC code from the .proto file:

### 3. Start the gRPC Server

python quadratic_server.py

### 4. Run the gRPC Client

python quadratic_client.py


### Output

Quadratic equation solution: Two real roots: 2.0 and 1.0

### Quadratic equation:  quadratic equation 1.0x^2 - 3.0x + 2.0 = 0

When we say the roots of the quadratic equation  1.0x^2 - 3.0x + 2.0 = 0  are 2.0 and 1.0, it means that these values of  x  satisfy the equation. In other words, if you substitute  x = 2.0  or  x = 1.0  into the equation, the left-hand side of the equation will equal zero. Therefore, the roots of the equation are 2.0 and 1.0.


```
