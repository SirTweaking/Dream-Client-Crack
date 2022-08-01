from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

client_config = {
    "esp": True,
    "bhop": False,
    "xray": False,
    "reach": False,
    "clicker": True,
    "tracers": False,
    "esp_mode": "esp_3d",
    "velocity": False,
    "aimassist": True,
    "esp_color": "22,22,22",
    "xray_coal": False,
    "xray_gold": False,
    "xray_iron": False,
    "bhop_speed": 1,
    "esp_health": False,
    "xray_lapis": False,
    "clicker_cps": 18,
    "esp_keybind": -1,
    "reach_range": 3.07,
    "reach_walls": False,
    "bhop_keybind": -1,
    "reach_liquid": False,
    "xray_diamond": False,
    "xray_emerald": False,
    "xray_keybind": -1,
    "aimassist_fov": 326,
    "bridge_assist": False,
    "reach_keybind": -1,
    "tracers_color": "255,255,255",
    "xray_redstone": False,
    "aimassist_lock": False,
    "velocity_delay": 5,
    "aimassist_speed": 20,
    "aimassist_walls": False,
    "clicker_keybind": -1,
    "reach_sprinting": False,
    "tracers_keybind": -1,
    "aimassist_nakeds": False,
    "esp_draw_corners": False,
    "tracers_distance": False,
    "velocity_keybind": -1,
    "aimassist_keybind": -1,
    "clicker_axes_only": False,
    "esp_draw_expanded": False,
    "velocity_clicking": False,
    "velocity_vertical": 100,
    "aimassist_clickaim": False,
    "aimassist_distance": 5.38,
    "velocity_push_back": False,
    "aimassist_axes_only": False,
    "clicker_swords_only": False,
    "esp_draw_invisibles": False,
    "velocity_horizontal": 98,
    "aimassist_multipoint": False,
    "bridge_assist_blocks": False,
    "clicker_break_blocks": False,
    "aimassist_breakblocks": False,
    "aimassist_swords_only": False,
    "bridge_assist_keybind": -1,
    "clicker_menu_whitelist": False,
    "bridge_assist_pitch_check": False,
}


@app.get("/api/guides")
async def get_guides(filter: str = "all"):
    return [
        {"id": 1, "title": "How to set up your HWID", "type": "SETUP"},
        {"id": 10, "title": "How to bypass#1 (No USB, Recommended)", "type": "BYPASS"},
    ]


@app.get("/api/guides/{guide_id}")
async def get_guide(guide_id: int):
    guides = [
        {
            "id": 1,
            "title": "How to set up your HWID",
            "body": [
                {"type": "title", "content": "Download Dream and log in. Your HWID is copied to your clipboard."},
                {"type": "image", "content": "guides/b0yjOLhfiIukdGviUJeaqP0zoRO78yUs3rWlhB2q.png"},
                {
                    "type": "title",
                    "content": 'Go to the "Settings" page and paste the contents of your clipboard in the HWID section.',
                },
                {"type": "image", "content": "guides/hsz8Nv1ywKYFW6uk5LxpnDXkxdrs7UOPr6IL0QdG.png"},
            ],
            "created_at": "2021-11-22T23:53:54.000000Z",
            "updated_at": "2021-11-22T23:53:54.000000Z",
            "type": "SETUP",
        },
        {
            "id": 10,
            "title": "How to bypass#1 (No USB, Recommended)",
            "body": [
                {"type": "title", "content": "Disabling MsMpEng"},
                {
                    "type": "text",
                    "content": "Press start and search up \u201cVirus & threat protection\u201d. Press manage settings under \u201cVirus and threat protection\u201d. Uncheck \u201cReal-time protection\u201d and \u201cTamper protection\u201d. Open your browser in incognito. Go to https:\/\/dreamclient.xyz\/i\/dControl.7z. Extract the files and open dControl.exe. Press Disable and delete all the files.",
                },
                {"type": "image", "content": "guides/oiEdFJEKeN3xKj02wAbkSqDdmm4npcPqGCOKbxJC.png"},
                {"type": "title", "content": "Disabling Smartscreen"},
                {
                    "type": "text",
                    "content": "Press start and type: \u201cWindows Security\u201d. On the left side select \u201cApp & Browser control\u201d. Select \u201cReputation-based protection\u201d. Turn off \u201cCheck apps and files\u201d, \u201cSmartscreen for Edge\u201d and \u201d Smartscreen for Microsoft Store Apps.",
                },
                {"type": "image", "content": "guides/KUwodl3c8JfqRuDSJJ86kP6mrjHWtz4ndsZ8t6yM.png"},
                {"type": "title", "content": "Preparing Windows processes"},
                {
                    "type": "text",
                    "content": "Press the Windows key + R. Type: \u201cservices.msc\u201d and press OK. Find \u201cDiagnostic Policy Service\u201d (DPS), double click it, set the \u201cStartup type\u201d to Automatic, press \u201cApply\u201d, then press \u201cStart\u201d. Find \u201cProgram Compatibility Assistant Service\u201d (PcaSvc), double click it, set the \u201cStartup type\u201d to Automatic, press \u201cApply\u201d, then press \u201cStart\u201d.",
                },
                {"type": "image", "content": "guides/Oy0vzbzq1aZgHXzPZcVwIOwc5oEFrDFfcasFQaUw.png"},
                {"type": "title", "content": "Cleaning old logs"},
                {
                    "type": "text",
                    "content": 'Open \u201cFile Explorer\u201d. In the top left press \u201cFile\u201c then "Change folder and search options\u201c. Press clear. Close File Explorer. In your start menu search up \u201ccmd\u201c and open it as an administrator. Type: \u201c fsutil usn deletejournal \/D C: \u201c',
                },
                {"type": "title", "content": "Preparing your browser"},
                {
                    "type": "text",
                    "content": "-If you\u2019re using Edge: Press the three dots in the top right and press Settings. Search up \u201cAsk me what to do with each download\u201d and enable this option. Search up \u201cDownloads\u201d and uncheck \u201cDefender Smartscreen\u201d and \u201cBlock potentially unwanted apps\u201d. -If you\u2019re using Firefox: Press the three lines in the top right and press Options. Search up \u201cDownloads\u201d. Check \u201cAlways ask you where to save files\u201d. Uncheck \u201cBlock dangerous downloads\u201d and \u201cWarn you about potentially unwanted and uncommon software\u201d.",
                },
                {"type": "image", "content": "guides/tJlRQA3lp9ORXLs9lKMbLnIYzKFqvCpW9Gu8gqSr.png"},
                {"type": "title", "content": "Setting up the client"},
                {
                    "type": "text",
                    "content": 'Open "File Explorer Options", go to "View" and uncheck "Hide extensions for know file types. Download dream with any name, and find a folder where you will hide it. (We reccomend places like application folders like Synapse, Discord, Lunar etc You cannot use protected fodlers like System32) Rename your Dream file to something similar to .dlls you see in the folder you chose. (For example Synapse3.Macros.xxx.dll, Microsoft.Owin.xxx.dll, vgrl.dll) After you\'ve chosen the name of your file make sure you change the extension from .exe to .dll and place the cheat in that folder. Open "Task Scheduler" and go to "Task Scheduler Library". Press right click and select "Create new task" (Not Create new basic task). Give it a believeable name. (For example if you chose something like Syanpse you would name it Razer Synapse Update) Copy the name and paste it in "Description".\n\nSelect "Hidden", under "Configure for:" select Windows 10. Go to "Triggers", press "New", under "Begin the task" select "At startup". Go to "Actions", press "New", under "Action" select "Start a program". Under "Program \/ Script" type the location of your cheat. (For example: C:\\Program Files (x86)Razer\\Razer Services\\Razer Central\\Microsoft.Practices.Core.dll) Make sure there are no " symbols! Under "Add Arguments" type "\/c vshost.exe" If a new window pops up after pressing "OK" select "Yes." Under "Conditions" uncheck "Start the task only if the computer is on AC Power" and "Stop if the computer switches to battery power" Restart your pc! (IMPORTANT!!!)',
                },
                {"type": "image", "content": "guides/pKeUBFDmksiJjF3yjNqL1RkkA6nhz4ai3KLVZW2e.png"},
                {"type": "title", "content": "Cheating"},
                {
                    "type": "text",
                    "content": 'As soon as your computer boots up, Dream will too. If it doesn\'t, open Task Scheduler, right click your fake schedule and press Run. Open a lot of random programs. Log in, open Minecraft, inject like usual. Open "Regedit", go to "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\bam\\State\\UserSettings" Right click on the UserSettings folder on the left side and select Permissions. Select "Administrators" and check "FULL CONTROL".\n\nYou will see a lot of folders (S-1-5-xx-xxxxxx), go through them until you notice the one with a lot of results. (One will have a lot, others will have 4-5 results) Inside that folder press CTRL+F and Search up the name of the cheat. Right click the cheat and select Delete. Right click on the UserSettings folder on the left side again and select Permissions. Select "Administrators" and uncheck "FULL CONTROL". Close all the folders with the little down arrow.',
                },
                {"type": "image", "content": "guides/Vnj9KVizSCRAl5NdZH9e9mZrYIihBxiiHKfYPwvw.png"},
                {"type": "title", "content": "Frozen"},
                {
                    "type": "text",
                    "content": 'Open "Task Scheduler", right click on your fake schedule and press Delete.',
                },
                {"type": "image", "content": "guides/smE0pXBxQmnc1KxCVnYJUFhNZFU9MrSgJWmhUOPx.png"},
                {"type": "text", "content": "Thank you Kendo for massively helping Dream \u2764\ufe0f"},
            ],
            "created_at": "2022-05-22T11:45:51.000000Z",
            "updated_at": "2022-05-22T11:45:51.000000Z",
            "type": "BYPASS",
        },
    ]
    for guide in guides:
        if guide.get("id") == guide_id:
            return guide

    return {"state": False}


@app.post("/api/users/self/state")
async def update_state():
    return {"state": True}


@app.post("/api/configs/me/set")
async def update_config(request: Request):
    json = await request.json()
    client_config[json["key"]] = json["value"]

    return {"state": True}


@app.get("/api/changelog")
async def get_changelog():
    return [
        {
            "id": 27,
            "version": "4.6d CRACKED",
            "beta": False,
            "features": [{"text": "Dream client is now FREE!", "type": "add"}],
            "created_at": "2022-07-08T18:44:33.000000Z",
            "updated_at": "2022-07-08T18:44:33.000000Z",
        },
        {
            "id": 26,
            "version": "4.6d",
            "beta": False,
            "features": [{"text": "Record proof is now togglable through the ESP module", "type": "modify"}],
            "created_at": "2022-07-08T18:44:33.000000Z",
            "updated_at": "2022-07-08T18:44:33.000000Z",
        },
        {
            "id": 22,
            "version": "4.6c",
            "beta": False,
            "features": [
                {"text": "OBS proof visuals now disabled by default, LCTRL+LSHIFT+V to toggle", "type": "modify"}
            ],
            "created_at": "2022-06-22T15:22:17.000000Z",
            "updated_at": "2022-06-22T15:22:17.000000Z",
        },
        {
            "id": 21,
            "version": "4.6b",
            "beta": False,
            "features": [
                {
                    "text": "Visuals are now ignored when recording the minecraft application (Recording bypass)",
                    "type": "modify",
                }
            ],
            "created_at": "2022-06-08T15:11:01.000000Z",
            "updated_at": "2022-06-08T15:11:01.000000Z",
        },
        {
            "id": 20,
            "version": "4.6a",
            "beta": False,
            "features": [{"text": "Blink module", "type": "add"}],
            "created_at": "2022-05-30T16:07:53.000000Z",
            "updated_at": "2022-05-30T16:07:53.000000Z",
        },
        {
            "id": 18,
            "version": "4.6",
            "beta": False,
            "features": [{"text": "New Loader", "type": "add"}, {"text": "Improved Stability", "type": "modify"}],
            "created_at": "2022-03-27T22:30:29.000000Z",
            "updated_at": "2022-03-27T22:30:29.000000Z",
        },
        {
            "id": 17,
            "version": "4.3",
            "beta": False,
            "features": [
                {"text": "3D Mode ESP", "type": "add"},
                {"text": "Tracers", "type": "add"},
                {"text": "X-Ray", "type": "add"},
                {"text": "More ESP conditionals", "type": "add"},
                {"text": "Velocity Push-back feature", "type": "add"},
                {"text": "Bridge assist pitch check feature", "type": "add"},
                {"text": "Bugs Fixed", "type": "modify"},
                {"text": "BLC Support", "type": "add"},
            ],
            "created_at": "2022-01-17T21:26:02.000000Z",
            "updated_at": "2022-01-17T21:26:02.000000Z",
        },
        {
            "id": 16,
            "version": "4.1.1",
            "beta": False,
            "features": [
                {"text": '"Beep" sound after destructing', "type": "remove"},
                {"text": "New security checks", "type": "add"},
            ],
            "created_at": "2021-12-04T21:21:40.000000Z",
            "updated_at": "2021-12-04T21:21:40.000000Z",
        },
        {
            "id": 14,
            "version": "4.1.0",
            "beta": False,
            "features": [
                {"text": "Completely new design of the website", "type": "add"},
                {"text": "Ticket System", "type": "add"},
                {"text": "Two new GUIs", "type": "add"},
                {"text": "Pop-out feature", "type": "add"},
                {"text": "Bhop & BridgeAssist added", "type": "add"},
                {"text": "Cloud based configs and guides", "type": "add"},
                {"text": "Email system", "type": "add"},
                {"text": "Coinbase added as a payment method", "type": "add"},
                {"text": "Fixed keybinds (They're instant now!)", "type": "add"},
                {"text": "Patched all detection methods", "type": "modify"},
                {"text": "Bugs", "type": "remove"},
            ],
            "created_at": "2021-11-23T00:27:24.000000Z",
            "updated_at": "2021-11-23T00:27:24.000000Z",
        },
        {
            "id": 12,
            "version": "4.0.1",
            "beta": False,
            "features": [
                {"text": "Fixed issues related to visual modules", "type": "modify"},
                {"text": "Improved destruct module", "type": "modify"},
            ],
            "created_at": "2021-10-21T00:08:21.000000Z",
            "updated_at": "2021-11-23T00:08:21.000000Z",
        },
        {
            "id": 11,
            "version": "4.0",
            "beta": False,
            "features": [
                {"text": "Recoded AutoClicker (added Swords\/Axes only, fixed menu whitelist)", "type": "add"},
                {"text": "Recoded Reach (added disable in liquids, sprinting only, hit through walls)", "type": "add"},
                {
                    "text": "Recoded AimAssist (added break blocks, lock target, aim through walls, Swords\/Axes only)",
                    "type": "add",
                },
                {"text": "Recoded Velocity (added clicking only)", "type": "add"},
                {"text": "Added ESP (added show health option)", "type": "add"},
                {"text": "Bhop \/ BridgeAssist coming soon", "type": "add"},
                {"text": "Fixed Keybinds", "type": "modify"},
                {"text": "Fixed all detections", "type": "modify"},
                {"text": "Removed RightClicker", "type": "remove"},
            ],
            "created_at": "2021-10-20T00:08:03.000000Z",
            "updated_at": "2021-11-23T00:08:03.000000Z",
        },
        {
            "id": 10,
            "version": "3.0",
            "beta": True,
            "features": [
                {"text": "Added Disabled in menus check to autoclicker", "type": "add"},
                {"text": "AimAssist (MultiPoint, Click Aim, Angle\/Speed\/Distance)", "type": "add"},
                {"text": "Right Clicker", "type": "add"},
                {"text": "Better AntiTamper", "type": "add"},
                {"text": "Reworked Velocity (Horizontal\/Vertical, added Delay", "type": "modify"},
                {"text": "Cpu Usage", "type": "modify"},
                {"text": "Reworked randomizer", "type": "modify"},
            ],
            "created_at": "2021-02-20T00:05:24.000000Z",
            "updated_at": "2021-11-23T00:05:24.000000Z",
        },
        {
            "id": 8,
            "version": "2.4",
            "beta": False,
            "features": [
                {"text": "Added how to bypass guide on discord !", "type": "add"},
                {"text": "Patched Detections", "type": "add"},
            ],
            "created_at": "2020-11-11T00:04:27.000000Z",
            "updated_at": "2021-11-23T00:04:27.000000Z",
        },
        {
            "id": 7,
            "version": "2.3",
            "beta": False,
            "features": [{"text": "Internal improvements", "type": "modify"}],
            "created_at": "2020-10-06T00:04:03.000000Z",
            "updated_at": "2021-11-23T00:04:03.000000Z",
        },
        {
            "id": 6,
            "version": "2.1",
            "beta": False,
            "features": [{"text": "Improved security", "type": "modify"}],
            "created_at": "2020-08-25T00:03:54.000000Z",
            "updated_at": "2021-11-23T00:03:54.000000Z",
        },
        {
            "id": 5,
            "version": "2.0",
            "beta": False,
            "features": [
                {"text": "Velocity module (horizontal)", "type": "add"},
                {"text": "Keybinds (will work smooth depending on your ping to server)", "type": "add"},
                {"text": "Changelog system", "type": "add"},
                {"text": "Settings section", "type": "add"},
                {"text": "Ability to choose the cheat name when downloading", "type": "add"},
                {"text": "Reach now goes to 6 blocks and uses 3.xx format", "type": "add"},
                {"text": "Complete ground up recode of the website with a stylish and secure design", "type": "modify"},
                {"text": "Improved randomizer", "type": "modify"},
                {"text": "Mouse sensitivity bug", "type": "remove"},
            ],
            "created_at": "2020-08-08T00:03:27.000000Z",
            "updated_at": "2021-11-23T00:03:27.000000Z",
        },
        {
            "id": 4,
            "version": "1.7",
            "beta": False,
            "features": [
                {"text": "Patched detections", "type": "modify"},
                {"text": 'Changed loader design to "Dream Lite"', "type": "modify"},
            ],
            "created_at": "2020-07-28T00:02:39.000000Z",
            "updated_at": "2021-11-23T00:02:39.000000Z",
        },
        {
            "id": 3,
            "version": "1.6",
            "beta": False,
            "features": [
                {"text": "New security system to avoid snitchers (Inspector Doggo)", "type": "add"},
                {"text": "Patched detections", "type": "modify"},
            ],
            "created_at": "2020-07-25T00:02:23.000000Z",
            "updated_at": "2021-11-23T00:02:23.000000Z",
        },
        {
            "id": 2,
            "version": "1.5",
            "beta": False,
            "features": [{"text": "Patched detections", "type": "modify"}],
            "created_at": "2020-04-12T00:02:10.000000Z",
            "updated_at": "2021-11-23T00:02:10.000000Z",
        },
    ]


@app.get("/api/stats")
async def get_stats():
    return {
        "users": 33635,
        "total_downloads": 183230,
        "downloads": [6276, 4687, 3255, 3321, 3165, 2814, 3892, 0, 0, 0, 0, 0],
        "total_launches": 294172,
        "launches": [23828, 17257, 16308, 20044, 18154, 20705, 25915, 0, 0, 0, 0, 0],
        "version": "4.6d",
    }


@app.get("/api/users/self")
async def get_self():
    return {
        "message": None,
        "referral": "vroom",
        "id": 1,
        "username": "Cracked by vroom",
        "email": "cracked_by_vroom@gmail.com",
        "email_verified_at": "2022-03-20T12:11:45.000000Z",
        "hwid": "cracked_shit_client",
        "started": True,
        "owned": True,
        "last_hwid_change": "2022-03-20T13:20:42.000000Z",
        "access": 3,
        "owned_expires_at": None,
        "department": -1,
        "created_at": "2022-01-20T16:12:24.000000Z",
        "updated_at": "2022-07-31T06:16:53.000000Z",
    }


@app.get("/api/stats/links")
async def get_self():
    return {"discord": "https:\/\/discord.gg\/eternalclient"}


@app.get("/api/configs/me")
async def get_config():
    return client_config


@app.get("/api/configs/struct")
async def get_modules():
    return {
        "modules": [
            {
                "id": "clicker",
                "name": "Clicker",
                "icon": "mouse-pointer",
                "settings": [
                    {
                        "id": "clicker_cps",
                        "name": "CPS",
                        "desc": "Clicks Per Second",
                        "type": "slider",
                        "default": 10,
                        "min": 1,
                        "max": 20,
                        "step": 1,
                    },
                    {
                        "id": "clicker_menu_whitelist",
                        "name": "Click in inventory",
                        "desc": "Allows clicking on menu windows",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "clicker_swords_only",
                        "name": "Swords Only",
                        "desc": "Only click when holding a sword",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "clicker_axes_only",
                        "name": "Axes Only",
                        "desc": "Only click when holding a axe",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "clicker_break_blocks",
                        "name": "Break Blocks",
                        "desc": "Let the clicker break things",
                        "type": "toggle",
                        "default": False,
                    },
                ],
            },
            {
                "id": "reach",
                "name": "Reach",
                "icon": "ruler",
                "settings": [
                    {
                        "id": "reach_range",
                        "name": "Range",
                        "desc": "How far you can hit",
                        "type": "slider",
                        "default": 3.5,
                        "min": 3,
                        "max": 6,
                        "step": 0.01,
                    },
                    {
                        "id": "reach_sprinting",
                        "name": "Sprinting Only",
                        "desc": "Only activate reach when sprinting",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "reach_liquid",
                        "name": "Disable In Liquids",
                        "desc": "Disables reach when inside liquids",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "reach_walls",
                        "name": "Walls",
                        "desc": "Hit through walls",
                        "type": "toggle",
                        "default": False,
                    },
                ],
            },
            {
                "id": "aimassist",
                "name": "Aim Assist",
                "icon": "bullseye",
                "settings": [
                    {
                        "id": "aimassist_fov",
                        "name": "FOV",
                        "desc": "Field of view",
                        "type": "slider",
                        "default": 180,
                        "min": 1,
                        "max": 360,
                        "step": 1,
                    },
                    {
                        "id": "aimassist_speed",
                        "name": "Speed",
                        "desc": "How fast to aim",
                        "type": "slider",
                        "default": 5,
                        "min": 1,
                        "max": 20,
                        "step": 0.01,
                    },
                    {
                        "id": "aimassist_distance",
                        "name": "Distance",
                        "desc": "Blocks distance to aim",
                        "type": "slider",
                        "default": 4,
                        "min": 3,
                        "max": 6,
                        "step": 0.01,
                    },
                    {
                        "id": "aimassist_multipoint",
                        "name": "Multipoint",
                        "desc": "Aim to the nearest point of the hitbox",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "aimassist_clickaim",
                        "name": "Click Aim",
                        "desc": "Aims when you click",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "aimassist_breakblocks",
                        "name": "Break Blocks",
                        "desc": "Allow breaking of blocks",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "aimassist_lock",
                        "name": "Lock Target",
                        "desc": "Lock onto target",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "aimassist_walls",
                        "name": "Walls",
                        "desc": "Aim through walls",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "aimassist_swords_only",
                        "name": "Swords Only",
                        "desc": "Only assist when holding a sword",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "aimassist_axes_only",
                        "name": "Axes Only",
                        "desc": "Only assist when holding a axe",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "aimassist_nakeds",
                        "name": "Ignore Nakeds",
                        "desc": "Ignore naked players",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "aimassist_teams",
                        "name": "Ignore Teams",
                        "desc": "Ignore team members",
                        "type": "toggle",
                        "default": False,
                    },
                ],
            },
            {
                "id": "blink",
                "name": "Blink",
                "icon": "wifi",
                "settings": [
                    {
                        "id": "blink_breadcrumbs",
                        "name": "Show Crumbs",
                        "desc": "Draws a line of your trajectory",
                        "type": "toggle",
                        "default": False,
                    }
                ],
            },
            {
                "id": "esp",
                "name": "ESP",
                "icon": "vr-cardboard",
                "settings": [
                    {
                        "id": "esp_mode",
                        "name": "ESP Mode",
                        "desc": "Swap between different modes",
                        "type": "select",
                        "options": {"esp_2d": "2D Boxes", "esp_3d": "3D Boxes"},
                        "default": "esp_2d",
                    },
                    {"id": "esp_health", "name": "Draw Health", "desc": "2D only", "type": "toggle", "default": False},
                    {
                        "id": "esp_draw_corners",
                        "name": "Draw Corners",
                        "desc": "2D only",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "esp_draw_expanded",
                        "name": "Draw Expanded",
                        "desc": "3D only",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "esp_draw_invisibles",
                        "name": "Draw Invisibles",
                        "desc": "",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "visuals_global_hook",
                        "name": "Record proof",
                        "desc": "Applies to all visual modules",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "esp_color",
                        "name": "Color",
                        "desc": "Change the color of the ESP",
                        "type": "color",
                        "default": "22,22,22",
                    },
                ],
            },
            {
                "id": "tracers",
                "name": "Tracers",
                "icon": "arrows-alt-h",
                "settings": [
                    {
                        "id": "tracers_distance",
                        "name": "Color by distance",
                        "desc": "Shows color by distance",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "tracers_color",
                        "name": "Color",
                        "desc": "Change the color of the Tracers",
                        "type": "color",
                        "default": "22,22,22",
                    },
                ],
            },
            {
                "id": "xray",
                "name": "X-Ray",
                "icon": "cube",
                "settings": [
                    {"id": "xray_diamond", "name": "Diamond", "desc": "", "type": "toggle", "default": False},
                    {"id": "xray_emerald", "name": "Emerald", "desc": "", "type": "toggle", "default": False},
                    {"id": "xray_iron", "name": "Iron", "desc": "", "type": "toggle", "default": False},
                    {"id": "xray_gold", "name": "Gold", "desc": "", "type": "toggle", "default": False},
                    {"id": "xray_lapis", "name": "Lapis", "desc": "", "type": "toggle", "default": False},
                    {"id": "xray_coal", "name": "Coal", "desc": "", "type": "toggle", "default": False},
                    {"id": "xray_redstone", "name": "Redstone", "desc": "", "type": "toggle", "default": False},
                ],
            },
            {
                "id": "velocity",
                "name": "Velocity",
                "icon": "bullseye",
                "settings": [
                    {
                        "id": "velocity_horizontal",
                        "name": "H Velocity",
                        "desc": "Horizontal Velocity %",
                        "type": "slider",
                        "default": 100,
                        "min": 1,
                        "max": 100,
                        "step": 1,
                    },
                    {
                        "id": "velocity_vertical",
                        "name": "V Velocity",
                        "desc": "Vertical Velocity %",
                        "type": "slider",
                        "default": 100,
                        "min": 1,
                        "max": 100,
                        "step": 1,
                    },
                    {
                        "id": "velocity_delay",
                        "name": "Delay",
                        "desc": "Delayed Knockback",
                        "type": "slider",
                        "default": 1,
                        "min": 1,
                        "max": 5,
                        "step": 1,
                    },
                    {"id": "velocity_push_back", "name": "Push Back", "desc": "", "type": "toggle", "default": False},
                    {
                        "id": "velocity_clicking",
                        "name": "Clicking Only",
                        "desc": "",
                        "type": "toggle",
                        "default": False,
                    },
                ],
            },
            {
                "id": "bhop",
                "name": "B-Hop",
                "icon": "frog",
                "settings": [
                    {
                        "id": "bhop_speed",
                        "name": "Speed",
                        "desc": "How fast you will go",
                        "type": "slider",
                        "default": 1,
                        "min": 1,
                        "max": 10,
                        "step": 1,
                    }
                ],
            },
            {
                "id": "bridge_assist",
                "name": "Bridge Assist",
                "icon": "walking",
                "settings": [
                    {
                        "id": "bridge_assist_blocks",
                        "name": "Blocks Only",
                        "desc": "Active only when holding blocks",
                        "type": "toggle",
                        "default": False,
                    },
                    {
                        "id": "bridge_assist_pitch_check",
                        "name": "Pitch Check",
                        "desc": "Active only when looking down",
                        "type": "toggle",
                        "default": False,
                    },
                ],
            },
        ]
    }


@app.get("/api/client/config")
async def get_config():
    serialized_config = ""
    count = 1

    for key in client_config:
        serialized_config += f"{key}={str(client_config[key]).lower()}"
        if count != len(client_config):
            serialized_config += "|"
        count += 1

    return Response(
        content=serialized_config,
        media_type="text/html",
    )


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 404:
            response = await super().get_response(".", scope)
        return response


app.mount("/dashboard/", SPAStaticFiles(directory="dashboard", html=True), name="dashboard")
app.mount("/img", SPAStaticFiles(directory="dashboard/static/img", html=True), name="img")
app.mount("/js", SPAStaticFiles(directory="dashboard/static/js", html=True), name="js")
app.mount("/css", SPAStaticFiles(directory="dashboard/static/css", html=True), name="css")
app.mount("/fonts", SPAStaticFiles(directory="dashboard/static/fonts", html=True), name="fonts")
app.mount("/storage", SPAStaticFiles(directory="dashboard/static/storage", html=True), name="storage")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(5555))
