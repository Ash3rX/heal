from heal.heal import heal
from heal.config import Authorzation

if __name__ == "__main__":
    bot = heal()
    bot.run(Authorzation.token, reconnect=True)