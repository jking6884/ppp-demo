# PPP Demo

After reading through the requirements in the document you put together and reading through
the documentation on the github page, I decided to approach this from the perspective 
of being a company that is working with a borrower and is writing an integration into the
API that you have written.

As such, I have tried to distill the data down the data that the your API deals with down into
various domain objects that would seem practical for representing companies, employees, loans and
the forgiveness requests.

I also took the approach of setting this up as a RESTful service that would serve as the back end
for this hypothetical company.

# In this project


## Postman

I have included a postman directory that has a collection and an environment file.

The collection has two main folders:
- one that corresponds to every endpoint for your SBA PPP API
- one that corresponds to the endpoints for the back end that I wrote

## PPP APP API

This is the the django project that represents that back end that I wrote for the hypothetical company.
 