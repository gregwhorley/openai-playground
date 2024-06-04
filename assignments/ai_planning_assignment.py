import time

from openai import OpenAI
from openai.types.beta.threads import MessageContentImageFile, MessageContentText

client = OpenAI()


def new_assistant(name, instructions):
    return client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=[{"type": "code_interpreter"}],
        model="gpt-4o"
    )


def new_thread():
    return client.beta.threads.create()


def upload_files(list_of_filenames=[]):
    file_objects = []
    for f in list_of_filenames:
        file_obj = client.files.create(
            file=open(f, "rb"),
            purpose="assistants"
        )
        file_objects.append(file_obj)
    return file_objects


def new_message(thread_id, content, file_ids=[]):
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content,
        file_ids=file_ids
    )


def new_run(thread_id, assistant_id):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )


def output_image_file_from_assistant(file_id):
    image_data = client.files.content(file_id)
    image_data_bytes = image_data.read()
    with open(f"./{file_id}", "wb") as file:
        file.write(image_data_bytes)


if __name__ == "__main__":
    # assistant = new_assistant(
    #     name="AI Planning Assignment",
    #     instructions="You are a helpful planner that will break down a task into steps and execute on them."
    # )
    # thread = new_thread()
    # message = new_message(
    #     thread_id=thread.id,
    #     content="I need to run several errands today in addition to my normal 8 hour work day with a 1 hour lunch break in the middle of the day. The errands include: grocery shopping, picking up clothes from the dry cleaners, buying new shoes, filling up my car's gas tank with gas, and getting 30 minutes of exercise. Please provide a step by step plan to complete these errands outside of my normal work hours. My one hour lunch break can be used to complete some of the errands."
    # )
    # run = new_run(
    #     thread_id=thread.id,
    #     assistant_id=assistant.id
    # )
    # print(assistant.id, thread.id, message.id, run.id)
    # time.sleep(120)
    message_2 = new_message(
        thread_id="thread_IOAO6cBYwCxWGWZL1MLzvARo",
        content="I need help preparing my grocery list. I need to get items for breakfast, lunch, and dinner. I need items like cereal, milk, and eggs for breakfast, bread and peanut butter for lunch, and chicken and vegetables for dinner. Please provide itemized output and sort it by aisle."
    )
    run_2 = new_run(
        thread_id="thread_IOAO6cBYwCxWGWZL1MLzvARo",
        assistant_id="asst_wsaitRvQvMDtR6nEtzS421zG"
    )
    time.sleep(120)
    message_list = client.beta.threads.messages.list(
        thread_id="thread_IOAO6cBYwCxWGWZL1MLzvARo",
        order="asc"
    )
    for message in message_list:
        for content in message.content:
            if isinstance(content, MessageContentImageFile):
                print(f"Message with file content. ID is {content.image_file.file_id}", "\n", "------------------")
            elif isinstance(content, MessageContentText):
                formatted_output = content.text.value.replace('\\n', '\n').replace('\\t', '\t')
                print(formatted_output, "\n", "------------------")
