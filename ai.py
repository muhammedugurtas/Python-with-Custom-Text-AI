import json
from difflib import get_close_matches

SUFFIX = "Poncik" # Default setting is Poncik

def get_knowledge_base(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_knowledge_base(data: str, knowledge_base_file: str):
    with open(knowledge_base_file, "w", encoding="utf-8") as file:
        json.dump(data, file)
        return True

def get_command(query: str, knowledge_base):
    matches = get_close_matches(query, [command["command"] for command in knowledge_base["commands"]] , n=1, cutoff=0.6)

    if matches:
        for command in knowledge_base["commands"]:
            if command["command"] == matches[0]:
                return command

    return False

def ai():
    while True:
        knowledge_base = get_knowledge_base("knowledge-data.json")

        query = input("You: ")

        if query != "" and SUFFIX in query or SUFFIX.lower() in query:
            command = get_command(query, knowledge_base)
            if command != False and command != None:
                print("AI: " + command["answer"] + "\n")
                print("AI: I got \"" + command["command_name"] + "\" command.")
            else:
                print("AI: I dont know this command :(")
        else:
            print("Please give a command.")


if __name__ == '__main__':
    ai()