package blackjack

import (
	"fmt"
	"math/rand"
	"time"
)

const (
	spade = iota
	club
	heart
	diamond
	suitNum
)

// deckType
const (
	fullSize = iota
	noJoker
	numOnly
)

type Deck struct {
	cards        []*Card
	discardCards []*Card
}

// """
// size: full_size, no_joker, num_only, single_suit
// duplicate >= 1
// """
func NewDeck(duplicate, size int) *Deck {
	deck := &Deck{}
	deck.cards = make([]*Card, 0)
	deck.discardCards = make([]*Card, 0)
	for dup := 0; dup < duplicate; dup++ {
		if size == noJoker {
			for suit := 0; suit < suitNum; suit++ {
				for value := 1; value < 14; value++ {
					deck.cards = append(deck.cards, NewCard(value, suit, false))
				}
			}
		}
	}
	deck.shuffle()
	return deck
}

func (d *Deck) shuffle() {
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(d.cards), func(i, j int) {
		d.cards[i], d.cards[j] = d.cards[j], d.cards[i]
	})
}

func (d *Deck) deal(flip bool) *Card {
	var card *Card
	if len(d.cards) > 0 {
		card = d.cards[0]
		if len(d.cards) == 1 {
			d.cards = make([]*Card, 0)
		} else {
			d.cards = d.cards[1:]
		}
	} else if len(d.cards) == 0 {
		d.recycle()
		card = d.deal(false)
	}
	if flip {
		card.flip()
	}
	return card
}

func (d *Deck) drop(card *Card) {
	if !card.faceUp {
		card.flip()
	}
	d.discardCards = append(d.discardCards, card)
}

func (d *Deck) recycle() {
	for _, card := range d.discardCards {
		card.flip()
		d.cards = append(d.cards, card)
	}
	d.discardCards = make([]*Card, 0)
	d.shuffle()
}

func (d *Deck) show(check bool) {
	fmt.Print("cards: ")
	for _, card := range d.cards {
		card.show(check)
		fmt.Print(" ")
	}
	fmt.Println()
	fmt.Print("discardCards: ")
	for _, card := range d.discardCards {
		card.show(check)
		fmt.Print(" ")
	}
	fmt.Println()
}

type Card struct {
	value  int
	suit   int
	faceUp bool
}

// """
// value: 1~15
// suit: spade, club, heart, diamond, None
// """
func NewCard(value, suit int, faceUp bool) *Card {
	card := &Card{
		value,
		suit,
		faceUp,
	}
	return card
}

func (c *Card) flip() {
	c.faceUp = !c.faceUp
}

func (c *Card) show(check bool) {
	if !c.faceUp && !check {
		fmt.Print("Hidden")
	} else if c.value == 15 {
		fmt.Print("Joker(Red)")
	} else if c.value == 14 {
		fmt.Print("Joker(Black)")
	} else if c.value == 13 {
		fmt.Print(fmt.Sprintf("%d-King", c.suit))
	} else if c.value == 12 {
		fmt.Print(fmt.Sprintf("%d-Queen", c.suit))
	} else if c.value == 11 {
		fmt.Print(fmt.Sprintf("%d-Jack", c.suit))
	} else {
		fmt.Print(fmt.Sprintf("%d-%d", c.suit, c.value))
	}
}
