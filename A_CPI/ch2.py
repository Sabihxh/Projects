from math import sqrt
critics = {

'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},


'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},


'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},

'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},

'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},


'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},

'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}

}

#returns a distance based similarity score for person1 and person2

def sim_distance(prefs, person1, person2):
    #get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    #if they have no ratings in common, return 0
    if len(si) == 0: return 0

    #add up squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) 
        for item in prefs[person1] if item in prefs[person2]])

    return 1.0/(1+sum_of_squares)


# sim_distance(critics, 'Gene Seymour', 'Lisa Rose')

#returns the pearson correlation for p1 and p2
def sim_pearson(prefs, p1, p2):
    #Get the list of mutually rated shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    #find the number of elements
    n = len(si)

    #If there are no ratings in common
    if n == 0: return 0

    #Add up all the preferences
    sum1 = sum([prefs[p1][item] for item in si])
    sum2 = sum([prefs[p2][item] for item in si])

    #Sum up all the squares
    sum1_Sq = sum([pow(prefs[p1][item], 2) for item in si])
    sum2_Sq = sum([pow(prefs[p2][item], 2) for item in si])
    # print 'Sum 1: ', sum1_Sq
    # print 'Sum 2: ', sum2_Sq
    
    #Sum up the products
    pSum = sum([prefs[p1][item]*prefs[p2][item] for item in si])
    # print 'product Sum: ', pSum

    #Calculate Pearson score
    num = (n*pSum) - (sum1 * sum2)
    den = sqrt((n * sum1_Sq - pow(sum1, 2)) * (n * sum2_Sq - pow(sum2, 2)))
    if den == 0: return 0
    r = float(num)/den
    # print 'r = ', r
    return r

def getRecommendations(prefs, person, similarity = sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        #dont compare the person to itself
        if other == person: continue
        sim = similarity(prefs, person, other)
        #ignore score of 0 or lower
        if sim <= 0: continue

        for movie in prefs[other]:
            #only get score the movies that the person hasn't seen yet
            if movie not in prefs[person] or prefs[person][movie] == 0:
                #similarity * Score
                totals.setdefault(movie, 0)
                # print 'This is totals: ',  totals
                totals[movie] = totals[movie] + prefs[other][movie] * sim
                #sum of similarities
                simSums.setdefault(movie, 0)
                simSums[movie] += sim
    #create the normalized list
    rankings = [(total/simSums[movie], movie) for movie, total in totals.items()]

    #Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings

# getRecommendations(critics, 'Toby', similarity = sim_pearson)

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            #Flip item and person
            result[item][person] = prefs[person][item]
    return result

#returns the top matches for a person from prefs table. 
#Number of results and simlary functions are optional.
def topMatches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]



def calculateSimilarItems(prefs,n=10):
    # Create a dictionary of items showing which other items they
    # are most similar to.
    result = {}
    # Invert the preference matrix to be item-centric
    itemPrefs = transformPrefs(prefs)
    c = 0
    for item in itemPrefs:
    # Status updates for large datasets
        c += 1
        if c % 100 == 0: 
            print "%d / %d" % (c,len(itemPrefs))

    # Find the most similar items to this one
    scores = topMatches(itemPrefs,item,n=n,similarity=sim_distance)
    result[item] = scores
    return result


def loadMovieLens(path='./ml-100k'):
    #Get movie titles
    movies = {}
    for line in open(path+'/u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title

    #Load data
    prefs = {}
    for line in open(path+'/u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)

    return prefs












