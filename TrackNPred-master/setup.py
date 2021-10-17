#taken from this StackOverflow answer: https://stackoverflow.com/a/39225039
import requests
import shutil
import subprocess
import os

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    print("Downloading file from google drive...")
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    print("have write to destination")

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def download_legacy(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    print("Downloading file from google drive...")
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination) 


if __name__ == "__main__":
    if(not os.path.isdir("resources")):
        file_id = '1jIpA-xQZIjKYz2_ixZ_CPC8ZKgI9h1K7'
        destination = 'resources.tar'	
        download_file_from_google_drive(file_id, destination)
        subprocess.call(["tar", "-xvf", "resources.tar"])
        #subprocess.call(["rm", "resources.tar"])
        #subprocess方法 https://www.cnblogs.com/zhou2019/p/10582716.html  https://www.runoob.com/w3cnote/python3-subprocess.html
    else:
        print("resources folder already exists. Not downloading")

    #install the requirement at first
    install = False
    if install:

        print("installing mask r-cnn")
        subprocess.call(["pip", "install", "-r", "model/Detection/Mask/requirements.txt"])
        os.chdir("model/Detection/Mask") #https://www.runoob.com/python/os-chdir.html   os.chdir
        subprocess.call(["python3", "setup.py", "install"])
