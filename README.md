# Dining Philosophers Problem in Python

This repository contains a Python implementation of the Dining Philosophers problem. The Dining Philosophers problem is a classic synchronization and concurrency problem that explores challenges in resource sharing among multiple processes or threads.

## Contributors

- Mehmood Ul Haq
- Muhammad Shahzaib
- Kashif Muneer
- Talal Muzammil

## Problem Description

- There are five philosophers sitting around a dining table.
- Each philosopher thinks and eats spaghetti.
- To eat, a philosopher must have two forks (one on the left and one on the right).
- There is a single fork between each pair of adjacent philosophers.
- Philosophers must pick up both forks to eat and put them down when they're done.

## Implementation

The Python implementation in this repository uses threading and synchronization techniques to solve the Dining Philosophers problem. It includes a solution that avoids deadlock and starvation.

## Solution to the problem

The dining philosopher’s problem is a typical synchronization problem. A group of philosophers is sitting around a dining table, and in front of each philosopher having a bowl of spaghetti. Between each pair of adjacent philosophers is a fork. The problem is to construct a solution that avoids deadlock and resource contention.
Here's a representation of a solution:
## 1.	Concurrency and Threading:
  •	The code represents each philosopher as an individual thread, allowing multiple philosophers to execute concurrently.
  
  •	The threading module is utilized for creating and managing threads.
## 2.	Resource Allocation and Synchronization:
  •	The code employs a locking mechanism (threading.Lock) to ensure mutual exclusion, preventing multiple philosophers from accessing shared resources simultaneously.
  
  •	Conditions (threading.Condition) are used to coordinate the synchronization between philosophers, allowing them to communicate and signal each other based on their states.
## 3.	Philosopher States:
  •	The state of each philosopher is represented by the state list, where 0 indicates thinking, 1 indicates being hungry, and 2 indicates eating.
  
  •	Transitions between states are managed to prevent conflicts and ensure that no two adjacent philosophers are eating at the same time.

For issues or feedback, please contact me at mehmodulhaq1040@gmail.com.

