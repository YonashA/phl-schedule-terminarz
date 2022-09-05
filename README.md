# Favorite Polish Hockey Team 2022 calendar events generator (.ics) in Python
Using web scraping (Beautiful Soup) to generate favorite polish hockey team calendar events (.ics) in Python for season 2022/2023. Adding all already scheduled games to phone, tablet, and computer as Events in Calendar app.

<br>

<p float="left">
<img src="https://user-images.githubusercontent.com/97128701/188421007-36b8b712-033d-4f62-9f74-04081d641fed.png" width="50" height="50">
<img src="https://user-images.githubusercontent.com/97128701/188421021-dfb04bcb-0e45-42b5-a0e2-7fbbca772c2a.png" width="50" height="50">
<img src="https://user-images.githubusercontent.com/97128701/188421027-e673a93b-1f1a-4f72-a6cd-b31f2cbaf299.png" width="50" height="50">
<img src="https://user-images.githubusercontent.com/97128701/188421037-f7223d61-2ce4-40ed-90c1-077b7b766282.png" width="50" height="50">
<img src="https://user-images.githubusercontent.com/97128701/188421044-2f303aea-dbed-4837-a80f-703521ec74ad.png" width="50" height="50">
<img src="https://user-images.githubusercontent.com/97128701/188421049-564a8488-cdd5-4cb8-ae50-91405bc2ccc8.png" width="50" height="50">
<img src="https://user-images.githubusercontent.com/97128701/188421054-69b3855f-17bb-4444-b4a7-dec0c64051b7.png" width="50" height="50">
<img src="https://user-images.githubusercontent.com/97128701/188421060-104503e5-d8a3-438e-a5b0-e0d64948d551.png" width="50" height="50">
<img src="https://user-images.githubusercontent.com/97128701/188421069-19e48261-b8a3-4f7d-a584-6c04cb0e41ab.png" width="50" height="50">
</p>

<strong><i>Why:</i></strong><br>
For all ice hockey fans in Poland (where hockey is not getting the right "prime time"), to have all games of their favorite team on the phone calendar (or pc, tablet), and to know when is the next game, at which location, against which team, together with a direct reminder. This feature is currently not available online to get anywhere.

Using web scraping technique with Beautiful Soup and iCalendar library to get the latest schedule for the 2022/2023 season and generate a .ics file with all already fixed games for a selected team. 

<strong><i>How:</i></strong><br>
Use test_plh.py file to run Python code, generate a list of all available teams in the polish league for the 2022/2023 season (using web scraping) and ask users for a choice of their favorite team.

![image](https://user-images.githubusercontent.com/97128701/188427858-53106dfd-4c4c-446b-a3ac-d7dd3f3b6c38.png)

Generates (using web scraping) and saves .ics file for all games where the selected team is host or away team (*from 144 games currently available adds the ones for the selected team only).

![image](https://user-images.githubusercontent.com/97128701/188428018-119620dc-44b3-4719-a0d5-4fd742731689.png)

Calendar events consist of the title (home vs. away team), location, date, and time. 

![image](https://user-images.githubusercontent.com/97128701/188428141-ddd493f1-96ca-4d23-ab6e-cde4756a5080.png)


<hr>
Note:
<ul>
<li>This is a personal project for the Python practice
</li>
<li>The schedule is generated as per the 5th Sep 2022 status of the PLH schedule only for 2 rounds (total of 144 games, where the schedule is confirmed)</li>
<li>The program does not generate a calendar subscription, hence any further changes to the fixtures (dates, timing, game cancellation, etc.) are not updated</li>
</ul>
