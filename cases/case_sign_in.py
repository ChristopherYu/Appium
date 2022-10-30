from cases_helper import sign_in
from utilities import get_driver
import configparser
import os


def test_sign_in():
    # init
    project_directory = os.getcwd()
    config = configparser.ConfigParser()
    config.read(f'{project_directory}/configs/config.ini')
    setting = config['GeneralSetting']

    # test data
    test_account = {"account": setting['test_account'], "password": setting['test_password'],
                    "username": setting['test_username']}

    # get driver
    driver = get_driver(project_directory, setting)

    verify_text = sign_in(driver, test_account)
    assert verify_text == "Verify your account"
