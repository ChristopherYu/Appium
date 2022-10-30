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

    driver = get_driver(project_directory, setting)
    test_account = {"account": setting['test_account'], "password": setting['password']}
    login_account_name = sign_in(driver, test_account)
    assert login_account_name == "expect_account_name"
