from AvengerMusic.core.bot import Avenger
from AvengerMusic.core.dir import dirr
from AvengerMusic.core.git import git
from AvengerMusic.core.userbot import Userbot
from AvengerMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Avenger()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
