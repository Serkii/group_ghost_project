import nltk
import re
from nltk.corpus import sentiwordnet as swn

def get_tags(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged

def get_tag_type(tags, tag_type):
    return [tag[0] for tag in tags if re.match(tag_type, tag[1])]

def verb_positivity(verb):
    pos = 0
    neg = 0
    for sense in swn.senti_synsets(verb, "v"):
        pos += sense.pos_score()
        neg += sense.neg_score()
        
    return pos - neg

def dump_sentence(sentence):
    global possible_subjects
    global possible_objects
    
    tags = get_tags(sentence)
    verbs = get_tag_type(tags, r'^VB.*$')
    nouns = get_tag_type(tags, r'^NN.*$')
    print("Verbs: " + repr(verbs))
    print("Nouns: " + repr(nouns))
    
    print("Approximating your intent:")
    if len(verbs) == 1 and len(nouns) == 1:
        print("You want to %s the %s." % (verbs[0].upper(), nouns[0].upper()))
    elif len(verbs) == 1 and len(nouns) == 2:
        subj = [thing for thing in nouns if thing in possible_subjects][0]
        nouns.remove(subj)
        obj = nouns[0]
        if verb_positivity(verbs[0]) > 0:
            print("You want to HELP the %s using the %s" % (obj.upper(), subj.upper()))
        else:
            print("You want to ATTACK the %s using the %s" % (obj.upper(), subj.upper()))
    else:
        print("That sentence is too complicated for me!")

possible_subjects = ["pizza", "book", "key"] # things in inventory
possible_objects = ["ghost"] # things in room

print("Loading...")
swn.senti_synsets("test", "v")

while True:
    dump_sentence(input("> "))
