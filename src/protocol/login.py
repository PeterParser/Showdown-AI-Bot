import json
import requests
import protocol.senders



async def log_in(websocket, user_name, password, sex, challid, chall):
    """
    Login in function. Send post request to showdown server.
    :param websocket: Websocket stream
    :param challid: first part of login challstr sent by server
    :param chall: second part of login challstr sent by server
    """
    username = user_name
    if sex == "m":
        avatar = "/avatar 167"
    elif sex == "f":
        avatar = "/avatar 166"
    else:
        avatar = "/avatar 101"

    resp = requests.post("https://play.pokemonshowdown.com/action.php?",
                         data={
                             'act': 'login',
                             'name': username,
                             'pass': password,
                             'challstr': challid + "%7C" + chall
                         })
    await protocol.senders.sender(websocket, "", "/trn " + username + ",0," + json.loads(resp.text[1:])['assertion'])
    await protocol.senders.sender(websocket, "", avatar)
