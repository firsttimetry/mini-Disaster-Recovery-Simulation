# Mini Cloud Disaster Recovery System

A lightweight Python simulation that demonstrates a basic cloud disaster recovery mechanism. It monitors system memory, simulates data backup when a fault is detected, encrypts the backup, and allows manual restoration when the system is recovered.

**Note:** This project was built with the help of ChatGPT for learning purposes. I'm currently studying how the system works and how it can be extended further.

**Note:** I have kept the maximum threashold as 10% of memory to simulate it in my computer. 

## What It Does

-  **Monitors system memory usage** using `psutil`
-  **Simulates a disaster** if memory exceeds a threshold (e.g., 10%)
-  **Encrypts** data from a simulated primary server and **moves it to backup**
-  **Logs** all events to `fault_ledger.txt` (both console & file)
-  **Restores** the last encrypted data upon user confirmation using ROT13 decryption

##  Tech Stack

| Tool       | Purpose                                      |
|------------|----------------------------------------------|
| Python     | Core programming                             |
| psutil     | System resource monitoring                   |
| simpy      | Event-based simulation environment           |
| logging    | Logs events to console and file              |
| codecs     | Basic encryption with ROT13 (for simulation) |

## Project Structure

mini-cloud-disaster-recovery-system/
├── disaster_recovery.py # Main script
├── primary_server.txt # Simulated primary server data
├── backup_server.txt # Backup server for encrypted data
├── fault_ledger.txt # Logs of faults & recovery
├── requirements.txt # Dependencies
└── README.md 

## Setup & Installation

### 1. Install Dependencies

pip install psutil simpy

### 2. Create Input Files

echo "Critical configuration and data..." > primary_server.txt
touch backup_server.txt

### 3. Run the Program

python3 disaster_recovery.py

### 4. Simulate Recovery

When prompted:
Is Server 1 restored? (yes/no):
Type yes to simulate a successful restoration of the server.

### How Encryption Works
This project uses ROT13 as a placeholder encryption method:

ROT13 shifts each letter 13 places in the alphabet

It's not secure, but useful to demonstrate the backup-encrypt-restore cycle

I will later replace it with AES or Fernet for real encryption.

### Log Output
All system events are logged in fault_ledger.txt:

2025-07-27 10:00:00 - INFO - Memory Usage: 12%
2025-07-27 10:00:00 - CRITICAL - Memory limit exceeded! Simulating disaster...
2025-07-27 10:00:01 - CRITICAL - Disaster simulated! Encrypted data moved from primary_server.txt to backup_server.txt.
2025-07-27 10:00:10 - INFO - Server 1 restored! Moving the exact last copied data back.
2025-07-27 10:00:11 - INFO - Recovery successful! Decrypted data restored to primary_server.txt.

### Learning Outcomes
This project is helping me explore:

Cloud fault tolerance concepts
Disaster recovery strategies
Encryption basics (e.g., ROT13 as a learning placeholder)
Logging and event-driven simulation
File operations in Python

### Future Improvements
Replace ROT13 with secure encryption (e.g., AES)
Add automated fault injection
GUI for fault monitoring and recovery
Trigger backup for CPU/network thresholds
Deploy to a cloud test environment (e.g., Azure VM simulation)

### Author Notes
This is a learning project created with guidance from ChatGPT. I plan to improve it by diving deeper into Python concurrency, encryption, and cloud automation concepts. Any suggestions or contributions are welcome!
