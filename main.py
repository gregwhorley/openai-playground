from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an expert at all things Kubernetes."
        },
        {
            "role": "user",
            "content": "Tell me 10 different ways I can copy files from a github repo to an persistent volume in an EKS cluster. All approaches must be automated and can be integrated into a CI pipeline."
        }
    ]
)

print(completion.choices[0].message.content)

"""
Revisit this later
"I am a Site Reliability Engineer for a small startup and I have ideas for professional growth that I would like to work on outside of office hours. These ideas include: becoming more familiar with Kubernetes API extentions and the control plane, writing software in GO and Rust, contributing to open source projects, writing my own AI Assistant chat bot with a graphical frontend, and posting my own projects on my Github account. Please provide 5 different ways to solve my time budgeting and motivation problem for professional development."
"""
