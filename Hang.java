import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Hang {
	
	private static String line = ""; 
	private static String hiddenWord;
	private static String coversWord;
	
	private static int words =0; // words
	private static int count = 0;
	
	private static File file;
	
	public static void main(String[] args) throws Exception
	{
		Hang hang = new Hang();
		
		Scanner sc=new Scanner(System.in);
		
		// Let user pick what to input
		System.out.println("Pick a category: animals, colors, movies, songs" ); 
		
		// User input
		String category = sc.nextLine().toLowerCase(); 

		hang.readFile(category);
		//System.out.println(hiddenWord ); 

		System.out.println(hang.coverWord()); 
		hang.userInput();
		System.out.println("Thank you for playing!");
		
	}

	public static void readFile (String category) throws Exception
	{
		String line = ""; 
		try {
			FileReader fileReader = null;
			BufferedReader bufferedReader;
			
			// Compare this category sting with the other strings
			if (category.equals("animals"))
				
				{
				 file = new File ("animals.txt");
			fileReader = new FileReader("animals.txt");
				}
			
			else if (category.equals("colors"))
				
				{
				 file = new File ("colors.txt");
				fileReader = new FileReader("colors.txt");
				}
			
			else if (category.equals("movies"))
				
				{
				 file = new File ("movies.txt"); 
				fileReader = new FileReader("movies.txt");
				}
			
			else if (category.equals("songs"))
				
				{
				file = new File ("songs.txt");
				fileReader = new FileReader("songs.txt");
				}
			
			ArrayList <String>words = new ArrayList<>();
			
			bufferedReader = new BufferedReader(fileReader);
			
			while((line = bufferedReader.readLine()) != null)
				
				{
		         words.add(line.trim());
		        }
				
				hiddenWord = words.get(new Random().nextInt(words.size()));
		            bufferedReader.close(); 
		}
		
		catch(FileNotFoundException ex) 
		
		{
			System.out.println("Unable to open file ");                
		}
		
		catch(IOException ex)
		{
			System.out.println("Error reading file ");  
	    }
		
		startGame(category);
	}

	public static void startGame (String category) throws FileNotFoundException 
	{
		
		System.out.println("Are you ready to play: Y or N");
		Scanner sc1=new Scanner(System.in);
		
		String ans =sc1.nextLine(); 
		ans = ans.toUpperCase();
		
		if (ans.equals("Y"))
		
		{
		System.out.println("HANGMAN GAME: Start");
		System.out.println("Hint:" + category);
		}
		
		else 
			
		{
			System.out.println("Goodbye");
			System.exit(0);
		}
	}
	
	public static String coverWord()
	{
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0 ; i < hiddenWord.length() ; i++)
		
		{
		    sb.append("_");
		}
		
		return coversWord=sb.toString();		
	}

	public static void userInput ()
	{
		
		
		while (count !=7)
		{
			
			
			Scanner sc = new Scanner(System.in);
			
			System.out.println("Guess a letter");
			
			String guess = sc.next().toLowerCase();
			
		
				if (hiddenWord.contains(guess))
				
				{
		
					System.out.println("Correct");
					
					char found = guess.charAt(0);
					
					StringBuilder sb = new StringBuilder(coversWord);
					 
					 for (int i =0; i <sb.length(); i++)
					 {
						 if(hiddenWord.charAt(i)==found)
							 
		           	  		{
		                     sb.replace(i, i + 1, guess);
		           	  		}
					 }
						 
						 coversWord = sb.toString();
						 
			             System.out.println(coversWord);  
			             
			             if (coversWord.matches(hiddenWord))
			             
			             	{
			            	 System.out.println("Congrats, you won");
			            	 //count = 7;
			            	 break;
			             	}
			            
			            
					 }
				 else if (!(hiddenWord.contains(guess)))
		      	{
			     	 count ++; 
			     	 System.out.println(guess + " is an incorrect letter");
			     	 
			     	 
		     	 
		      	}
				 else if(count == 7) {
					 System.out.println("You lost");
		             
		             
				 }
				
				
		}
	}
		
}
	
	 
