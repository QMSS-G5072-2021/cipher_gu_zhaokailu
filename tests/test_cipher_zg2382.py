from cipher_zg2382 import cipher_zg2382

def test_cipher_single_word():
    w = 'ModernDataStructure'
    assert cipher(w, 1) == 'NpefsoEbubTusvduvsf', "Should be NpefsoEbubTusvduvsf"
