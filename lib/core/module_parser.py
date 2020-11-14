import json
import yaml
import lib.modules

# TODO change hard coded directory
config_dir = "/Users/tylerbutler/Documents/projects/programming/Github/sendbirdy/lib/modules/modules.yml"
module_file = open(config_dir)
parsed_yaml = yaml.load(module_file, Loader=yaml.FullLoader)

def parse_yaml(app, option):
    return parsed_yaml[app][option]

def parse_yaml_list(app, options):
    returned = []
    for things in parsed_yaml[app][options]:
        returned.append(parsed_yaml[app][option])

    return returned

def parse_headers(app,option,set):
    return parsed_yaml[app][option][set]



# TODO Add Feature to Set Settings in modules.yml
def put_yaml():
    return
