"""
Make the LLM explain its reasoning can make it work better for us. If it can explain its reasoning correctly, then it's
more likely that it's going to produce the right answer; because the right answer, intuitively, should come after the
correct reasoning. If you break down the problem you're solving into multiple independent steps, and you explain them,
and there's a natural sequence, logic, and flow to them, it's more likely that the final output is going to be a natural
extension of the correct reasoning, and therefore, it's more likely to be correct if your goal is to accurately predict
the next token. The technique for accomplishing this is called chain of thought prompting.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Q: I have four bike racers start a race and travel and average of 25mph. They each race for 2 hours.\
                        Is the total number of miles ridden by all riders greater than 200? \
                        A: Reasoning - Each rider will ride 30mph x 2hrs = 60 miles. I have four riders. Therefore, the \
                        total number of miles ridden by the riders is 4 x 60 miles = 240 miles. Answer - YES"
         },
        {
            "role": "user",
            "content": "Q: I have a staging process for a bike race to line up racers. It takes 47s to stage a group of \
            8 riders and 67s to get the group to the starting gate and ready to race. I want a new group to start the \
            race every 30s. Do I need 8 groups staged at all times in order to have racers continually starting every \
            30s?\
            A: Reasoning - Each group takes 47s + 67s = 114s to be ready to race. In order to race every 30s, I \
            will need to calculate how many races will need to run before a group is ready to race. A group will have \
            114s / 30s = 3.8 races run before it is ready to race. I can't have a partial group, so I need to round up \
            to 4. I only need 4 groups staged to be able to race every 30s, so I do not need 8 groups. Answer - NO"
        },
        {
            "role": "user",
            "content": "Q: I am in a space ship without gravity, I have a cup with a needle in it. I move my foot on \
            the bed, knocking over the cup onto the floor. I lift a book up and put it on a desk. Is anything on the \
            floor?\
            A: Reasoning - <REASONING> Answer - <ANSWER>"
        }
    ]
)

print(completion.choices[0].message.content)
