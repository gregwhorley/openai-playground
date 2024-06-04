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


def output_file_from_assistant(file_id):
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
        name="Outlining for content assignment",
        instructions="You are a helpful data analyst that specializes in summarizing and outlining content from file input."
    )
    thread = new_thread()
    files = upload_files(
        list_of_filenames=["./k8s_brown_bag_presentation.pdf"]
    )
    """
    Have Code Interpreter write an outline for a presentation that you are going to give. The initial outline should
    have one bullet item per slide. Incrementally build out the outline so that it specifies what should go on each
    slide and stores the outline for each slide in a separate file. 
    """
    message = new_message(
        thread_id=thread.id,
        file_ids=[file.id for file in files],
        content="The pdf file I've attached is a script for a presentation, with a short agenda at the beginning,  that I gave to my development team on the history and general concepts of Kubernetes. Create an outline for the key portions of the presentation."
    )
    run = new_run(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    print(assistant.id, thread.id, message.id, run.id)
    store_ids({"assistant.id": assistant.id, "thread.id": thread.id, "message.id": message.id, "run.id": run.id})
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
