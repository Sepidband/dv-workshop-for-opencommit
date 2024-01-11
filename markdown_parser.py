from models import Step, Codelab

def parse_markdown(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    title = ''
    steps = []
    current_label = ''
    current_content = ''

    for line in lines:
        if line.startswith('# '):
            title = line.strip('# ').strip()
        elif line.startswith('## '):
            if current_label:
                steps.append(Step(current_label, current_content.strip()))
            current_label = line.strip('## ').strip()
            current_content = ''
        else:
            current_content += line

    if current_label:
        steps.append(Step(current_label, current_content.strip()))

    return Codelab(title, steps)