import pytest
from encoder import Encoder, State

@pytest.fixture
def encoder():
    return Encoder()

def test_encoder_init():
    enc = Encoder()
    assert enc.state == State.LL
    assert enc.out == 0

@pytest.mark.parametrize("a, b", [ (True, False), (False, False), (False, True), (True, True) ])
def test_encoder_update_unchanged(a, b):
    enc = Encoder(a, b)
    enc.update(a, b)
    assert enc.state == State.classify(a, b)
    assert enc.out == 0

def test_encoder_invalid_transition(encoder):
    with pytest.raises(ValueError):
        encoder.update(True, True)

def test_encoder_LL_to_HL(encoder):
    encoder.update(True, False)
    assert encoder.state == State.HL
    assert encoder.out == 1

def test_encoder_clockwise(encoder):
    encoder.update(True, False)
    assert encoder.out == 1

    encoder.update(True, True)
    assert encoder.out == 2

    encoder.update(False, True)
    assert encoder.out == 3

    encoder.update(False, False)
    assert encoder.out == 4

def test_encoder_counter_clockwise(encoder):
    encoder.update(False, True)
    assert encoder.out == -1

    encoder.update(True, True)
    assert encoder.out == -2

    encoder.update(True, False)
    assert encoder.out == -3

    encoder.update(False, False)
    assert encoder.out == -4

def test_encoder_spin_opposing(encoder):
    # Spin counterclockwise
    encoder.update(False, True)
    encoder.update(True, True)
    encoder.update(True, False)
    encoder.update(False, False)
    # Spin clockwise
    encoder.update(True, False)
    encoder.update(True, True)
    encoder.update(False, True)
    encoder.update(False, False)
    
    assert encoder.out == 0
