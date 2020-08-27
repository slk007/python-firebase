from firebase import firebase

firebase = firebase.FirebaseApplication("https://test-practise-1d48a.firebaseio.com/", None)

result = firebase.get('/test-practise-1d48a/Customer', '')
print(result)
