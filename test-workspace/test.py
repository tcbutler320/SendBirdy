import lib.core.module_parser as parser


def test1():
    app = 'Hinge'
    options = ['app-name', 'sendbird-id']
    parser.parse_yaml(app, options)


def test2():
    arg = "Hinge"
    parser.parse_yaml(arg, )


def test3():
    app = 'Hinge'
    args = ['app-name']
    parser.parse_yaml(app, args)

def get_things():
    print("App: " + parser.parse_yaml('Hinge','app-name'))

    print("Accept-Encoding: " + parser.parse_headers('Hinge','headers','Accept-Encoding'))




def main():
    get_things()

# TODO Create Feature to List All Module Attributes
def dump_attributes():
    return



main()
