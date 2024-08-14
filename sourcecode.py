'''
Source Code. Testing is already being done at the bottom. Must run with errors and a final printed statement of "All tests passed"
'''
class digraph(object): # Main backbone of the game. Handles traversing and construction
    '''A directed graph that constructs the main backbone of the game.'''
    def __init__(self, vertex = 0):
        '''Creates an empty graph with (vertex) amount of vertices'''
        self.vertex = vertex # Number of vertices currently in the graph
        self.edges = 0 # Number of edges currently in the graph
        self.adj = [list() for vertex in range(self.total_vertex())] # Index 0 should always be empty since there is no page zero. Makes an adjacency list, indexed by the vertx (pagenumber)
        self.choice = {} # Empty choices dictionary

    def construct_choicesdict(self, fp):
        '''Constructs a dictionary of the choices'''
        try:
            fp = open(fp)
        except FileNotFoundError:
            print('File not found')
        for line in fp:
            if line.startswith('#'): # Skips any comments added
                continue
            elif line.startswith('\n'): # Skips empty lines
                continue
            if line.strip().isdigit(): # Reads page number
                pagenumber = int(line) # Obtains page number
                question = fp.readline().strip().split(':') # Reads NEXT line to get question
                answer1 = fp.readline().strip().split(':') # Reads NEXT line to get answer1
                answer2 = fp.readline().strip().split(':') # Reads NEXT line to get answer2
                self.choice[pagenumber] = {question[0]: question[1], answer1[0]: answer1[1],answer2[0]: answer2[1]} # Constructs the dictionary
            else:
                raise ValueError('File format is not correct')
        self.vertex = len(self.choice) + 1 # Update
        self.adj = [list() for vertex in range(self.total_vertex())] # Update the adjacency list
        fp.close()
        return self.choice
    
    def total_vertex(self):
        '''Returns the number of vertices in the graph'''
        return self.vertex
    
    def total_edges(self):
        '''Return the number fo edges in the graph'''
        return self.edges
    
    def check_vertex(self, v):
        '''Checks to see if the vertex, v, is legal'''
        if v < 0 or v >= self.vertex:
            raise ValueError('Vertex not legal: out of range')
    
    def addEdge(self, vertex1, vertex2):
        '''Adds a directed edge from vertex1 to vertex2'''
        self.check_vertex(vertex1) # Checks to see if vertex1 is legal
        self.check_vertex(vertex2) # Checks to see if vertex2 is legal
        self.adj[vertex1].append(vertex2) # Appends vertex2 to the index of vertex at adjacency list
        self.edges += 1 # Increases the number of edges
    
    def read_edge_file(self, fp):
        '''Reads the file of edges'''
        try:
            fp = open(fp)
        except FileNotFoundError:
            print('File not found')
        for line in fp:
            if line.startswith('#'): # Skips any comments added
                continue
            elif line.startswith('\n'):
                pass
                continue
            try:
                vertex1, vertex2 =[int(x) for x in line.split()]
            except ValueError: #If there is a letter or special characters in there
                print('File format contains characters not allowed')
            self.addEdge(vertex1, vertex2)
        fp.close()
        return
    
    def read_edge_file2(self, fp):
        '''Secondary version of the function to read file edges. Works, but not impleneted.'''
        try:
            with open(fp) as file:
                for line in file:
                    if line.startswith('#'): # Skips any comments added
                        continue
                    elif line.startswith('\n'): # Skips any empty lines
                        continue
                    try:
                        vertex1, vertex2 = [int(x) for x in line.split()]
                    except ValueError: # Handles any letters or special chaarcters
                        print('File Format contains characters not allowed. Story may not have been read correctly')
                        continue
                    self.addEdge(vertex1, vertex2)
        except FileNotFoundError: # If the file is not found
            print('File not found')

    def totalfilevertex(self): #Must match self.vertex
        '''Obtains the total number of vertices from the choice dictionary'''
        try:
            totalvertex = max(self.choice.keys()) # Gets the total vertices from the choice dictionary
        except KeyError:
            print("Please implement the script first")
        return totalvertex
            
    def next_page(self, currentpage, nextpageindex): 
        '''Access the next page from the adjacency list from the current page 
        where the nextpage index is the index of the sublist of the current page 
        index in the adjecency list'''
        try:
            if not isinstance(currentpage, int) or not isinstance(nextpageindex, int): # Checks to see if arguments are integers
                raise TypeError('Invald page or index')
        except TypeError:
            return 'Invalid page or index'
        try: # nextpagenumber represents the index of the adjacency list
            if nextpageindex == 0: #User clicks the left button
                nextpagenumber = self.adj[currentpage][0]
            elif nextpageindex == 1: #User clicks the right button
                nextpagenumber= self.adj[currentpage][1]
            else:
                raise IndexError
            return self.next_question(nextpagenumber)
        except IndexError:
            return 'Page not found'
    
    def next_question(self, nextpagenumber):
        '''Access the information for the next question'''
        try:
            question = self.choice[int(nextpagenumber)]['Question']
            answer1 = self.choice[int(nextpagenumber)]['Answer1'] #Should be left button
            answer2 = self.choice[int(nextpagenumber)]['Answer2'] #Should be right button
        except IndexError: 
            return 'Page not found'
        except ValueError:
            return 'Page not found'
        except KeyError:
            return 'Question not found'
        return question, answer1, answer2


##################################################################
##################################################################


class story(digraph): # Runs the game
    '''Class representation of the story as a graph'''
    def __init__(self): #Preferably, file1 is scriptfile and file2 is edgefile
        '''Contructs the story'''
        super().__init__() # Starts the init from digraph to make the adj list and dictionary
        self.current_page = 1
        self.question = "Question"
        self.answer1 = "Answer1"
        self.answer2 = "Answer2"
    
    def legalscript(self, file1, file2):
        '''Will check if the script text file and edge representation text file work'''
        try:
            choicesfile, edgefile = file1, file2 # Tries this order
            self.construct_choicesdict(choicesfile)
            self.read_edge_file(edgefile)
            self.question = self.choice[1]['Question'] # The following assignments need to be done to be able to update the question and answers on the ui
            self.answer1 = self.choice[1]['Answer1']
            self.answer2 = self.choice[1]['Answer2']
        except ValueError:
            choicesfile, edgefile = file2, file1 # Tries other order
            self.construct_choicesdict(choicesfile)
            self.read_edge_file(edgefile)
            self.question = self.choice[1]['Question']
            self.answer1 = self.choice[1]['Answer1']
            self.answer2 = self.choice[1]['Answer2']

    def start_game(self):
        '''Starts the game by obtaining the questions of the current page (page 1)''' 
        # Keeps track of the current page
        left_button = 0 # Assigns the index value 0 to the left button. Code not needed but for reference
        right_button = 1 # Assigns the index value 1 to the right button. Code not needed but for reference
        self.question, self.answer1, self.answer2 = self.next_question(self.current_page) # Gets the starting question and answers
    
    def left_button_click(self):
        self.question, self.answer1, self.answer2 = self.next_page(self.current_page, 0) # Gets the next page's information
        self.current_page = self.adj[self.current_page][0] # Updates the current page to the new one
        return self.question, self.answer1, self.answer2, self.start_game()
    
    def right_button_click(self):
        self.question, self.answer1, self.answer2 = self.next_page(self.current_page, 1) # Gets the next page's information
        self.current_page = self.adj[self.current_page][1] # Updates the current page to the new one
        return self.question, self.answer1, self.answer2, self.start_game()


##################################################################
##################################################################


# Very small amount of testing
if __name__ == '__main__':

    test_questions= {1:{
    'Question': 'Left or right?',
    'Answer1': 'Left',
    'Answer2': 'Right'},
    2:{
    'Question': 'Up or down?',
    'Answer1': 'Up',
    'Answer2': 'Down'},
    3:{
    'Question': 'Forward or backward?',
    'Answer1': 'Forward',
    'Answer2': 'Backward'}}

    test_adjlist = [[], [2,3], [],  []]
    questions = 'scripts/q&atest.txt'
    edges = 'scripts/edgereptest.txt'
    
    # Testing read edge version 1
    dg = digraph(0)
    dg.construct_choicesdict(questions)
    dg.read_edge_file(edges)
    assert dg.choice == test_questions
    assert dg.adj == test_adjlist
    assert dg.edges == 2
    assert dg.total_edges() == 2
    assert dg.vertex == 4
    assert dg.total_vertex() == 4
    assert dg.totalfilevertex() == 3

    # Testing read edge version 2
    dg2 = digraph()
    dg2.construct_choicesdict(questions)
    dg2.read_edge_file2(edges)
    assert dg2.adj == test_adjlist
    assert dg2.edges == 2
    assert dg2.total_edges() == 2
    assert dg2.vertex == 4
    assert dg2.total_vertex() == 4
    assert dg2.totalfilevertex() == 3

    # Digraph Question and Answer Testing
    x = digraph()
    x.construct_choicesdict(questions)
    x.read_edge_file(edges)
    assert x.next_question(2) == ('Up or down?', 'Up', 'Down')
    assert x.next_question(3) == ('Forward or backward?', 'Forward', 'Backward')
    assert x.next_question(4) == 'Question not found'
    assert x.next_question('g') == 'Page not found'
    
    script0 = 'scripts/script0.txt' 
    edgerep0 = 'scripts/edgerep0.txt' 
    y = digraph()
    y.construct_choicesdict(script0)
    y.read_edge_file(edgerep0)
    assert y.adj == [[], [2, 3], [4, 5], [6, 7], [8, 9], [], [], [], [], []] 
    assert y.next_page(1, 0) == ('You go left, and see a dragon sleeping on the ground. You have a choice of running away to the forest up ahead or fighting it with a sword on the ground near it. What do you do?', 
                               'Run to the forest', 
                               'Pick up the sword and fight') # Access adjacent list at page 1, go to index 0, 2, then access the info on page 2
    assert y.next_page(2, 0) == ('You run to the forest and get captured by gremlins, who take you their fortress. They plan on eating you alive. What do you do?', 
                                 'Accept your fate', 
                                 'Start shaking the cage in hope that it breaks')
    assert y.next_page(2, 5) == 'Page not found'
    assert y.next_page('text', 1) == 'Invalid page or index' 
    assert y.next_page(3, 'text') == 'Invalid page or index'
    assert y.next_page(2, 1) == ('You pick the sword to fight, and the dragon awakens, spotting you. As you approach it with the sword, it burns you alive with its fire. You died.', 
                                 'None', 
                                 'None') 
        
    # Story class testing
    test_story = story()
    assert test_story.question == "Question" # Should initiate with this
    assert test_story.answer1 == "Answer1" # Should initiate with this
    assert test_story.answer2 == 'Answer2' # Should initiate with this
    test_story.legalscript('scripts/edgerep0.txt', 'scripts/script0.txt')
    test_story.start_game()
    assert not test_story.choice == {} 
    assert test_story.choice == y.choice
    assert test_story.adj == [[], [2, 3], [4, 5], [6, 7], [8, 9], [], [], [], [], []]
    assert test_story.adj == y.adj
    assert not test_story.adj == [[], [2, 3], [4, 5], [6, 7], [8, 9]]
    assert test_story.edges == 8 
    assert not test_story.edges == 7
    assert test_story.question == 'You are on a path, and you have the choice of going left or right. Where do you go?'
    assert not test_story.question == "Question"
    assert test_story.answer1 == 'Left'
    assert test_story.answer2 == 'Right'
    assert not test_story.current_page == 2
    test_story.right_button_click() # Imitating a right button click
    assert test_story.vertex == 10
    assert test_story.current_page == 3
    assert test_story.question == "You go right and see a helicopter in the sky over you. What do you do?"
    assert test_story.answer1 == "Scream for help"
    assert test_story.answer2 == "Hide near a rock nearby"
    test_story.left_button_click() # Imitating a left button click
    assert test_story.current_page == 6
    assert test_story.question == 'You scream for help and the helicopter spots you. It lets down a ladder and you clutch on. It carries you back to civilization. You are saved.'
    assert test_story.answer1 == 'None'
    assert test_story.answer2 == "None"

    print('All tests passed') 