import os
import time

def create_child_processes(num_processes):
    for _ in range(num_processes):
        pid = os.fork()
        if pid == 0:
            # Дочерний процесс
            print(f"Child process PID: {os.getpid()}")
            time.sleep(60)  # Процесс будет жить 60 секунд
            os._exit(0)
        else:
            # Родительский процесс
            print(f"Created child process with PID: {pid}")

if __name__ == "__main__":
    create_child_processes(20)
