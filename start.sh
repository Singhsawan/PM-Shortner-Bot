if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TeamHMT/ben-url-filter-bot.git /ben-url-filter-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ben-url-filter-bot
fi
cd /ben-url-filter-bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
