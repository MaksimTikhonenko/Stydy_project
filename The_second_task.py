# 2_task_list_comprehension

Basic_phrases = ["basic phrases", "thank you", "excuse me", "i’m sorry", "good morning!", "good afternoon!",
                 "good evening!", "how are you?", "i’m fine, thank you", "nice to meet you", "you’re welcome",
                 "where are you from?", "what do you do?", "how old are you?", "i don’t understand"]
Updated_list = []

for el in Basic_phrases:
        Updated_list.append(el.title())

print(Updated_list)