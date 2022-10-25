<h2> Telegram Self Finance Bot </h2>

Telegram bot which helps you keep track of your finances.<br>
Now this Bot works only with a single Telegram account, but <br>
in future it will work with spread of users.<br><br>
If you want to use this bot, you need to set up and run up<br>
it locally. Installation guide below.

---

<h3> Stack of technologies </h3>

1) Python ≥ 3.10
2) aiogram
3) sqlite3

---

<h3> Installation guide for Linux/GNU OS </h3>


1) Create your own Telegram Bot using
   <a href="https://t.me/BotFather">Bot Father</a>.
2) Install all required solutions. Replace 'apt' with
   your distribution package manager.
   ```commandline
   sudo apt update && sudo apt upgrade
   sudo apt install -y git python3-venv python3-pip vim
   git clone https://github.com/pkozhem/pywish.git
   cd SelfFinanceBot
   ```
3) Create and activate virtual environment.
   ```commandline
   python3 -m venv venv
   source venv/bin/activate
   ```
4) Set up your environment variables in
   _.env.template_ file.
   ```commandline
   vim .env.template
   cp .env.template .env
   ```
5) Install all dependencies.
   ```commandline
   pip install -r requirements.txt
   ```
6) Run up locally.
   ```commandline
   python3 manage.py
   ```
