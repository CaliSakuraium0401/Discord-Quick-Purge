import re
import datetime
import time

def extract_id(text):
    return re.findall(r'\((\d+)\)', text)[0]

def main():
    # Get the list of unverified members from external file.
    with open("unverifiedusers.txt", "r") as file:
        data = file.read()
        usernames_and_ids = data.split("\n")

    # Uses the list of unverified members to automatically create
    # the list of commands to be copy pasta onto discord.
    with open('commands.txt', 'w') as commands:
        for username_and_id in usernames_and_ids:
            commands.write(f"?kick {extract_id(username_and_id)} unverified for more than 7 days.\n")

    # Automatically generate the log to posted in the logging channel.
    with open('log.txt', 'w') as log:
        log.write('**Kicked**\n')
        for unverified_user in usernames_and_ids:
            log.write(f"{unverified_user}\n")
        log.write("**Reason:** unverified for more than 7 days.\n")
        date = datetime.datetime.now()
        log.write(f"**D&T:** <t:{round(time.mktime(date.timetuple()))}:F>\n")
    
    print(f"Completed!")

if __name__ == '__main__':
    main()
