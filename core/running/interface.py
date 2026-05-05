#!/usr/bin/env python3

"""
AION Interface Layer
-------------------
Human ↔ System interaction
Non-blocking, inspectable, minimal assumptions
"""

import time
import json
import os
from datetime import datetime

STATE_FILE = "aion_state.json"
COMMAND_FILE = "aion_command.json"


def read_state():
    if not os.path.exists(STATE_FILE):
        return None
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def send_command(command: dict):
    command["timestamp"] = datetime.utcnow().isoformat()
    with open(COMMAND_FILE, "w") as f:
        json.dump(command, f, indent=2)


def print_state(state):
    print("\n--- AION STATE SNAPSHOT ---")
    for k, v in state.items():
        print(f"{k}: {v}")
    print("---------------------------\n")


def interface_loop():
    print("\nAION INTERFACE ONLINE")
    print("Commands: status | pause | resume | set <key> <value> | quit\n")

    while True:
        try:
            user_input = input("AION> ").strip()

            if user_input == "quit":
                send_command({"type": "shutdown"})
                print("Shutdown signal sent.")
                break

            elif user_input == "status":
                state = read_state()
                if state:
                    print_state(state)
                else:
                    print("No state available.")

            elif user_input == "pause":
                send_command({"type": "pause"})

            elif user_input == "resume":
                send_command({"type": "resume"})

            elif user_input.startswith("set"):
                _, key, value = user_input.split(maxsplit=2)
                send_command({
                    "type": "set_parameter",
                    "key": key,
                    "value": value
                })

            else:
                print("Unknown command.")

            time.sleep(0.1)

        except KeyboardInterrupt:
            print("\nDetaching interface (AION continues).")
            break


if __name__ == "__main__":
    interface_loop()
