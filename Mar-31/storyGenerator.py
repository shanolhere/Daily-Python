#Story Generator with Python
import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print("{}, {} named {} that lived in {} went to {} and {}". format(random.choice(when), random.choice(who), random.choice(name), random.choice(residence), random.choice(went), random.choice(happened)))