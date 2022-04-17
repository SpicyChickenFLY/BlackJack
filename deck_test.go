package blackjack

import "testing"

func TestDeck_All(t *testing.T) {
	deck := NewDeck()
	deck.show(true)
	deck.shuffle()
	card := deck.deal()
	deck.drop(card)
	card = deck.deal()
	card.flip()
	deck.drop(card)
	deck.show(False)
	deck.recycle()
	deck.show(False)
}
