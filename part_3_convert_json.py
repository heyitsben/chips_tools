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
level_pack = cc_classes.CCLevelPack()
for level in levels:
    title = cc_classes.CCMapTitleField(level["title"])
    password = cc_classes.CCEncodedPasswordField(level["password"])
    hint = cc_classes.CCMapHintField(level["hint"])

    monsterTemp = level["monster"]
    monster_coords = []
    for m in monsterTemp:
        mc = cc_classes.CCCoordinate(monsterTemp[0],monsterTemp[1])
        monster_coords.append(mc)
    monster = cc_classes.CCMonsterMovementField(monster_coords)

    level_number = level["level_number"]
    time = level["time"]
    chip_count = level["chip_count"]
    upper_layer = level["top_layer"]

    new_level = cc_classes.CCLevel()

    new_level.level_number = level_number
    new_level.time = time
    new_level.num_chips = chip_count
    new_level.upper_layer = upper_layer

    new_level.add_field(title)
    new_level.add_field(password)
    new_level.add_field(hint)
    new_level.add_field(monster)

    new_level.title = title
    new_level.password = password
    new_level.hint = hint
    new_level.monsters = monster_coords

    level_pack.add_level(new_level)
#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "data/bennerr_cc1.dat")