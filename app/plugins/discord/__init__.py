import sys
import logging
from app.commands import Command

class DiscordCommand(Command):
    def execute(self):
        logging.info("DiscordCommand executed: Preparing to send something to Discord.")
        print(f'I Will send something to discord')  # Maintain the user interaction
