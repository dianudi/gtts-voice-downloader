from gtts import gTTS
from os.path import exists
from os import mkdir
from locale import getlocale

if not exists('out'):
    mkdir('out')


def main():
    if not exists('input.txt'):
        raise Exception('input.txt file is missing')
    lang = getlocale()[0].split('_')[0]
    with open('input.txt', 'r') as file:
        texts = file.readlines()
        if len(texts) == 0:
            raise Exception('No input text')
        for text in texts:
            text2 = text.split(' ')
            name = text2[0]
            text2.pop(0)
            tts = gTTS(' '.join(text2), lang=lang)
            tts.save(f'out/{name}.mp3')


if __name__ == '__main__':
    main()
