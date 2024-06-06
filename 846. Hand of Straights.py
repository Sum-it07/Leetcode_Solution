class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        # Count the frequency of each card
        count = {}
        for card in hand:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1
        
        # Sort the unique cards
        unique_cards = sorted(count.keys())
        
        for card in unique_cards:
            while count[card] > 0:
                # Try to create a group starting from this card
                for i in range(groupSize):
                    if card + i not in count or count[card + i] <= 0:
                        return False
                    count[card + i] -= 1
        
        return True
