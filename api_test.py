import http.client

conn = http.client.HTTPSConnection("google-translate113.p.rapidapi.com")

payload = "{\"from\":\"auto\",\"to\":\"vi\",\"protected_paths\":[\"extra.last_comment.author\"],\"common_protected_paths\":[\"image\"],\"json\":{\"title\":\"The Importance of Regular Exercise\",\"author\":\"John Doe\",\"rate\":4.2999,\"extra\":{\"image\":\"hello.jpg\",\"comment_counts\":10,\"last_comment\":{\"author\":\"not be translated\",\"short_text\":\"Hi thank for your post... We need more information\"}}}}"

headers = {
    'x-rapidapi-key': "e7b9e86cf0msh0cf27be123339bep17e891jsna72c5f4179cd",
    'x-rapidapi-host': "google-translate113.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/api/v1/translator/json", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))