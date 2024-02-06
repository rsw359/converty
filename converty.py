import re
import g4f
from termcolor import colored

async def make_conversion(conversion:str ) -> str :
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
  
  ONLY RETURN THE CONVERSION. DO NOT ENGAGE IN ANY OTHER TYPE OF CONVERSATION. KEEP YOUR RESPONSES SHORT AND TO THE POINT. IF THE REQUEST IS OFF THE TOPIC OF CONVERSION, DO NOT PROVIDE AN ANSWER IN RELATING TO IT AT ALL. REQUEST A VALID CONVERSION REQUEST.
  ABSOLUTELY DO NOT RETURN THE SOURCE.

  """
  response = await g4f.ChatCompletion.create_async(
    # model= g4f.models.gpt_35_turbo_16k_0613,
    model= g4f.models.gpt_4_turbo,
    messages=[{'role':'user', 'content':prompt,}],
  )

  print(colored(response, 'green'))
  ## response cleanups
  #remove asterisks from the response
  response = response.replace('*', '')
  # Remove anything in square brackets or parentheses
  response = re.sub(r'\[.*?\]|\(.*?\)', '', response)
  # Remove anything after a newline
  response = re.sub(r'\n.*', '', response)
  
  return response

#for use in the terminal and testing
# conversion_request = input("What conversion would you like to make? ")
# make_conversion(conversion_request)
