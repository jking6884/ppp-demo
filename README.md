# PPP Demo

After reading through the requirements in the document you put together and reading through
the documentation on the github page, I decided to approach this from the perspective 
of being a lender that is working with a borrower and is writing an integration into the
API that you have written.

As such, I have tried to distill the data that your API uses down into 
various domain objects that would seem practical for lenders: company, user (employee), loan and then also
a forgiveness request domain class to represent the external records in your system.

I also took the approach of setting this up as a RESTful service that would serve as the back end
for this hypothetical lender.

# In this project


## Postman

I have included a postman directory that has a collection and an environment file.

The collection has two main folders:
- `SBA Loan Forgiveness API` is a collection of all of the endpoints in your API
- `PPP-Loan-API` is a collection of all of the endpoints that are in the back end app that I wrote

## PPP APP API

This is the the django rest framework project that represents that back end that I wrote for the hypothetical lender.
 
