import time

from openai import OpenAI

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


def upload_files(list_of_filenames=None):
    if list_of_filenames is None:
        list_of_filenames = []
    file_objects = []
    for f in list_of_filenames:
        file_obj = client.files.create(
            file=open(f, "rb"),
            purpose="assistants"
        )
        file_objects.append(file_obj)
    return file_objects


def new_message(thread_id, content, attachments=None):
    if attachments is None:
        attachments = []
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content,
        attachments=attachments
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
    # asst = new_assistant(
    #     name="Cover letter assistant",
    #     instructions="You are an experienced cover letter writer and data analyst. You will help write a cover letter when you are provided with a resume and job description. Do not put too much emphasis on the company values."
    # )
    # thread = new_thread()
    # uploaded_files = upload_files(["./greg_whorley.txt", "./job_description.txt"])
    # # thread_id = "thread_elsheFqzfBuCfYwz9TErAalU"
    # # asst_id = "asst_20YYyRUAFJVOxVVeOttJBpru"
    # message = new_message(
    #     thread_id=thread.id,
    #     content="I have attached my resume named greg_whorley.txt and a job description named job_description.txt. Please draft a cover letter that accurately frames my experience as it is relevant to the job description.",
    #     attachments=[file.id for file in uploaded_files]
    # )
    # run = new_run(
    #     thread_id=thread.id,
    #     assistant_id=asst.id
    # )
    # print(asst.id, thread.id)
    # time.sleep(60)
    message_list = client.beta.threads.messages.list(
        thread_id="thread_mSZ2rZdhpIpnEdUvVmnotPnp",
        order="asc"
    )
    # for message in message_list:
    #     for content in message.content:
    #         if isinstance(content, MessageContentImageFile):
    #             print(f"Message with file content. ID is {content.image_file.file_id}", "\n", "------------------")
    #         elif isinstance(content, MessageContentText):
    #             formatted_output = content.text.value.replace('\\n', '\n').replace('\\t', '\t')
    #             print(formatted_output, "\n", "------------------")
    for message in message_list:
        for content in message.content:
            print(type(content))
            formatted_output = content.text.value.replace('\\n\\n', '\n').replace('\\n', '\n')
            print(formatted_output, "\n", "---------------------------------------------")
