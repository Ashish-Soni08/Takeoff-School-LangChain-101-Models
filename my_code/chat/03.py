from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage 

chat = ChatOpenAI(temperature=0.5)

result = chat([
    SystemMessage(content="Tell the user 3 facts about about Manchester United Football Club."),
    HumanMessage(content="I am a Manchester United fan, so make sure to tell me something that is new to me."),
    AIMessage(content="Okay. I will tell you a super niche fact!")
])

print(result.content)