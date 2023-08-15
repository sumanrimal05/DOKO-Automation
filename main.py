from pages.authenticate import authenticate
from utilities.setupDriverChrome import browser
from pages.createGame import Game
from pages.createSeason import Season
from pages.createEpisode import Episode
from pages.createPackage import Package
from pages.assignQuestion import AssignQuestion
from utilities.setEnv import setEnv


def main():
    driver = browser()
    env = 'dev'
    # env = 'uat'

    email = "superadmin@mailinator.com"
    password = "123admin@"
    BASE_URL = setEnv(env)
    authenticate(driver, email, password, BASE_URL)

    # game = Game(driver=driver, name_of_game="Nimesh Game", BASE_URL=BASE_URL)
    # game_id = game.create_game()
    # # game_id = "b633d531-0ee3-4ba0-889e-9b3bfc5f59fa"
    # season = Season(driver=driver, game_id=game_id,
    #                 name_of_season="Season", number_of_ads=3, BASE_URL=BASE_URL)
    # season_id = season.create_seasons()
    season_id = "43c548bf-7cbc-476e-b6dd-02ff9e289808"

    # Manual episode
    season_episode_type = "manual"
    game_host_name = "Suman Host"
    game_manager_name = "Suman Manager"
    episode = Episode(driver=driver, name_of_episode="Episode",
                      season_episode_type=season_episode_type, season_id=season_id, game_host_name=game_host_name, game_manager_name=game_manager_name, BASE_URL=BASE_URL)

    # # Auto episode
    # season_episode_type = "auto"
    # episode = Episode(driver=driver, name_of_episode="Episode",
    #                   season_episode_type=season_episode_type, season_id=season_id, BASE_URL=BASE_URL)

    episode_URL = "https://www.youtube.com/watch?v=40SNdIiu9Cw"
    number_of_episodes = 1

    episode_ids, episode_numbers = episode.create_episodes(
        number_of_episodes=number_of_episodes, episode_live_URL=episode_URL)
    # episode_ids = ['epiosde_id_1','epiosde_id_2','epiosde_id_3']
    print("Episode Id are:", episode_ids)
    print("Episode numbers are:", episode_numbers)
    number_of_question = 5
    question = AssignQuestion(driver=driver, BASE_URL=BASE_URL,
                              episode_ids=episode_ids, number_of_question=number_of_question)

    question.assign_questions()
    # episode_numbers = [12]

    episode.publish_episode(episode_numbers, season_id)

    package = Package(driver=driver, season_id=season_id,
                      number_of_episodes=number_of_episodes, BASE_URL=BASE_URL)
    package.update_packages()


if __name__ == "__main__":
    main()
