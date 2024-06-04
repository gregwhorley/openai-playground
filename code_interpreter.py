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


def store_ids(id_map):
    for k, v in id_map.items():
        with open("./outlining_for_content_assignment.ids", "a") as fh:
            fh.write(f"{k}={v}")


if __name__ == "__main__":
    assistant = new_assistant(
        name="ACHIEVE bot",
        instructions="You are a helpful data analyst and problem solver."
    )
    thread = new_thread()
    files = upload_files(["./ACHIEVE.txt"])
    message = new_message(
        thread_id=thread.id,
        file_ids=[file.id for file in files],
        content="Read the attached text file and provide examples how I can solve real problems in either my job or personal life related to each aspect of the framework described in the text file. Here is some background information on me: I am 46 years old and have been working in IT and Software Engineering for over 20 years. I am currently a Site Reliability Engineer and am interested in moving on to a management role in the next 5-10 years. In my personal life, I like to play video board or card games, go camping and hiking with my fiance, play trivia at a local bar, watch movies at a local historic theater, strength training, and read sci-fi and fantasy books."
    )
    run = new_run(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    id_map = {"thread": thread.id, "assistant": assistant.id, "message": message.id, "run": run.id}
    store_ids(id_map)
    print(id_map)
    time.sleep(120)
    message_list = client.beta.threads.messages.list(
        thread_id=thread.id,
        order="asc"
    )
    for message in message_list:
        for content in message.content:
            if isinstance(content, MessageContentImageFile):
                print(f"Message with file content. ID is {content.image_file.file_id}", "\n", "------------------")
            elif isinstance(content, MessageContentText):
                formatted_output = content.text.value.replace('\\n', '\n').replace('\\t', '\t')
                print(formatted_output, "\n", "------------------")
