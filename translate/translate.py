import click
import dataclasses
import os

from ollama import GenerateResponse, Client

# MODEL = "llama3"
MODEL = "mixtral:8x22b"
LANGUAGES = ["en"]

OLLAMA_URL = "http://10.1.0.2:11434"

MAIN_PROMPT = """
Traduce from french to {language} if necessary. Else just re-write original string.
The result string will be used in a .po file, as translation of my project's documentation.
Preserve markdown and restructured text syntax.

You response must follow this pattern:
Here is the translated string:
***
REPLACE_WITH_TRANSLATION
***

The string to translate is: {string}
"""


@dataclasses.dataclass
class PoChunk:
    original: str
    output: str = None
    ignore: bool = False

language_map: dict[str, str] = {
    "en": "english"
}

@click.command()
@click.option('-l', '--language', default="en", type=str)
@click.option('-o', '--ollama', type=str, default=OLLAMA_URL, help="Ollama server url")
@click.option('-m', '--model', type=str, default=MODEL, help="Ollama model to use")
@click.argument("files", nargs=-1, type=str)
def main(language: str, ollama: str, model: str, files: tuple[str] = ("../locale/en/LC_MESSAGES")):
    if not language in language_map:
        print(f"Language {language} is not supported use one of {', '.join(language_map.keys())} instead")
        return
    for file in files:
        if not os.path.exists(file):
            print(f"file not found: {file}")
            return
        print(f"{file}")
        print(f"\n====================================\nTranslating to {language}")
        translate_files(file, language, ollama, model)
    print("Finished")


def translate_files(path: str, language: str, ollama_url: str, model: str):
    # it's a file to traduce !
    if os.path.isfile(path) and path.endswith(".po"):
        print(f"File: {path}")
        content = open(path, "r").read()
        translation = translate(content, language, ollama_url, model)
        open(path, "w").write(translation)
    elif os.path.isdir(path):
        for name in os.listdir(path):
            translate_files(os.path.join(path, name), language, ollama_url, model)


def translate(content: str, target_language: str, ollama_url: str, model: str) -> str:
    if content.startswith("### AUTO-TRANSLATION IGNORE"):
        print("❕ File marked as ignored")
        return content

    # parse original file
    chunks: list[PoChunk] = chunk_po_file(content)

    # translate chunks
    chunks_to_translate = [c for c in chunks if not c.ignore]
    print(f"Found {len(chunks_to_translate)} chunks to translate")

    i: int = 0
    for chunk in chunks_to_translate:
        i += 1
        print(f"chunk {i} / {len(chunks_to_translate)}")
        original_sentence: str = chunk.original.split("msgid")[-1].strip().split("msgstr")[0].strip().removeprefix("\"").removesuffix("\"").strip()
        if not original_sentence:
            print("❕ignored empty sentence")
            continue

        client = Client(host=ollama_url)
        prompt: str = MAIN_PROMPT.format(language=language_map[target_language], string=original_sentence)
        response: GenerateResponse = client.generate(model=model, prompt=prompt)

        # check response follow pattern
        if response.response.count("***") == 2:
            traduced_sentence = response.response.split("***")[1].strip()
            chunk.output = chunk.original.split("msgstr")[0] + "msgstr \"" + traduced_sentence.replace("\"", "\\\"") + "\""
        else:
            print(f"⚠️ Invalid response: {response.response}")

    # compute output file
    output: str = ""
    for chunk in chunks:
        if chunk.output:
            # translated again a fuzzy string, remove fuzzy marker
            if chunk.output.find("#, fuzzy\n") != -1:
                chunk.output = chunk.output.replace("#, fuzzy\n", "")
                output += chunk.output
            # newly translated using ollama sentence: add '# translated using ollama' marker
            else:
                output += "# translated using ollama\n" + chunk.output
        else:
            output += chunk.original
        output += "\n\n"

    return output

def is_chunk_start(line: str):
    # #: comment with position in original file, #, start of comment for fuzzy translation
    return line.startswith("# translated using ollama") or line.startswith("#:") or line.startswith("#,")

def chunk_po_file(file_content: str) -> list[PoChunk]:
    lines = file_content.splitlines(keepends=True)
    chunks: list[PoChunk] = []
    i: int = 0
    while i < len(lines):
        # if line starts by #: it's a valid chunk, else we ignore it
        fuzzy: bool = False
        already_translated: bool = False
        # found a valid chunk
        if is_chunk_start(lines[i]):
            already_translated = lines[i].startswith("# translated using ollama")
            fuzzy = lines[i].startswith("#, fuzzy")
        j = i + 1
        while j < len(lines) and lines[j].strip():
            if lines[j].startswith("# translated using ollama"):
                already_translated = True
            elif lines[j].startswith("#, fuzzy"):
                fuzzy = True
            j += 1
        while j < len(lines) and not is_chunk_start(lines[j]):
            if lines[j].startswith("# translated using ollama"):
                already_translated = True
            elif lines[j].startswith("#, fuzzy"):
                fuzzy = True
            j += 1

        if fuzzy:
            ignore: bool = False
        elif already_translated:
            ignore: bool = True
        else:
            ignore: bool = False

        chunks.append(PoChunk("".join(lines[i:j]).strip(), ignore=ignore))
        i = j
    return chunks


if __name__ == "__main__":
    main()
