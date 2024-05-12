# 2_task_list_comprehension

Basic_phrases = ["basic phrases", "thank you", "excuse me", "i’m sorry", "good morning!", "good afternoon!",
                 "good evening!", "how are you?", "i’m fine, thank you", "nice to meet you", "you’re welcome",
                 "where are you from?", "what do you do?", "how old are you?", "i don’t understand"]
Updated_list = []

for el in Basic_phrases:
  el_titled = el.title()
  
  for idx in range(1, len(el_titled)):
    if el_titled[idx-1] == "’":
      el_titled = el_titled[:idx] + el_titled[idx].lower() + el_titled[idx+1:]

  Updated_list.append(el_titled)

print(Updated_list)