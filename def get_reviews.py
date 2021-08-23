import os

def main():
    """Read the main data file and run the menu loop."""
    print('Welcome to the movie sentiment program.')
    print('Enter a word to see the average rating of movies with that word.')
    file_name = 'movie_3_test.txt'
    # file_name = input('Enter file name with reviews: ')
    reviews = get_reviews(file_name)
    # choice = get_choice()
    # List of our functions. They all take a single parameter,
    # the reviews.
    # functions = [print_word_sentiment, print_sentiments_from_file,
    #              print_longest_review, print_shortest_review]
    # while '1' <= choice <= '4':
    #     # Get the index of the function to call.
    #     print
    #     index = ord(choice) - ord('1')
    #
    #     functions[index](reviews)
    #     choice = get_choice()


def get_reviews(file_name):
    """Given the file name, create a list of lists with the reviews.

    We expect one review per line. The first element will be an int [0, 4].
    The rest of the line is the review.
    All letters in the reviews are converted to lower case.
    """
    review_file = open(file_name, 'r')
    reviews = []
    line_number = 0
    line = review_file.readline().strip().lower()
    while line:
        line_number += 1
        reviews.append(line.split())
        line = review_file.readline().strip().lower()
        print(line)
      
        
    print(reviews)
  
    for a_review in reviews:
        print(a_review[0])
    # print('Found', line_number, 'lines')

    return reviews

    review_file.close()
    return reviews
    
main()
