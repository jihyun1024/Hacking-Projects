import numpy as np
import matplotlib.pyplot as plt
import wave
import binascii
import os

def text_to_bin(text):
    binary = bin(int(binascii.hexlify(text.encode()), 16))
    return binary[2:]

def bin_to_text(binary):
    n = int('0b' + binary, 2)
    return binascii.unhexlify('%x' % n).decode('latin-1')

def hide_text_in_wave(wave_file, text):
    binary_text = text_to_bin(text)
    wave_data = wave.open(wave_file, 'rb')
    frame_bytes = bytearray(list(wave_data.readframes(wave_data.getnframes())))

    for i in range(len(binary_text)):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(binary_text[i])

    modified_wave = wave.open('modified_' + wave_file, 'wb')
    modified_wave.setparams(wave_data.getparams())
    modified_wave.writeframes(bytes(frame_bytes))
    modified_wave.close()

def extract_text_from_wave(wave_file, length):
    wave_data = wave.open(wave_file, 'rb')
    frame_bytes = bytearray(list(wave_data.readframes(wave_data.getnframes())))

    extracted_bits = [str(frame_bytes[i] & 1) for i in range(length * 8)]
    binary_text = ''.join(extracted_bits)
    text = bin_to_text(binary_text)
    return text


if __name__ == '__main__':
    input_wave_file = "Beethoven_Symphony No.6 in F major op.68 'Pastorale'.wav"
    text_to_hide = '''Two roads diverged in a wood, 
    and I took the one less traveled by, 
    And that has made all the difference.'''  

    choice = int(input('Enter 0 to hide, 1 to seek: '))
    filepath = os.chdir(input('Enter directory to hide and seek message: '))
    if choice == 0:
        hide_text_in_wave(input_wave_file, text_to_hide)
        print('An audio file with hidden text was created.')
    elif choice == 1:
        extracted_text = extract_text_from_wave('modified_' + input_wave_file, len(text_to_hide))
        print('Hidden text:', extracted_text)
    else:
        print('Enter 0 or 1')