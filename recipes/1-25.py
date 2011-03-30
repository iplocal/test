# Converting html documents to text on a unix terminal

import sys, os, htmllib, formatter

bold = os.popen('tput bold').read()
underline = os.popen('tput smul').read()
reset = os.popen('tput sgr0').read()

class TtyFormatter(formatter.AbstractFormatter):
    def __init__(self, writer):
        formatter.AbstractFormatter.__init__(self, writer)
        self.font_stack = []
        self.font_state = (0, 0)
    def push_font(self, font):
        size, italic, bd, tt = font
        self.font_stack.append((italic, bd))
        self.update_font_state()
    def pop_font(self):
        try: self.font_stack.pop()
        except: pass
        self.update_font_state()
    def update_font_state(self):
        try: new_state = self.font_stack[-1]
        except: new_state = (0, 0)
        if self.font_state != new_state:
            print reset,
            if new_state[0]: print underline,
            if new_state[1]: print bold,
            self.font_state = new_state

my_writer = formatter.DumbWriter()

if sys.stdout.isatty():
    my_formatter = TtyFormatter(my_writer)
else:
    my_formatter = formatter.AbstractFormatter(my_writer)

my_parser = htmllib.HTMLParser(my_formatter)
my_parser.feed(sys.stdin.read())
my_parser.close()
