#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def group_players_by_position(players):
    # Initialize an empty dictionary to store grouped players
    grouped_players = {}
    
    # Process each player
    for player in players:
        # Extract the position from the player's data
        position = player[1]
        
        # Create a new entry in the dictionary if the position is not already present
        if position not in grouped_players:
            grouped_players[position] = []
        
        # Append the player dictionary to the list for this position
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
        }
        grouped_players[position].append(player_dict)
    
    return grouped_players

# Example input list of players
players = [
    ["1", "GK", "Juan Botasso", "(1908-10-23)23 October 1908 (aged 21)", "", "Quilmes", "Argentina", "Argentina", "1930"],
    ["9", "FW", "Roberto Cherro", "(1907-02-23)23 February 1907 (aged 23)", "", "Boca Juniors", "Argentina", "Argentina", "1930"],
    ["2", "DF", "Carlos Pardo", "(1906-03-12)12 March 1906 (aged 24)", "", "San Lorenzo", "Argentina", "Argentina", "1930"],
    ["3", "MF", "Luis Monti", "(1901-05-15)15 May 1901 (aged 29)", "", "Boca Juniors", "Argentina", "Argentina", "1930"]
    # Add more players as needed
]

# Group players by position
grouped_players = group_players_by_position(players)

# Print the result
for position, players in grouped_players.items():
    print(f"Position: {position}")
    for player in players:
        print(player)
    print()

