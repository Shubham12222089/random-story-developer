import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
place = ['Barcelona','India', 'Germany', 'Venice', 'England']
where = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends.','Eats a burger.', 'found a secret key.', 'solved a mistery.', 'wrote a book.']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(place) + ', went to the ' + random.choice(where) + ' and ' + random.choice(happened))