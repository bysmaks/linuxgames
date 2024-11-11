import lorem
import random

FLAG = "You find my little secrets: UnicornPony9433"
output_file = 'large_text_file.txt'

def generate_data():
    num_paragraphs = random.randint(1000,2000)
    with open(output_file, 'a') as file:
        for _ in range(num_paragraphs):
            paragraph = lorem.paragraph()
            file.write(paragraph + "\n")

generate_data()
open(output_file, 'a').write(FLAG + "\n")
generate_data()

