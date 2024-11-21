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
# Suicide mode: у тебя нет права на ошибку
# Time mode: успей за 30 секунд...

Какой то хулиган
Слишком активно пытается подобрать пароль
Покопайся в логах и выясни
Кто это делает с внешнего адреса
У кого больше всех запросов
Вычисли по ip и...
Ну ты понял
"""

output_script = generate_script(input_text)

# Записываем выходной файл
with open('banner.sh', 'w') as file:
    file.write(output_script)

print("Banner has been generated.")