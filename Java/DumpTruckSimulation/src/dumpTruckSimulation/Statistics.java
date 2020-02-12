package dumpTruckSimulation;

public class Statistics
{
	private String name;
	private int numberOfFalseAlarms = 0;
	private double falseAlarmsTime = 0;
	private int numberOfSeriousCalls = 0;
	private double seriousCallsTime = 0;
	private int numberOfNormalCalls = 0;
	private double normalCallsTime = 0;
	private int totalCalls = 0;
	private double totalTime = 0;
	private int maxAmbulancesInUse = 0;

	public Statistics(String name)
	{

		this.name = name;
	}

	public void incrementFalseAlarms(double time)
	{
		this.numberOfFalseAlarms++;
		this.falseAlarmsTime += time;
	}

	public void incrementAmbulancesInUse(int numberInUse)
	{
		if (numberInUse > this.maxAmbulancesInUse)
			this.maxAmbulancesInUse = numberInUse;
	}

	public void incrementSeriousCalls(double time)
	{
		this.numberOfSeriousCalls++;
		this.seriousCallsTime += time;
	}

	public void incrementNormalCalls(double time)
	{
		this.numberOfNormalCalls++;
		this.normalCallsTime += time;
	}

	public void setTotalTime(double time)
	{
		this.totalTime = time;
	}

	public void setTotalCalls(int calls)
	{
		this.totalCalls = calls;
	}

	public void reportGeneration()
	{
		double totalCallTime = this.falseAlarmsTime + this.seriousCallsTime + this.normalCallsTime;
		System.out.println(this.name);
		System.out.print(String.format("There were %d false alarms, for a total of %.2f minutes, ",
				this.numberOfFalseAlarms, this.falseAlarmsTime));
		System.out.println(String.format("and average of %.2f minutes per false alarm.",
				this.falseAlarmsTime / this.numberOfFalseAlarms));
		System.out.println(String.format("The proportion of call time spent on false alarms is %.2f\n",
				this.falseAlarmsTime / totalCallTime));

		System.out.print(String.format("There were %d serious calls, for a total of %.2f minutes, ",
				this.numberOfSeriousCalls, this.seriousCallsTime));
		System.out.println(String.format("and average of %.2f minutes per serious call.",
				this.seriousCallsTime / this.numberOfSeriousCalls));
		System.out.println(String.format("The proportion of call time spent on serious calls is %.2f\n",
				this.seriousCallsTime / totalCallTime));

		System.out.print(String.format("There were %d normal calls, for a total of %.2f minutes, ",
				this.numberOfNormalCalls, this.normalCallsTime));
		System.out.println(String.format("and average of %.2f minutes per normal call.",
				this.normalCallsTime / this.numberOfNormalCalls));
		System.out.println(String.format("The proportion of call time spent on normal calls is %.2f\n",
				this.normalCallsTime / totalCallTime));

		System.out.println(String.format("There was a total of %d in %.2f minutes.", this.totalCalls, this.totalTime));
		System.out.println("The maximum ambulances in use at one time is " + this.maxAmbulancesInUse);
	}
}
