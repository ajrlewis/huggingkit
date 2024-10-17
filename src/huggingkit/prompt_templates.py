summarize = "Summarize the following text: `{text}`. Return only the summary of the text in your response."
extract = "Extract (infer if not present) these data points: {data_points}, from the following text: `{text}`. Return only the extracted data points as a JSON object in your response. Do not include any other text."
sentiment = "Determine the sentiment from the following text: `{text}`. Return only 'positive', 'negative' or 'neutral' depending on the sentiment. Do not include any other text."
code = "Generate code in the following language `{language}` to do the following: `{description}`. Return only the code in your response. Do not include any other text."
slogan = "Generate a slogan for company called `{name} ({description})`. Return only the slogan in your response."
paragraph = "Generate a website paragraph for company called `{name} ({description})`. Return only the paragraph in your response."
condense = "Analyze this text: `{text}`. Condense the text into a maximum of {number_of_words} words. Return only the condensed text in your response."


def render(template: str, **kwargs) -> str:
    return template.format(**kwargs)
