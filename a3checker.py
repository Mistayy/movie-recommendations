import sys

sys.path.insert(0, './pyta')


print("================= Start: checking coding style =================")

import python_ta
python_ta.check_all('recommender_functions.py', config='pyta/a3_pyta.txt')

print("================= End: checking coding style =================\n")


print("================= Start: checking parameter and return types =================")

import builtins
import copy
from io import StringIO

import recommender_functions as rf

# Check for use of functions print and input.

our_print = print
our_input = input

def disable_print(*args):
    raise Exception("You must not call built-in function print!")

def disable_input(*args):
    raise Exception("You must not call built-in function input!")

builtins.print = disable_print
builtins.input = disable_input

# Type check the recommender_functions.py functions

MOVIE_DICT_SMALL_COPY = copy.deepcopy(rf.MOVIE_DICT_SMALL)
USER_RATING_DICT_SMALL_COPY = copy.deepcopy(rf.USER_RATING_DICT_SMALL)
MOVIE_USER_DICT_SMALL_COPY = copy.deepcopy(rf.MOVIE_USER_DICT_SMALL)

TYPECHECK_FEEBACK = 'The return type for {} should be {}, but your code returned {}'

# Type check recommender_functions.read_movies
result = rf.read_movies(StringIO(rf.MOVIE_FILE_STR))
assert isinstance(result, dict), \
    TYPECHECK_FEEBACK.format('read_movies', 'dict', type(result))
for key in result:
    assert isinstance(key, int), \
        TYPECHECK_FEEBACK.format('read_movies', 'dict with int keys', 'dict with ' + type(key) + ' keys') 
    assert isinstance(result[key], tuple), \
        TYPECHECK_FEEBACK.format('read_movies', 'dict with tuple values', 'dict with ' + type(result[key]) + ' values')  

    assert isinstance(result[key][0], str) and isinstance(result[key][1], list), \
        TYPECHECK_FEEBACK.format('read_movies', 
                                 'dict with tuple values of (str, list)', 
                                 'list of tuple of (' + type(result[key][0]) + ', ' + \
                                 type(result[key][1]) + ')')


# Type check recommender_functions.read_ratings
result = rf.read_ratings(StringIO(rf.RATING_FILE_STR))
assert isinstance(result, dict), \
    TYPECHECK_FEEBACK.format('read_ratings', 'dict', type(result))
for key in result:
    assert isinstance(key, int), \
        TYPECHECK_FEEBACK.format('read_ratings', 'dict with int keys', 'dict with ' + type(key) + ' keys') 
    assert isinstance(result[key], dict), \
        TYPECHECK_FEEBACK.format('read_ratings', 'dict with dict values', 'dict with ' + type(result[key]) + ' values')  

# Type check recommender_functions.remove_unknown_movies
small_ratings = {1001: {68735: 5.0, 302156: 3.5, 10: 4.5}, 1002: {11: 3.0}}
small_ratings_copy = copy.deepcopy(small_ratings)
result = rf.remove_unknown_movies(small_ratings, rf.MOVIE_DICT_SMALL)
assert result == None, \
    TYPECHECK_FEEBACK.format('remove_unknown_movies', 'None', type(result))
assert small_ratings_copy != small_ratings, \
       'remove_unknown_movies should mutate the parameter'

# Type check recommender_functions.movies_to_users
result = rf.movies_to_users(rf.USER_RATING_DICT_SMALL)
assert isinstance(result, dict), \
    TYPECHECK_FEEBACK.format('movies_to_users', 'dict', type(result))
for key in result:
    assert isinstance(key, int), \
        TYPECHECK_FEEBACK.format('movies_to_users', 'dict with int keys', 'dict with ' + type(key) + ' keys') 
    assert isinstance(result[key], list), \
        TYPECHECK_FEEBACK.format('movies_to_users', 'dict with list values', 'dict with ' + type(result[key]) + ' values')  

# Type check recommender_functions.get_users_who_watched
result = rf.get_users_who_watched([293660], rf.MOVIE_USER_DICT_SMALL)
assert isinstance(result, list), \
    TYPECHECK_FEEBACK.format('get_users_who_watched', 'list', type(result))
for item in result:
    assert isinstance(item, int), \
        TYPECHECK_FEEBACK.format('get_users_who_watched', 'list of int', 'list of ' + type(item))
assert MOVIE_USER_DICT_SMALL_COPY == rf.MOVIE_USER_DICT_SMALL, \
       'get_users_who_watched should not mutate the parameter'

# Type check recommender_functions.get_similar_users
result = rf.get_similar_users({293660: 3.5}, rf.USER_RATING_DICT_SMALL, rf.MOVIE_USER_DICT_SMALL)
assert isinstance(result, dict), \
    TYPECHECK_FEEBACK.format('get_similar_users', 'dict', type(result))
for key in result:
    assert isinstance(key, int), \
        TYPECHECK_FEEBACK.format('get_similar_users', 'dict with int keys', 'dict with ' + type(key) + 'keys')
    assert isinstance(result[key], float), \
        TYPECHECK_FEEBACK.format('get_similar_users', 'dict with float values', 'dict with ' + type(result[key]) + ' values')

assert USER_RATING_DICT_SMALL_COPY == rf.USER_RATING_DICT_SMALL, \
       'get_similar_users should not mutate the parameter'
assert MOVIE_USER_DICT_SMALL_COPY == rf.MOVIE_USER_DICT_SMALL, \
       'get_similar_users should not mutate the parameter'

# Type check recommender_functions.recommend_movies
result = rf.recommend_movies({302156: 4.5},
                             rf.USER_RATING_DICT_SMALL,
                             rf.MOVIE_USER_DICT_SMALL,
                             2)
assert isinstance(result, list), \
    TYPECHECK_FEEBACK.format('recommend_movies', 'list', type(result))
for item in result:
    assert isinstance(item, int), \
        TYPECHECK_FEEBACK.format('recommend_movies', 'list of int', 'list of ' + type(item))
assert MOVIE_DICT_SMALL_COPY == rf.MOVIE_DICT_SMALL, \
       'recommend_movies should not mutate the parameter'
assert MOVIE_USER_DICT_SMALL_COPY == rf.MOVIE_USER_DICT_SMALL, \
       'recommend_movies should not mutate the parameter'


builtins.print = our_print
builtins.input = our_input

print("================= End: checking parameter and return types =================\n")

print("The parameter and return type checker passed.")
print("This means we will be able to test your code.")
print("It does NOT mean your code is necessarily correct.")
print("You should run your own thorough tests to convince yourself your code is correct.")
print()
print("Scroll up to review the output of checking coding style.")
print("Make sure you scroll all the way to the top to see style checking for both files")
