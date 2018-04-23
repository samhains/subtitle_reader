from webvtt import WebVTT

last = ''
for caption in WebVTT().read('./subs/Ashtar Command ! How The Event Will Unfold ! Messages from Ashtar-mt7PfVtGkA8.en.vtt'):
    textArr = caption.text.strip().split("\n")
    for text in textArr:
        if text == last:
            pass
        else:
            print(text)
            last = text

