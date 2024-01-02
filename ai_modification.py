import json
from difflib import get_close_matches

def get_knowledge_base(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_knowledge_base(data: str, knowledge_base_file: str):
    with open(knowledge_base_file, "w", encoding="utf-8") as file:
        json.dump(data, file)
        return True

def get_answer_command(query: str, knowledge_base):
    matches = get_close_matches(query, [command["command"] for command in knowledge_base["commands"]] , n=1, cutoff=0.6)

    if matches:
        for command in knowledge_base["commands"]:
            if command["command"] == matches[0]:
                return command


def ai_modification():
    while True:
        knowledge_base = get_knowledge_base("knowledge-data.json")

        query = input("You: ")

        if query != "" and "Ponçik" in query or "ponçik" in query or "Poncik" in query or "poncik" in query:
            answer = get_answer_command(query, knowledge_base)
            if answer != False:
                print("AI: I dont know this command :(\nCan you teach me?")
                command = input("You: ")
                answer = input("You: ")
                command = input("You: ")
            else:
                print("AI: I already know this command :)")
        else:
            print("Please give a command.")


if __name__ == '__main__':
    ai_modification()