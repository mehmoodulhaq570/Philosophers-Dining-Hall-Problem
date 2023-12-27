import threading
import time
import random

NUMPHIL = 5
num_iterations = 1
LEFT = lambda i: (i - 1 + NUMPHIL) % 5
RIGHT = lambda i: (i + 1) % 5

state = [0] * NUMPHIL
identity = [0, 1, 2, 3, 4]
lock = threading.Lock()
cond = [threading.Condition(lock) for _ in range(NUMPHIL)]

def think(id):
    think_time = random.randint(1, 3)
    print(f"Philosopher {id} is thinking for {think_time} seconds")
    time.sleep(think_time)
    print(f"Philosopher {id} reappears from sleep from thinking")

def pickup_forks(id):
    left = LEFT(id)
    right = RIGHT(id)
    with lock:
        state[id] = 1  # HUNGRY

        while state[id] == 1 and (state[left] == 2 or state[right] == 2):
            print(f"Philosopher {id} is hungry and waiting to pick up forks to eat")
            cond[id].wait()

        if state[id] == 1:
            state[id] = 2  # EATING
            print(f"Philosopher {id} is allowed to eat now")

def eat(id):
    eating_time = random.randint(1, 3)
    print(f"Philosopher {id} is eating for {eating_time} seconds")
    time.sleep(eating_time)
    print(f"Philosopher {id} reappears from sleep from eating")

def return_forks(id):
    left = LEFT(id)
    right = RIGHT(id)
    with lock:
        state[id] = 0  # THINKING

        print(f"Philosopher {id} has put down forks")
        cond[left].notify()
        print(f"Philosopher {id} signaled philosopher {left} to see if it can eat")
        cond[right].notify()
        print(f"Philosopher {id} signaled philosopher {right} to see if it can eat")

def philosopher(num, iterations):
    id = num
    for _ in range(iterations):
        think(id)
        pickup_forks(id)
        eat(id)
        return_forks(id)


if __name__ == "__main__":
    philosophers = [threading.Thread(target=philosopher, args=(i, num_iterations)) for i in range(NUMPHIL)]

    for phil in philosophers:
        phil.start()

    for phil in philosophers:
        phil.join()
