import json
from notion.client import NotionClient
from constants import TRANSLATIONS, TOKEN, REACT, REACT_FILE

client = NotionClient(token_v2=TOKEN)
database = client.get_collection_view(REACT)
current_rows = database.default_query().execute()

data = {}

for translation in TRANSLATIONS:
    translation_data = {}
    is_set = False

    for row in current_rows:
        key = row.get_property("key")
        value = row.get_property(translation)

        if len(value) > 0:
            is_set = True
            translation_data[key] = row.get_property(translation)

    if is_set:
        data[translation] = translation_data

outfile = open(REACT_FILE, 'w+', encoding="utf8")
json.dump(data, outfile, indent=4, sort_keys=True, ensure_ascii=False)
outfile.close()
