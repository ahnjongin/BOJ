#include<stdio.h>

int main()
{
	int a,b,c,d;
	int count = 0;
	scanf("%d", &a);
	b = a;
	while (1)
	{

		c = (a % 10 + a / 10)%10;
		d = ((a % 10) * 10) + c;
		a = d;
		count++;
		if (b == a)
			break;
	}
	printf("%d", count);
	return 0;

}