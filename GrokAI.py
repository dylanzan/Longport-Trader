import os

from openai import OpenAI

from __init__ import _X_GROK_API_BASE_URL, _X_GROK_API_KEY, _X_GROK_API_MODEL

class GrokAiX(object):

    def __init__(self):
        self.client = OpenAI(
            api_key=_X_GROK_API_KEY,
            base_url=_X_GROK_API_BASE_URL
        )

    def get_response(self, prompt):
        print(prompt)
        response = self.client.chat.completions.create(
            model=_X_GROK_API_MODEL,
            messages=[
                {"role": "system", "content": prompt}
            ],
        )
        return response.choices[0].message.content
