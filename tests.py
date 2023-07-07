from datetime import datetime
from constants import *
from tcompress import is_existing, list_files
from helpers import list_visible_folders

number_of_tests = 0
number_of_successful_tests = 0

def record_test_results(failures):
    """
    Tracks the test results in a logs file.

    Args:
        results (int): The number of test failures.

    Returns:
        None
    """
    now = datetime.now()
    hour = now.strftime("%H")
    dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
    time = dt_string.split(" ")[0]
    date = dt_string.split(" ")[1]

    if failures == 1:
        failures = str(failures) + " Failure"
    elif failures == 0:
        failures = str("No Failures")
    else:
        failures = str(failures) + " Failures"
    with open(logs_file, "a") as file:
        if int(hour) == 5:
            file.write(
                "{:<15s} {:<15s} {:<15s} {:<15s}\n".format(
                    time, date, "Automated", failures
                )
            )
        else:
            file.write(
                "{:<15s} {:<15s} {:<15s} {:<15s}\n".format(
                    time, date, "Manual", failures
                )
            )

def validate_path_existence(path):
    """
    Validates the existence of a path.

    Args:
        path (str): The path to validate.

    Returns:
        None
    """
    global number_of_tests
    global number_of_successful_tests
    try:
        if is_existing(path):
            print("Test " + str(number_of_tests) + ": Passed\n")
            number_of_successful_tests += 1
        else:
            raise Exception("Test " + str(number_of_tests) + ": Failed\n")
    except Exception as e:
        print(e)
    number_of_tests += 1

def test_folder_for_files(folder_path):
    """
    Tests if a folder contains any files.

    Args:
        folder_path (str): The path of the folder to test.

    Returns:
        None
    """
    global number_of_tests
    global number_of_successful_tests
    try:
        list_of_files = list_files(folder_path)
        if len(list_of_files) == 0:
            print("Test " + str(number_of_tests) + ": Passed\n")
            number_of_successful_tests += 1
        else:
            raise Exception("Test " + str(number_of_tests) + ": Failed\n")
    except Exception as e:
        print(e)
    number_of_tests += 1

def validate_folder_structure(folder_path, original_folders):
    """
    Validates the folder structure by checking if the visible folders match the original folders.

    Args:
        folder_path (str): The path of the folder to validate.
        original_folders (list): A list of original folder paths.

    Returns:
        None
    """
    global number_of_tests
    global number_of_successful_tests
    try:
        visible_folders = list_visible_folders(folder_path)
        for folder in visible_folders:
            if folder not in original_folders:
                raise Exception("Test " + str(number_of_tests) + ": Failed\n")
        print("Test " + str(number_of_tests) + ": Passed\n")
        number_of_successful_tests += 1
    except Exception as e:
        print(e)
    number_of_tests += 1


def get_results():
    return number_of_tests - number_of_successful_tests


def run_tests():
    folders_to_test = [
        (root, "root directory"),
        (desktop, "'Desktop' folder"),
        (documents, "'Documents' folder"),
        (downloads, "'Downloads' folder"),
        (developer, "'Developer' folder"),
        (icloud_drive, "'iCloud Drive' folder"),
    ]

    for folder_path, folder_name in folders_to_test:
        print(f"Checking if there are any files in the {folder_name}")
        test_folder_for_files(folder_path)

    folders_to_validate = [
        (root, root_folders, "root directory"),
        (desktop, desktop_folders, "'Desktop' folder"),
        (documents, documents_folders, "'Documents' folder"),
        (downloads, downloads_folders, "'Downloads' folder"),
        (icloud_drive, icloud_drive_folders, "'iCloud Drive' folder")
    ]

    for folder_path, original_folders, folder_name in folders_to_validate:
        print(f"Checking if there are any archived folders in the {folder_name}")
        validate_folder_structure(folder_path, original_folders)

    paths_to_validate = [
        (root, "root directory"),
        (desktop, "'Desktop' folder"),
        (documents, "'Documents' folder"),
        (downloads, "'Downloads' folder"),
        (developer, "'Developer' folder"),
        (icloud_drive, "'iCloud Drive' folder"),
        (desktop_folders[0], "'CS 146' folder"),
        (system_applications_file, "'system.txt' file"),
        (downloaded_applications_file, "'downloaded.txt' file"),
        (logs_file, "'logs' file")
    ]

    for path, path_name in paths_to_validate:
        print(f"Checking if {path_name} still exists")
        validate_path_existence(path)

    results = get_results()
    print("\n" + str(results) + " tests failed.\n\n")
    record_test_results(results)
    return results