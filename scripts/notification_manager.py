import subprocess

# Test
user_notification = "testststst"

ntfy_command = f"ntfy -t 'Benachrichtigung' send '{user_notification}'"

try:
    subprocess.run(ntfy_command, shell=True, check=True)
    print("'user_notification' has be send successfully.")
except subprocess.CalledProcessError as e:
    print(f"sending has been failed. {e}")
