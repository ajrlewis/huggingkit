from huggingface_hub import InferenceClient
from loguru import logger

import prompt_templates


def completion(
    client: InferenceClient,
    messages: list[dict],
    max_tokens: int = 7000,
    temperature: float = 0.2,
) -> dict:
    """Returns the next message using a chat completion.

    Args:
        client: The inference client.
        messages: A list of messages.
        max_token: The maximum number of tokens allowed in the response 75 words approximately equals 100 tokens.
        temperature: Controls randomness of the generations between [0, 2]. Lower values ensure less random completions.
    """
    logger.debug(f"{temperature = } {max_tokens = }")
    logger.debug(f"{messages = }")
    output = client.chat_completion(
        messages, temperature=temperature, max_tokens=max_tokens
    )
    choices = output.choices
    choice = choices[0]
    message = choice.message
    message = {"role": message.role, "content": message.content}
    return message


def create_message(role: str, content: str) -> dict:
    return {"role": role, "content": content}


def create_user_message(content: str) -> dict:
    return {"role": "user", "content": content}


def extract(client: InferenceClient, text: str, data_points: dict) -> dict:
    content = prompt_templates.render(
        prompt_templates.extract, text=text, data_points=data_points
    )
    messages = [{"role": "user", "content": content}]
    message = completion(client=client, messages=messages)
    logger.debug(f"{message = }")
    return message


def summarize(client: InferenceClient, text: str) -> dict:
    content = prompt_templates.render(prompt_templates.summarize, text=text)
    messages = [{"role": "user", "content": content}]
    message = completion(client=client, messages=messages)
    logger.debug(f"{message = }")
    return message


def sentiment(client: InferenceClient, text: str) -> dict:
    content = prompt_templates.render(prompt_templates.sentiment, text=text)
    messages = [{"role": "user", "content": content}]
    message = completion(client=client, messages=messages)
    logger.debug(f"{message = }")
    return message


def code(client: InferenceClient, language: str, description: str) -> dict:
    content = prompt_templates.render(
        prompt_templates.code, language=language, description=description
    )
    messages = [{"role": "user", "content": content}]
    message = completion(client=client, messages=messages)
    logger.debug(f"{message = }")
    return message


def slogan(client: InferenceClient, name: str, description: str) -> dict:
    content = prompt_templates.render(
        prompt_templates.slogan, name=name, description=description
    )
    messages = [{"role": "user", "content": content}]
    message = completion(client=client, messages=messages)
    logger.debug(f"{message = }")
    return message


def paragraph(client: InferenceClient, name: str, description: str) -> dict:
    content = prompt_templates.render(
        prompt_templates.paragraph, name=name, description=description
    )
    messages = [{"role": "user", "content": content}]
    message = completion(client=client, messages=messages)
    logger.debug(f"{message = }")
    return message


def condense(client: InferenceClient, text: str, number_of_words: int) -> dict:
    content = prompt_templates.render(
        prompt_templates.condense, text=text, number_of_words=number_of_words
    )
    messages = [{"role": "user", "content": content}]
    message = completion(client=client, messages=messages)
    logger.debug(f"{message = }")
    return message
