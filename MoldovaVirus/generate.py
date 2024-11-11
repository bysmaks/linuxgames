import os
import random
import string

def random_filename():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def create_random_directory(base_path, depth, text_index, text):
    if depth == 0:
        return text_index

    dir_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    dir_path = os.path.join(base_path, dir_name)
    os.makedirs(dir_path, exist_ok=True)

    if text_index < len(text):
        file_path = os.path.join(dir_path, str(random_filename()))
        with open(file_path, 'w') as f:
            f.write(f"{text_index}\n{text[text_index]}")
        text_index += 1

    for _ in range(random.randint(1, 3)):
        text_index = create_random_directory(dir_path, depth - 1, text_index, text)

    return text_index

def main():
    base_path = './challenge'
    os.makedirs(base_path, exist_ok=True)

    text = "flagissuperfounder"
    text_index = 0
    while text_index < len(text):
        for _ in range(10):
            text_index = create_random_directory(base_path, 10, text_index, text)

if __name__ == "__main__":
    main()
