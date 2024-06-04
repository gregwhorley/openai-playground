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
    with open(f"{file_id}", "wb") as file:
        file.write(image_data_bytes)


"""
Assistant ID: asst_cV55TCM17xiD6bsnDg2aCoeg
Thread ID: thread_nsQrJZjwqrDon0BQf7iJQjTM
File IDs: ['file-Iz2hkNkB0TaTO4KrtmCOMhOQ', 'file-wXsqpuJi2iJ7iZAKCEME8HPO']
Message ID: msg_yrCZyt5GJ3v3qO0YF0Wwj1qY
Run ID: run_jLrN0S7X2PSh7u6iNL2SGCYw
"""

if __name__ == "__main__":
    # assistant = new_assistant(
    #     name="Inspiration Assignment",
    #     instructions="You are an expert in data analysis. When given input in the form of prompts and file data, your output will guide the user in finding ways to use it in their personal life and work."
    # )
    # thread = new_thread()
    # files = upload_files(["./combined_libraries_data.csv", "street_art.jpg"])
    # print(f"Assistant ID: {assistant.id}")
    # print(f"Thread ID: {thread.id}")
    # print(f"File IDs: {[file.id for file in files]}")
    # message = new_message(
    #     thread_id=thread.id,
    #     content="1. Ask me questions about the context of the work I am doing (e.g., work/personal, job title, industry, goals). 2. I have uploaded two files. One is a CSV file named combined_libraries_data.csv that you are going to use as a reference. The other file is the one I need ideas for. 3. Using the attached CSV, look at the type of the other file I just uploaded, then, based on the file extension and data type, look into the combined_libraries_data.csv CSV for potential things that you could do with this file and provide me with 10 ideas related to what you know about me. Explain the ideas by a) describing the problem that is being solved, b) explaining what Code Interpreter could do to solve the problem, c) listing the text for the prompt that you would cut/paste into ChatGPT Advanced Data Analysis along with the file to implement the solution. None of the solutions should be about generating software. Ask me the just the first question.",
    #     file_ids=[file.id for file in files]
    # )
    # print(f"Message ID: {message.id}")
    # run = new_run(
    #     thread_id=thread.id,
    #     assistant_id=assistant.id
    # )
    # print(f"Run ID: {run.id}")
    # message = new_message(
    #     thread_id="thread_nsQrJZjwqrDon0BQf7iJQjTM",
    #     content="1. Personal project 2. Job title is SRE and I work in security software industry 3. My goal is to experiment with OpenAI's Assistants API by programmatically inputting data and prompts in order to familiarize myself with the structure of the outputs."
    # )
    # run = new_run(
    #     thread_id="thread_nsQrJZjwqrDon0BQf7iJQjTM",
    #     assistant_id="asst_cV55TCM17xiD6bsnDg2aCoeg"
    # )
    # message = new_message(
    #     thread_id="thread_nsQrJZjwqrDon0BQf7iJQjTM",
    #     content="Out of all of the use cases in this thread, pick one that you think would be most helpful to someone like me. Then, write a social media post about how you are taking the Coursera course \"ChatGPT Code Interpreter by Jules White\" and explain what Code Interpreter is, explain the problem the use case solves, what data you could upload to support the use case, and what it would do for other people like me that would make their lives so much easier. Make the post exciting and have viral potential. Make sure readers have enough information to quickly implement the idea by cutting / pasting some things into Code Interpreter and know what to include with it in order to immediately take advantage of the idea."
    # )
    # run = new_run(
    #     thread_id="thread_nsQrJZjwqrDon0BQf7iJQjTM",
    #     assistant_id="asst_cV55TCM17xiD6bsnDg2aCoeg"
    # )
    print(client.beta.threads.messages.list(
        thread_id="thread_nsQrJZjwqrDon0BQf7iJQjTM",
        order="desc"
    ))
