import textwrap

text = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Comment line
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

# Fungsi predicate untuk tidak mengindentasi baris yang dimulai dengan '#'
def should_indent(line):
    return not line.lstrip().startswith('#')

# Menambahkan indentasi ke setiap baris teks kecuali baris yang dimulai dengan '#'
indented_text = textwrap.indent(text, prefix='    ', predicate=should_indent)

print(indented_text)
