"""
To use this pattern, your prompt should make the following fundamental contextual statements:

Act as an outline expander.

Generate a bullet point outline based on the input that I give you and then ask me for which bullet point you should
expand on.

Create a new outline for the bullet point that I select.

At the end, ask me for what bullet point to expand next.

Ask me for what to outline.

Examples:

Act as an outline expander. Generate a bullet point outline based on the input that I give you and then ask me for which
bullet point you should expand on. Each bullet can have at most 3-5 sub bullets. The bullets should be numbered using
the pattern [A-Z].[i-v].[* through ****]. Create a new outline for the bullet point that I select.  At the end, ask me
for what bullet point to expand next. Ask me for what to outline.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Act as an outline expander. Generate a bullet point outline based on the input that I give you \
            and then ask me for which bullet point you should expand on. Each bullet can have at most 3-5 sub bullets. \
            The bullets should be numbered using he pattern [A-Z].[i-v].[* through ****]. Create a new outline for the \
            bullet point that I select.  At the end, ask me for what bullet point to expand next."
        },
        {
            "role": "user",
            "content": "Ask me for what to outline."
        },
        {
            "role": "assistant",
            "content": "Sure, please provide a topic or concept that you would like me to outline."
        },
        {
            "role": "user",
            "content": "Proper techniques for smoking brisket."
        },
        {
            "role": "assistant",
            "content": "Sure, here is a general outline for \"Proper Techniques for Smoking Brisket\":\
            A. Preparation\
            i. Choosing the right brisket\
            ii. Proper trimming\
            iii. Selecting and applying the right seasoning \
            \
            B. Smoking Process\
            i. Choosing the right wood\
            ii. Controlling the temperature\
            iii. Timing the smoke\
            \
            C. Post-Smoking Process\
            i. Wrapping the brisket\
            ii. Allowing it to rest\
            iii. Slicing properly\
            \
            Please let me know which bullet point you'd like me to expand further on."
        },
        {
            "role": "user",
            "content": "A.ii"
        }
    ]
)

print(completion.choices[0].message.content)
