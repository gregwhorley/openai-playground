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
    #     name="Data to Content Assignment",
    #     instructions="You are a helpful data analyst. You will be given a CSV file and a list of questions about this file."
    # )
    # thread = new_thread()
    # uploaded_files = upload_files(["./VanderbiltFinancialReport2.csv"])
    # message = new_message(
    #     thread_id=thread.id,
    #     content="Read and explain all of the columns in the attached CSV file.",
    #     file_ids=[file.id for file in uploaded_files]
    # )
    # run = new_run(
    #     thread_id=thread.id,
    #     assistant_id=assistant.id
    # )
    # print(f"Assistant ID: {assistant.id}")
    # print(f"Thread ID: {thread.id}")
    # print(f"File IDs: {[file.id for file in uploaded_files]}")
    # print(f"Message ID: {message.id}")
    # print(f"Run ID: {run.id}")
    # second_msg = new_message(
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI",
    #     content="Create four interesting visualizations of this data that show the school's admissions rate and other indicators of success over time and try to use the Vanderbilt school colors. Draw trend lines on all charts."
    # )
    # second_run = new_run(
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI",
    #     assistant_id="asst_N70abWNqmg4i20uCAk8DArs3"
    # )
    # third_msg = new_message(
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI",
    #     content="Save each of these visualizations as a separate image file for me to download."
    # )
    # third_run = new_run(
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI",
    #     assistant_id="asst_N70abWNqmg4i20uCAk8DArs3"
    # )
    # fourth_msg = new_message(
    #     content="Create a PowerPoint presentation for me that has each of these images as separate slides.",
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI"
    # )
    # fourth_run = new_run(
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI",
    #     assistant_id="asst_N70abWNqmg4i20uCAk8DArs3"
    # )
    # last_msg = new_message(
    #     content="Output CSV describing the process that you just performed starting from the data and going all the way to the production of the slides.",
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI"
    # )
    # last_run = new_run(
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI",
    #     assistant_id="asst_N70abWNqmg4i20uCAk8DArs3"
    # )
    # new_message(
    #     content="Find a really interesting insight in this data. Visualize the insight for me and save it as an image. Write a social media post explaining that you used prompts from the Coursera course 'ChatGPT Code Interpreter by Jules White' to create an interesting analysis of Vanderbilt's 2022 finances and include in the post the interesting thing seen in the visualization.",
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI"
    # )
    # new_run(
    #     thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI",
    #     assistant_id="asst_N70abWNqmg4i20uCAk8DArs3"
    # )
    message_list = client.beta.threads.messages.list(
        thread_id="thread_4s6uzNkFEJg0GSwRVJsI0CgI",
        order="asc"
    )
    for message in message_list:
        for content in message.content:
            if isinstance(content, MessageContentImageFile):
                print(f"Message with file content. ID is {content.image_file.file_id}", "\n", "------------------")
            elif isinstance(content, MessageContentText):
                formatted_output = content.text.value.replace('\\n', '\n').replace('\\t', '\t')
                print(formatted_output, "\n", "------------------")
    # output_image_file_from_assistant(file_id="file-2hvSeq0mQQAUahXcblpHYmXT.png")

"""
Assistant ID: asst_N70abWNqmg4i20uCAk8DArs3
Thread ID: thread_4s6uzNkFEJg0GSwRVJsI0CgI
"""
