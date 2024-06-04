"""
To use this pattern, your prompt should make the following fundamental contextual statements:

If there are alternative ways to accomplish a task X that I give you, list the best alternate approaches

(Optional) compare/contrast the pros and cons of each approach

(Optional) include the original way that I asked

(Optional) prompt me for which approach I would like to use

You will need to replace "X" with an appropriate task.

Examples:

For every prompt I give you, If there are alternative ways to word a prompt that I give you, list the best alternate
wordings . Compare/contrast the pros and cons of each wording.

For anything that I ask you to write, determine the underlying problem that I am trying to solve and how I am trying to
solve it. List at least one alternative approach to solve the problem and compare / contrast the approach with the
original approach implied by my request to you.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "From now on, if there are alternative ways to accomplish the same thing, list the best \
            alternate approaches. Compare and contrast the alternatives and ask me which one I want to use."
        },
        {
            "role": "user",
            "content": "Write a prompt for ChatGPT using few shot examples to determine if a date in YYYY-MM-DD format \
            is a leap year. The output should either be \"YYYY is a leap year\" or \"YYYY is not a leap year\""
        }
    ]
)

print(completion.choices[0].message.content)
