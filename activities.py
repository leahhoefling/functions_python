# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

# For example, Jay ran like a fool! or Chantelle slid down the slide!.

# The following lists of children should be iterated, and the names sent to the appropriate functions.

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]


def run(kid_name):
    print(f"{kid_name} can run as fast as a cheetah!")


def slide(kid_name):
    print(f"{kid_name} slid like a snake!")


def swing(kid_name):
    print(f"{kid_name} swings like a monkey!")


def hide_and_seek(kid_name):
    print(f"{kid_name} hid during a game of hide & seek like an ostrich!")


for kid in hiding_kids:
    hide_and_seek(kid)

for kid in running_kids:
    run(kid)

for kid in sliding_kids:
    slide(kid)

for kid in swinging_kids:
    swing(kid)
