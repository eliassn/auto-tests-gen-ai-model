import os
import glob

CYPRESS_TEST_DIR = "/Users/dev/Documents/youslide/tests/cypress/support"

OUTPUT_FILE = "data/raw/cypress_tests.txt"

def extract_test_cases():
    test_cases = []
    
    print(f"Searching for Cypress test files in: {CYPRESS_TEST_DIR}")

    test_files = glob.glob(os.path.join(CYPRESS_TEST_DIR, "**/*.js"), recursive=True)

    print(f"Found {len(test_files)} test files:")
    for file in test_files:
        print(f" - {file}")

    if not test_files:
        print("❌ No test files found! Check your folder structure or file extensions.")
        return

    for file_path in test_files:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            test_cases.append(content)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(test_cases))

    print(f"✅ Extracted {len(test_cases)} test cases into {OUTPUT_FILE}")

if __name__ == "__main__":
    extract_test_cases()
