import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
        # TODO: What about a case where userID or friendID does not exist in self.users?

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()
        self.lastID += 1  # automatically increment the ID to assign the new user

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # for user in range(len(numUsers)):
        for _ in range(numUsers):
            # add new user
            self.addUser('Tim')  # Everyone is named Tim.



        # Create friendships
        totalFriendships = 0
        runs = 0

        # while totalFriendships < (numUsers * avgFriendships)
        while totalFriendships < ((numUsers * avgFriendships) // 2):
            # Choose a random person that is
            # 1) Not this person
            # 2) Not already in this persons friends
            runs += 1
            userID = random.choice(range(len(self.users)))
            friendID = random.choice(range(len(self.users)))
            disallowed = self.friendships[userID].copy()
            disallowed.add(userID)

            if friendID in disallowed:
                continue

            self.addFriendship(userID, friendID)
            totalFriendships += 1
        print(f'ran {runs} times for {totalFriendships * 2} total friendships')

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue = Queue()
        queue.enqueue([userID])
        visited = {}

        while queue.size() > 0:
            path = queue.dequeue()
            user = path[-1]

            if user not in visited:
                visited[user] = path

                for next_user in self.friendships[user]:
                    queue.enqueue([*path, next_user])

        count = 0;
        for f in visited:
            count += len(visited[f]) - 1
        
        print(f'Average Degrees of Separation: {count / len(visited)}')
        # print(len(visited))

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    # print(connections)
