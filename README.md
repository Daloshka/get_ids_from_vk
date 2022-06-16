1. Открываешь группу например вот так  https://vk.com/search?c%5Bgroup%5D=138898193&c%5Bname%5D=1&c%5Bonline%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D=1
2. Скролишь в самый низ
3. Пишешь в консоли эту команду

b = document.querySelectorAll("#results > div > div.info > div.labeled.name > a")
ids = []
for (let i = 0; i < document.querySelectorAll('#results > div > div.info > div.labeled.name > a').length; i++) { 
  id = b[i].href.split('/')[3]
  ids.push(id)
}

4.Пишешь в той же консоли ids и ПКМ на idшиники Copy object
Убираешь квадратные скобки и в Sublime заходишь, жмёшь CTRL-H, меняешь " на пустоту и пробел на пустоту

5.Затем вствляешь эту всю парашу в https://dev.vk.com/method/users.get и копируешь ответ, вставляешь его в скрипт get_id.py
6.Получаешь ответ в result.txt

Если есть вопросы в Telegram @lerrrkk
