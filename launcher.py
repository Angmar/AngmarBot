from bot.main import MusicBot

VERSION = "0.7.3"


def main(): 
    bot = MusicBot()

    bot.run(VERSION)


if __name__ == "__main__":
    main()
