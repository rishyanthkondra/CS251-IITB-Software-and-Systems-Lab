/**
*@file LinkList.java
*@brief Implementing the Linkedlists
*@detail We use this to remove or add elements at the both ends in constant time.
**/
/** Here we create queue data structure,where adding and removing elements is possible 
at both ends using linkedlist.**/
//!We define a class called LinkList and define some functions using the class node.
public class LinkList<T> {

    //! We define front node using node class
    /*front node is to the front so it's previous node is null.*/
    private Node<T> front;
    //!We define rear node using node class
    /*rear node is at the very end so it's next node is set to null*/
    private Node<T> rear;
     /**To add an element at the beginning of the queue.We create a node with the 'item' input
     * as its value and as the new node is nd and is at the front so its previous node is set to null
     * and the next node is the front node previously,if the queue not empty,else it is also set to null.
     *if previously queue was not empty then the preivous front node's previous node is  set to the present front node.**/
    public void insertFront(T item){
        //add element at the beginning of the queue
        System.out.println("adding at front: "+item);
        Node<T> nd = new Node<T>();
        nd.setValue(item);
        nd.setNext(front);
        if(front != null) front.setPrev(nd);
        if(front == null) rear = nd;
        front = nd;
    }
     /**To insert an element at the end of the queue.We create a new node nd with item as its value
     * and set its previous node to the previous end node if queue was not empty else null 
     *and the next node to null.
     *And the previous rear node would have its next node as nd.
    /*
        \param item -> element to insert at the end .
        \return void
        */
    public void insertRear(T item){
        //add element at the end of the queue
        System.out.println("adding at rear: "+item);
        Node<T> nd = new Node<T>();
        nd.setValue(item);
        nd.setPrev(rear);
        if(rear != null) rear.setNext(nd);
        if(rear == null) front = nd;
         
        rear = nd;
    }
    /**To remove the item from beginning of the queue
    *If queue was not empty then remove the node at front,else unable to remove message is printed.**/
    public void removeFront(){
        if(front == null){
            System.out.println("Deque underflow!! unable to remove.");
            return;
        }
        //remove an item from the beginning of the queue
        Node<T> tmpFront = front.getNext();
        if(tmpFront != null) tmpFront.setPrev(null);
        if(tmpFront == null) rear = null;
        System.out.println("removed from front: "+front.getValue());
        front = tmpFront;
    }
    /**To remove the last element of the double ended queue
    *If queue was not empty then remove node at the end ,else print unable to remove message.**/
    public void removeRear(){
        if(rear == null){
            System.out.println("Deque underflow!! unable to remove.");
            return;
        }
        //remove an item from the beginning of the queue
        Node<T> tmpRear = rear.getPrev();
        if(tmpRear != null) tmpRear.setNext(null);
        if(tmpRear == null) front = null;
        System.out.println("removed from rear: "+rear.getValue());
        rear = tmpRear;
    }
    //!The driving function to create a double ended queue.
    public static void main(String a[]){
        //!We define deque as linklist variable of integers.
        LinkList<Integer> deque = new LinkList<Integer>();
        deque.insertFront(34);
        deque.insertFront(67);
        deque.insertFront(29);
        deque.insertFront(765);
        deque.removeFront();
        deque.removeFront();
        deque.removeFront();
        deque.insertRear(43);
        deque.insertRear(83);
        deque.insertRear(84);
        deque.insertRear(546);
        deque.insertRear(356);
        deque.removeRear();
        deque.removeRear();
        deque.removeRear();
        deque.removeRear();
        deque.removeFront();
        deque.removeFront();
        deque.removeFront();
    }
}
//!Define a class called 'node' to store information abt the value at that node and reference to 
//!previous node and the next node
class Node<T>{
    //!We define a previous node
    private Node<T> prev;
    //!We define a next node
    private Node<T> next;
    //!We have value of present node.
    private T value;
    //!Gives the previous node.
    public Node<T> getPrev() {
        return prev;
    }
    //!Sets the previous node to some new node
    public void setPrev(Node<T> prev) {
        this.prev = prev;
    }
    //!Gives the next node
    public Node<T> getNext() {
        return next;
    }
    //Sets the next node to some new node
    public void setNext(Node<T> next) {
        this.next = next;
    }
    //!Gives the value at present node
    public T getValue() {
        return value;
    }
    //!Sets the value of present node to the required value
    public void setValue(T value) {
        this.value = value;
    }
}