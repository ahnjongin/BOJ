#include<stdio.h>
int main()
	{
		int a, b, c, d;
		scanf("%d %d", &a, &b);
		c = (a % 10 * 100) + (a % 100 / 10 * 10) + (a /100);
		d = (b % 10 * 100) + (b % 100 / 10 * 10) + (b /100);

			printf("%d", c > d ? c : d);
	}
