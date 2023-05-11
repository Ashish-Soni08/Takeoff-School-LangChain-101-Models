# Takeoff School: LangChain 101 - Models

Introduction to LangChain, a framework for developing applications powered by language models.

## LLMs

How to instantiate an llm from OpenAI and make a request to the OPENAI API
```
python3 my_code/llm/01.py
```

How to use the `generate` method to make two requests instead of one.

```
python3 my_code/llm/02.py
```

Understanding token usage
```
python3 my_code/llm/03.py
```

Using Streaming which allows us to "stream" tokens as they come in from the request
```
python3 my_code/llm/04.py
```


## Chat Models

Initializing a Chat model
```
python3 my_code/chat/01.py
```

Making a request to the chat model, it needs 3 types of messages
- System messages: The system message acts as the instruction for the system.
- Human messages: Messages from the user.
- AI messages: The messages that were returned from the model.

```
python3 my_code/chat/02.py
```

A Full Chat
```
python3 my_code/chat/03.py
```

Streaming
```
python3 tut_code/chat/04.py
```

Using Generate
```
python3 my_code/chat/05.py
```

## Embedding Models

Embedding models take a piece of text and turn it into a vector.

The vector stores semantic information about the text and allows us to do powerful things like semantic search over embedded text.

Initialize An Embedding Model
```
python3 my_code/embeddings/01.py
```
Embedding A Query
```
python3 my_code/embeddings/02.py
```

Embedding Multiple Documents
```
python3 my_code/embeddings/03.py
```