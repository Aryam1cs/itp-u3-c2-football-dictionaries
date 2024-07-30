#!/usr/bin/env python
# coding: utf-8

# In[1]:


def group_players_by_country_and_position(players):
    # Initialize an empty dictionary to store grouped players by country and position
    grouped_players = {}
    
    # Process each player
    for player in players:
        # Extract player details
        country = player[6]
        position = player[1]
        
        # Ensure the country entry exists in the dictionary
        if country not in grouped_players:
            grouped_players[country] = {}
        
        # Ensure the position entry exists in the dictionary for the specific country
        if position not in grouped_players[country]:
            grouped_players[country][position] = []
        
        # Create the player dictionary
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
        
        # Append the player dictionary to the correct position list
        grouped_players[country][position].append(player_dict)
    
    return grouped_players

# Example input list of players
players = [
    ["1", "GK", "Juan Botasso", "(1908-10-23)23 October 1908 (aged 21)", "", "Quilmes", "Argentina", "Argentina", "1930"],
    ["9", "FW", "Roberto Cherro", "(1907-02-23)23 February 1907 (aged 23)", "", "Boca Juniors", "Argentina", "Argentina", "1930"],
    ["2", "DF", "Carlos Pardo", "(1906-03-12)12 March 1906 (aged 24)", "", "San Lorenzo", "Argentina", "Argentina", "1930"],
    ["3", "MF", "Luis Monti", "(1901-05-15)15 May 1901 (aged 29)", "", "Boca Juniors", "Argentina", "Argentina", "1930"],
    ["4", "GK", "Carlos Alberto", "(1902-05-20)20 May 1902 (aged 28)", "", "Santos", "Brazil", "Brazil", "1930"],
    ["5", "FW", "Didi", "(1916-10-23)23 October 1916 (aged 14)", "", "Vasco", "Brazil", "Brazil", "1930"]
    # Add more players as needed
]

# Group players by country and position
grouped_players = group_players_by_country_and_position(players)

# Print the result
for country, positions in grouped_players.items():
    print(f"Country: {country}")
    for position, players in positions.items():
        print(f"  Position: {position}")
        for player in players:
            print(f"    {player}")
    print()


# In[ ]:




