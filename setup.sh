#!/bin/bash

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Create the .env file with necessary environment variables
cat <<EOL > .env
DISCORD_TOKEN=
RCON_HOST=
RCON_PORT=27020
RCON_PASSWORD=
OPENAI_API_KEY=
MONGO_URI=
EOL

# Create the Start.sh file that activates the venv and runs the bot
echo "#!/bin/bash" > Start.sh
echo "source venv/bin/activate" >> Start.sh
echo "python3 arkbot.py" >> Start.sh
echo "deactivate" >> Start.sh

# Make Start.sh executable
chmod +x Start.sh

# Notify that setup is complete
echo "Setup complete! You can now run ./Start.sh to activate the environment and run the bot."

# Deactivate the virtual environment after setup
deactivate
