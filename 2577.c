#include<stdio.h>

int main(void)
{
	int a, b, c;
	int arr[10] = { 0, };
	scanf("%d\n", &a);
	scanf("%d\n", &b);
	scanf("%d\n", &c);
	int n = a * b * c;
	int num;
	while (n > 0)
	{
		num = n % 10;
		arr[num]++;
		n /= 10;
	}
	for (int i = 0; i < 10; i++)
	{
		printf("%d\n", arr[i]);
	}


	return 0;
}