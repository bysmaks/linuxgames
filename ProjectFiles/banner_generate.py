def generate_script(text):
    
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    block_width = max(max_length + 4, 50)
    border = '#' * block_width 

    formatted_lines = []
    for line in lines:
        padding = (block_width - len(line) - 2) // 2
        formatted_line = f"# {' ' * padding}{line}{' ' * (block_width - len(line) - padding - 2)} #"
        formatted_lines.append(formatted_line)

    output = f"""#!/bin/sh
echo "\\n{border}##"
"""
    for formatted_line in formatted_lines:
        output += f'echo "{formatted_line}"\n'
    output += f'echo "{border}##"\n'

    return output

input_text = """
# Oneliner mode: ты можешь ввести только одну команду

Знаешь как выглядит золушка 21 века?
Отделять мусор от не мусора тебе конечно не придется
А вот сесть и подсчитать длину имен файлов в папке /challenges
Без учета расширения
И найти их сумму - да
Не затягивай с этим.
Удачи ;)
"""

output_script = generate_script(input_text)

# Записываем выходной файл
with open('banner.sh', 'w') as file:
    file.write(output_script)

print("Banner has been generated.")
