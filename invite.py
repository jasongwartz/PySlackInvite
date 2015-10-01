# Invite users
import requests, json

def invite(email, firstname, lastname, access):
	with open("config.json", "rb") as fp:
		config = json.loads(fp.read())
		
	if access.lower() != config['key']:
		return "Error: Incorrect access code."
	
	email = email.lower()
	if "@ucl.ac.uk" not in email:
		return "Error: Please use a UCL email address."
	
	params = {
		"token":config['token']
		}
	
	channels = requests.get("https://slack.com/api/channels.list", params=params)

	channel_list = [c['id'] for c in channels.json()['channels']]
	
	params["channels"] = ",".join(channel_list)

	params["email"] = email
	params["first_name"] = firstname
	params["last_name"] = lastname
	response = requests.post("https://slack.com/api/users.admin.invite", params=params)
	
	print response
	print response.json()
	
	if response.json()['ok']:
		return "Thanks! You should receive an email shortly."
	elif not response.json()['ok']:
		return "Error: " + str(response.json()['error']) # Error response from Slack
	else:
		return "An unexpected error occured. [2]" # Unkonwn error
	
