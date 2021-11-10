def cipher(text, shift, encrypt=True):
    """
    encrypting or decrypting a text with Caesar cipher.
    It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet

    Parameters
    ----------
    text : string
      text waiting to be encoded.
    shift: int
      shift of positions.
    encrypt: boolean
       If True, shift down the alphabet(encrypt);
       If False, shift up the alphabet(decrypt)

    Returns
    -------
    string
       text output after encrypt or decrypt.

    Examples 
    --------
    >>> from cipher_zg2382 import cipher
    >>> cipher('D', 3, True)
    'A'
    
    encrypting

    >>> from cipher_zg2382 import cipher
    >>> cipher('A', 3, False)
    'D'

    decrypting

    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
