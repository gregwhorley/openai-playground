"""
To use this pattern, your prompt should make the following fundamental contextual statements:

I would like you to ask me questions to achieve X

You should ask questions until condition Y is met or to achieve this goal (alternatively, forever)

(Optional) ask me the questions one at a time, two at a time, ask me the first question, etc.

You will need to replace "X" with an appropriate goal, such as "creating a meal plan" or "creating variations of my marketing materials."
You should specify when to stop asking questions with Y. Examples are "until you have sufficient information about my audience and goals"
or "until you know what I like to eat and my caloric targets."

Examples:

I would like you to ask me questions to help me create variations of my marketing materials.  You should ask questions until
you have sufficient information about my current draft messages, audience, and goals. Ask me the first question.

I would like you to ask me questions to help me diagnose a problem with my Internet. Ask me questions until you have enough
information to identify the two most likely causes. Ask me one question at a time. Ask me the first question.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Ask me questions about fitness goals until you have enough information to suggest a strength \
            training regimen for me. When you have enough information, show me the strength training regimen. Ask me the \
            first question. "
        },
        {
            "role": "assistant",
            "content": "What is your current fitness level?"
        },
        {
            "role": "user",
            "content": "I have not been active since 6 months ago when I was jogging 3-4 times per week. It has been a full year since I last lifted weights."
        },
        {
            "role": "assistant",
            "content": "How many days are you willing to commit to working out in a week?"
        },
        {
            "role": "user",
            "content": "I am willing to commit to working out 5 days per week."
        },
        {
            "role": "assistant",
            "content": "What are your main fitness goals? Are you aiming for weight loss, muscle gain, toning, or endurance improvement?"
        },
        {
            "role": "user",
            "content": "My main fitness goals are: weight loss, endurance and stamina improvement."
        },
        {
            "role": "assistant",
            "content": "Do you have any specific areas of your body you want to focus on or are you looking for a full-body training program?"
        },
        {
            "role": "user",
            "content": "I am looking for a full-body training program."
        },
        {
            "role": "assistant",
            "content": "Do you have any kind of injuries or limitations that may affect what kind of exercises you are able to perform?"
        },
        {
            "role": "user",
            "content": "I have metal rods in my left ankle from surgery to fix a fracture, which slightly impedes ankle flexibility."
        }
    ]
)

print(completion.choices[0].message.content)
