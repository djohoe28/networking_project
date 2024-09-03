import anvil.secrets
import anvil.server

# anvil.secrets.encrypt_with_key("secret_encryption_key", b"something or other")
# anvil.secrets.decrypt_with_key("secret_encryption_key", b"encrypted something or other")

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
