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
    #     name="Ideas for what to create assignment",
    #     instructions="You are a helpful data analyst and creative problem solver. You will provide ideas for creative solutions when prompted with a list of domains and a file containing a list of supported file extensions and data types"
    # )
    # thread = new_thread()
    # uploaded_files = upload_files(["./combined_libraries_data.csv"])
    # message = new_message(
    #     thread_id=thread.id,
    #     content="Based on the list of file extensions and data types listed in this CSV file, come up with 100 ideas of types of files or outputs that you could create. Start with a generic list of types of files.",
    #     file_ids=[file.id for file in uploaded_files]
    # )
    # run = new_run(
    #     thread_id=thread.id,
    #     assistant_id=assistant.id
    # )
    # print(assistant.id, thread.id)
    # time.sleep(60)
    # Example follow-up prompt:
    # Using the domains of education, finance, sales, marketing, leadership, and management, generate 10 different ideas
    # of things you could create that are specific to each domain based on these types of files.
    # Optional:
    # All of the examples should be with Excel, Word, PDF, text, epub, CSV, images, movies, gifs, PowerPoint, html, or
    # other non-coding related formats.
    # asst_4d8zKv5Asyhrmzt1wLO6XNyX thread_YNguZnjyqmWwHKo2j7Sdhotl
    message_two = new_message(
        thread_id="thread_YNguZnjyqmWwHKo2j7Sdhotl",
        content="Using the domains of software engineering, system design, software architecture, financial operations, site reliability engineering, and platform engineering, generate 10 different ideas of things you could create that are specific to each domain based on these types of files."
    )
    run_two = new_run(
        thread_id="thread_YNguZnjyqmWwHKo2j7Sdhotl",
        assistant_id="asst_4d8zKv5Asyhrmzt1wLO6XNyX"
    )
    time.sleep(120)
    message_list = client.beta.threads.messages.list(
        thread_id="thread_YNguZnjyqmWwHKo2j7Sdhotl",
        order="asc"
    )
    for message in message_list:
        for content in message.content:
            if isinstance(content, MessageContentImageFile):
                print(f"Message with file content. ID is {content.image_file.file_id}", "\n", "------------------")
            elif isinstance(content, MessageContentText):
                formatted_output = content.text.value.replace('\\n', '\n').replace('\\t', '\t')
                print(formatted_output, "\n", "------------------")
