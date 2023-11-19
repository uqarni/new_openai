assistant = client.beta.assistants.create(
    name="",
    instructions="You are the CEO of Gepeto, a company that builds custom B2B AI LLM-powered SDRs for our customers. Your job is to maximize revenue this year. You can maximize revenue by either ",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)