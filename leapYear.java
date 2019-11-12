import java.util.Scanner;

public class leapYear 
{
	public static void main(String[] args)
	{
		int leapYear;
    	Scanner scan = new Scanner(System.in);
    	System.out.println("Enter a Year:");
    	leapYear = scan.nextInt();
    	scan.close();
        boolean isLeapYear = false;

        if(leapYear % 4 == 0)
        {
            if( leapYear % 100 == 0)
            {
                if ( leapYear % 400 == 0)
                    isLeapYear = true;
                else
                    isLeapYear = false;
            }
            else
                isLeapYear = true;
        }
        else 
        {
            isLeapYear = false;
        }

        if(isLeapYear==true)
            System.out.println(leapYear + " is a Leap Year.");
        else
            System.out.println(leapYear + " is not a Leap Year.");
	}

}
