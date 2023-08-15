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

    game = Game(driver=driver, BASE_URL=BASE_URL)
    game_id = game.create_game()

    # game_id = "060620ad-3f47-48f9-818f-64bd464abd13"
    season = Season(driver=driver, game_id=game_id,  BASE_URL=BASE_URL)
    season_id = season.create_seasons()

    # season_id = "767628a9-e4f5-4ed2-8e71-0d6da89e7649"
    number_of_episodes = 5
    episode = Episode(driver=driver, season_id=season_id, BASE_URL=BASE_URL)
    episode_ids, episode_numbers = episode.create_episodes(
        number_of_episodes=number_of_episodes)

    # episode_ids = ['epiosde_id_1','epiosde_id_2','epiosde_id_3'] --> You can add question to existing episode by providing
    # their epiosode id here
    number_of_question = 5
    question = AssignQuestion(driver=driver, BASE_URL=BASE_URL,
                              episode_ids=episode_ids, number_of_question=number_of_question)
    question.assign_questions()

   # episode_numbers[10,11,12] --> This will publish episode 10, 11,12 of the season
    # episode_numbers = [12]
    episode.publish_episode(episode_numbers, season_id)

    package = Package(driver=driver, season_id=season_id,
                      number_of_episodes=number_of_episodes, BASE_URL=BASE_URL)
    package.update_packages()


if __name__ == "__main__":
    main()
