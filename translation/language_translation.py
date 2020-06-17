from time import sleep
from googletrans import Translator
from notion.client import NotionClient
from constants import TRANSLATIONS, TOKEN, REACT, REACT_FILE

translator = Translator()
to_language = input("Введите язык, на который переводить\n")
base_language = "en"
link = REACT

client = NotionClient(token_v2=TOKEN)
database = client.get_collection_view(link)
current_rows = database.default_query().execute()

for row in current_rows:
    base_text = row.get_property(base_language)
    to_text = row.get_property(to_language)

    if to_text is None or len(to_text) == 0:
        sleep(1)

        translated = translator.translate(base_text, src=base_language, dest=to_language).text.capitalize()
        print(translated)
        row.set_property(to_language, translated)
