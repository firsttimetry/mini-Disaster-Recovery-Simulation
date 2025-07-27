import simpy
import psutil
import time
import logging
import sys
import codecs

# Setup Logging (Logs to both Console & File)
FAULT_LEDGER = "fault_ledger.txt"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Logs to console
        logging.FileHandler(FAULT_LEDGER, mode='a', encoding='utf-8')  # Logs to file
    ]
)

# Thresholds for Disaster Recovery
MEMORY_THRESHOLD = 10  # Memory usage in %
CHECK_INTERVAL = 3      # Time interval for monitoring

# Server File Simulation
PRIMARY_SERVER = "primary_server.txt"
BACKUP_SERVER = "backup_server.txt"

# --------------------- ENCRYPTION & DECRYPTION ---------------------
def encrypt(data):
    """Encrypts data using ROT13."""
    return codecs.encode(data, 'rot_13')

def decrypt(data):
    """Decrypts data using ROT13."""
    return codecs.decode(data, 'rot_13')

# --------------------- BACKUP MECHANISM ---------------------
def simulate_disaster(source, destination):
    """Moves encrypted data from source to destination and logs the event."""
    try:
        with open(source, "r") as src:
            data = src.read().strip()

        if data:
            encrypted_data = encrypt(data)  # Encrypt before storing

            with open(destination, "a") as dest:
                dest.write(encrypted_data + "\n")  # Save encrypted data

            with open(source, "w") as src:
                src.write("")  # Clear primary server after copying

            log_msg = f" Disaster simulated! Encrypted data moved from {source} to {destination}."
            logging.critical(log_msg)
            sys.stdout.flush()  # Force log display

        else:
            logging.info(f"No data in {source} to move.")

    except Exception as e:
        logging.error(f" Error simulating disaster: {e}")

# --------------------- RESTORATION MECHANISM ---------------------
def restore_from_backup(source, destination):
    """Restores decrypted data back to the primary server and removes it from backup."""
    try:
        with open(source, "r") as src:
            backup_data = src.readlines()

        if backup_data:
            last_encrypted_data = backup_data[-1].strip()  # Get the last encrypted data
            decrypted_data = decrypt(last_encrypted_data)  # Decrypt it

            with open(destination, "a") as dest:
                dest.write(decrypted_data + "\n")  # Restore decrypted data

            # Remove only the restored line from backup
            with open(source, "w") as src:
                src.writelines(backup_data[:-1])  # Remove last line

            log_msg = f" Recovery successful! Decrypted data restored to {destination}."
            logging.info(log_msg)
            logging.info(f"🗑️ Deleted restored data from {source}.")
            sys.stdout.flush()  # Ensure logs appear immediately

        else:
            logging.info(" No stored data to restore.")

    except Exception as e:
        logging.error(f" Error restoring data: {e}")

    logging.info(" Simulation completed. Exiting...")
    sys.stdout.flush()
    sys.exit(0)  # Exit the program after recovery

# --------------------- USER-INPUT RECOVERY ---------------------
def ask_for_recovery():
    """Waits for user confirmation to restore the last moved data."""
    while True:
        user_input = input("Is Server 1 restored? (yes/no): ").strip().lower()
        if user_input == "yes":
            logging.info(" Server 1 restored! Moving the exact last copied data back.")
            restore_from_backup(BACKUP_SERVER, PRIMARY_SERVER)
            break
        else:
            logging.warning(" Server 1 is still down. Checking again in 2 seconds...")
            time.sleep(2)

# --------------------- FAULT DETECTION & MONITORING ---------------------
def monitor_resources(env):
    """Monitors system resources and triggers disaster recovery if needed."""
    while True:
        memory_usage = psutil.virtual_memory().percent
        logging.info(f" Memory Usage: {memory_usage}%")

        if memory_usage > MEMORY_THRESHOLD:
            logging.critical(" Memory limit exceeded! Simulating disaster...")
            simulate_disaster(PRIMARY_SERVER, BACKUP_SERVER)

            # Ask for recovery confirmation
            ask_for_recovery()

        yield env.timeout(CHECK_INTERVAL)

# --------------------- SIMULATION SETUP ---------------------
env = simpy.Environment()
env.process(monitor_resources(env))

logging.info(" Starting Cloud Disaster Recovery Simulation...")
env.run()
