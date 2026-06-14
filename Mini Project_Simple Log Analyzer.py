#Day 5 Mini Project: Simple Log Analyzer
def analyze_log(file_name):
    errors = 0
    warnings = 0
    info = 0

    with open(file_name, "r") as f:
        for line in f:
            if "ERROR" in line:
                errors += 1
            elif "WARNING" in line:
                warnings += 1
            elif "INFO" in line:
                info += 1

    # Write summary to a new file
    with open("summary.txt", "w") as f:
        f.write(f"Errors: {errors}\n")
        f.write(f"Warnings: {warnings}\n")
        f.write(f"Info: {info}\n")

    print("Analysis complete. Summary written to summary.txt")


# --- Example usage ---
# Create a sample log file
with open("system.log", "w") as f:
    f.write("INFO: System started\n")
    f.write("WARNING: Low memory\n")
    f.write("ERROR: Disk not found\n")
    f.write("INFO: User login\n")
    f.write("ERROR: Timeout occurred\n")

# Run analyzer
analyze_log("system.log")
