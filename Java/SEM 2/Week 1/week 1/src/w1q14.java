import java.util.Scanner;
public class w1q14 {
    public static void main(String[] args) {
        Scanner n= new Scanner(System.in);
        System.out.println("Enter an integer : ");
        int no=n.nextInt();
        if(no%5==0){
            System.out.println("Its divisible by 5");
        }
        else{
            System.out.println("Its not divisible by 5");
        }


    }
}
