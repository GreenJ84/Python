class Player:
    player_inst = []
    def __init__(self, player_info):
        self.name = player_info['name']
        self.age = player_info['age']
        self.position = player_info['position']
        self.team = player_info['team']

    def diplay_info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)

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
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

def list_to_object(self, list):
    player_inst = []
    for items in list:
        x = items['name']
        player_name = f'player_{x}'
        player_name = Player(list[items])
        Player.player_inst.append(self)
        print(Player.player_inst)
        return self



# kevin = {
#     	"name": "Kevin Durant", 
#     	"age":34, 
#     	"position": "small forward", 
#     	"team": "Brooklyn Nets"
# }
# jason = {
#     	"name": "Jason Tatum", 
#     	"age":24, 
#     	"position": "small forward", 
#     	"team": "Boston Celtics"
# }
# kyrie = {
#     	"name": "Kyrie Irving", 
#     	"age":32, "position": "Point Guard", 
#     	"team": "Brooklyn Nets"
# }
    
# # Create your Player instances here!
# player_kevin = Player(kevin)
# player_kevin.diplay_info()

# player_jason = Player(jason)
# player_jason.diplay_info()

# player_kyrie = Player(kyrie)
# player_kyrie.diplay_info()

