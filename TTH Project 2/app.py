import constants
import random

if __name__ == "__main__":
    players = constants.PLAYERS
    teams = constants.TEAMS

    #print(players)
    player_info = []
    team_info = []
    
    for player in players:
        player_info.append(player)

    for team in teams:
        team_info.append(team)


def unpack_players_dic():


    for k, v in player.items():
        if(k == 'height'):   
            player['height'] = int(v[0:2])

        if(k == 'experience'):
            if(v == 'YES'):
                player['experience'] = True
            else:
                player['experience'] = False


def pack_player_roster():
    names = [d['name'] for d in player_info if 'name' in d]
    stacked = []

    random.shuffle(names)
    shuffled_names = [names[i] for i in range(6)]
    print([names[i] for i in range(6)])

    


    

    

pack_player_roster()