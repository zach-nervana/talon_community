from talon.voice import Context, Key, Str
from ..misc import basic_keys
from ..utils import parse_words, text, is_filetype
import string

FILETYPES = (".py",)

ctx = Context("talon_editor", func=is_filetype(FILETYPES))


def make_key(function_name="Key"):
    def key(m):
        modifiers = basic_keys.get_modifiers(m)
        key = basic_keys.get_keys(m)[0]
        if key is None:
            print("no key", m)
            return
        key_text = "-".join(modifiers + [key])
        Str(f"{function_name}('{key_text}')")(None)

    return key


def format_text(fmt):
    def wrapper(m):
        Str(fmt.format(" ".join(parse_words(m))))(None)

    return wrapper


ctx.keymap(
    {
        "key {basic_keys.modifiers}* {basic_keys.keymap}": make_key("Key"),
        "press {basic_keys.modifiers}* {basic_keys.keymap}": make_key("press"),
        "talon map <dgndictation>": ("'", text, "': ,", Key("left")),
        "talon map string <dgndictation>": format_text("'{0}': '{0}',"),
        "dragon dictation": "<dgndictation>",
        "stir": ["Str()(None)"] + [Key("left")] * 7,
    }
)
