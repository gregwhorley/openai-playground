"""
To use this pattern, your prompt should make the following fundamental contextual statements:

Whenever I type: X, you will do Y.

(Optional, provide additional menu items) Whenever I type Z, you will do Q.

At the end, you will ask me for the next action.

You will need to replace "X" with an appropriate pattern, such as "estimate <TASK DURATION>" or "add FOOD". You will
then need to specify an action for the menu item to trigger, such as "add FOOD to my shopping list and update my
estimated grocery bill".

Examples:

Whenever I type: "add FOOD", you will add FOOD to my grocery list and update my estimated grocery bill. Whenever I type
"remove FOOD", you will remove FOOD from my grocery list and update my estimated grocery bill. Whenever I type "save"
you will list alternatives to my added FOOD to save money. At the end, you will ask me for the next action.
Ask me for the first action.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Whenever I type: \"add FOOD\", you will add FOOD to my grocery list and update my estimated \
            grocery bill. Whenever I type \"remove FOOD\", you will remove FOOD from my grocery list and update my \
            estimated grocery bill. Whenever I type \"save\" you will list alternatives to my added FOOD to save money. \
            At the end, you will ask me for the next action. Ask me for the first action."
        },
        {
            "role": "assistant",
            "content": "What is your first action?"
        },
        {
            "role": "user",
            "content": "add applewood smoked bacon"
        },
        {
            "role": "assistant",
            "content": "Sure, I have added Applewood Smoked Bacon to your grocery list. Based on average prices, let's \
            estimate the cost at $5.00. Your current estimated grocery bill is $5.00. What is your next action?"
        },
        {
            "role": "user",
            "content": "add all purpose flour, add baking powder, add buttermilk, add butter, add cane sugar"
        },
        {
            "role": "assistant",
            "content": "I have added All Purpose Flour, Baking Powder, Buttermilk, Butter, and Cane Sugar to your grocery list. Here are the estimated costs for each: - All Purpose Flour: $2.50 - Baking Powder: $2.00 - Buttermilk: $2.50 - Butter: $3.00 - Cane Sugar: $3.50 Your current estimated grocery bill is now $18.50. What is your next action?"
        },
        {
            "role": "user",
            "content": "remove applewood smoked bacon, save"
        }
    ]
)

print(completion.choices[0].message.content)
