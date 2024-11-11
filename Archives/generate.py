import os
import random
import string
import tarfile
import zipfile
import gzip

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_extension():
    extensions = ['gz', 'tar', 'zip']
    return random.choice(extensions)

def create_archive(file_name, archive_name, extension):
    if extension == 'gz':
        with open(file_name, 'rb') as f_in:
            with gzip.open(archive_name, 'wb') as f_out:
                f_out.writelines(f_in)
    elif extension == 'tar':
        with tarfile.open(archive_name, 'w') as tar:
            tar.add(file_name)
    elif extension == 'zip':
        with zipfile.ZipFile(archive_name, 'w') as zipf:
            zipf.write(file_name)

def main():
    flag = "flag_is_super_archive"
    os.makedirs('challenges', exist_ok=True)

    for i, char in enumerate(flag):
        file_name = f'challenges/{i}.txt'
        archive_name = f'challenges/{i}.{generate_random_extension()}'

        with open(file_name, 'w') as file:
            file.write(char)

        create_archive(file_name, archive_name, archive_name.split('.')[-1])
        os.remove(file_name)

if __name__ == "__main__":
    main()
