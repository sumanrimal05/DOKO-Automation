from constants import constants


def setEnv(self, env='dev'):
    try:

        if (env == 'dev'):
            BASE_URL = constants.DEV_URL
            return BASE_URL

        elif (env == 'uat'):
            BASE_URL = constants.UAT_URL
            return BASE_URL

    except Exception as e:
        print(f"Make sure the env is either dev or uat, Error:{e}")
