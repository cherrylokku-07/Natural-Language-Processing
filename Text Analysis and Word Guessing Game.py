import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from random import randint

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet') 
#nltk.download('averaged_perceptron_tagger') 

def main():
    if len(sys.argv) < 2:
        print("No sys arg found")
        sys.exit(1)
    
    txt = sys.argv[1]

    print("System argument: ", txt)
    part2(txt)
    game(txt)

def part2(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("Reading contents...\n")
            tokens = nltk.word_tokenize(contents)
            tkset = set(tokens)
            ldiver = 100*len(tkset)/len(tokens)
            print("Lexical diversity: {:.2f}%\n".format(ldiver))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def part3(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        tokens = nltk.word_tokenize(content.lower())
        stop_words = set(stopwords.words('english'))
        filter_tokens = [token for token in tokens if token.isalpha() and token not in stop_words and len(token)>5 ]
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(token) for token in filter_tokens]
        lemmas = list(set(lemmas))
        ptag = pos_tag(lemmas)
        print("First 20 pos tag \n")
        for i,j in ptag[:20]:
            print(f"{i}: {j}")
        
        nounlemmas = [i for i,j in ptag if j.startswith('N')]
        print("\nNumber of tokens: ",len(tokens),"\nNumber of nouns: ",len(nounlemmas))
        return tokens,nounlemmas


def part4(file_path):
    tokens,nouns = part3(file_path)     
    noun_count = {}
    for noun in nouns:
        count = tokens.count(noun)
        noun_count[noun] = count
    
    sorted_dict = dict(sorted(noun_count.items(),key = lambda item:item[1],reverse=True))
    print("\n50 most common nouns are")
    for i,j in list(sorted_dict.items())[:50]:
        print(f"{i}: {j}")

    nounlist = list(sorted_dict.keys())[:50]
    return nounlist

def game(file_path):
    nouns = part4(file_path)
    test = str(nouns[randint(0,50)])
    score = 5
    testlen = len(test)
    t1 = ["_"]* testlen
    print("\nLet's play a word guessing game!\n")
    print(" ".join(t1))

    index=-1
    pos=[]
    while score>=1:
        user_input = input("Guess a letter: ")
        if  not user_input.strip():
            print("Empty input enter again\n")
            print(" ".join(t1))
            continue

        if user_input in test:
            if user_input in t1:
                print(f"{user_input} is present. Please enter another letter")
            else:
                score+=1
                pos = [i for i,j in enumerate(test) if j == user_input]
                for i in pos:
                    t1[i] = user_input
                print(f"Right! Score is {score}")
                print(" ".join(t1))

        else:
            score-=1
            print(f"Sorry, guess again. Score is {score}")
            print(" ".join(t1))
        if score == 0:
            print(f"You ran out of attempts, the word was: {test}")
            break
        if "_" not in t1:
            print("You solved it!\n")
            print(f"Current score: {score}")
            break

if __name__ == "__main__":
    main()