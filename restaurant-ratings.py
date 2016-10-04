# your code goes here
def restaurant_ratings(path):
    """
    Creates a dictionary of restauirant names and scores, and allows the user to add one new entry.

    Prints dictionary contents, sorted by restaurant name.
    """
    scores_data = open(path)
    scores = {}
    for line in scores_data:
        line = line.rstrip()
        line = line.split(":")
        scores[line[0]] = line[1]
    scores_data.close() 

    user_answer = ''
    while user_answer.lower() != 'q':
        user_answer = raw_input("You can view our restaurant scores, or add a new entry!\n To view our restaurant scores, type 'view'\n To add a score entry type 'add'\n To exit, type 'q' \n") 
        if user_answer == 'view':
            for restaurant, score in sorted(scores.iteritems()):
                print "%s is rated at %s." % (restaurant, score)
        elif user_answer == "add":
            user_restaurant = raw_input("Please enter a restaurant you'd like to add to our survey!\n")
            user_score = int(raw_input("How would you score this restaurant?\n"))
            scores[user_restaurant] = user_score

            for restaurant, score in sorted(scores.iteritems()):
                print "%s is rated at %s." % (restaurant, score)
        elif user_answer != "q":
            print "\n I'm sorry! I don't recognize your input. Start again \n"


   # It doesn't matter if we use item() or .iteritem() here. Seince we are sorting it 
   # Which means uploading the dictionary first in memory any ways, and then only sort it.

   # for restaurant, score in sorted(scores.iteritems()):
   #      print "%s is rated at %s." % (restaurant, score)

restaurant_ratings("scores.txt")