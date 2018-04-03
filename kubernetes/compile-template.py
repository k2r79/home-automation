import os

properties_file = open('config/template.properties', 'r')

properties = []
for line in properties_file:
    properties.append(line.rstrip().split(' = '))

for template_file in os.listdir('templates/'):
    with open('templates/' + template_file, 'r') as template:
        template_data = template.read()
        for p in properties:
            template_data = template_data.replace('{{' + p[0] + '}}', p[1])

    with open(os.path.basename(template_file), 'w') as template_output:
        template_output.write(template_data)
    