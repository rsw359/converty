import g4f
from termcolor import colored

def make_conversion(conversion:str ) -> str :
  """
  Make unit conversion from one unit to another.

  Args: 
      conversion: conversion with units (str). Example 10m to feet.

  Returns: 
       str:conversion in the desired unit.

  """

  prompt = f""" 
  Make the requested conversion from one unit to another
  Conversion: {conversion}
  The conversion is to be returned as a string with the desired unit conversion in a similar format as the following: '100ft is equal to 30.48ft'

  No other conversion is required.
  Do not reference this response directly.
  If the user input is not a conversion request, please respond with the following: " I'm sorry, but I can only make unit conversions. Please provide a valid conversion request."
  ONLY RETURN THE CONVERSION. Do NOT ENGAGE IN ANY OTHER TYPE OF CONVERSATION.

  """
  response = g4f.ChatCompletion.create(
    model= g4f.models.gpt_35_turbo_16k_0613,
    messages=[{'role':'user', 'content':prompt,}],
  )

  print(colored(response, 'green'))

conversion_request = input("What conversion would you like to make? ")
make_conversion(conversion_request)
