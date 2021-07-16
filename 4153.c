#include<stdio.h>
int main()
{
	int a, b, c,a1,b1,c1;
	while(1)
	{
		scanf("%d %d %d\n", &a1, &b1, &c1);
		if (a1 == 0 && b1 == 0 && c1 == 0)
		{
			break;
		}
		a = a1 * a1;
		b = b1 * b1;
		c = c1 * c1;
		if ((a == b + c) || (b == a + c) || (c == a + b))
		{
			printf("right\n");
		}
		else
		{
			printf("wrong\n");
		}
	}
}