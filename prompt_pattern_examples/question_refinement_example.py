"""
To use this pattern, your prompt should make the following fundamental contextual statements:

From now on, whenever I ask a question, suggest a better version of the question to use instead

(Optional) Prompt me if I would like to use the better version instead


Examples:

From now on, whenever I ask a question, suggest a better version of the question to use instead

From now on, whenever I ask a question, suggest a better version of the question and ask me if I would like to use it instead


Tailored Examples:

Whenever I ask a question about dieting, suggest a better version of the question that emphasizes healthy eating habits and sound nutrition. Ask me for the first question to refine.

Whenever I ask a question about who is the greatest of all time (GOAT), suggest a better version of the question that puts multiple players unique accomplishments into perspective  Ask me for the first question to refine.

"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Whenever I ask a question about strength training, suggest a better version of the question that emphasizes gaining hypertrophy more quickly and working as many different muscle groups as possible."
        },
        {
            "role": "user",
            "content": "What weight lifting exercises should I do today?"
        },
    ]
)

print(completion.choices[0].message.content)
