from pages.authenticate import authenticate
from utilities.setupDriverChrome import browser
from pages.createGame import Game
from pages.createSeason import Season
from pages.createEpisode import Episode
from pages.createPackage import Package


def main():
    driver = browser()

    # Env = 0 for dev and 1 for uat
    env = 0
    # env = 1

    email = "superadmin@mailinator.com"
    password = "123admin@"
    authenticate(driver, email, password, env=env)
    game = Game(driver=driver, name_of_game="Nimesh Game", env=env)
    game_id = game.create_game()
    # game_id = "f4a69811-b43b-4a9c-9afc-9ae165012800"
    season = Season(driver=driver, game_id=game_id,
                    name_of_season="Season", env=env)
    season_id = season.create_seasons()
    # season_id = "43c548bf-7cbc-476e-b6dd-02ff9e289808"

    # Manual episode
    season_episode_type = "manual"
    game_host_name = "Nimesh Host"
    game_manager_name = "Nimesh Manager"
    episode = Episode(driver=driver, name_of_episode="Episode",
                      season_episode_type=season_episode_type, season_id=season_id, game_host_name=game_host_name, game_manager_name=game_manager_name, env=env)

    # # Auto episode
    # season_episode_type = "auto"
    # episode = Episode(driver=driver, name_of_episode="Episode",
    #                   season_episode_type=season_episode_type, season_id=season_id)

    episode_URL = "https://youtu.be/21yj2ji6D1s"

    episode_number = episode.create_episodes(
        number_of_episodes=5, episode_live_URL=episode_URL, number_of_question=8)

    package = Package(driver=driver, season_id=season_id,
                      number_of_episodes=episode_number, env=env)
    package.update_packages()


if __name__ == "__main__":
    main()
