#Transaction Validator
import csv
import logging

# Configure logging
logging.basicConfig(
    filename="transaction_log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class TransactionError(Exception):
    """Custom exception for critical transaction issues"""
    pass

def validate_transaction(transaction):
    try:
        amount = float(transaction["amount"])
        status = transaction["status"]

        if amount < 0:
            logging.warning(f"Negative amount detected: {transaction}")
        
        if status not in ["SUCCESS", "FAILED", "PENDING"]:
            raise TransactionError(f"Invalid status: {status}")

        logging.info(f"Transaction validated: {transaction}")

    except ValueError:
        logging.error(f"Invalid amount format: {transaction}")
    except TransactionError as e:
        logging.critical(f"Critical error: {e}")
        raise

def process_transactions(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            validate_transaction(row)

if __name__ == "__main__":
    try:
        process_transactions("transactions.csv")
    except Exception as e:
        logging.critical(f"Program terminated due to: {e}")
