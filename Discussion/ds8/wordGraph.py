from basicgraph import *

# CS1210 Spring 2020. Discussion section 8. April 15-17, 2020
#
# Complete steps 1, 2.1, 2.2, and 2.3 so that
# buildWordGraph(somefilename) will return a graph with words from somefilename as Nodes
# and an edge between each pair of Nodes that represents two words that differ in exactly
# one position.
#
# Test on a small file first - wordsTest.txt
# You should draw the graph for wordsTest.txt on paper by hand, and then look at the result
# of buildWordGraph("wordsTest.txt") to see if they match
#
# Test also on large file - words5.txt.
# The file contains 2415 words. It should take several seconds to build this
# graph (but not several minutes)
#


# return True if there should be an edge between nodes for word1 and word2
# in the word graph. That is, if the two words are the same length and differ
# at exactly one position.  Return False otherwise (including when the two words
# don't differ at all!)
#
def shouldHaveEdge(word1, word2):
    result = False
    # Step 1: make this function correct
    if len(word1) == len(word2):
        indexDif = 0
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                indexDif += 1
        if indexDif == 1:
            result = True
            
    # Test it carefully by calling it with various words in the Python
    # shell.  Don't do step 2 until you are confident this fn is correct.
    return result

# Give a file of words, return a graph with
# - one node for each word
# - an edge for every pair of words, w1 and w2,
#      where shouldHaveEdge(w1, w2) is True.
#
def buildWordGraph(wordsFile):
    # Steps 2.1, 2.2, 2.3
    wordGraph = Graph()
    instream = open(wordsFile,"r")
    for line in instream:
             # Step 2.2
             # Each line of the input file will contain a single word
        lineStrip = line.strip()
             # First use line.strip() to get the word (so the "\n" end of line
             # is not included.
             # Then, create a Node for each word and add that Node to the graph
        newNode = Node(lineStrip)
        wordGraph.addNode(newNode)
    # At this point, wordGraph should have a Node for each word but no edges
    # Step 2.3 Check every relevant pair of Nodes to see whether the graph
    # should have an edge between those Nodes (based on whether the function
    # shouldHaveEdge returns True/False on the Nodes' words)
    # Notes:
    for node in wordGraph.nodes:
        for node2 in wordGraph.nodes:
            nodeName = node.getName()
            node2Name = node2.getName()
            edge = shouldHaveEdge(nodeName, node2Name)
            if edge: 
                if node not in wordGraph.adjacencyLists[node2]:
                    wordGraph.addEdge(node, node2)
                    
    # 1) DO NOT pass Nodes to shouldHaveEdge.  shouldHaveEdge works on
    #    *strings*/words, not Nodes)
    # 2) DO NOT try to add the same edge twice. For instance, if Node n1 has
    #    name 'black' and Node n2 has name 'blank',
    #    shouldHaveEdge(n1.getName(), n2.getName) and
    #    shouldHaveEdge(n2.getName(),n2.getName() will both return True.  Make
    #    sure you don't call both wordGraph.addEdge(n1,n2) and wordGraph.addEdge(n2,n1)
    #    because addEdge will generate an error if an edge between the given nodes already
    #    exists
    #    
    # Add code here.  Recommended: use nested loops.
    return wordGraph