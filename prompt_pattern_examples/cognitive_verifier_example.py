"""
To use the Cognitive Verifier Pattern, your prompt should make the following fundamental contextual statements:

When you are asked a question, follow these rules

Generate a number of additional questions that would help more accurately answer the question

Combine the answers to the individual questions to produce the final answer to the overall question


Examples:

When you are asked a question, follow these rules. Generate a number of additional questions that would help you more
accurately answer the question. Combine the answers to the individual questions to produce the final answer to the overall question.

Tailored Examples:

When you are asked to create a recipe, follow these rules. Generate a number of additional questions about the ingredients
I have on hand and the cooking equipment that I own. Combine the answers to these questions to help produce a recipe that I have the ingredients and tools to make.

When you are asked to plan a trip, follow these rules. Generate a number of additional questions about my budget, preferred
activities, and whether I will have a car. Combine the answers to these questions to better plan my itinerary.
"""

from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "When you are asked a plan a trip, follow these rules. Generate a number of additional questions \
            about my budget, preferred activities, and whether or not I will have a car. Combine the answers to these \
            questions to better plan my itinerary."},
        {
            "role": "user",
            "content": "Can you plan a romantic getaway for two to Costa Rica?"
        },
        {
            "role": "assistant",
            "content": "Absolutely! I will need a little bit more information to give you a personalized plan:\
            1. What is your budget for this trip?\
            2. Do you have preference for beach, jungle, or city exploration? Or would you like a mixture?\
            3. Will you be renting a car or do you prefer public transport?\
            4. Do you have interest in adventure activities like zip-lining, hiking, or bird watching?\
            5. Do you enjoy trying local food or do you prefer international cuisines?\
            6. Are you interested in visiting historical or cultural sites?\
            7. Would you like to include any spa or wellness activities in your itinerary?\
            8. What is your ideal hotel accommodation, luxury, mid-range or budget?\
            9. How many days are you planning to stay in Costa Rica?\
            10. Are there any specific destinations in Costa Rica you'd like to visit?\
            Once I have these details, I can create a tailored itinerary for your romantic getaway to Costa Rica."
        },
        {
            "role": "user",
            "content": "1. $3000 2. mixture 3. public transport or taxi 4. bird watching, hiking, food tour 5. local food 6. yes 7. yes 8. mid-range 9. 7 days 10. no"
        }
    ]
)


print(completion.choices[0].message.content)
