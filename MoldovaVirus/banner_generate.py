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

input_text = """Бедный молдавский вирусописатель
Наконец то сделал первый РАБОТАЮЩИЙ вирус
В этот раз эта шняга научилась воровать пароли
И распихивать их по разным файлам
Жаль, что имена файлов все таки предсказуемы
Имеют численный формат
И более того - идут по порядку...
В папке /root/challenge тебя ждет невиданное приключение
"""

output_script = generate_script(input_text)

# Записываем выходной файл
with open('banner.sh', 'w') as file:
    file.write(output_script)

print("Banner has been generated.")