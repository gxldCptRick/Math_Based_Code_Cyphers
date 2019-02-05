import sys
import cypher_app.command_line.command_line_app as command_line_app
import cypher_app.command_line.command_line_parser as command_line_parser

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        command_line_parser.start(sys.argv[1:])
    else:
        command_line_app.app()
