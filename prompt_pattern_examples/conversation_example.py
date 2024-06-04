from openai import OpenAI

client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "user",
#             "content": "I want to build a house. Can you help me with that?"
#         }
#     ]
# )

# completion = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "user",
#             "content": "I'm going to continue the conversation, but I'm going to continue the conversation assuming that I have architects and contractors available to help me."
#         }
#     ]
# )

# completion = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "user",
#             "content": "We are designing a residential building on a half acre of land in the pacific northwest of the united states. I want three bedrooms: one for me and my wife, one for visitors, and a third to act as an office. It will have two bathrooms, one of with is adjoining with the main bedroom. There will be a finished basement with space for a home gym and a few pinball tables. There is no set timeline but the budget has to be a maximum of $250,000 US dollars."
#         }
#     ]
# )

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "What enhancements to the house would be possible if the budget was increased by another $250,000?"
        }
    ]
)

print(completion.choices[0].message.content)

with open("conversation_example.txt", "a") as fh:
    fh.write(completion.choices[0].message.content)
