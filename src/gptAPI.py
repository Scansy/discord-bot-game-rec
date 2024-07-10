from openai import OpenAI

GPT_MODEL = "gpt-4o"

class gpt():
  def __init__(self):
    self.client = OpenAI()
    self.chatHistory = [
      {"role": "system", "content": "You are a video game recommender. You provide tailored game recommendations based on the user's preferences and past games they enjoyed. Please don't answer irrelevant questions."},
      {"role": "user", "content": "I enjoy 4X strategy games with deep strategic gameplay and historical settings. Recently, I played and loved Civilization VI. Can you recommend another game similar to it?"},
      {"role": "assistant", "content": "If you enjoyed Civilization VI, you might like Endless Legend. It offers rich strategic depth, a unique fantasy setting, and a variety of factions with different playstyles."},
      {"role": "user", "content": "That sounds great! I also enjoy action games with fast-paced combat and strong storylines. I recently finished Devil May Cry 5. Can you recommend another game like it?"},
      {"role": "assistant", "content": "If you liked Devil May Cry 5, you should try Bayonetta 2. It features intense combat, stylish moves, and a captivating story, making it a thrilling action game experience."}
    ] # context prompts
    self.model = GPT_MODEL

  def askGPT(self, msg: str):
    if msg == "": # if msg is empty
      print("Error: empty message, returning false.")
      return 0;

    # append msg to chatHistory
    self.chatHistory.append({"role" : "user", "content": msg})

    # create completion
    completion = self.client.chat.completions.create(model=self.model, messages=self.chatHistory)

    # get response from GPT
    response = completion.choices[0].message.content

    # append response to chatHistory
    self.chatHistory.append({"role" : "system", "content": response})

    return response;