package blackjack

import "fmt"

type Hand struct {
	cards []*Card
}

func NewHand() *Hand {
	return &Hand{make([]*Card, 0)}
}

func (h *Hand) add(card *Card) {
	h.cards = append(h.cards, card)
}

func (h *Hand) drop() []*Card {
	cards := h.cards
	h.cards = make([]*Card, 0)
	return cards
}

func (h *Hand) showDown() {
	for _, card := range h.cards {
		if card.faceUp {
			card.flip()
		}
	}
}

func (h *Hand) show(check bool) {
	for _, card := range h.cards {
		card.show(check)
		fmt.Print(" ")
	}
	fmt.Println()
}

type HandBlackJack struct {
	Hand
}

func (hb *HandBlackJack) checkHitAllow() bool {
	return hb.calcTotalValue() != 22 && len(hb.cards) < 5
}

func (hb *HandBlackJack) checkSplitAllow() bool {
	return len(hb.cards) == 2 && hb.cards[0].value == hb.cards[1].value
}

func (hb *HandBlackJack) calcTotalValue() int {
	value := 0
	aceNum := 0
	for _, card := range hb.cards {
		if card.value == 1 {
			aceNum++
		} else if card.value > 10 {
			value += 10
		} else {
			value += card.value
		}
		if value > 21 {
			return 22
		}
	}
	// first count all ACE as 11
	value += aceNum * 11
	for i := 1; i < aceNum; i++ {
		if value > 21 {
			value -= 10
		}
	}
	if value > 21 {
		return 22
	}
	return value
}
