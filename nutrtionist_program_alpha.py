from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Act as a nutritionist. Generate a list of foods with estimated calorie count per serving based \
            on the meal input I give you, which can be one of: breakfast, lunch, dinner, or snack. Then ask me which food to \
            choose and produce output that is the recipe for that food. At the end, ask me for the next meal input."
        },
        {
            "role": "user",
            "content": "Ask me for which meal I would like to see a list of foods."
        },
        {
            "role": "assistant",
            "content": "Sure! Which meal would you like to see a list of foods for? Breakfast, lunch, dinner, or a snack?"
        },
        {
            "role": "user",
            "content": "breakfast"
        },
        {
            "role": "assistant",
            "content": "Great! Here are some healthy breakfast ideas along with their estimated calories per serving:\
            1. Whole Grain Toast with Avocado (200 calories)\
            2. Greek Yogurt with Berries and Granola (250 calories)\
            3. Scrambled Eggs with Spinach and Feta Cheese (300 calories)\
            4. Almond Butter Smoothie with Banana and Spinach (350 calories)\
            5. Steel Cut Oats with Apples and Nuts (300 calories)\
            Which of these choices would you like more information on?"
        },
        {
            "role": "user",
            "content": "3"
        }
    ]
)

print(completion.choices[0].message.content)
