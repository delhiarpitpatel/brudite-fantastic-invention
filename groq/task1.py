from groq import Groq

GROQ_API_KEY=''
with open('GROQ_API_KEY.key') as f:
    GROQ_API_KEY = f.read()
client = Groq(api_key=GROQ_API_KEY)
def completion(query):
    stream = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="openai/gpt-oss-120b",
        # top_k=40,
        # top_p=0.10,
        # temperature=0.3,
        # max_tokens=1000,
        stream=True
    )
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if(type(content) == str and not content.isspace()):
            print(content, end="")

while True:
    try:
        print()
        c = input(">>> ")
        if(c == '' or c == '/?'):
            c = 'help'
        match(c):
            case 'help':
                print("Help Info:\n /bye to exit.\n Or ask anything else.")
            case '/bye':
                print("Thanks for using it!")
                break
            case _:
                completion(c)
    except KeyboardInterrupt:
        print("\n\nDo you want to exit?\n Type /bye to exit.")