"""
Provide input and example output for the LLM to learn then follow up with a prompt that triggers the LLM to respond

Simple example:
Input: Rock
Output: Hard
Input: Pillow
Output: Soft
Input: Wood
Output: Hard
Input: Baby
Output: Soft

Given this prompt, follow up with an additional Input line to get output from the LLM

Input: Car

=============

Another way to apply the pattern is by providing intermediate steps. For example:

Situation: I want to build a table
Think: I need access to a cutting tool and a tree
Action: Cut down a tree with an axe
Think: I need access to a tool that can cut the tree trunk into boards
Action: Cut the trunk into 2x6 boards with a saw mill
Think: I need to affix the boards together to form the tabletop
Action: Use wood glue to stick the boards together on their sides
Think: I need a set of metal legs to bolt on to the tabletop
Action: Purchase metal legs and bolt them on to each corner of the tabletop using wood screws

Given this prompt, follow up with an additional Situation line to get output from the LLM

Situation: I want to build chairs for my new table

============

In cases where the examples may be vague enough that the LLM does not provide the desired output from your examples. This
is where context is added via prompt: For example:

Your output can only be soft or hard.

Input: Rock
Output: Hard
Input: Pillow
Output: Soft

Then follow up with an input to trigger the desired output from the LLM

Input: Car

"""

from openai import OpenAI

client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "user",
#             "content": "Situation: I want to build a table \
#             Think: I need access to a cutting tool and a tree \
#             Action: Cut down a tree with an axe \
#             Think: I need access to a tool that can cut the tree trunk into boards \
#             Action: Cut the trunk into 2x6 boards with a saw mill \
#             Think: I need to affix the boards together to form the tabletop \
#             Action: Use wood glue to stick the boards together on their sides \
#             Think: I need a set of metal legs to bolt on to the tabletop \
#             Action: Purchase metal legs and bolt them on to each corner of the tabletop using wood screws"
#         },
#         {
#             "role": "user",
#             "content": "Situation: I want to build chairs for my new table."
#         }
#     ]
# )

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Situation: I want to bake a pecan pie. \
                        Action: I mix flour, butter, salt, and water together to make the dough. I then roll out the \
                        dough with a rolling pin until it is wide enough to cover the bottom and sides of a pie pan. I \
                        gently put the rolled out dough into a pie pan and put it in the refridgerator to chill while \
                        I prepare the filling. In a bowl, I combine corn syrup, sugar, eggs, butter, molasses, and pecans \
                        and mix thoroughly. I preheat the oven to 350 degrees F, pull the chilled dough in the pie pan \
                        out of the fridge, pour the filling into the pan, and set it in the center rack of the oven. I \
                        close the oven door and set a timer for 50 minutes. I check if the pie is done by gently shaking \
                        the pan and observing the way the filling reacts. If the outside of the pie is set and the center \
                        is slightly wobbly, the pie is done and I take it out of the oven."

        },
        {
            "role": "user",
            "content": "Situation: I want to bake a pound cake."
        }
    ]
)

print(completion.choices[0].message.content)
