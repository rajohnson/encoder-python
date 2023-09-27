from enum import Enum, auto


class State(Enum):
    HH = auto()
    HL = auto()
    LL = auto()
    LH = auto()

    @classmethod
    def classify(cls, a: bool, b: bool):
        if a and b:
            return State.HH
        elif a and not b:
            return State.HL
        elif not a and not b:
            return State.LL
        elif not a and b:
            return State.LH

class Encoder:
    def __init__(self, a: bool = False, b: bool = False) -> None:
        self.state = State.classify(a, b)
        self.out = 0

    def update(self, a: bool, b: bool):
        old_state = self.state
        self.state = State.classify(a, b)
        if old_state == self.state: # No change since last update
            ...
        elif old_state == State.HH and self.state == State.HL:
            self.out -= 1
        elif old_state == State.HH and self.state == State.LH:
            self.out += 1
        elif old_state == State.HL and self.state == State.LL:
            self.out -= 1
        elif old_state == State.HL and self.state == State.HH:
            self.out += 1
        elif old_state == State.LL and self.state == State.LH: 
            self.out -= 1
        elif old_state == State.LL and self.state == State.HL:
            self.out += 1
        elif old_state == State.LH and self.state == State.HH:
            self.out -= 1
        elif old_state == State.LH and self.state == State.LL:
            self.out += 1
        else:
            raise ValueError("Unhandled state transition")
        