"""
To use this pattern, your prompt should make the following fundamental contextual statements:

Generate a set of facts that are contained in the output

The set of facts should be inserted at POSITION in the output

The set of facts should be the fundamental facts that could undermine the veracity of the output if any of them are incorrect

You will need to replace POSITION with an appropriate place to put the facts, such as "at the end of the output".

Examples:

Whenever you output text, generate a set of facts that are contained in the output. The set of facts should be inserted
at the end of the output. The set of facts should be the fundamental facts that could undermine the veracity of the
output if any of them are incorrect.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": ""
        },
    ]
)

print(completion.choices[0].message.content)
