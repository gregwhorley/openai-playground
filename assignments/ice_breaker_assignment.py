from openai import OpenAI

client = OpenAI()


def instantiate_assistant(name, instructions):
    return client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=[{"type": "code_interpreter"}],
        model="gpt-4o"
    )


def instantiate_thread():
    return client.beta.threads.create()


def instantiate_file(file_with_relative_path):
    return client.files.create(
        file=open(file_with_relative_path, "rb"),
        purpose="assistants"
    )


def instantiate_message(thread_id, file_id, role, content):
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=content,
        file_ids=[file_id]
    )


def instantiate_run(thread_id, assistant_id):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

def output_image_file_from_assistant(file_id):
    image_data = client.files.content(file_id)
    image_data_bytes = image_data.read()
    with open(f"{file_id}", "wb") as file:
        file.write(image_data_bytes)


if __name__ == "__main__":
    # assistant = instantiate_assistant(
    #     name="Ice Breaker Assignment 1",
    #     instructions="You are a data analyst. Read in CSV files and produce output based on the prompt you are given by the user."
    # )
    # thread = instantiate_thread()
    # file = instantiate_file(
    #     file_with_relative_path="VanderbiltFinancialReport.csv"
    # )
    # print(f"Assistant ID: {assistant.id}")
    # print(f"Thread ID: {thread.id}")
    # print(f"File ID: {file.id}")
    # message = instantiate_message(
    #     thread_id=thread.id,
    #     file_id=file.id,
    #     role="user",
    #     content="Draw four visualizations for me that show me interesting things in this dataset. The visualization should show unexpected things based on higher education trends. Write 2-3 paragraphs describing the visualizations and what they show."
    # )
    # print(f"Message ID: {message.id}")
    # run = instantiate_run(
    #     thread_id="thread_LCL0Tgrw7d2wbA7UaTTPQBhQ",
    #     assistant_id="asst_AANLpTLHADd78OpBO09VOcBx"
    # )
    # print(f"Run ID: {run.id}")
    # run = client.beta.threads.runs.retrieve(
    #     thread_id="thread_LCL0Tgrw7d2wbA7UaTTPQBhQ",
    #     run_id="run_BJCi2i78dZQgBUaYKN5NkIU2"
    # )
    # print(run.status)
    # print(client.beta.threads.messages.list(
    #     thread_id="thread_LCL0Tgrw7d2wbA7UaTTPQBhQ"
    # ))
    # run_steps = client.beta.threads.runs.steps.list(
    #     thread_id="thread_LCL0Tgrw7d2wbA7UaTTPQBhQ",
    #     run_id="run_BJCi2i78dZQgBUaYKN5NkIU2"
    # )
    # print(run_steps)
    # output_image_file_from_assistant(file_id="file-quB0AHds6rvquuRTEwqlbPe1")
    # assistant = instantiate_assistant(
    #     name="Ice Breaker Assignment 2",
    #     instructions="You are a document reader. Read in PDF files and produce output based on the prompt you are given by the user."
    # )
    # thread = instantiate_thread()
    # file = instantiate_file(
    #     file_with_relative_path="./prompt_pattern_catalog.pdf"
    # )
    # message = instantiate_message(
    #     thread_id=thread.id,
    #     file_id=file.id,
    #     role="user",
    #     content="Please extract each page of this PDF to a plain text file. Then, manually read the first three pages and learn what a prompt pattern is. Don't worry if there are formatting issues, just do your best and proceed. Then, ask me to describe my job or interests. Use what I tell you to describe to me what a prompt pattern is assuming I have no background in computer science. Make sure and use concrete examples based on my job or interests to show how I could use these patterns.   Make sure and write some sample prompt patterns that could be cut/pasted into Code Interpreter for me to try out. Each pattern should rely on a document or dataset relevant to me. Describe the purpose of the pattern, the problem it is trying to solve, what data the pattern needs and why, and then the prompt that will be used on the document."
    # )
    # run = instantiate_run(
    #     thread_id=thread.id,
    #     assistant_id=assistant.id
    # )
    # run_retriever = client.beta.threads.runs.retrieve(
    #     thread_id="thread_jMANzBktIDqQzKHHtbofJHAP",
    #     run_id="run_LoqRHyobztGMB0oReEZwa48x"
    # )
    # print(f"Thread ID: {thread.id}")
    # print(f"Run ID: {run.id}")
    # print(f"Status: {run_retriever.status}")
    # print(client.beta.threads.messages.list(
    #     thread_id="thread_jMANzBktIDqQzKHHtbofJHAP"
    # ))
    # new_message = client.beta.threads.messages.create(
    #     thread_id="thread_jMANzBktIDqQzKHHtbofJHAP",
    #     role="user",
    #     content="My interests include: jigsaw puzzles, reading, video games, cooking, and weight lifting."
    # )
    print(client.beta.threads.messages.list(
        thread_id="thread_jMANzBktIDqQzKHHtbofJHAP"
    ))
    # new_run = instantiate_run(
    #     thread_id="thread_jMANzBktIDqQzKHHtbofJHAP",
    #     assistant_id="asst_9sBIkhkn6KEt2rugBTCqXp7o"
    # )
    # last_message = client.beta.threads.messages.create(
    #     thread_id="thread_jMANzBktIDqQzKHHtbofJHAP",
    #     role="user",
    #     content="Pick the ChatGPT Code Interpreter prompt pattern that you think would be most helpful to someone like me. Then, write a social media post about how you are taking the Coursera course \"ChatGPT Code Interpreter by Jules White\" and explain what Code Interpreter is, explain the problem the prompt pattern solves, what data you could upload with the prompt pattern, and what it would do for other people like me that would make their lives so much easier. Make the post exciting and have viral potential. Make sure readers have enough information to quickly cut/paste the pattern into Code Interpreter and know what to include with it in order to immediately take advantage of the prompt pattern."
    # )
    # last_run = instantiate_run(
    #     thread_id="thread_jMANzBktIDqQzKHHtbofJHAP",
    #     assistant_id="asst_9sBIkhkn6KEt2rugBTCqXp7o"
    # )
