from cases_helper import login
from utilities import get_driver
import configparser
import os


def test_login():
    # init
    project_directory = os.getcwd()
    config = configparser.ConfigParser()
    config.read(f'{project_directory}/configs/config.ini')
    setting = config['GeneralSetting']

    driver = get_driver(project_directory, setting)

    try:
        login(driver, setting['test_account'])
        assert True
    except Exception as e:
        print(e)
        assert False
