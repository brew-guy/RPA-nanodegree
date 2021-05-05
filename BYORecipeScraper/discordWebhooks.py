import requests #dependency

webhook = 'https://discordapp.com/api/webhooks/823536264593670174/jBzQ_IWikDaoTd5lg2iOnwal1RyxyK0sn_M9R2-Wtl-7t2eZaW9X-JbtQA5jdRuynIRb'

#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "content" : "Hey, listen up!",
    "username" : "Valheim Server 🎅"
}

#leave this out if you dont want an embed
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
data["embeds"] = [
    {
        "title" : "embed title",
        "description" : "hi there, this is **embedded** text. It supports normal *Markdown*."
    }
]

result = requests.post(webhook, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))

#result: https://i.imgur.com/DRqXQzA.png