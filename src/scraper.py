import requests

from bs4 import BeautifulSoup
from typing import Any, List


class Scraper:
  def __init__(self, url:str) -> None:
    try:
      response = requests.get(url=url)
      self.soup = BeautifulSoup (response.content, 'html.parser')
    except Exception as e:
      raise Exception(e)

  def create_vectorstore (self) -> Any:
    # TODO 1. Extract the paragraphs

    # TODO 2. Create a vectorstore with the paragraphs 

    # TODO 3. Return the vectorstore
    pass
