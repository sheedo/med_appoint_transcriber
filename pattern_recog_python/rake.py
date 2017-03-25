def clean_sentence():
    import RAKE
    import re
    path = "C:/Users/sunil/PycharmProjects/voice/pattern_recog_python/words.txt"
    r = RAKE.Rake(path)
    text = "Have two paracetamol in the morning.Have three advil in the night.Apply vicks in the night and morning.take asprin twice a day"
    split_sentences = text.split(".")
    i=0
    k = []
    for word in split_sentences:
        #print(r.run(word))
        #print("\n")
        #k[i]=r.run(word)
        #i+=1;
        k.append(r.run(word))

    print(k)
    clean_string = []
    for word in k:
        clean_string.append(re.sub('[^A-Za-z ]+', '', str(word)))

    for word in clean_string:
        print(word)
    return (clean_string)
#x=r.run(text)
#print (split_sentences) list.append(elem)