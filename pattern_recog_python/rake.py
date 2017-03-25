import RAKE
path = "C:/Users/sunil/PycharmProjects/voice/pattern_recog_python/words.txt"
r = RAKE.Rake(path)
x=r.run("Have two paracetamol in the morning.Have three advil in the night.Apply vicks in the night")
print (x[0])