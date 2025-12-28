import random

DEFAULT_OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
DEFAULT_POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
DEFAULT_PERSONAL_PRONOUNS = ['She', 'He', 'They']
DEFAULT_STATES = ['California','Texas','Florida','New York','Pennsylvania','Illinois','Ohio','Georgia','North Carolina','Michigan']
DEFAULT_NOUNS = ['Athlete','Clown','Shovel','Paleo Diet','Doctor','Parent','Cat','Dog','Chicken','Robot','Video Game','Avocado','Plastic Straw','Serial Killer','Telephone Psychic']
DEFAULT_PLACES = ['House','Attic','Bank Deposit Box','School','Basement','Workplace','Donut Shop','Apocalypse Bunker']
DEFAULT_WHEN = ['Soon','This Year','Later Today','RIGHT NOW','Next Week']

def generate_headline(words):
    OP, PP, PER, ST, NO, PL, WH = words
    t = random.randint(1,8)

    if t == 1:
        return f"Are Millennials Killing the {random.choice(NO)} Industry?"
    if t == 2:
        return f"Without This {random.choice(NO)}, {random.choice(NO)}s Could Kill You {random.choice(WH)}"
    if t == 3:
        return f"Big Companies Hate {random.choice(OP)}! See How This {random.choice(ST)} {random.choice(NO)} Invented a Cheaper {random.choice(NO)}"
    if t == 4:
        return f"You Won't Believe What This {random.choice(ST)} {random.choice(NO)} Found in {random.choice(PP)} {random.choice(PL)}"
    if t == 5:
        return f"What {random.choice(NO)}s Don't Want You To Know About {random.choice(NO)}s"
    if t == 6:
        return f"{random.randint(7,15)} Gift Ideas to Give Your {random.choice(NO)} From {random.choice(ST)}"
    if t == 7:
        n1 = random.randint(3,19)
        n2 = random.randint(1,n1)
        return f"{n1} Reasons Why {random.choice(NO)}s Are More Interesting Than You Think (Number {n2} Will Surprise You!)"
    
    i = random.randint(0,2)
    if PP[i] == "Their":
        return f"This {random.choice(ST)} {random.choice(NO)} Didn't Think Robots Would Take {PP[i]} Job. {PER[i]} Were Wrong."
    else:
        return f"This {random.choice(ST)} {random.choice(NO)} Didn't Think Robots Would Take {PP[i]} Job. {PER[i]} Was Wrong."
