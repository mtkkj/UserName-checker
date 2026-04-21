import random
import string 
import requests
import os
import time
import json
from colorama import Fore,init
import datetime
from configparser import ConfigParser
import sys
init(autoreset=True)
__version__ = "Author: suenerve DSV 1.9"
__github__= "https://github.com/suenerve"

def get_base_dir():
   if getattr(sys, "frozen", False):
      return os.path.dirname(sys.executable)
   return os.path.dirname(os.path.realpath(__file__))

dir_path = get_base_dir()
configur = ConfigParser()
configur.read(os.path.join(dir_path, f"config.ini"))
tokens_list = os.path.join(dir_path, f"tokens.txt")
integ_0 = 0
sys_url = "https://discord.com/api/v9/users/@me"
URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"
def s_sys_h():
   if configur.getboolean("sys","MULTI_TOKEN") == True:
      return {
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":avail_tokens(tokens_list)[integ_0]
    }
   elif configur.getboolean("sys","MULTI_TOKEN") == False:
      return{
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":configur.get("sys","TOKEN")
    }
   else:
      return {
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":configur.get("sys","TOKEN")
    }
def sys_c_t():
   if configur.get("sys","TOKEN") != "":
      pass
   elif configur.get("sys","TOKEN") == "" and configur.getboolean("sys","MULTI_TOKEN") == False:
        print(f"{Lb}[!]{Fore.RED} No token found. You must paste your token inside the 'config.ini' file, in front of the value 'TOKEN'.")
        exit()
   elif configur.getboolean("sys","MULTI_TOKEN") == True and not avail_tokens(tokens_list)[0]:
       print(f"{Lb}[!]{Fore.RED} No tokens found. You must paste your tokens inside the 'tokens.txt' file.")
       exit()
   elif configur.getboolean("sys","MULTI_TOKEN") is not True and configur.getboolean("sys","MULTI_TOKEN") is not False and configur.get("sys","TOKEN") == "":
       print(f"{Lb}[!]{Fore.RED} Invalid config detected. Please re-check the config file, `config.ini` and your settings.")
       exit()
available_usernames = []
av_list = os.path.join(dir_path, f"available_usernames.txt")
sample_0 = r"_."
Lb = Fore.LIGHTBLACK_EX
Ly = Fore.LIGHTRED_EX

def ensure_config():
   config_path = os.path.join(dir_path, "config.ini")
   required_sections = ("sys", "config")

   if not os.path.exists(config_path):
      print(f"{Lb}[!]{Fore.RED} Arquivo 'config.ini' nao encontrado em: {config_path}")
      print(f"{Lb}[!]{Ly}Coloque o 'config.ini' na mesma pasta do executavel.")
      sys.exit(1)

   missing_sections = [section for section in required_sections if not configur.has_section(section)]
   if missing_sections:
      print(f"{Lb}[!]{Fore.RED} Configuracao invalida. Secoes ausentes: {', '.join(missing_sections)}")
      print(f"{Lb}[!]{Ly}O 'config.ini' precisa conter as secoes [sys] e [config].")
      sys.exit(1)

ensure_config()
Delay = configur.getfloat("config","default_delay")

def fetch_current_user():
   try:
      response = requests.get(sys_url, headers=s_sys_h(), timeout=10)
      data = response.json()
   except (requests.RequestException, ValueError):
      return None

   if isinstance(data, dict) and data.get("username"):
      return data
   return None

def connected_as():
   user = fetch_current_user()
   if not user:
      return "Unknown User"

   discriminator = user.get("discriminator")
   if discriminator and discriminator != "0":
      return f"{user['username']}#{discriminator}"
   return user["username"]

def setconf():
   global string_0
   global digits_0
   global punctuation_0
   global webhook_0
   #global multi_token_0
   global sat_string
   global sat_digits
   global sat_multi_token
   global sat_punct
   global sat_webhook
   sat_webhook = configur.get("sys","WEBHOOK_URL")
   sat_string = configur.getboolean("config","string")
   sat_digits = configur.getboolean("config","digits")
   sat_punct = configur.getboolean("config","punctuation")
   sat_multi_token = configur.getboolean("sys","MULTI_TOKEN")
   if sat_webhook =="":
      webhook_0 = False
   elif sat_webhook !="":
      webhook_0 = True
   if sat_string == True:
      string_0 = string.ascii_lowercase
   elif sat_string == False:
      string_0 = ""
   else:
      string_0 = string.ascii_lowercase
      sat_string = True
   if sat_digits == True:
      digits_0 = string.digits
   elif sat_digits == False:
      digits_0 = ""
   else:
      digits_0 = string.digits
      sat_digits = True
   if sat_punct == True:
      punctuation_0 = sample_0
   elif sat_punct == False:
      punctuation_0 = ""
   else:
      punctuation_0 = sample_0
      sat_punct = True
   if sat_punct == False and sat_digits == False and sat_string == False:
      punctuation_0 = sample_0
      digits_0 = string.digits
      string_0 = string.ascii_lowercase

def main():
    sys_c_t()
    current_user = fetch_current_user()
    if not current_user:
        print(f"{Lb}[!]{Fore.RED} Couldn't fetch account details from Discord. Make sure your token is valid and still works.")
        exit()

    display_name = connected_as()
    os.system(f"title {__version__} - Connected as {display_name}")
    s_sys_h()
    setconf()    
    print(f"""{Fore.LIGHTRED_EX}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                       
                                          {Fore.WHITE}Connected as {display_name}{Ly}
                            
███    ███ ████████                     {Fore.WHITE}1-{Fore.LIGHTBLACK_EX}[{Fore.RED}Gerar user e checkar{Fore.LIGHTBLACK_EX}]{Ly}             
████  ████    ██                        {Fore.WHITE}2-{Fore.LIGHTBLACK_EX}[{Fore.RED}Checkar lista especifica{Fore.LIGHTBLACK_EX}]{Ly}             
██ ████ ██    ██                       
██  ██  ██    ██                       Config.ini:
██      ██    ██                         {Fore.WHITE}Números: {Fore.RED}{sat_digits}{Ly}
██      ██    ██                         {Fore.WHITE}Letras: {Fore.RED}{sat_string}{Ly}
██      ██    ██                         {Fore.WHITE}Pontuação: {Fore.RED}{sat_punct}{Ly}
                                         {Fore.WHITE}Vários tokens: {Fore.RED}{sat_multi_token}{Ly}
                                         {Fore.WHITE}Webhook: {Fore.RED}{webhook_0}{Ly}
                                         {Fore.WHITE}Delay: {Fore.RED}{Delay}{Ly}
                                                         

  Disponibilidade de User no Discord
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")
    proc0()
    
def setdelay():
   global Delay
   print(f"{Lb}[!]{Ly} Delay Padrão: {Delay}s (config.ini){Lb}")
   d_input = input(f"{Lb}[{Ly}Editar Delay (Aperte Enter para Pular){Lb}]:> ")
   if d_input=="" or d_input.isspace():
      return
   else:   
    try:
      int(d_input)
      Delay = int(d_input)
    except ValueError:
      print(f"{Lb}[!]{Fore.RED}Erro: Você deve inserir um número inteiro válido. Não Letras.")
      setdelay()

def proc0():
    m_input = input(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}MT{Fore.LIGHTBLACK_EX}]:> {Fore.LIGHTYELLOW_EX}").lower()
    if m_input=="exit":
        sys.exit(0)
    if m_input=="":
        proc0()
    elif m_input=="2":
        setdelay()
        opt2load()
    elif m_input=="1":
       setdelay()
       opt1load()
    else:
        proc0()
def validate_names(opt,usernames):
   global available_usernames
   global integ_0
   if opt == 2:
    for username in usernames:
       body = {
           "username": username
       }
       time.sleep(Delay)
       endpoint = requests.post(URL, headers=s_sys_h(), json=body)
       json_endpoint = endpoint.json()
       if endpoint.status_code == 429 and sat_multi_token == True and len(avail_tokens(tokens_list)) != integ_0:
           integ_0 = (integ_0 +1) % len(avail_tokens(tokens_list))
           print(f"{Lb}[!]{Ly} Token {integ_0} tomou rate limited. Usando token: {integ_0} conectado a: {connected_as()}")
       elif endpoint.status_code == 429 and sat_multi_token == False:
         sleep_time = endpoint.json()["retry_after"]
         print(f"{Lb}[!]{Fore.RED} Rate limit . Pausado por {sleep_time}s (Discord rate limit)")
         time.sleep(sleep_time)
       if json_endpoint.get("taken") is not None:
           if json_endpoint["taken"] is False:
            print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{username}' available.")
            ch_send_webhook(username)
            save(username)
            available_usernames.append(username)
           elif json_endpoint["taken"] is True:
              print(f"{Lb}[-]{Fore.RED} '{username}' taken.")
       else:
           print(f"{Lb}[?]{Fore.RED} Erro ao validar '{username}': {endpoint.json()['message']} Verifique de ter um token válido.")
   elif opt == 1:
       body = {
           "username": usernames
       }
       endpoint = requests.post(URL, headers=s_sys_h(), json=body)
       json_endpoint = endpoint.json()
       if endpoint.status_code == 429 and len(avail_tokens(tokens_list)) != integ_0 and sat_multi_token == True:
           integ_0 = (integ_0 +1) % len(avail_tokens(tokens_list))
           print(f"{Lb}[!]{Ly} Token {integ_0} tomou rate limited. Usando token: {integ_0} conectado a: {connected_as()}")
       elif endpoint.status_code == 429 and sat_multi_token == False:
         sleep_time = endpoint.json()["retry_after"]
         print(f"{Lb}[!]{Fore.RED} Rate limit. Pausado por {sleep_time}s (Discord rate limit)")
         time.sleep(sleep_time)
       if json_endpoint.get("taken") is not None:
           if json_endpoint["taken"] is False:
            print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{usernames}' disponivel.")
            ch_send_webhook(usernames)
            save(usernames)
            available_usernames.append(usernames)
           elif json_endpoint["taken"] is True:
              print(f"{Lb}[-]{Fore.RED} '{usernames}' taken.")
       else:
           print(f"{Lb}[?]{Fore.RED} Erro ao validar '{usernames}': {endpoint.json()['message']} Verifique de ter um token válido.")
def avail_tokens(path):
   with open(path, 'r') as at:
        tokens = at.read().splitlines()
   return tokens
def exit():
   input(f"{Fore.YELLOW}Pressione Enter para sair.")
   sys.exit(0)
def checkavail(): 
   if len(available_usernames) < 1:
      print(f"{Lb}[!]{Fore.RED} Erro: Nenhum nome de usuário disponível encontrado.")
      exit()
   else:
      return
def opt2load():
    global av_list
    global dir_path
    list_path = os.path.join(dir_path, f"usernames.txt")
    print(f"{Lb}[!]{Ly}Checkando 'usernames.txt' para validar...")
    try:
     with open(list_path) as file:
      usernames = [line.strip() for line in file]
      validate_names(2,usernames)
     checkavail()
     print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
     exit()
    except FileNotFoundError:
       print(f"{Lb}[!]{Fore.RED} Erro: Não foi possível encontrar a lista (usernames.txt). Certifique-se de criar um arquivo de lista válido no mesmo diretório: \n({dir_path}\\)")
       exit()
def opt1load():
   opt1_input:int = input(f"{Lb}[{Ly}Quantas letras no nome de usuário{Lb}]:> ")
   try:
    int(opt1_input)
    if int(opt1_input) >32 or int(opt1_input) <2:
       print(f"{Lb}[!]{Fore.RED} Erro: O nome de usuário deve conter entre 2 e 32 caracteres.")
       opt1load()
    opt2_input:int = input(f"{Lb}[{Ly}Quantos nomes de usuário gerar{Lb}]:> ")
    opt1func(int(opt2_input),int(opt1_input))
   except ValueError:
      print(f"{Lb}[!]{Fore.RED} Erro: Você deve inserir um número inteiro válido. Nenhuma letra permitida.")
      opt1load()
def save(content:string):
   with open(av_list, "a") as file:
        file.write(f"\n{content}")
def ch_send_webhook(val0:str):
   if webhook_0 == True:
    webhook = Discord(url=sat_webhook)
    try:
     webhook.post(
       username="User",
       avatar_url="https://i.pinimg.com/1200x/e4/aa/ea/e4aaeaa23844ea0f489b1237b9bb1352.jpg",
       embeds=[
    {
      "title": f"<:Seta:1490393391798681803> User disponivel: `{val0}`",
      "fields": [],
      "color": 000000
    }
  ],

    )
    except Exception as s:
       print(f"{Lb}[!]{Fore.RED} Erro: Algo deu errado ao enviar a solicitação do webhook. Exceção: {s} Certifique-se de ter uma URL de webhook válida")
   else:
      return
def opt1func(v1,v2):
   for i in range(v1):
    name = get_names(int(v2))
    validate_names(1,name)
    time.sleep(Delay)
   checkavail()
   print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Concluído. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Os nomes de usuário disponíveis são salvos no seguinte arquivo: '{av_list}' .")
   exit()
def get_names(length: int) ->str:
   return ''.join(random.sample(string_0 + digits_0 + punctuation_0, length))
# Source of this class: https://github.com/10mohi6/discord-webhook-python/blob/master/discordwebhook/discordwebhook.py
class Discord:
    def __init__(self, *, url):
        self.url = url
    def post(
        self,
        *,
        content=None,
        username=None,
        avatar_url=None,
        tts=False,
        file=None,
        embeds=None,
        allowed_mentions=None
    ):
        if content is None and file is None and embeds is None:
            raise ValueError("required one of content, file, embeds")
        data = {}
        if content is not None:
            data["content"] = content
        if username is not None:
            data["username"] = username
        if avatar_url is not None:
            data["avatar_url"] = avatar_url
        data["tts"] = tts
        if embeds is not None:
            data["embeds"] = embeds
        if allowed_mentions is not None:
            data["allowed_mentions"] = allowed_mentions
        if file is not None:
            return requests.post(
                self.url, {"payload_json": json.dumps(data)}, files=file
            )
        else:
            return requests.post(
                self.url, json.dumps(data), headers={"Content-Type": "application/json"}
            )
if __name__ == "__main__":
    main()
