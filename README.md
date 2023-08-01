# Doko Game management Automation

Welcome to Doko Game managment. This is a brief guide on using this automation tool

## Get Started

To run this project you need to have following:

1. Clone this project
2. Install latest version of python

   If you don't have Python installed, download and install the latest version from the official Python website: https://www.python.org/downloads/

3. Install Selenium
   ```bash
   $pip install selenium
   ```
4. Install web driver

```bash
$pip install web-driver
```

5. Run the project
   ```bash
   $python main.py
   ```

# Creating Game

Change the main.py file to acheive the type of game, season or episode you want to create. Follow instructions below for more information.

## Authentication

Authentication is the first module of the application. You need to authenticate to perform any task. Replace the existing email and password with yours credentials.

```bash
    email = "Your_CMS_LOGIN_EMail"
    password = "PASSWORD"
    authenticate(driver, email, password)
```

## Create a game with a season, episode and packages

To create a full game that contains season, episode and packages. Comment out game_id, season_id and rest of the code should not be commented.

1. Provide your CMS Auto credentials
2. Set Game name
3. Set Season name
4. Set Episode type, game host and game manager
5. Set Number of episodes, Episode URl and number of question in an episode
6. Update package

```bash
    # game_id = "b4ca4e1a-7b44-4c81-b5a7-b0740fcbb2d6"
    # season_id = "b4ca4e1a-7b44-4c81-b5a7-b0740fcbb2d6"
```

#### Create Auto Episode

To create auto episode comment Manual episode and uncomment Auto episode.

```bash

    # # Manual episode
    # season_episode_type = "manual"
    # game_host_name = "Suman Host"
    # game_manager_name = "Suman Manager"
    # episode = Episode(driver=driver, name_of_episode="Episode",
    #                   season_episode_type=season_episode_type, season_id=season_id, game_host_name=game_host_name, game_manager_name=game_manager_name)

    # Auto episode
    season_episode_type = "auto"
    episode = Episode(driver=driver, name_of_episode="Episode",
                      season_episode_type=season_episode_type, season_id=season_id)
```

#### Create Manual Episode

To create manual episode comment Auto episode and uncomment manual episode.

```bash

    # Manual episode
    season_episode_type = "manual"
    game_host_name = "Suman Host"
    game_manager_name = "Suman Manager"
    episode = Episode(driver=driver, name_of_episode="Episode",
                      season_episode_type=season_episode_type, season_id=season_id, game_host_name=game_host_name, game_manager_name=game_manager_name)

    # # Auto episode
    # season_episode_type = "auto"
    # episode = Episode(driver=driver, name_of_episode="Episode",
    #                   season_episode_type=season_episode_type, season_id=season_id)
```

## Create season in existing game

To Create a seson in existing game, comment out these two lines and provide game id of the game where you want to add season.

```bash
    # game = Game(driver=driver, name_of_game="Desired Game name")
    # game_id = game.create_game()
    game_id = "9eba9420-f580-4f22-bd04-7e4ae2816102"
```

## Add episode in existing season

To Create an episode in existing season, comment out these everything exept driver and authenticaion and provide season id of the season where you want to add episode.

```bash
    # game = Game(driver=driver, name_of_game="Desired Game name")
    # game_id = game.create_game()
    # game_id = "9eba9420-f580-4f22-bd04-7e4ae2816102"
    # season = Season(driver=driver, game_id=game_id,
    #                 name_of_season="Season")
    # season_id = season.create_seasons()
    season_id = "b4ca4e1a-7b44-4c81-b5a7-b0740fcbb2d6"
```
