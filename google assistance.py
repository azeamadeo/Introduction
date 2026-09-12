name = input("Enter your name: ")
print("Hello,", name, "what on your mind today?")
question = input("Ask me a question: ")
if question.lower() == "What is the meaning of life?":
    print("The meaning of life is a philosophical question that has been debated for centuries. Some believe it is to seek happiness, others believe it is to fulfill a purpose or destiny.")
elif question.lower() == "What is the capital of France?":
    print("The capital of France is Paris.")
elif question.lower() == "What is the square root of 16?":
    print("The square root of 16 is 4.")
elif question.lower() == "What is the largest mammal?":
    print("The largest mammal is the blue whale.")
elif question.lower() == "What is the speed of light?":
    print("The speed of light is approximately 299,792,458 meters per second.")
elif question.lower() == "What is the tallest mountain in the world?":
    print("The tallest mountain in the world is Mount Everest, which stands at 8,848 meters (29,029 feet) above sea level.")


else:
    print("Sorry, I don't understand, i don t think you ahve enough aura to ask me that question.")