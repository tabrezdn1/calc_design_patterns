import sys
import logging
from app.commands import Command

class EmailCommand(Command):
    def execute(self):
        logging.info("EmailCommand executed: Initiating email process.")  # Log the execution
        print(f'I will email you')  # Maintain user interaction with a print statement
