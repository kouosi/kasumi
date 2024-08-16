#!/usr/bin/env python3

import argparse
from server import createApp

def runServer(port: int):
    print("Running the server...")
    server_app = createApp()
    server_app.run(debug=True, port=port)

def runClient():
    print("Running the client...")


def main():
    parser = argparse.ArgumentParser(description="A simple script to run both server and client.")
    parser.add_argument('--run-server', '-s', action='store_true', help='Run the server[DEFAULT]')
    parser.add_argument('--run-client', '-c', action='store_true', help='Run the client')
    parser.add_argument('--port', '-p', type=int, default=5003, help='Port number for the server (default: 5003)')
    args = parser.parse_args()

    if args.run_server:
        runServer(args.port)
    elif args.run_client:
        runClient()
    else:
        runServer(args.port)

if __name__ == "__main__":
    main()
