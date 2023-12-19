import openai
import json
openai.api_key="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"
def assist(text="I'm participating in a hackathon"):
    assistant = openai.beta.assistants.create(
        name="Mind AI",
        instructions="you are a friend who is helping a friend who is going through a though mental state you will be getting their emotional analysis as emotion and generate a mood card which contains mood, trigger, focus, personality, mental profile, environment, and habit. And you will be getting a text which is generated from their speech provide the mood card",
        model="gpt-3.5-turbo-16k"
    )
    with open("data.json", "r") as json_file:
            data = json.load(json_file)
    thread = openai.beta.threads.create(
    messages=[
        {
        "role": "user",
        "content": data+text
        
        }
    ]
    )
    run = openai.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as your friend."
    )
    run = openai.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
    )
    messages = openai.beta.threads.messages.list(
    thread_id=thread.id
    )
    print(messages)
