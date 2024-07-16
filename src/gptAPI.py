from openai import OpenAI
import json
import os

GPT_MODEL = "gpt-4o"
INITIAL_CONTEXT_PROMPT = [
      {"role": "system", "content": "You are a video game recommender. You provide tailored game recommendations based on the user's preferences and past games they enjoyed. Please don't answer irrelevant questions."},
      {"role": "user", "content": "I enjoy 4X strategy games with deep strategic gameplay and historical settings. Recently, I played and loved Civilization VI. Can you recommend another game similar to it?"},
      {"role": "assistant", "content": "If you enjoyed Civilization VI, you might like Endless Legend. It offers rich strategic depth, a unique fantasy setting, and a variety of factions with different playstyles."},
      {"role": "user", "content": "That sounds great! I also enjoy action games with fast-paced combat and strong storylines. I recently finished Devil May Cry 5. Can you recommend another game like it?"},
      {"role": "assistant", "content": "If you liked Devil May Cry 5, you should try Bayonetta 2. It features intense combat, stylish moves, and a captivating story, making it a thrilling action game experience."}
    ] # context prompts

def getChatHistory(author: str):
  path = f"./src/chat-history/{author}.json"
  try:
    with open(path, 'r') as file:
      print("file exists")
      history = json.load(file)
    return history;
  except FileNotFoundError: # file not found
    # create new json file and return base chat history
    print("file does not exist")
    return saveChatHistory(INITIAL_CONTEXT_PROMPT, author)


def saveChatHistory(history: list, author: str):
  path = f"./src/chat-history/{author}.json"
  with open(path, 'w+') as file:
      json.dump(history, file)
  return history


class gpt():
  def __init__(self):
    self.client = OpenAI()
    self.model = GPT_MODEL

  def askGPT(self, msg: str, author: str):
    if msg == "": # if msg is empty
      print("Error: empty message, returning false.")
      return 0;

    # load chat history
    history = getChatHistory(author)
    
    # append new chat to history
    history.append({"role" : "user", "content": msg})      

    # create completion
    completion = self.client.chat.completions.create(model=self.model, messages=history)

    # get response from GPT
    response = completion.choices[0].message.content

    # append and save response to chatHistory
    history.append({"role" : "system", "content": response})
    saveChatHistory(history, author)

    return response;