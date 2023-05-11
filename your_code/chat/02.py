from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage

chat = ChatOpenAI(temperature=0.5)

result = chat([SystemMessage(content="Tell the user 3 facts about Manchester United Football Club!")])

print(result.content)