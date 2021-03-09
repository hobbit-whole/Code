import constants

if __name__ == "__main__":
    players = constants.PLAYERS
    teams = constants.TEAMS

    player_info = []
    
    def unpack_players_dic():
        for player in players:
            player_info.append(player)

            for k, v in player.items():
                if(k == 'height'):   
                    player['height'] = int(v[0:2])

                if(k == 'experience'):
                    if(v == 'YES'):
                        v.replace('YES', 'True')
                        v = bool(v)
                    else:
                        v.replace('NO', 'False')
                        v = bool(v)