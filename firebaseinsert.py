from firebase import firebase


firebase = firebase.FirebaseApplication("https://test-practise-1d48a.firebaseio.com/", None)
data = {
    'Name': 'Prateek Soni',
    'email': 'prateek.soni@gmail.com',
    'phone': "1646131331",
}

result = firebase.post('/test-practise-1d48a/Customer', data)
print(result)
