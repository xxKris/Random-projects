import time

def typing_test(sentence):
    start_time = time.time()
    user_input = input(sentence)
    end_time = time.time()
    return end_time - start_time

sentence = "The quick brown fox jumps over the lazy dog."
time_elapsed = typing_test(sentence)
wpm = len(sentence.split()) / (time_elapsed / 60)
print("You typed at a speed of {:.2f} words per minute.".format(wpm))
