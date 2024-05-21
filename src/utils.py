from IPython.display import display
from IPython.display import Markdown

import textwrap

def to_markdown(text: str):
  text = text.replace('·', ' *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
