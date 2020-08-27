from firebase import firebase

firebase = firebase.FirebaseApplication("https://test-practise-1d48a.firebaseio.com/", None)

firebase.put('/test-practise-1d48a/Customer/-MFjwndxPKEzHoX9wvlS', 'Name', 'Mayank')
print("updated")
