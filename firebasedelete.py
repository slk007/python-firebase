from firebase import firebase

firebase = firebase.FirebaseApplication("https://test-practise-1d48a.firebaseio.com/", None)

firebase.delete('/test-practise-1d48a/Customer/','-MFjvhSs3rMdYEoDqbln')
print("deleted")
