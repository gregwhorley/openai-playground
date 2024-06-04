"""
To use this pattern, your prompt should make the following fundamental contextual statements:
 - Create a game for me around X OR we are going to play an X game
 - One or more fundamental rules of the game

You will need to replace "X" with an appropriate game topic, such as "math" or "cave exploration game to discover a lost
language". You will then need to provide rules for the game, such as "describe what is in the cave and give me a list of
actions that I can take" or "ask me questions related to fractions and increase my score every time I get one right."

Examples:

Create a cave exploration game  for me to discover a lost language. Describe where I am in the cave and what I can do. I
should discover new words and symbols for the lost civilization in each area of the cave I visit. Each area should also
have part of a story that uses the language. I should have to collect all the words and symbols to be able to understand
the story. Tell me about the first area and then ask me what action to take.

Create a group party game for me involving DALL-E. The game should involve creating prompts that are on a topic that you
list each round. Everyone will create a prompt and generate an image with DALL-E. People will then vote on the best
prompt based on the image it generates. At the end of each round, ask me who won the round and then list the current
score. Describe the rules and then list the first topic.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user",
         "content": "Create a text adventure game for me to discover an artifact in a 5 level dungeon. Describe where I \
         am, what actions are available, and which direction or directions I can move. There should be armor and weapon \
         upgrades available in each level of the dungeon. Monster strength and resilience will increase for every level \
         of the dungeon. There should be a final magic weapon hidden in the dungeon that will be used to defeat the \
         final monster that guards the artifact. Tell me about the first area I am in and what actions and directions \
         are available."},
        {
            "role": "assistant",
            "content": "Welcome to the Dungeons of Destiny! Your task is to navigate through the cavernous dark depths, \
            survive fearsome beasts and ultimately discover the legendary artefact known as the \"Luminous Eye of Eternity\".\
            **LEVEL 1: The Winding Catacombs**\
            You find yourself in the Winding Catacombs, surrounded by dank stone walls. The smell of moss and decay \
            gives you an unsettling feeling. The only source of light is the flicker of your torch burning away the \
            shadows, hinting at untold dangers lurking in the dark. The cold floor beneath you is rough and uneven, \
            suggesting it hasn't been traversed for a long while. Your actions include: exploring the area, interacting \
            with various objects and potentially combat with creatures. You currently possess a rusty iron sword and a \
            worn-out leather armor. There are two paths leading further into the dungeon. To your left is a serpentine \
            path bathed in darkness, chilling to chill your soul. To your right is a stifled passageway, wherein eerie \
            voices echo, scrawling horror on the canvas of your mind. On the ground in front of you is a skeleton \
            clutching a better-conditioned weapon than your rusty iron sword. It is a steel shortsword. There's also a \
            studded leather armor sprawled across the skeleton. You can choose to upgrade your gear at here. But \
            remember, a sound echoing off the stone walls could disturb the roaming monsters. Which path will you take, \
            Adventurer? Left or right? Will you dare to steal from the dead to enhance your odds against the creatures \
            of the dark? The choices are all yours. This is Level One of the dungeon, do not let your guard down. The \
            creatures lurking here are Goblins, not too tough but a direct approach could turn perilous. The deeper you \
            delve into the dungeon, the more powerful and resilient the monsters will become. The final key to defeating \
            the last guardian of the “Luminous Eye of Eternity” lies hidden somewhere within these ominous depths.\
            So, what will you do now?"
        },
        {
            "role": "user",
            "content": "I take the shortsword and studded leather armor off of the skeleton and equip them."
        },
        {
            "role": "assistant",
            "content": "You carefully approach the ancient skeleton, its bones brittle and worn with the passing of \
            time. You gently take the shortsword and studded leather armour, your movements creating only a muffled \
            clanking that reverberates slightly within the catacombs. As you equip your new armour and weapon, you feel \
            a surge of confidence. The studded leather armor is a great improvement both in comfort and protection over \
            your previous gear. The shortsword is a solid piece of steel, light and balanced, it feels natural in your \
            hand. Be cautious though, this dungeon rewards the brave but punishes those who lower their guard. With your \
            new gear, you are better prepared for the challenges that lie ahead. Two paths remain, to the left, the \
            chilling serpentine path, and to the right, the stifled passageway with eerie voices. \
            Which one will you take, adventurer?"
        },
        {
            "role": "user",
            "content": "I take the left path."
        },
        {
            "role": "assistant",
            "content": "With a deep breath and a firm grip on your new sword, you venture down the left path. The cold \
            serpentine route winds before you, seeming to slither its way down into the unforgiving darkness. As you \
            delve deeper into the dungeon, a low growl reaches your ears, drenching the cold stone around you in dread. \
            A pair of menacing, glinting eyes suddenly pierce the darkness up ahead - it appears you are not alone. \
            You have encountered your first beast, a hulking Goblin. This adversary seems sturdier than the average \
            Goblin, a Level 2 beast perhaps. It is heavily adorned with rough cracked armor, stone daggers omitting a \
            sinister edge in the glimmer of your torchlight. You have the option to initiate combat, use stealth to \
            bypass the creature, or utilize your surroundings, perhaps a loose stalactite on the cave ceiling, to your \
            advantage. What will you do, brave adventurer?"
        },
        {
            "role": "user",
            "content": "I throw my shortsword at the loose stalactite in the hopes that it breaks free and lands on the Goblin."
        },
        {
            "role": "assistant",
            "content": "You take a moment to gauge the stalactite's size and distance and take aim with your shortsword. \
            With a short running start, you hurl the blade up towards the hanging menace. The sword whirls through the \
            air, the torchlight glinting off its edge as it strikes the stalactite with a resonating crack. The monster \
            beneath raises its head just in time to see the stalactite break free and come crashing down towards it. The \
            stalactite skewers the unsuspecting goblin sending a spray of dust and debris into the surrounding area. A \
            final guttural cry echoes off the cavern walls and then there’s silence. With the goblin eliminated, the \
            path is clear for you to move further. Your shortsword is lodged in the stalactite now, but the goblin is \
            clutching a hefty looking stone mace, still radiating with heat from the sudden impact. You can keep your \
            current gear or take advantage of the stone mace that has enhanced striking power. Remember, you will face \
            more dangerous enemies in the deeper levels. Choose wisely, adventurer."
        },
        {
            "role": "user",
            "content": "I take the stone mace and move further down the path."
        },
        {
            "role": "assistant",
            "content": "With your heart still racing from the encounter, you carefully approach the fallen goblin. \
            Now silent and still, the goblin is a grim testament to the dangers lurking within the dungeon. You retrieve \
            the stone mace it was holding. Despite its crude appearance, the mace feels sturdy and well-balanced in your \
            hands, its heated surface adding a comforting warmth. As you continue your journey through the dark serpentine \
            path, you soon come across a stone door, massive in size, adorned with intricate markings. This is the \
            boundary to Level 2: The Catacomb Depths. Do you wish to enter, adventurer, or do you need to prepare further?"
        },
        {
            "role": "user",
            "content": "I wish to enter through the stone door to Level 2."
        }
    ]
)

print(completion.choices[0].message.content)
