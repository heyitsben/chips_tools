import cc_dat_utils
import json
import cc_classes

#Part 3
#Load your custom JSON file
input_json_file = "data/bennerr_cc1.json"
with open(input_json_file, "r") as reader:
    json_input = json.load(reader)
#Convert JSON data to CCLevelPack
levels = json_input["levels"]
for level in levels:
    title = cc_classes.CCMapTitleField(level["title"])
    password = cc_classes.CCEncodedPasswordField(level["password"])
    hint = cc_classes.CCMapHintField(level["hint"])
    monster = cc_classes.CCMonsterMovementField(level["monster"])
#Save converted data to DAT file