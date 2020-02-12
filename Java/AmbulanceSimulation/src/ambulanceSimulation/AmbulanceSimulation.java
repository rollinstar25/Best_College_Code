package ambulanceSimulation;

import generalSimulation.DiscreteDistribution;
import generalSimulation.Distribution;
import generalSimulation.DistributionFactory;

/**
 * Ambulance Simulation Class
 * @author Grace Street
 *
 *Creates a simulation of ambulances on duty.
 */
public class AmbulanceSimulation
{
	public static final int FALSE_ALARM = 1;
	public static final int SERIOUS = 2;
	public static final int NORMAL = 3;

	private Distribution interarrivalTimes;
	private Distribution falseAlarmCalls;
	private Distribution seriousCalls;
	private Distribution normalCalls;
	private DiscreteDistribution kindOfCall;
	private Statistics stats;
	private EventList eventList;
	private int callsComplete = 0;
	private double clock;
	private int numberOfCalls = 500;
	private int numberOfAmbulancesOut = 0;

	/**
	 * Constructor for Ambulance Simulation
	 */
	public AmbulanceSimulation()
	{
		DistributionFactory factory = new DistributionFactory(12345);
		int[] values = { FALSE_ALARM, SERIOUS, NORMAL };
		double[] probabilities = { 0.15, 0.1275, 0.7225 };

		// Use the factory to create the needed distributions.
		this.eventList = new EventList();
		this.interarrivalTimes = factory.createUniformDistribution(5, 25);
		this.normalCalls = factory.createUniformDistribution(10, 30);
		this.seriousCalls = factory.createUniformDistribution(20, 30);
		this.falseAlarmCalls = factory.createUniformDistribution(10, 14);
		this.kindOfCall = factory.createDiscreteEmpiricalDistribution(values, probabilities);
		

		this.eventList.addEvent(new Event(Event.CALL, this.kindOfCall.getNext(), 0));
		this.stats = new Statistics("Ambulance Simulation with Infinite Ambulances!");
		// Ignore this print statement; my Eclipse deletes anything unused when I
		// save so I'm using values and probabilities.
		System.out.println("" + values + probabilities);
	}

	/**
	 * processCall method
	 * processes an incoming call into the system, sends an ambulance, and schedules call completion
	 * @param event  the call event
	 */
	public void processCall(Event event)
	{
		Event nextCall = new Event(Event.CALL, this.kindOfCall.getNext(), this.clock + this.interarrivalTimes.getNext());
		this.eventList.addEvent(nextCall);
		scheduleCompletion(event.getCallType());
		numberOfAmbulancesOut++;
		this.stats.incrementAmbulancesInUse(numberOfAmbulancesOut);;
	}

	/**
	 * scheduleCompletion method
	 * Adds a calls imminent completion to the future evetn list
	 * @param callType  the severity of the call
	 */
	public void scheduleCompletion(int callType)
	{
		Event complete = new Event(Event.COMPLETE, callType, this.clock);
		this.eventList.addEvent(complete);
		
	}

	/**
	 * processComplete method
	 * Updates stats after completion of event
	 * @param event  event completed
	 */
	public void processComplete(Event event)
	{
		if(event.getCallType() == FALSE_ALARM){
			this.stats.incrementFalseAlarms(this.clock);
		}
		else if(event.getCallType() == SERIOUS){
			this.stats.incrementSeriousCalls(this.clock);
		}
		else{
			this.stats.incrementNormalCalls(this.clock);
		}
		numberOfAmbulancesOut--;
		callsComplete++;
	}

	/**
	 * runSimulation method
	 * runs the simulation
	 */
	public void runSimulation()
	{
		while (this.callsComplete < this.numberOfCalls)
		{
			Event event = this.eventList.getImminentEvent();
			this.clock = event.getEventTime();
			if (event.getEventType() == Event.CALL)
				processCall(event);
			else
				processComplete(event);
		}
		this.stats.setTotalTime(this.clock);
		this.stats.setTotalCalls(this.numberOfCalls);
		this.stats.reportGeneration();
	}

	public static void main(String[] args)
	{
		AmbulanceSimulation simulation = new AmbulanceSimulation();
		simulation.runSimulation();
	}

	/**
	 * toString method
	 * @return interarrivalTimes, falsAlarmCalls, seriousCalls, normalCalls, clock, eventList, kindOfCall, stats, callsComplete,
	 * numberOfCalls numberOfAmbulancesOut
	 */
	@Override
	public String toString()
	{
		return "" + this.interarrivalTimes + this.falseAlarmCalls + this.seriousCalls + this.normalCalls + this.clock
				+ this.eventList + this.kindOfCall + this.stats + this.callsComplete + this.numberOfCalls
				+ this.numberOfAmbulancesOut;
	}
}
