"""
Author: Omar-Bounawara
Round Robin CPU Scheduling Algorithm

This program simulates the Round Robin CPU scheduling algorithm. It defines functions for creating processes,
checking process arrivals, and executing processes. The main program initializes a set of processes and runs the
Round Robin algorithm on them, displaying the execution order in a table.

"""

# Function to create a process dictionary
def create_process(process_name, arrival_time, burst_time):
    """
    Create a dictionary representing a process with attributes:
    - process_name: Process name
    - arrival_time: Arrival time of the process
    - burst_time: Burst time (time required for execution) of the process
    """
    return {"process_name": process_name, 'arrival_time': arrival_time, "burst_time": burst_time}


# Function to check for process arrivals
def check_arrival(current_time, process_list, queue):
    """
    Check for processes that have arrived at the given time and add them to the queue.
    """
    for process in process_list:
        if process.get("arrival_time") == current_time:
            queue.append(process)


# Function to execute processes using the Round Robin algorithm
def execute_process(current_time, time_quantum, queue, execution_order):
    """
    Execute processes using the Round Robin scheduling algorithm.
    """
    current_process = queue.pop(0)
    remaining_time = current_process.get("burst_time")

    if remaining_time > time_quantum:
        for _ in range(time_quantum):
            execution_order.append(current_process.get("process_name"))
            current_time += 1
            check_arrival(current_time, process_list, queue)

        current_process["burst_time"] -= time_quantum
        queue.append(current_process)
    else:
        for _ in range(remaining_time):
            execution_order.append(current_process.get("process_name"))
            current_time += 1
            check_arrival(current_time, process_list, queue)

        current_process["burst_time"] = 0

    return current_time


# Main Program
print("Round Robin CPU Scheduling Algorithm")

# Initialize global variables
process_list = [
    create_process("p1", 0, 5),
    create_process("p2", 1, 3),
    create_process("p3", 3, 6),
    create_process("p4", 5, 1),
    create_process("p5", 6, 4)
]
time_quantum = 3
execution_order = []
current_time = 0
process_queue = []

# Main loop
while process_queue or any(process.get("burst_time") > 0 for process in process_list):
    check_arrival(current_time, process_list, process_queue)
    current_time = execute_process(current_time, time_quantum, process_queue, execution_order)

# Display the execution order
print("\nExecution Table:")
print("Time (t) | Process")
print("------------------")
i = 0
for process in execution_order:
    print(f"{i} | {process}")
    i += 1
