import json

def check_user(userid):
    try:
        with open("src/programs/user_data.json", "r") as f:
            data = json.load(f)
    except:
        return False

    user = data.get(userid)

    if user is not None:
        return True
    
    else:
        return False