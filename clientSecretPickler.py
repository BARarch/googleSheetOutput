import jsonpickle

def get_project_id(client_secret_file_name='client_secret.json'):
    ''' Be sure that your client secrets file is in the same directory as 
        the python runtime
    '''
    try:
        f = open(client_secret_file_name, 'r')
        
    except FileNotFoundError:
        raise FileNotFoundError("Plug in the client secrets, go to the developer console and get your client secret file, then bring it to the directory of the pyhton runtime")

    secret = jsonpickle.decode(f.read())
    f.close()

    return secret["web"]["project_id"]