import configparser

credentials_file = '~/.aws/credentials'

# mac
# - cat ~/.aws/credentials

# win
# - C:\Users\inseop\.aws\credentials
# - type C:\Users\inseop\.aws\credentials

config = configparser.ConfigParser()
config.read(credentials_file)