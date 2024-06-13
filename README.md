# Integrity-Checker-Simple-Code

**REQUIRMENTS & INSTALLATIONS (Libraries):
**
1.)Haslib

    pip install hashlib

2.) os   
    
    pip install os-sys

3.) Json 

    pip install jsonpython

**Execution Process:**

Directory Input:

The program will prompt you to enter the path of the directory you want to check. Ensure the path is correct and that the directory exists.
Menu Selection:

The program displays a menu with three options:

    Select an option:
    1. Generate Report
    2. Check Integrity
    3. Compare Reports
   
**Option 1:** Generate Report:

If you choose option 1, the program will generate a report of the current state (hashes) of all files in the specified directory and save it to integrity_report_old.json.
The report generation status will be displayed.

**Option 2:** Check Integrity:

If you choose option 2, the program first generates a new report (integrity_report_new.json) of the current state of the files.
It then compares this new report with the old report (integrity_report_old.json) to check if any files have been modified or are missing.
It will print out the status of the integrity check, indicating any issues.

**Option 3:** Compare Reports:

If you choose option 3, the program compares two reports (integrity_report_old.json and integrity_report_new.json).
It prints out any discrepancies, such as missing files, hash mismatches, or new files.

Continue or Exit:

After completing the selected operation, the program asks if you want to continue running the program:

    Do you want to continue (yes(y)/no(n))?
    Enter yes, y, no, or n to continue or exit.
