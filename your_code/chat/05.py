from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)

result = chat.generate([[
    SystemMessage(content="Tell the user 3 facts about about Manchester United Football Club."),
    HumanMessage(content="I am a Manchester United fan, so make sure to tell me something that is new to me."),
    AIMessage(content="Okay. I will tell you a super niche fact!")
]] * 2)

print(len(result.generations))

