import threading
import time
import random

NUMPHIL = 5
LEFT = lambda i: (i - 1 + NUMPHIL) % 5
RIGHT = lambda i: (i + 1) % 5

# Enum for states
THINKING, HUNGRY, EATING = range(3)

# Initialize semaphores
mutex = threading.Lock()
forks = [threading.Semaphore(1) for _ in range(NUMPHIL)]

def think(id):
    think_time = random.randint(1, 3)
    print(f"Philosopher {id} is thinking for {think_time} seconds")
    time.sleep(think_time)
    print(f"Philosopher {id} reappears from sleep from thinking")

def pickup_forks(id):
    global mutex
    global forks

    mutex.acquire()
    state[id] = HUNGRY
    print(f"Philosopher {id} is hungry and trying to pick up forks")
    mutex.release()

    forks[id].acquire()
    forks[RIGHT(id)].acquire()
    forks[LEFT(id)].acquire()

    mutex.acquire()
    state[id] = EATING
    print(f"Philosopher {id} is allowed to eat now")
    mutex.release()

def eat(id):
    eating_time = random.randint(1, 3)
    print(f"Philosopher {id} is eating for {eating_time} seconds")
    time.sleep(eating_time)
    print(f"Philosopher {id} reappears from sleep from eating")

def return_forks(id):
    global forks
    global mutex

    forks[id].release()
    forks[RIGHT(id)].release()
    forks[LEFT(id)].release()

    mutex.acquire()
    state[id] = THINKING
    print(f"Philosopher {id} has put down forks")
    mutex.release()

def philosopher(num):
    global state

    id = num[0]

    while True:
        think(id)
        pickup_forks(id)
        eat(id)
        return_forks(id)

# Initialize states and philosopher threads
state = [THINKING] * NUMPHIL
philosophers = [threading.Thread(target=philosopher, args=([i],)) for i in range(NUMPHIL)]

if __name__ == "__main__":
    for phil in philosophers:
        phil.start()

    for phil in philosophers:
        phil.join()
