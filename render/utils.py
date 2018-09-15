from jinja2 import Template


def render_to_string(path_file, context):
    string = open(path_file, 'r').read()
    template = Template(string)
    return template.render(**context)