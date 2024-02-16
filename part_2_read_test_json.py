import json
import test_data

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    for game in json_data:
        class platform:
            def __init__(self, launchYear=-1, name=None):
                self.launchYear = launchYear
                self.name = name

        class Game:
            def __init__(self, title=None, year=-1):
                self.title = title
                self.year = year
                self.platforms = []

            def __str__(self):
                return_str = "Game:\n"
                return_str += "  Title:\n"
                return_str += "    " + self.title + "\n"
                return_str += "  Year:\n"
                return_str += "    " + self.year + "\n"
                return_str += "  Platforms:\n"
                for platform in self.platforms:
                    return_str += "    " + platform.name + ", " + str(platform.launchYear) + "\n"
                return return_str

            def add_platform(self, platform=None):
                self.platforms.append(platform)
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
with open(input_json_file, "r") as reader:
    # load the JSON data and store it in the variable family_json_data
    games_json_data = json.load(reader)

    # Get the parents array from the JSON data (it is an array of strings)
    title = games_json_data["name"]
    year = games_json_data["year"]
    # Create a new Family object that is initialized with the parents
    new_game = game_classes.Game(title, year)

    # Get the kids array from the JSON data (it is an array of dicts)
    platform = games_json_data["platform"]
    # Iterate through the kids array
    for platform in platforms:
        # Creat a new Kid with the "name" and "age" from the JSON data
        new_platform = game_classes.platform(platform["name"], platform["launch year"])
        # Add the Kid to the Family
        new_games.add_platform(new_platform)

    print(new_games)
### End Add Code Here ###
