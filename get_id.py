# https://dev.vk.com/method/users.get
# Вставляешь токен и id участников через запятую, которые достал через JavaScript
# В саблайме оборачиваешь в кавычки true и false 
# hot keys to do it  CTRL+H

# EXAMPLE
ids = [{
    "response": [
        {
            "id": 132174289,
            "first_name": "Татьяна",
            "last_name": "Николаева",
            "can_access_closed": "true",
            "is_closed": "false"
        },
        {
            "id": 192422850,
            "first_name": "Натали",
            "last_name": "Еврукова",
            "can_access_closed": "true",
            "is_closed": "false"
        }
    ]
}]

result = []

for i in range(len(ids[0]['response'])):
    #print(ids[0]['response'][i]['id'])
    result.append(ids[0]['response'][i]['id'])

with open("result.txt", "w") as output:
    output.write(str(result))
    output.close()