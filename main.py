from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import json

if not os.path.isfile("conf.json"):
    site_name = input("Enter your site name: ")
    path_to_services = input("Enter your folder with services (ex. /home/admin/My\ Services/): ")
    domain_api = input("Domain name for api (ex. https://88:88:88:88/): ")
    site_conf = { "path_to_services": path_to_services, "domain_api": domain_api, "site_name": site_name }
    with open("conf.json", "w") as conf_file:
        json.dump(site_conf, conf_file)

path_to_services = ""
domain_api = ""
site_name = ""

with open("conf.json", "r") as conf_file:
    site_conf = json.load(conf_file)
    domain_api = site_conf["domain_api"]
    path_to_services = site_conf["path_to_services"]
    site_name = site_conf["site_name"]

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
    return {
        "title": site_name,
        "services": domain_api + "services",
    }

@app.get("/services")
async def services_list():
    return [
        {
            "id": 0,
            "text": "Testing first message.",
        },
        {
            "id": 1,
            "text": "Testing second message.",
        },
        {
            "id": 2,
            "text": "Testing third message.",
        },
        {
            "id": 3,
            "text": "Testing fourth message.",
        },
    ]

@app.get("/services/{service_id}")
async def read_service(service_id):
    return {"service_id": service_id}
