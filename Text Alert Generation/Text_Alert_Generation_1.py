import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {
	"authorization": "0o5qKSJNjUw2zMBAbixO1VDPadpeHG7tr93YmWXvLFcnElZIfTpWSqZFuDK5dJ2R9Ec18VX7GrNCz3U4",
	"message": "This is test Message sent from \
		Python Script using REST API.",
	"language": "english",
	"route": "q",
	"numbers": "+19377942440, +19379564850"}

headers = {
	'cache-control': "no-cache"
}
try:
	response = requests.request("GET", url, headers = headers, params = querystring)
	
	print("SMS Successfully Sent")
except:
	print("Oops! Something wrong")
