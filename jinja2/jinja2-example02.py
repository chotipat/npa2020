from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('template02.txt')

devices = yaml.load(open('devices_info.yml'), Loader=yaml.FullLoader)

path = 'config/'
for device in devices:
    config_file = path + device['name'] + '_config.txt'
    with open(config_file, 'w') as f:
        f.write(template.render(device))
