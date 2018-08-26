def html_tag(tag):

    def wrap_text(msg):
        # E.G. h1, "Hello" >>> <h1>Hello</h1>
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1("Test headline")
print_h1("Another headline")
