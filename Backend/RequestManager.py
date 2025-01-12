import sys
import json
import ast

# This is temporary file instead of the model

route = ast.literal_eval(sys.argv[1])
name = ast.literal_eval(sys.argv[2])

if route == "greet":
    message = f"Hello, {name}!"

elif route == "goodbye":
    message = f"Goodbye, {name}!"

else:
    message = "Invalid route!"

print(message)

sys.stdout.flush()