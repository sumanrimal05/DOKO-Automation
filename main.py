from pages.authenticate import authenticate
from utilities.setupDriverChrome import browser
from pages.createGame import Game
from pages.createSeason import Season
from pages.createEpisode import Episode
from pages.createPackage import Package


def main():
    driver = browser()

    email = "superadmin@mailinator.com"
    password = "123admin@"
    authenticate(driver, email, password)
    # game = Game(driver=driver, name_of_game="SumanTestGame")
    # game_id = game.create_game()
    # # game_id = "9eba9420-f580-4f22-bd04-7e4ae2816102"
    # season = Season(driver=driver, game_id=game_id,
    #                 name_of_season="Season")
    # season_id = season.create_seasons()
    season_id = "43c548bf-7cbc-476e-b6dd-02ff9e289808"

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

    episode_URL = "https://youtu.be/1GXB1KTzDps"

    episode_number = episode.create_episodes(
        number_of_episodes=2, episode_URL=episode_URL, number_of_question=10)

    package = Package(driver=driver, season_id=season_id,
                      number_of_episodes=episode_number)
    package.update_packages()


if __name__ == "__main__":
    main()
