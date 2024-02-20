import cc_dat_utils
import json
import cc_classes

#Part 3
#Load your custom JSON file
input_json_file = "data/bennerr_cc1.json"
with open(input_json_file, "r") as reader:
    json_input = json.load(reader)
#Convert JSON data to CCLevelPack

#Save converted data to DAT file