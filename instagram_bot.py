from instabot import Bot

bot = Bot()
bot.login(username="python08", password="123456789")
bot.follow('@tigerjackieshroff')
bot.upload_photo("/photo_path/_photo_name_write", caption="I am insta bot for automation")
bot.unfollow('@tigerjackieshroff')
bot.send_message("I love python programming language",['@tigerjackieshroff'])
followers=bot.get_user_followers("python08")
for follower in followers:
    print(bot.get_user_info(follower))



