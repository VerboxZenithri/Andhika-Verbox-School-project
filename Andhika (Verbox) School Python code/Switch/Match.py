command="exit"
match command:
    case "strt":
        action="fire up the engine"
    case "stop":
        action="stop engine"
    case "pause":
        action="stop time"
    case "exit":
        action="explode de engine"
    case _:
        action="unknown command"
print(action)