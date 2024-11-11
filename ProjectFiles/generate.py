import os
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_extension():
    extensions = ['txt', 'md', 'json', 'csv', 'xml', 'html', 'css', 'js', 'py', 'sh']
    return random.choice(extensions)

def generate_files(directory, num_files, min_length=5, max_length=15):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(num_files):
        file_name = generate_random_string(random.randint(min_length, max_length))
        file_extension = generate_random_extension()
        file_path = os.path.join(directory, f"{file_name}.{file_extension}")
        with open(file_path, 'w') as file:
            file.write(generate_random_string(random.randint(50, 100)))

if __name__ == "__main__":
    directory = './challenges'
    num_files = 150
    generate_files(directory, num_files)
    print(f"Generated {num_files} files in {directory}")
