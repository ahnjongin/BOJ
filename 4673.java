import java.util.Arrays;
public class Main
{
    public static int fuction(int number)
    {
        int dn=number;
        while(number>0) {
            dn = dn + (number%10);
            number= number/10;
        }
        return dn;
    }
    public static void main(String[] args)
    {
        boolean[]check = new boolean[10001];
        for(int i=1; i<10001; i++) {
            int n = fuction(i);
            if(n<10001) {
            check[n]=true;
            }
            }
        for(int i=1; i<check.length; i++) {
        if(!check[i])
        {
            System.out.println(i);
        }
        }
        }

        }