from openai import OpenAI
from openai.types.beta.threads import MessageContentImageFile, MessageContentText
import time


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


def download_file_from_assistant(file_id):
    file_data = client.files.content(file_id)
    file_data_bytes = file_data.read()
    with open(f"./{file_id}", "wb") as file:
        file.write(file_data_bytes)


if __name__ == "__main__":
    # assistant = new_assistant(
    #     name="Exploring Code Interpreter Use Cases Assignment",
    #     instructions="You are a helpful assistant that can analyze input in the form of PDF files or images and produce output based on prompts that are sent to you."
    # )
    # thread = new_thread()
    # uploaded_files = upload_files(["./street_art1.jpg", "./street_art2.jpg", "./street_art3.jpg"])
    # message = new_message(
    #     thread_id=thread.id,
    #     content="For each image provided, I want you to resize them in multiple ways. First, shrink each image to half its original size. Next, stretch each image to twice its original size. Lastly, change each image's aspect ratio to a setting that you choose. After you have done this, create a CSV file with a catalog of the images and the transformations applied to them.",
    #     file_ids=[file.id for file in uploaded_files]
    # )
    # run = new_run(
    #     thread_id=thread.id,
    #     assistant_id="asst_80PYLOc32bLYIYDNbL8cL1hW"
    # )
    # print(thread.id, message.id, run.id)
    # print("Waiting two minutes...")
    # time.sleep(120)
    message_list = client.beta.threads.messages.list(
        thread_id="thread_cD1LhGFLxSmCC579MleIjxD9",
        order="asc"
    )
    for message in message_list:
        for content in message.content:
            if isinstance(content, MessageContentImageFile):
                print(f"Downloading file content with ID {content.image_file.file_id}", "\n", "------------------")
                download_file_from_assistant(content.image_file.file_id)
            if isinstance(content, MessageContentText):
                formatted_output = content.text.value.replace('\\n', '\n').replace('\\t', '\t')
                print(formatted_output, "\n", "------------------")
    for message in message_list:
        for content in message.content:
            annotations = content.text.annotations
            for annotation in annotations:
                if annotation.file_path:
                    print(f"Downloading file with ID: {annotation.file_path.file_id}")
                    download_file_from_assistant(annotation.file_path.file_id)


"""
Upload one or more images and have Code Interpreter create copies of each image in multiple different sizes.
Have Code Interpreter create a CSV file with a catalog of the images and the transformations applied to the
images. 
"""
