import unirest
# Get the drug name - can be used for verification of the drug name
query = 'tyl' # Possible drug name
response = unirest.get("https://iterar-mapi-us.p.mashape.com/api/autocomplete?query="+query,
  headers={
    "X-Mashape-Key": "BnN2GCt4eSmshetDxrUePKkzVuGNp1kmc5rjsnXGWoKy45MpHe",
    "Accept": "application/json"
  }
)
# Get the results HERE
print(response.body['suggestions'])

