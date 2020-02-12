package dumpTruckSimulation;
/**
 * 
 * @author Dolores Petropulos, Carlos Rendon, Grace Street
 *
 * The Queue Class contains the Linklist named Queue for the simulation template and includes
 * the enqueue and dequeue method.  The tail puts the new entries to the back end of the Queue. 
 * The tail is the front of the Queue. 
 * 
 */

import java.util.NoSuchElementException;

public class Queue<T>
{
	private Node<T> head = null;
	private Node<T> tail = null;
	private int queueLength = 0;
	private Statistics stats;

	/**
	 * Constructor for Queue 
	 * @param T customer  customer in queue
	 */
	public Queue(Statistics stats)
	{
		this.stats = stats;
	}

	/**
	 * Synchronized void enqueue passes T customer.  If it's empty the queue gets a 
	 * new customer and adds it to the Linklist and adjusts Max Queue Length. 
	 * @param T customer  customer in queue
	 */
	public synchronized void enqueue(T customer)
	{
		if (isEmpty())
		{
			this.head = this.tail = new Node<T>(customer);
		} else
		{
			this.tail.next = new Node<T>(customer);
			this.tail = this.tail.next;
		}
		this.queueLength++;
		this.stats.adjustMaxQueueLength(this.queueLength);
	}

	/**
	 * Public boolean returns null if the queue is empty as the queue has to contain
	 * a customer.
	 * @return:  null
	 */
	public boolean isEmpty()
	{
		return this.head == null;
	}

	/**
	 * Public synchronized T dequeue throws a NoSuch ElementException if the Customer Queue
	 * is empty.  It also deals with the length and subtracts queueLength the customer 
	 * from the Queue and returns customer when the customer leaves.  Synchronized is used
	 * so two or more threads can't be accessed at the same time.  The second thread has to
	 * wait to the first to finish.
	 * @return customer   customer being dequeded
	 * @throws NoSuchElementException  if queue is empty
	 */
	public synchronized T dequeue() throws NoSuchElementException
	{
		if (isEmpty())
			throw new NoSuchElementException();
		T customer = this.head.customer;
		this.head = this.head.next;
		if (this.head == null)
			this.tail = null;
		this.queueLength--;
		return customer;
	}

	/**
	 * public T peek method throws NoSuchElementException if the queue isEmpty and returns
	 * to the head.customer.
	 * @return head.customer  customer at front of queue
	 * @throws NoSuchElementException  if queue is empty
	 */
	public T peek() throws NoSuchElementException
	{
		if (isEmpty())
			throw new NoSuchElementException();
		return this.head.customer;
	}

	// ////////////////////////////////////////////////
	private class Node<T>
	{
		T customer;
		Node<T> next;

		public Node(T customer)
		{
			this.customer = customer;
			this.next = null;
		}
	}// end class Node
}// end class Queue
