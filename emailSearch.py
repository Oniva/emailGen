import os
import json
from validate_email import validate_email as val_email

with open("wordList.json", "r") as read_file:
    wordList = json.load(read_file)

data = {
    "emails": []
}
try:
    for firstname in wordList["firstname"]:
        for lastname in wordList["lastname"]:
            for esp in wordList["ESP"]:
                currentEmail = "{0}{1}@{2}.com".format(
                    firstname, lastname, esp)
                if(val_email(currentEmail)):
                    data["emails"].append(currentEmail)
                currentEmail = "{0}{1}@{2}.com".format(
                    lastname, firstname, esp)
                if(val_email(currentEmail)):
                    data["emails"].append(currentEmail)

except KeyboardInterrupt:
    with open('emails.json', 'w') as outfile:
        json.dump(data, outfile)


with open('emails.json', 'w') as outfile:
    json.dump(data, outfile)
