import sys
import command_line_app
import command_line_parser



if(len(sys.argv) > 1):
    command_line_parser.start(sys.argv[1:])
else:
    command_line_app.app()