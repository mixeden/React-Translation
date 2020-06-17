import json
from notion.client import NotionClient
from constants import TRANSLATIONS, TOKEN, REACT, REACT_FILE

client = NotionClient(token_v2=TOKEN)
database = client.get_collection_view(REACT)


def find_or_add_row(key):
    current_rows = database.default_query().execute()

    for row in current_rows:
        row_key = row.get_property("key")

        if row_key == key:
            return row

    row = database.collection.add_row()
    row.key = key

    return row


with open(REACT_FILE, "r") as read_file:
    text = read_file.read()
    text = text.replace("\n", "").replace("\t", "") \
        .replace("\r", "").replace("\" + \"", "") \
        .replace("\" +\"", "").replace("\"+\"", "") \
        .replace("\"+ \"", "")

    data = json.loads(text)

for translation in TRANSLATIONS:
    if translation in data:
        keys = data[translation]

        for key in keys:
            print("Getting key {} of {} language".format(key, translation))

            new_row = find_or_add_row(key)
            value = keys[key]

            new_row.set_property(translation, value)
