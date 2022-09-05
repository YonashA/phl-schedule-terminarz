from bs4 import BeautifulSoup
import requests
from icalendar import Calendar, Event
from datetime import datetime
import pytz

# BeautifulSoup setup and url
URL = "https://hokej.net/terminarz/180/regularny-2"
web_request = requests.get(URL)
web_request_text = web_request.text
soup = BeautifulSoup(web_request_text, "html.parser")

# Get all games' key details (date & time, home and away team, venue)
all_dates = soup.find_all(name="td", class_="game-date")
all_home = soup.find_all(name="td", class_="game-home")
all_away = soup.find_all(name="td", class_="game-away")
game_info = soup.find_all(name="a", class_="game-icering")

# Add each game key detail into new separate lists (with small clean-up)
teams_home = [item.getText().strip('\n') for item in all_home]
teams_away = [item.getText().strip('\n') for item in all_away]
game_dates = [item.getText().strip('\n') for item in all_dates]
game_icering = [item.getText().replace(', PL', '') for item in game_info]

# Split date & time element into nested list to separate time from date
game_time_date = [item.split(' ') for item in game_dates]

# Combine all lists into one major list with all games
game_teams = [list(tup) for tup in zip(game_time_date, teams_home, teams_away, game_icering)]

# Print header
print("\nLista wszystkich drużyn Polskiej Hokej Ligi na sezon 2022/2023:\n")

# Get all unique names of PHL Teams and print all available teams
num_unique_list = []
def unique(game_teams):
    unique_list = []
    for i in game_teams:
        if i[1] not in unique_list:
            unique_list.append(i[1])
    # Add numbering to each team string to help with user selection
    for idx, team in enumerate(unique_list, 1):
        num_unique_list.append(f"{idx}. {team}")
    # Print all teams
    for i in num_unique_list:
        print(i)

# Run unique team list function
unique(game_teams)

# Ask user to select the team (by entering number assinged to a team)
while True:
    try:
        user_input = int(input("\nWybierz zespół (wpisz nr): "))
        if user_input < 1 or user_input > len(num_unique_list):
            raise ValueError
        break
    except ValueError:
        print('Nieprawidłowy wybór.\nWprowadź liczbę przypisaną do zespołu!')

# Assign user_input (number) to a specifc team name to allow look-up
selected_team = [i for i in num_unique_list if i.startswith(f"{user_input}")]
team_name = selected_team[0].split('. ')[1]

# Get number and games for user selected team name to be added as events to calendar
number_of_games = 0
selected_games = []
for i in range(len(game_teams)):
    if game_teams[i][1] == team_name or game_teams[i][2] == team_name:
        selected_games.append(game_teams[i])
        number_of_games += 1

# Create a new calendar
c = Calendar()
# Mandatory fields for iCalendar
c.add('prodid', '-//Terminarz PHL 2022//example.com//')
c.add('version', '2.0')

# Adding events (selected team games) to calendar
for i in range(number_of_games):
    e = Event()
    e.add('uid', f'{i}1')
    e.add('summary', f'🏒PHL: {selected_games[i][1]} vs. {selected_games[i][2]}')
    e.add('dtstart', datetime(year=int(selected_games[i][0][0].split("-")[0]), month=int(selected_games[i][0][0].split("-")[1]), day=int(selected_games[i][0][0].split("-")[2]), hour=int(selected_games[i][0][1].split(":")[0]), minute=int(selected_games[i][0][1].split(":")[1]), second=0, tzinfo=pytz.timezone("Europe/Warsaw")))
    e.add('dtend', datetime(year=int(selected_games[i][0][0].split("-")[0]), month=int(selected_games[i][0][0].split("-")[1]), day=int(selected_games[i][0][0].split("-")[2]), hour=int(selected_games[i][0][1].split(":")[0])+2, minute=int(selected_games[i][0][1].split(":")[1]), second=0, tzinfo=pytz.timezone("Europe/Warsaw")) )
    e.add('location', selected_games[i][3] )
    c.add_component(e)
    f = open(f'Terminarz {team_name}.ics', 'wb')
    f.write(c.to_ical())
f.close()

# Confirm file generated
print(f"\nTerminarz dla zespołu: {team_name} - został zapisany z sukcesem.\nOtwórz plik .ics i dodaj wszystkie mecze do kalendarza.\n")