def fcfs_scheduling(processes):
    current_time = 0
    waiting_time = 0
    for process in processes:
        if process['arrival_time'] > current_time:
            current_time = process['arrival_time']
        waiting_time += current_time - process['arrival_time']
        current_time += process['burst_time']
    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time

# Example usage:
num_processes = int(input("Enter the number of processes: "))
processes = []

for i in range(num_processes):
    name = input(f"Enter the name of process {i + 1}: ")
    arrival_time = int(input(f"Enter the arrival time for process {name}: "))
    burst_time = int(input(f"Enter the burst time for process {name}: "))
    processes.append({'name': name, 'arrival_time': arrival_time, 'burst_time': burst_time})

average_waiting_time = fcfs_scheduling(processes)
print(f"Average Waiting Time: {average_waiting_time}")
