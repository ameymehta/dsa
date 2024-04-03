public class HelloWorld {

  public static void main(String[] args){
    //Prints "Hello, World" to the terminal
    System.out.println("Hello, World");
  }

}

// Messages are <key, value> pairs
class Msg
{
  long m_key;  // unique
  long m_val;
};
 
// This is the sliding window that needs to be implemented.
class Window
{
  // Define a window of a certain size in microsecond granularity
  Window(int nMicrosecs);
 
  // add a new incoming message
  addMsg(Msg m);
 
  // get a message given a key. If the message does not exist or message is older than the window size, return NULL
  // it's *important* to be correct
  Msg getMsg(long key);
 
  // get the average of message values in the window. Like getMsg, it's important to be correct.
  Double getAvg();
    
  void removeExpiredMsgs();
};

--

class Node:
    def __init__
    self.next Node
    self.msg Msg
    
class LinkedList:
    self.head
    self.tail
    

class Map:
    add(msg.key, Node)
    
    
class AvgValue:
    self.sum
    self.count
    
    self.getAvg
    
-----

lock = Lock()
lock.acquire()
lock.release()

class Window:
    def __init__(self, nMicrosecs):
        self.nMicrosecs = nMicrosecs
        self.messagesList = LinkedList()
        self.map = Map()
        
    def addMsg(m):
        currentNode = Node(m)
        currentNode.next =LinkedList.tail
        LinkedList.tail = currentNode
        map
    
    def getMsg(key):
       
    
    def getAvg():
        
        