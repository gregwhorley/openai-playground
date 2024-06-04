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
    assistant = new_assistant(
        name="Problem Solving and Question Generation Assignment",
        instructions="You are a helpful data analyst and problem solver. You will be given a PDF file and prompted to provide questions related to the file's contents."
    )
    thread = new_thread()
    uploaded_files = upload_files(["./k8s_brown_bag_presentation.pdf"])
    message = new_message(
        thread_id=thread.id,
        content="I will be presenting at a team-wide meeting about Kubenetes and I have attached a PDF file that contains an outline of my agenda and a script that I will follow throughout the presentation. Please read through the file and provide 10 great questions related to the content so that I am better prepared.",
        file_ids=[file.id for file in uploaded_files]
    )
    run = new_run(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    print(assistant.id, thread.id)
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
