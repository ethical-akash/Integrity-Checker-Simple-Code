import hashlib
import os
import json




def calculate_hash(file_path, block_size=65536):
    """Calculate the hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(block_size)
    return hasher.hexdigest()




def generate_report(directory, report_file):
    """Generate a report for the integrity of files in a directory."""
    report = {}
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_hash(file_path)
            report[file_path] = file_hash

    # Save the report to a JSON file
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=4)

    return f"Report generated successfully at {report_file}"




def check_integrity(directory, old_report_file, new_report_file):
    """Check the integrity of files in a directory by comparing old and new reports."""
    if not os.path.exists(old_report_file) or not os.path.exists(new_report_file):
        return "Error: Integrity report files not found."

    with open(old_report_file, 'r') as f:
        old_report = json.load(f)

    with open(new_report_file, 'r') as f:
        new_report = json.load(f)




    print("Checking integrity...")
    integrity_ok = True
    for file_path, old_hash in old_report.items():
        new_hash = new_report.get(file_path)
        if new_hash is None:
            print(f"File missing: {file_path}")
            integrity_ok = False
        elif old_hash != new_hash:
            print(f"Integrity issue: {file_path}")
            integrity_ok = False




    if integrity_ok:
        print("Integrity: OK")
    else:
        print("Integrity Break")




def compare_reports(old_report_file, new_report_file):
    """Compare two integrity reports file by file."""
    if not os.path.exists(old_report_file) or not os.path.exists(new_report_file):
        return "Error: Integrity report files not found."

    with open(old_report_file, 'r') as f:
        old_report = json.load(f)

    with open(new_report_file, 'r') as f:
        new_report = json.load(f)

    print("Comparing reports...")
    integrity_ok = True
    



    # Compare files present in the old report
    for file_path, old_hash in old_report.items():
        new_hash = new_report.get(file_path)
        if new_hash is None:
            print(f"File missing in new report: {file_path}")
            integrity_ok = False
        elif old_hash != new_hash:
            print(f"Hash mismatch for file: {file_path}")
            integrity_ok = False




    # Check for any new files added in the new report
    for file_path, new_hash in new_report.items():
        if file_path not in old_report:
            print(f"New file found in report: {file_path}")
            integrity_ok = False

    if integrity_ok:
        print("Integrity: OK")
    else:
        print("Integrity Break!")





# Function to display menu and get user choice
def display_menu():

    print("Select an option:")
    print("1. Generate Report")
    print("2. Check Integrity")
    print("3. Compare Reports")
    choice = input("Enter your choice (1, 2, or 3): ")
    
    return choice




if __name__ == "__main__":
    while True:
        while True:
            directory = input("Enter directory path: ")

            if not os.path.exists(directory):
                print("Error: Directory does not exist.")
                continue
            break

        old_report_file = "integrity_report_old.json"
        new_report_file = "integrity_report_new.json"

        choice = display_menu()

        if choice == "1":
            print(generate_report(directory, old_report_file))


        elif choice == "2":

            # Generate new report before checking integrity
            print(generate_report(directory, new_report_file))

            # Check integrity
            check_integrity(directory, old_report_file, new_report_file)

            
        elif choice == "3":
            compare_reports(old_report_file, new_report_file)


        else:
            print("Invalid choice. Please select 1, 2, or 3.")


        
        # Ask if the user wants to continue running the program


        while True:
            continue_option = input("Do you want to continue (yes(y)/no(n))? ").lower()
            if continue_option in ["yes", "no","y","n"]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if continue_option == "no" or "n":
            print("Exiting the program...")
            break
