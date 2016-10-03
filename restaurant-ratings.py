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

   user_restaurant = raw_input("Please enter a restaurant you'd like to add to our survey!\n")
   user_score = int(raw_input("How would you score this restaurant?\n"))
   scores[user_restaurant] = user_score

   # It doesn't matter if we use item() or .iteritem() here. Seince we are sorting it 
   # Which means uploading the dictionary first in memory any ways, and then only sort it.

   for restaurant, score in sorted(scores.iteritems()):
        print "%s is rated at %s." % (restaurant, score)

restaurant_ratings("scores.txt")