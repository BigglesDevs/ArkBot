@echo off
REM Create the virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Install dependencies from requirements.txt
pip install -r requirements.txt

REM Create the Start.bat file that activates the venv and runs the bot
echo @echo off > Start.bat
echo call venv\Scripts\activate >> Start.bat
echo python arkbot.py >> Start.bat
echo deactivate >> Start.bat

REM Notify that setup is complete
echo Setup complete! You can now run Start.bat to activate the environment and run the bot.

REM Deactivate the virtual environment after setup
deactivate