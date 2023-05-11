from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature = 1)

llm("Tell me a joke about dogs.")