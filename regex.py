import re
import os

# ✅ Define file path (modify if needed)
file_path = "row.txt"

# ✅ Check if file exists before proceeding
if not os.path.exists(file_path):
    print("\n❌ Error: File 'row.txt' not found! Please check the file path.\n")
    exit()  # Stop execution if file is missing

# ✅ Read file content with UTF-8 encoding
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# ✅ Debugging: Print confirmation that file was read successfully
print("\n✅ File read successfully!\n")

# 🔹 Function to print solutions with better formatting
def print_solution(ex_num, description, result):
    print(f"\n🔹 Solution for Exercise {ex_num}: {description}")
    print("-------------------------------------------------")
    print(result if result else "⚠️ No matches found!")
    print("-------------------------------------------------\n")

# ✅ 1. Match string with 'a' followed by zero or more 'b's
pattern1 = r"ab*"
matches1 = re.findall(pattern1, content)
print_solution(1, "'a' followed by zero or more 'b's", matches1)

# ✅ 2. Match string with 'a' followed by two to three 'b's
pattern2 = r"ab{2,3}"
matches2 = re.findall(pattern2, content)
print_solution(2, "'a' followed by 2 to 3 'b's", matches2)

# ✅ 3. Find sequences of lowercase letters joined with an underscore
pattern3 = r"\b[a-z]+_[a-z]+\b"
matches3 = re.findall(pattern3, content)
print_solution(3, "Lowercase words joined by underscore", matches3)

# ✅ 4. Find sequences of one uppercase letter followed by lowercase letters
pattern4 = r"\b[A-Z][a-z]+\b"
matches4 = re.findall(pattern4, content)
print_solution(4, "One uppercase letter followed by lowercase letters", matches4)

# ✅ 5. Match string with 'a' followed by anything, ending in 'b'
pattern5 = r"a.*b"
matches5 = re.findall(pattern5, content)
print_solution(5, "'a' followed by anything, ending in 'b'", matches5)

# ✅ 6. Replace spaces, commas, and dots with a colon ':'
pattern6 = r"[ ,.]"
modified_text6 = re.sub(pattern6, ":", content)
print_solution(6, "Replacing spaces, commas, and dots with ':'", modified_text6[:500])  # Print first 500 chars

# ✅ 7. Convert snake_case to camelCase
def snake_to_camel(text):
    return re.sub(r"_(\w)", lambda m: m.group(1).upper(), text)

matches7 = [snake_to_camel(match) for match in matches3]
print_solution(7, "Converting snake_case to camelCase", matches7)

# ✅ 8. Split a string at uppercase letters
pattern8 = r"(?=[A-Z])"
split_text8 = re.split(pattern8, content)
print_solution(8, "Splitting at uppercase letters", split_text8[:20])  # Show first 20 results

# ✅ 9. Insert spaces between words starting with capital letters
pattern9 = r"([a-z])([A-Z])"
modified_text9 = re.sub(pattern9, r"\1 \2", content)
print_solution(9, "Inserting spaces before capital letters", modified_text9[:500])  # Print first 500 chars

# ✅ 10. Convert camelCase to snake_case
def camel_to_snake(text):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", text).lower()

matches10 = [camel_to_snake(match) for match in re.findall(r"\b[A-Za-z]+(?:[A-Z][a-z]*)+\b", content)]
print_solution(10, "Converting camelCase to snake_case", matches10)
