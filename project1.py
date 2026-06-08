from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


client=Groq(api_key=os.getenv("api_key"))

print("   AI Study Assistant   ")
print("1. Explain a Concept")
print("2. Generate Quiz Questions")
print("3. Create a Study Plan")
print("4. Explain this like I'm 5 years old")
c =input("\nChoose an option (1-4): ")
user_input=input("Enter your text: ")
if user_input.strip()=="":
    print("Error: \nInput is empty!!!")
    exit()
if c=="1":
    p="Explain the following concept in simple terms\n Concept: "+user_input
elif c=="2":
    p= "Generate 5 quiz questions about: "+user_input
elif c=="3":
    p="Create a 7-day study plan for: "+user_input
elif c=="4":
    p="Explain the given topic considering me to be a 5 year old\n Topic: "+user_input
else:
    print("Invalid choice.")
    exit()
print("Generating api response......")
response=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": p
        }
    ]
)
print("\n=== Response ===\n")
print(response.choices[0].message.content)