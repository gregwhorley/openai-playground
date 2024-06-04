"""
To use this pattern, your prompt should make the following fundamental contextual statements:

When I say X, I mean Y (or would like you to do Y)

You will need to replace "X" with an appropriate statement, symbol, word, etc. You will then need to apply this to a meaning, Y.

Examples:

When I say "variations(<something>)", I mean give me ten different variations of <something>

Usage: "variations(company names for a company that sells software services for prompt engineering)"

Usage: "variations(a marketing slogan for pickles)"

-------

When I say Task X [Task Y], I mean Task X depends on Task Y being completed first.

Usage: "Describe the steps for building a house using my task dependency language."

Usage: "Provide an ordering for the steps: Boil Water [Turn on Stove], Cook Pasta [Boil Water], Make Marinara
[Turn on Stove], Turn on Stove [Go Into Kitchen]"
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "When I type \"experience(<job title>)\", I would like you to give me the number of years \
            experience usually required for the provided job title."
        },
        {
            "role": "user",
            "content": "experience(staff SRE)"
        },
    ]
)

print(completion.choices[0].message.content)
