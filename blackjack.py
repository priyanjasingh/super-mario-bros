import simpleguitk as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "djcnd"
score = 0

ask = "kcjdkc"
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card_object = []
        
        pass	# create Hand object

    def __str__(self):
        ans = ""
        for i in range(len(self.card_object)):
            ans += str(self.card_object[i])
            ans+= ','
        return ans
        pass	# return a string representation of a hand

    def add_card(self, card):
        
        self.card_object.append(card)
        pass	# add a card object to a hand

    def get_value(self):
        value=0
        flag=False
        for i in self.card_object:
            if(i.get_rank() == 'A'):
                flag=True
            value += VALUES[i.get_rank()]
        if(flag==False):
            return value
        else:
            if(value+10<21):
                return value+10
            else:
                return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.card_object:
            pos1 = ((pos[0]+ i*(CARD_SIZE[0]+20))-100,pos[1])
            
            if(i<5):
                card.draw(canvas,pos1)
                i+=1
        pass	# draw a hand on the canvas, use the draw method for cards
 
    

    
    
class Deck:
    def __init__(self):
        self.deck = []
        
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit,rank)
                self.deck.append(card)              
                
        pass	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
        pass    # use random.shuffle()

    def deal_card(self):
        
        return self.deck.pop()
        pass	# deal a card object from the deck
    
    def __str__(self):
        ans = ""
        for i in range(len(self.deck)):
            ans += str(self.deck[i])
            ans+= ' '
        return ans
     
        pass	# return a string representing the deck

DECK = Deck()
dealer = Hand()
Player = Hand() 


#define event handlers for buttons
def deal():
    global outcome, in_play,dealer,Player,DECK,outcome,ask
    outcome=""
    ask="Hit or Stand ?"
    DECK = Deck()
    DECK.shuffle()
    dealer = Hand()
    Player = Hand() 
  
    dealer.add_card(DECK.deal_card())
    dealer.add_card(DECK.deal_card())
    Player.add_card(DECK.deal_card())
    Player.add_card(DECK.deal_card())
    print dealer
    print Player
    # your code goes here
    
    in_play = True
  

def hit():
    pass	# replace with your code below
    global score,outcome,ask,Player,DECK,in_play
    if in_play==False:
        return
    Player.add_card(DECK.deal_card())
    
    if(Player.get_value()>21):
        print "You have Busted"
        score-=1
        outcome = "You Lost"
        ask = "New Deal ?"
        in_play=False
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global score,outcome,ask,in_play,Player,dealer
    in_play = False
    if(Player.get_value()>=21):
        outcome = "You Lost"
    else:
        while(dealer.get_value()<17):
            dealer.add_card(DECK.deal_card())
        if(dealer.get_value()<=21):
            if(dealer.get_value()<=Player.get_value()):
                print "Player won"
                outcome = "You won"
                ask = "New Deal ?"
                score+=1
                
            else:
                print "dealer won"
                outcome = "You lost"
                ask = "New Deal ?"
        else:
            print "Dealer Busted"
            outcome = "You won"
            ask = "New Deal ?"
        
            
        
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome,ask,card_back,CARD_CENTER,CARD_SIZE,card,dealer,Player
    dealer.draw(canvas,[200,200])
    Player.draw(canvas,[200,370])
    canvas.draw_text("Blackjack",(100,80), 50, "Cyan")
    
    canvas.draw_text("Dealer",(100,190), 30, "Black")
    canvas.draw_text("Player",(100,360), 30, "Black")
    canvas.draw_text(outcome,(350,190), 30, "Black")
    canvas.draw_text(ask,(350,360), 30, "Black")
    canvas.draw_text("Score= "+str(score),(400,80), 30, "Black")
    
    if in_play==True:
        card_loc = (CARD_BACK_CENTER[0] ,  CARD_BACK_CENTER[1])            
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [100 + CARD_CENTER[0], 200 + CARD_CENTER[1]], CARD_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
label = frame.add_label('Outcome')
#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
