import os

SERVER_HOST_ENV_VAR = "SERVER_HOST_ENV_VAR"
SERVER_USR_SSH_NAME_ENV_VAR = "SERVER_USR_SSH_NAME_ENV_VAR"
SERVER_USR_PASS_ENV_VAR = "SERVER_USR_PASS_ENV_VAR"

# For windows console:
#   SET SERVER_HOST_ENV_VAR=127.0.0.1
#   SET SERVER_USR_SSH_NAME_ENV_VAR=vaal12
#   SET SERVER_USR_PASS_ENV_VAR=somepass


class ServerCredentials:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
    

def getCredentialEnvironOnConsole(envVarName, consoleRequest):
    # https://www.freecodecamp.org/news/python-env-vars-how-to-get-an-environment-variable-in-python/
    cred = os.environ.get(envVarName, None)
    if cred == None:
        cred = input(consoleRequest)
    return cred

def getServerCredentials():
    host = getCredentialEnvironOnConsole(SERVER_HOST_ENV_VAR, 
        "Please provide server host address:")
    user = getCredentialEnvironOnConsole(SERVER_USR_SSH_NAME_ENV_VAR, 
        "Please provide server user name:")
    password = getCredentialEnvironOnConsole(SERVER_USR_PASS_ENV_VAR, 
        "Please provide server user password:")
    return ServerCredentials(host, user, password)