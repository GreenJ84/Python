# Create a class for a Basketball player with a constructor for name, age, position, and team attributes
# Update a class constructor to take in a player dictionary
# Create Player instances
# Write a class method that poplates a team(list) of Player instances from a list of player dictionaries.

# List of player dictionaries
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
    }
]

# Individual Player Dictionaries
kevinData = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jasonData = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrieData = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Player class updated to take in full dictionaries
class Player:
    def __init__(self, playerData):
        self.name = playerData['name']
        self.age = playerData['age']
        self.position = playerData['position']
        self.team = playerData['team']

    # Create a class function that creates team of Player objects using a list of player data dictionaries
    def get_team(team_list):
        new_team = []
        for player in players:
            new_player = Player(player)
            new_team.append(new_player)
        return new_team

# Creating player objects using dictionaries of player data
kevin = Player(kevinData)
jason = Player(jasonData)
kyrie = Player(kyrieData)
