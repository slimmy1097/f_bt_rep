print('s')

MORSE_CODE = {}
MORSE_CODE['.-'] = 'A'
MORSE_CODE['--...'] = '7'
MORSE_CODE['...-..-'] = '$'
MORSE_CODE['...'] = 'S'
MORSE_CODE['---'] = 'O'

#        test.assert_equals(decode_morse('...---...'), 'SOS')
#        test.assert_equals(decode_morse('... --- ...'), 'SOS')
#   test.assert_equals(decode_morse('...   ---   ...'), 'S O S')

inp = '...   ---   ...'

def decode_morse(morse_code: str):
    inp = morse_code.strip()
    inp = inp.split(' ')
    try:
        iterartion = iter(morse_code)
        a = str(next(iterartion))
        print(iterartion)
    except:
        return ''

print(decode_morse(inp))