import configparser
import os

file = os.path.join(os.path.abspath('.'), 'config.ini')
config = configparser.ConfigParser()
config.read(file, encoding="utf8")

code = config['system']['code']
time = config['system']['time']
time = int(time)

print(f'code: {code}')
print(f'time: {time}')
