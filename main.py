from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import json
from bot import *
from pydantic import BaseModel

class Message(BaseModel):
    phone: str
    description: str | None = None

app = FastAPI()

if not os.path.isfile("conf.json"):
    site_name = input("Enter your site name: ")
    path_to_services = input("Enter your folder with services (ex. /home/admin/My Services/): ")
    domain_api = input("Domain name for api (ex. https://88:88:88:88/): ")
    BOT_TOKEN = input("Enter your telegram bot token: ")
    chat_id = input("Enter your private chat id: ")
    site_conf = { "path_to_services": path_to_services, "domain_api": domain_api, "site_name": site_name, "BOT_TOKEN": BOT_TOKEN, "chat_id": chat_id }
    with open("conf.json", "w") as conf_file:
        json.dump(site_conf, conf_file)

path_to_services = ""
domain_api = ""
site_name = ""
BOT_TOKEN = ""
chat_id = ""

with open("conf.json", "r") as conf_file:
    site_conf = json.load(conf_file)
    domain_api = site_conf["domain_api"]
    path_to_services = site_conf["path_to_services"]
    site_name = site_conf["site_name"]
    BOT_TOKEN = site_conf["BOT_TOKEN"]
    chat_id = site_conf["chat_id"]

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    nav_bar_items_list = os.listdir(path_to_services)
    nav_bar_item = {}
    nav_bar_items = []
    i = 0
    while i < len(nav_bar_items_list):
        url = "/" + nav_bar_items_list[i].lower()
        if nav_bar_items_list[i].startswith(".") == False:
            nav_bar_items.append({"id": i, "title": nav_bar_items_list[i], "url": url})
        i += 1
    return {
        "title": site_name,
        "items": nav_bar_items,
    }

@app.post("/form")
async def message(message: Message):
    send_message(BOT_TOKEN, chat_id, message)
    return message

@app.get("/{item}")
async def items_list(item):
    items_list = os.listdir(path_to_services + item)
    items = []
    i = 0
    while i < len(items_list):
        items.append({"id": i, "text": items_list[i]})
        i += 1
    return items
