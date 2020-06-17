from time import sleep
from googletrans import Translator
from notion.client import NotionClient
from constants import TRANSLATIONS, TOKEN, REACT, REACT_FILE

translator = Translator()
base_language = "ru"
link = REACT

client = NotionClient(token_v2=TOKEN)
database = client.get_collection_view(link)
current_rows = database.default_query().execute()

array = TRANSLATIONS
array.remove("en")
array.insert(0, "en")

for to_language in array:
    if to_language != base_language:
        for row in current_rows:
            base_text = row.get_property(base_language)
            to_text = row.get_property(to_language)

            if to_text is None or len(to_text) == 0:
                sleep(1)

                translated = translator.translate(base_text, src=base_language, dest=to_language).text.capitalize()
                print(translated)
                row.set_property(to_language, translated)

    base_language = "en"
